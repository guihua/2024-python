from collections import ChainMap
import os, argparse

# 构造缺省参数
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数
# argparse 解析命令行参数，将命令行参数解析成一个命名空间
# ArgumentParser 是一个命令行参数解析器，用于解析命令行参数
parser = argparse.ArgumentParser()

# 添加参数
# -u, --user 表示可选参数，-u 表示短参数，--user 表示长参数
# -c 表示短参数，--color 表示长参数
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')

# 解析参数，将命令行参数解析成一个命名空间
namespace = parser.parse_args()
# 构造命令行参数，将命令行参数解析成一个字典
command_line_args = {
    k: v for k,
    v in vars(namespace).items() if v
}

# 组合成ChainMap，使用优先级顺序访问参数
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])