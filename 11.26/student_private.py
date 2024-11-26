class Student:
    # 定义私有属性，在属性名前加上双下划线
    def __init__(self, name, student_id, age):
        """
        初始化学生信息
        :param name: 学生姓名
        :param student_id: 学号
        :param age: 年龄
        """
        self.__name = name            # 私有属性
        self.__student_id = student_id  # 私有属性
        self.__age = age             # 私有属性
        self.__scores = {}           # 私有属性，用于存储各科成绩

    # 定义属性访问器（getter）和修改器（setter），以保护私有属性的访问和修改，并提供公共的访问接口，以实现对私有属性的安全访问
    @property
    def name(self):
        return self.__name

    @property
    def student_id(self):
        return self.__student_id

    @property
    def age(self):
        return self.__age

    def add_score(self, subject, score):
        """
        添加或更新某门课程的成绩
        :param subject: 科目
        :param score: 分数
        """
        if 0 <= score <= 100:
            self.__scores[subject] = score
        else:
            raise ValueError("成绩必须在0-100之间")

    def get_score(self, subject):
        """
        获取某门课程的成绩
        :param subject: 科目
        :return: 该科目的成绩，如果没有则返回None
        """
        return self.__scores.get(subject)

    def get_average_score(self):
        """
        计算平均成绩
        :return: 所有科目的平均分
        """
        if not self.__scores:
            return 0
        return sum(self.__scores.values()) / len(self.__scores)

    def get_grade(self):
        """
        根据平均分计算等级
        :return: 成绩等级（A/B/C/D/F）
        """
        avg_score = self.get_average_score()
        if avg_score >= 90:
            return 'A'
        elif avg_score >= 80:
            return 'B'
        elif avg_score >= 70:
            return 'C'
        elif avg_score >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        """
        返回学生信息的字符串表示
        """
        return f"学生：{self.__name}，学号：{self.__student_id}，年龄：{self.__age}，平均分：{self.get_average_score():.1f}"

# 使用示例
if __name__ == "__main__":
    # 创建学生实例
    student = Student("张三", "2024001", 20)

    # 添加成绩
    student.add_score("数学", 85)
    student.add_score("语文", 92)
    student.add_score("英语", 88)

    # 打印学生信息
    print(student)
    print(f"学生姓名：{student.name}")  # 通过属性访问器访问私有属性
    print(f"数学成绩：{student.get_score('数学')}")
    print(f"平均分：{student.get_average_score():.1f}")
    print(f"成绩等级：{student.get_grade()}")

    # 尝试直接访问私有属性（这会导致错误）
    try:
        print(student.__name)
    except AttributeError as e:
        print("无法直接访问私有属性：", e)
