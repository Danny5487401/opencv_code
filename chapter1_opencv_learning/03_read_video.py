### 数据读取-视频
"""
- cv2.VideoCapture可以捕获摄像头，用数字来控制不同的设备，例如0,1。
- 如果是视频文件，直接指定好路径即可。

"""
import cv2 #opencv读取的格式是BGR
vc = cv2.VideoCapture('../photos/test.mp4')


# 检查是否打开正确
if vc.isOpened():
    open, frame = vc.read()
else:
    open = False

while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        if cv2.waitKey(100) & 0xFF == 27:  # ESC
            break
vc.release()
cv2.destroyAllWindows()