import base64, struct

# BMP 格式的前 2 个字节是 'BM'，表示这是一个 BMP 文件，接下来的 4 个字节是文件大小，接下来的 4 个字节是保留字，接下来的 4 个字节是数据偏移量
# BMP 格式的后 4 个字节是 BMP 的宽，接下来的 4 个字节是 BMP 的高，接下来的 2 个字节是 BMP 的颜色数，接下来的 2 个字节是 BMP 的重要颜色数
# BMP 格式的颜色数和重要颜色数都是 2 的幂次，颜色数表示 BMP 的颜色数，重要颜色数表示 BMP 的重要颜色数，0 表示所有颜色都是重要颜色

# 下面是一个 28 x 10 的 16 色位图，保存为 bmp 格式，大小为 178 x 22，前面的 14 个字节是 BMP 的头，后面的 178 x 22 个字节是 BMP 的内容
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
    'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
    '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
    'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
    '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
    '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
    'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
    '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
    '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
    'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
    'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
    '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

# 解析 BMP 格式，返回一个字典，包含 BMP 的宽、高、颜色等信息
def bmp_info(data):
    # 检查 BMP 格式，前 2 个字节是 'BM'，否则不是 BMP 格式
    if data[:2] != b'BM':
        return 'Not BMP file'
    else:
        # unpack 解析 BMP 格式，返回一个元组，包含 BMP 的宽、高、颜色等信息
        # '<' 表示小端模式
        # 'cc' 表示 2 个字节，'II' 表示 4 个字节，'HH' 表示 2 个字节，'IIHH' 表示 4 个字节，'HH' 表示 2 个字节，'I' 表示 4 个字节，'I' 表示 4 个字节
        s = struct.unpack('<ccIIIIIIHH', data[:30])
        print(s)

        width = s[6] # 宽度
        height = s[7] # 高度
        color = s[9] # 颜色数

    return {
        'width': width,
        'height': height,
        'color': color
    }

# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')