import argparse

def main():
    # 定义一个 ArgumentParser 实例，用于解析命令行参数
    parser = argparse.ArgumentParser(
        prog='backup', # 程序名，在帮助信息的最前面显示，可以用来显示程序的名称
        description='Backup MySQL database.', # 描述，在帮助信息的最前面显示，可以用来显示程序的用途
        epilog='Copyright(r), 2023' # 说明信息，在帮助信息的最后，可以用来显示版权信息
    )
    # 定义位置参数，即必须输入的参数，位置参数必须在关键字参数之前
    parser.add_argument('outfile')

    # 定义关键字参数，即可以输入的参数，关键字参数必须在位置参数之后
    # --host参数，允许用户输入--host参数，此参数默认值为localhost
    parser.add_argument('--host', default='localhost')
    # --port 参数，允许用户输入--port参数，此参数默认值为3306，且必须为int类型
    parser.add_argument('--port', default='3306', type=int)
    # --user参数，允许用户输入-u参数，此参数必须输入，且必须为str类型
    parser.add_argument('-u', '--user', required=True)
    # --password参数，允许用户输入-p参数，此参数必须输入，且必须为str类型
    parser.add_argument('-p', '--password', required=True)
    # --database参数，允许用户输入-d参数，此参数必须输入，且必须为str类型
    parser.add_argument('--database', required=True)
    # --gzcompress参数，允许用户输入-gz参数，此参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True，且必须为bool类型
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')

    # 解析参数，将参数解析成一个Namespace对象，Namespace对象包含了所有的参数
    # 可以通过属性名来访问参数，也可以通过属性值来访问参数
    args = parser.parse_args()

    # 打印参数
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')

if __name__ == '__main__':
    main()