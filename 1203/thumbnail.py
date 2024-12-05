from PIL import Image

# 打开一个 jpg 图像文件
# 相对路径，1203/test.jpg
# 绝对路径，/Users/guihua.pgh/workspace/python/2024-python/1203/test.jpg
im = Image.open('1203/test.jpg')

# 获得图像尺寸
# size 是一个 tuple，它的第一个元素是图像的宽度，第二个元素是图像的高度
w, h = im.size
print('Original image size: %sx%s' % (w, h))

# 缩放到 50%
# thumbnail() 方法会保持比例，并且缩略图的尺寸小于等于指定的尺寸
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用 jpeg 格式保存
# 路径为当前路径下的 thumb.jpg，如果没有该路径，会自动创建，如果有同名文件，会自动覆盖
# 路径中不能有中文
im.save('1203/thumbnail.jpg', 'jpeg')
