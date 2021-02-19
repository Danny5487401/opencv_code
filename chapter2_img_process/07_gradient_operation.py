### 梯度运算

import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB


# 梯度=膨胀-腐蚀
pie = cv2.imread('../photos/pie.png')
kernel = np.ones((7,7),np.uint8)
dilate = cv2.dilate(pie,kernel,iterations = 5)
erosion = cv2.erode(pie,kernel,iterations = 5)

res = np.hstack((dilate,erosion))

# cv2.imshow('res', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# gradient = cv2.morphologyEx(pie, cv2.MORPH_GRADIENT, kernel)
#
# cv2.imshow('gradient', gradient)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
### 礼帽与黑帽  #OpenCV(4.5.1)这版本没有
- 礼帽 = 原始输入-开运算结果
- 黑帽 = 闭运算-原始输入
"""
# img = cv2.imread('dige.png')
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# cv2.imshow('tophat', tophat)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread('dige.png')
# blackhat  = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT, kernel)
# cv2.imshow('blackhat ', blackhat )
# cv2.waitKey(0)
# cv2.destroyAllWindows()