### 图像平滑

import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB


img=cv2.imread('../photos/lenaNoise.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 均值滤波
# # 简单的平均卷积操作
blur = cv2.blur(img, (3, 3))
#
# cv2.imshow('blur', blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 方框滤波
# 基本和均值一样，可以选择归一化
# box = cv2.boxFilter(img,-1,(3,3), normalize=True)
#
# cv2.imshow('box', box)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 方框滤波
# 基本和均值一样，未归一化,容易越界
# box = cv2.boxFilter(img,-1,(3,3), normalize=False)
#
# cv2.imshow('box', box)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 高斯滤波
# 高斯模糊的卷积核里的数值是满足高斯分布，相当于更重视中间的
aussian = cv2.GaussianBlur(img, (5, 5), 1)

# cv2.imshow('aussian', aussian)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 中值滤波
# 相当于用中值代替  此案例最好
median = cv2.medianBlur(img, 5)  # 中值滤波

# cv2.imshow('median', median)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 展示所有的
res = np.hstack((blur,aussian,median))
#print (res)
cv2.imshow('median vs average', res)
cv2.waitKey(0)
cv2.destroyAllWindows()