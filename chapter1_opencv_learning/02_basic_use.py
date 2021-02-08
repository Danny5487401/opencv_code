"""

数据读取-图像
- cv2.IMREAD_COLOR：彩色图像
- cv2.IMREAD_GRAYSCALE：灰度图像

"""

import cv2 #opencv读取的格式是BGR

import numpy as np


# img=cv2.imread('../photos/cat.jpg')
# print(img.shape)  #(414, 500, 3)
# #图像的显示,也可以创建多个窗口
# cv2.imshow('image',img)
# # 等待时间，毫秒级，0表示任意键终止
# cv2.waitKey(0)
# cv2.destroyAllWindows()



def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img=cv2.imread('../photos/cat.jpg',cv2.IMREAD_GRAYSCALE)
#图像的显示,也可以创建多个窗口
cv2.imshow('image',img)
# 等待时间，毫秒级，0表示任意键终止
cv2.waitKey(10000)
cv2.destroyAllWindows()
#保存
# cv2.imwrite('mycat.png',img)
print(type(img))  # <class 'numpy.ndarray'>