
### Canny边缘检测

import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB
"""
- 1)        使用高斯滤波器，以平滑图像，滤除噪声。

- 2)        计算图像中每个像素点的梯度强度和方向。

- 3)        应用非极大值（Non-Maximum Suppression）抑制，以消除边缘检测带来的杂散响应。

- 4)        应用双阈值（Double-Threshold）检测来确定真实的和潜在的边缘。

- 5)        通过抑制孤立的弱边缘最终完成边缘检测。
"""
#### 1:高斯滤波器
# canny_1.png

#### 2:梯度和方向
# canny_2.png

#### 3：非极大值抑制
#(canny_3.png)
# canny_6.png

#### 4：双阈值检测
#(canny_5.png)


def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey()
    cv2.destroyAllWindows()

img = cv2.imread('../photos/lena.jpg',cv2.IMREAD_GRAYSCALE)
cv_show(img,'img')

img=cv2.imread("../photos/lena.jpg",cv2.IMREAD_GRAYSCALE)

v1=cv2.Canny(img,80,150)
v2=cv2.Canny(img,50,100)

res = np.hstack((v1,v2))
cv_show(res,'res')
