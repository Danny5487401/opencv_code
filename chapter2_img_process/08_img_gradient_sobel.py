### 图像梯度-Sobel算子  获取轮廓

import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB


img = cv2.imread('../photos/pie.png',cv2.IMREAD_GRAYSCALE)
# cv2.imshow("img",img)
# cv2.waitKey()
# cv2.destroyAllWindows()

"""
dst = cv2.Sobel(src, ddepth, dx, dy, ksize)
- ddepth:图像的深度
- dx和dy分别表示水平和竖直方向
- ksize是Sobel算子的大小
"""

def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey()
    cv2.destroyAllWindows()

# 只有半边
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)

# cv_show(sobelx,'sobelx')
# 原因
"""
白到黑是正数，黑到白就是负数了，所有的负数会被截断成0，所以要取绝对值
"""
# 少了垂直中间部分
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
# cv_show(sobelx,'sobelx')

# 少了水平中间部分
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobely = cv2.convertScaleAbs(sobely)
# cv_show(sobely,'sobely')

"""
分别计算x和y，再求和
"""

#完整展示
# sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
# cv_show(sobelxy,'sobelxy')

"""
不建议直接计算
"""
sobelxy=cv2.Sobel(img,cv2.CV_64F,1,1,ksize=3)
sobelxy = cv2.convertScaleAbs(sobelxy)
# cv_show(sobelxy,'sobelxy')



# img = cv2.imread('../photos/lena.jpg',cv2.IMREAD_GRAYSCALE)
# # cv_show(img,'img')
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
# sobelx = cv2.convertScaleAbs(sobelx)
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
# sobely = cv2.convertScaleAbs(sobely)
# sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
# cv_show(sobelxy,'sobelxy')


img = cv2.imread('../photos/lena.jpg',cv2.IMREAD_GRAYSCALE)

sobelxy=cv2.Sobel(img,cv2.CV_64F,1,1,ksize=3)
sobelxy = cv2.convertScaleAbs(sobelxy)
cv_show(sobelxy,'sobelxy')