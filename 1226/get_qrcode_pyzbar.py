import cv2
from pyzbar.pyzbar import decode

# 读取图片
cv_img = cv2.imread("./1226/qr.jpg")

# 使用 pyzbar 库检测和解析二维码
decoded_objects = decode(cv_img)

# 打印所有检测到的二维码数据
if decoded_objects:
    for obj in decoded_objects:
        print(f"QRCode data:\n{obj.data.decode('utf-8')}")
else:
    print("No QR codes detected.")
