import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB


def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey()
    cv2.destroyAllWindows()

#### 直方图均衡化
"""
(hist_2.png)
hist_3.png
hist_4.png
"""

img = cv2.imread('./photos/clahe.jpg',0) #0表示灰度图 #clahe
plt.hist(img.ravel(),256)
plt.show()

equ = cv2.equalizeHist(img)
plt.hist(equ.ravel(),256)
plt.show()

res = np.hstack((img,equ))
cv_show(res,'res')

#### 自适应直方图均衡化  效果比较好

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
res_clahe = clahe.apply(img)
res = np.hstack((img,equ,res_clahe))
cv_show(res,'res')

