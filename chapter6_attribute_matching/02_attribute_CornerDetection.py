### 图像特征-harris角点检测(harris_1.png)

#### 基本原理
"""
(harris_2.png)
(harris_9.png)
(harris_4.png)
(harris_5.png)
(harris_6.png)
(harris_11.png)

"""

#### cv2.cornerHarris()
"""
- img： 数据类型为 ﬂoat32 的入图像
- blockSize： 角点检测中指定区域的大小
- ksize： Sobel求导中使用的窗口大小 
- k： 取值参数为 [0,04,0.06]
"""

import cv2
import numpy as np

img = cv2.imread('./images/test_1.jpg')
print('img.shape:', img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
print('dst.shape:', dst.shape)

img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
