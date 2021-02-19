### 灰度图

import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB


img=cv2.imread('../photos/cat.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# print(img_gray.shape)

#
# cv2.imshow("img_gray", img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
### HSV
- H - 色调（主波长）。 
- S - 饱和度（纯度/颜色的阴影）。 
- V值（强度）
"""

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("hsv", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()