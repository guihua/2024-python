from PIL import Image, ImageFilter

# 打开一个jpg图像文件
# 当前路径：当前路径下的 1203 文件夹下的 test.jpg
# TODO：相对路径为何不是从 1203 目录开始？
# 绝对路径：/Users/guihua.pgh/workspace/python/2024-python/1203/test.jpg
im = Image.open('1203/test.jpg')

# 应用模糊滤镜
# filter() 方法返回一个新的 Image 对象，是原图的模糊版本
# 模糊滤镜的半径默认值为 2，半径越大，模糊效果越严重
# ImageFilter.BLUR 是一个常量，它表示模糊滤镜，它的值为 ImageFilter.BoxBlur(2)
im2 = im.filter(ImageFilter.BLUR)

# 保存模糊后的图像
# 当前路径：当前路径下的 1203 文件夹下的 blur.jpg
# TODO：不加 1203 路径时，图片会保存到根目录下
im2.save('1203/blur.jpg', 'jpeg')