from xml.parsers.expat import ParserCreate

# Sax 解析 XML 时，需要自己实现一个 ContentHandler，并将其传入 ParserCreate() 中
class DefaultSaxHandler(object):
    # start_element() 方法在读取到 XML 开始标签时调用，name 是标签的名称，attrs 是标签的属性
    # 注意：name 是一个字符串，所以，我们可以通过 name 来判断标签的名称
    # 注意：attrs 是一个 dict，所以，我们可以通过 attrs['href'] 来获取 href 属性的值
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    # end_element() 方法在读取到 XML 结束标签时调用，name 是标签的名称
    def end_element(self, name):
        print('sax:end_element: %s' % name)

    # char_data() 方法在读取到 XML 文本时调用，text 是文本内容
    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

# 解析 XML
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)