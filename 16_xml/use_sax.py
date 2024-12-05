from xml.parsers.expat import ParserCreate
from urllib import request

def parseXml(xml_str):
    # print(xml_str)
    d={}
    cname=''
    parser=ParserCreate()

    # 解析 XML
    # 解析 XML 时，需要自己实现一个 ContentHandler，并将其传入 ParserCreate() 中
    # 注意：name 是一个字符串，所以，我们可以通过 name 来判断标签的名称
    # 注意：attrs 是一个 dict，所以，我们可以通过 attrs['href'] 来获取 href 属性的值
    # start_element() 方法在读取到 XML 开始标签时调用，name 是标签的名称，attrs 是标签的属性
    # end_element() 方法在读取到 XML 结束标签时调用，name 是标签的名称
    def start_element(name,attrs):
        print("开始",name,attrs)
        nonlocal cname
        cname=name

    # 解析 XML 文本时调用，text 是文本内容
    def char_data(text):
        print("获取到的标签中间数据",text)
        d[cname]=text

    def end_element(name):
        print("结束",name)

    parser.StartElementHandler= start_element
    parser.EndElementHandler=end_element
    parser.CharacterDataHandler=char_data

    parser.Parse(xml_str)

    return {
        'city': d.get('region'),
        'weather': {
            'condition': d.get('text'),
            'temperature': d.get('temp_c'),
            'wind': d.get('windchill_c')
        }
    }

# 测试:
URL = 'https://api.weatherapi.com/v1/current.xml?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'
print('OK')