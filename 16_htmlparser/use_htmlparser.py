from html.parser import HTMLParser
from html.entities import name2codepoint

# 自定义 HTML 解析器，继承自 HTMLParser
# 注意：HTMLParser 是一个基类，所以，我们需要自定义一个类，继承自 HTMLParser，并重写一些方法
class MyHTMLParser(HTMLParser):
    # 处理开始标签，例如：<a href="/python">Python</a>
    def handle_starttag(self, tag, attrs):
        print("<%s>" % tag)

    # 处理结束标签，例如：</a>
    def handle_endtag(self, tag):
        print("</%s>" % tag)

    # 处理自结束标签，例如：<img />
    def handle_startendtag(self, tag, attrs):
        print("<%s/>" % tag)

    # 处理文本，例如：Python
    def handle_data(self, data):
        print(data)

    # 处理注释，例如：<!-- test html parser -->
    # 注意：HTML 注释是一种特殊的注释，它的格式是：<!-- test html parser -->
    # 所以，我们可以通过 data 来判断注释的内容
    def handle_comment(self, data):
        print("<!--", data, "-->")

    # 处理特殊字符，例如：&nbsp;
    # 注意：HTML 特殊字符是一种特殊的字符，它的格式是：&nbsp;
    # 所以，我们可以通过 name 来判断特殊字符的名称
    def handle_entityref(self, name):
        print("&%s;" % name)

    # 处理特殊字符，例如：&#1234;
    # 注意：HTML 特殊字符是一种特殊的字符，它的格式是：&#1234;
    # 所以，我们可以通过 name 来判断特殊字符的编号
    def handle_charref(self, name):
        print("&#%s;" % name)

parser = MyHTMLParser()
parser.feed(
    """
<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body>
</html>
"""
)
