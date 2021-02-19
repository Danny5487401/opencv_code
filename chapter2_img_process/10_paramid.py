import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB
### 图像金字塔  放大缩小
"""
- 高斯金字塔
- 拉普拉斯金字塔
Pyramid_1.png
"""

#### 高斯金字塔：向下采样方法（缩小）
# Pyramid_2.png

#### 高斯金字塔：向上采样方法（放大）
# Pyramid_3.png


def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey()
    cv2.destroyAllWindows()


img=cv2.imread("../photos/AM.png")
cv_show(img,'img')
print(img.shape)

up=cv2.pyrUp(img)
cv_show(up,'up')
print (up.shape)

# down=cv2.pyrDown(img)
# cv_show(down,'down')
# print (down.shape)
#
# up2=cv2.pyrUp(up)
# cv_show(up2,'up2')
# print (up2.shape)

up=cv2.pyrUp(img)
up_down=cv2.pyrDown(up)
cv_show(up_down,'up_down')

cv_show(np.hstack((img,up_down)),'up_down')

up=cv2.pyrUp(img)
up_down=cv2.pyrDown(up)
cv_show(img-up_down,'img-up_down')

#### 拉普拉斯金字塔
#Pyramid_4.png

down=cv2.pyrDown(img)
down_up=cv2.pyrUp(down)
l_1=img-down_up
cv_show(l_1,'l_1')
