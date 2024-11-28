import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
    """
    测试 Dict 类的初始化功能。
    创建一个 Dict 对象，传入键值对，然后检查属性和类型是否正确。
    """
    def test_init(self):
        d = Dict(a=1, b="test")
        # 检查属性 a 的值是否为 1
        self.assertEqual(d.a, 1)
        # 检查属性 b 的值是否为 "test"
        self.assertEqual(d.b, "test")
        # 检查 d 是否是 dict 的实例
        self.assertTrue(isinstance(d, dict))

    """
    测试通过键添加元素到 Dict 类的功能。
    创建一个 Dict 对象，添加一个键值对，然后检查属性是否正确。
    """
    def test_key(self):
        d = Dict()
        d["key"] = "value"
        # 检查属性 key 的值是否为 "value"
        self.assertEqual(d.key, "value")

    """
    测试通过属性添加元素到 Dict 类的功能。
    创建一个 Dict 对象，添加一个属性，然后检查键是否存在且值是否正确。
    """
    def test_attr(self):
        d = Dict()
        d.key = "value"
        # 检查键 "key" 是否在 d 中
        self.assertTrue("key" in d)
        # 检查键 "key" 的值是否为 "value"
        self.assertEqual(d["key"], "value")

    """
    测试访问不存在的键时是否会引发 KeyError。
    创建一个 Dict 对象，尝试访问不存在的键，期望引发 KeyError。
    """
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            # 尝试访问不存在的键 "empty"
            value = d["empty"]

    """
    测试访问不存在的属性时是否会引发 AttributeError。
    创建一个 Dict 对象，尝试访问不存在的属性，期望引发 AttributeError。
    """
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            # 尝试访问不存在的属性 empty
            value = d.empty

if __name__ == "__main__":
    unittest.main()
