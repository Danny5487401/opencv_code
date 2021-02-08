### 数值计算

import cv2
import matplotlib.pyplot as plt
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_cat=cv2.imread('../photos/cat.jpg')
img_dog=cv2.imread('../photos/dog.jpg')

img_cat2= img_cat +10
print(img_cat[:5,:,0])

print(img_cat2[:5,:,0])
#相当于% 256
print((img_cat + img_cat2)[:5,:,0] )
print(cv2.add(img_cat,img_cat2)[:5,:,0])


### 图像融合

print(img_cat.shape) # (414, 500, 3)
# 注意宽高
img_dog = cv2.resize(img_dog, (500, 414))
print(img_dog.shape)

res = cv2.addWeighted(img_cat, 0.4, img_dog, 0.6, 0)
plt.imshow(res)

# img=cv2.imread('../photos/cat.jpg')
#
# res = cv2.resize(img, (0, 0), fx=4, fy=4)
# plt.imshow(res)
#
# res = cv2.resize(img, (0, 0), fx=1, fy=3)
# plt.imshow(res)

plt.show()