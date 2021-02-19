### 形态学-膨胀操作
import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB

# img = cv2.imread('../photos/dige.png')
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# kernel = np.ones((3,3),np.uint8)
# erosion = cv2.erode(img,kernel,iterations = 1)
#
# cv2.imshow('erosion', erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # 膨胀
# kernel = np.ones((3,3),np.uint8)
# dige_dilate = cv2.dilate(erosion,kernel,iterations = 1)
#
# cv2.imshow('dilate', dige_dilate)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


pie = cv2.imread('../photos/pie.png')

kernel = np.ones((30,30),np.uint8)
dilate_1 = cv2.dilate(pie,kernel,iterations = 1)
dilate_2 = cv2.dilate(pie,kernel,iterations = 2)
dilate_3 = cv2.dilate(pie,kernel,iterations = 3)
res = np.hstack((dilate_1,dilate_2,dilate_3))
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()