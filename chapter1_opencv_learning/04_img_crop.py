### 截取部分图像数据
import cv2
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img=cv2.imread('../photos/cat.jpg')
cat=img[0:50,0:200]
cv_show('cat',cat)

### 颜色通道提取
#
# #%%
#
# b,g,r=cv2.split(img)
# print(r.shape)
# img=cv2.merge((b,g,r))
# print(img.shape)
#
# # 只保留R
# cur_img = img.copy()
# cur_img[:,:,0] = 0
# cur_img[:,:,1] = 0
# cv_show('R',cur_img)
#
# # 只保留G
# cur_img = img.copy()
# cur_img[:,:,0] = 0
# cur_img[:,:,2] = 0
# cv_show('G',cur_img)
#
# #%%
#
# # 只保留B
# cur_img = img.copy()
# cur_img[:,:,1] = 0
# cur_img[:,:,2] = 0
# cv_show('B',cur_img)

### 边界填充
"""
- BORDER_REPLICATE：复制法，也就是复制最边缘像素。
- BORDER_REFLECT：反射法，对感兴趣的图像中的像素在两边进行复制例如：fedcba|abcdefgh|hgfedcb   
- BORDER_REFLECT_101：反射法，也就是以最边缘像素为轴，对称，gfedcb|abcdefgh|gfedcba
- BORDER_WRAP：外包装法cdefgh|abcdefgh|abcdefg  
- BORDER_CONSTANT：常量法，常数值填充。
"""
top_size,bottom_size,left_size,right_size = (50,50,50,50)

replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_CONSTANT, value=0)

import matplotlib.pyplot as plt
plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()