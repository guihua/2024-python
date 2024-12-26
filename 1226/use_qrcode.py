# 安装 qrcode 库
# pip install qrcode
# 引入 qrcode 库
# qrcode 是一个 Python 库，用于生成二维码，它可以将任意的数据转换为二维码，例如 URL、文本、联系人信息等
# qrcode 的使用非常简单，只需要导入 qrcode 库，然后创建一个二维码实例，然后调用 add_data() 方法添加数据，最后调用 make() 方法生成二维码
import qrcode

# 创建数据
data="https://www.showmeai.tech"

# 创建二维码实例
# QRCode 类是 qrcode 库中的一个类，用于生成二维码，它的构造函数有以下参数：
# version 参数表示二维码的版本，它的值为 1 到 40，值越大，二维码的尺寸越大，但是生成的二维码也越复杂，默认值为 1
# box_size 参数表示每个小格子的大小，默认值为 10
# border 参数表示边框的大小，默认值为 4
# error_correction 参数表示纠错级别，它的值为以下常量：
# qrcode.constants.ERROR_CORRECT_L：低纠错级别，适用于较小的二维码
# qrcode.constants.ERROR_CORRECT_M：中纠错级别，适用于一般的二维码
qr= qrcode.QRCode(version=1, box_size=10, border=4, error_correction=qrcode.constants.ERROR_CORRECT_H)
# 添加数据
# add_data() 方法用于添加数据，它的参数为一个字符串，字符串的长度不能超过 4296 个字符
qr.add_data(data)
# 生成二维码
# make() 方法用于生成二维码，它的参数为一个布尔值，默认为 False，如果为 True，则会自动调整二维码的尺寸，以适应数据的长度
qr.make(fit=True)

# 保存二维码
# make_image() 方法用于生成二维码的图片，其参数包括：
# fill_color：二维码的填充颜色，默认为黑色
# back_color：二维码的背景颜色，默认为白色
qr_img=qr.make_image(fill_color="black", back_color="white")
# 保存图片
# save() 方法用于保存图片，它的参数为一个文件名
qr_img.save("./1226/qr.jpg")