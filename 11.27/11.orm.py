# 简单的使用元类的 ORM（对象关系映射）示例

# 定义一个基础的 Field 类，用于表示数据库字段
class Field(object):
    """
    Field 类，作为其他具体字段类的基类。
    存储字段的名称和列类型。
    """
    def __init__(self, name, column_type):
        # 存储字段名称
        self.name = name
        # 存储字段的列类型
        self.column_type = column_type

    def __str__(self):
        # 返回 Field 类名和字段名称的字符串表示
        return "<%s:%s>" % (self.__class__.__name__, self.name)


# 定义一个 StringField 类，继承自 Field 类，用于表示字符串类型的字段
class StringField(Field):
    """
    StringField 类，继承自 Field 类，用于表示字符串类型的字段。
    列类型默认为 "varchar(100)"。
    """
    def __init__(self, name):
        # 调用父类的构造函数，设置字段名称和列类型
        super(StringField, self).__init__(name, "varchar(100)")


# 定义一个 IntegerField 类，继承自 Field 类，用于表示整数类型的字段
class IntegerField(Field):
    """
    IntegerField 类，继承自 Field 类，用于表示整数类型的字段。
    列类型默认为 "bigint"。
    """
    def __init__(self, name):
        # 调用父类的构造函数，设置字段名称和列类型
        super(IntegerField, self).__init__(name, "bigint")


# 定义一个 ModelMetaclass 元类，继承自 type 类
class ModelMetaclass(type):
    """
    ModelMetaclass 元类，用于创建 Model 类的子类。
    负责处理类的属性，将 Field 实例存储到 __mappings__ 中，并设置 __table__ 属性。
    """
    def __new__(cls, name, bases, attrs):
        # 如果类名为 "Model"，直接使用 type 的 __new__ 方法创建类
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        # 打印找到的模型名称
        print("Found model: %s" % name)
        # 存储字段映射的字典
        mappings = dict()
        # 遍历类的属性
        for k, v in attrs.items():
            # 如果属性是 Field 类型
            if isinstance(v, Field):
                # 打印找到的映射关系
                print("Found mapping: %s ==> %s" % (k, v))
                # 将映射添加到 mappings 字典中
                mappings[k] = v
        # 从属性中移除已存储的 Field 实例
        for k in mappings.keys():
            attrs.pop(k)
        # 将映射存储到 __mappings__ 属性中
        attrs["__mappings__"] = mappings
        # 将表名设置为类名
        attrs["__table__"] = name
        # 使用 type 的 __new__ 方法创建类
        return type.__new__(cls, name, bases, attrs)


# 定义一个 Model 类，继承自 dict 类，使用 ModelMetaclass 作为元类
class Model(dict, metaclass=ModelMetaclass):
    """
    Model 类，继承自 dict 类，使用 ModelMetaclass 作为元类。
    提供了属性访问和设置的方法，以及保存对象的 save 方法。
    """
    def __init__(self, **kw):
        # 调用父类 dict 的构造函数，存储传入的关键字参数
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        """
        当访问不存在的属性时，尝试从字典中获取。
        :param key: 要访问的属性名称
        :return: 对应的值，如果不存在则抛出 AttributeError
        """
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        # 将属性存储到字典中
        self[key] = value

    def save(self):
        """
        保存对象的方法，生成 SQL 插入语句。
        收集字段、参数占位符和参数值。
        """
        fields = []
        params = []
        args = []
        # 遍历映射，收集字段、参数占位符和参数值
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        # 生成 SQL 插入语句
        sql = "insert into %s (%s) values (%s)" % (self.__table__, ",".join(fields), ",".join(params))
        # 打印 SQL 语句
        print("SQL: %s" % sql)
        # 打印参数值
        print("ARGS: %s" % str(args))


# 测试代码：

# 定义一个 User 类，继承自 Model 类
class User(Model):
    # 定义整数类型的 id 字段
    id = IntegerField("id")
    # 定义字符串类型的 name 字段
    name = StringField("username")
    # 定义字符串类型的 email 字段
    email = StringField("email")
    # 定义字符串类型的 password 字段
    password = StringField("password")


# 创建一个 User 实例并保存
u = User(id=12345, name="Michael", email="test@orm.org", password="my-pwd")
u.save()
