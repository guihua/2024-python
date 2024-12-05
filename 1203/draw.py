from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母，随机大小写
def rndChar():
    # chr() 方法返回一个整数对应的字符，范围在 [65, 90] 之间，包括 65 和 90
    return chr(random.randint(65, 90))

# 随机颜色1
def rndColor():
    # randint() 方法返回一个随机整数，范围在 [64, 255] 之间，包括 64 和 255
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 图片尺寸：240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象，指定字体类型和大小
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象，指定图像和字体
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        # point() 方法可以在图像上绘制一个点，它的参数是一个 tuple，代表像素的坐标，和一个可选的颜色
        draw.point((x, y), fill=rndColor())

# 输出文字
for t in range(4):
    # text() 方法可以在图像上绘制文字，它的参数是一个 tuple，代表文字的坐标，和一个字符串，代表要绘制的文字，和一个可选的字体和颜色
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊
# filter() 方法返回一个新的 Image 对象，是原图的模糊版本
image = image.filter(ImageFilter.BLUR)
# 保存图片
# 路径为当前路径下的 code.jpg，如果没有该路径，会自动创建，如果有同名文件，会自动覆盖
# 路径中不能有中文
# TODO：不加 1203 路径时，图片会保存到根目录下
# save() 方法的第一个参数是图片的路径，它的值为 code.jpg
# save() 方法的第二个参数是图片的格式，它的值为 jpeg，也可以是 png，bmp，gif，tiff 等
image.save('1203/code.jpg', 'jpeg')