### 开运算与闭运算

import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB


# # 开：先腐蚀，再膨胀
# img = cv2.imread('../photos/dige.png')
#
# kernel = np.ones((5,5),np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#
# cv2.imshow('opening', opening)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 闭：先膨胀，再腐蚀
# img = cv2.imread('../photos/dige.png')
#
# kernel = np.ones((5,5),np.uint8)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#
# cv2.imshow('closing', closing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()