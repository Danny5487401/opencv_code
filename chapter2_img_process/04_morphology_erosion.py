import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB

### 形态学-腐蚀操作


# img = cv2.imread('../photos/dige.png')

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#腐蚀
# kernel = np.ones((3,3),np.uint8)
# erosion = cv2.erode(img,kernel,iterations = 1)
#
# cv2.imshow('erosion', erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

pie = cv2.imread('../photos/pie.png')

# cv2.imshow('pie', pie)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# kernel = np.ones((30,30),np.uint8)
# erosion_1 = cv2.erode(pie,kernel,iterations = 1)
# erosion_2 = cv2.erode(pie,kernel,iterations = 2)
# erosion_3 = cv2.erode(pie,kernel,iterations = 3)
# res = np.hstack((erosion_1,erosion_2,erosion_3))
# cv2.imshow('res', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


