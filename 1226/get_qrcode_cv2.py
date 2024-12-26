# 安装 cv2 库
# pip install opencv-python
# opencv-python 是一个 Python 的计算机视觉库，它包含了许多用于图像处理和计算机视觉的函数和算法，例如图像的读取、写入、显示、转换、滤波、特征提取、目标检测、跟踪、识别、分类、聚类、回归、深度学习等
import cv2

# 读取图片
# imread() 函数用于读取图片，它的参数为一个文件名，返回一个图像对象
cv_img= cv2.imread("./1226/qr.jpg")

# 检测二维码
# QRCodeDetector 类是 opencv-python 库中的一个类，用于检测二维码，它的 detectAndDecode() 方法用于检测二维码并解码，它的参数为一个图像对象，返回值为一个元组，包含二维码的数据、二维码的边界框和二维码的状态
qr_detect= cv2.QRCodeDetector()
# detectAndDecode() 方法的返回值为一个元组，包含二维码的数据、二维码的边界框和二维码的状态，其中：
# 二维码的数据为一个字符串，如果没有检测到二维码，则返回一个空字符串
# 二维码的边界框为一个列表，包含二维码的四个角的坐标，如果没有检测到二维码，则返回一个空列表
data, bbox, st_qrcode= qr_detect.detectAndDecode(cv_img)
print(f"QRCode data:\n{data}")