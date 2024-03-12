import cv2
import numpy as np

# 读取图像
image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gray_blurred = cv2.GaussianBlur(gray, (9, 9), 0)

# 执行 Canny 边缘检测
edges = cv2.Canny(gray_blurred, 50, 100)

# Hough 圆变换识别圆形图案
circles = cv2.HoughCircles(edges,
                           cv2.HOUGH_GRADIENT, dp=1.3, minDist=80,
                           param1=100, param2=50, minRadius=10, maxRadius=100)


if circles is not None:

    circles_round = np.round(circles[0, :]).astype("int")

    # 绘制圆圈和其中心
    for (x, y, r) in circles_round:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

# 显示结果
cv2.imshow('Detected Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
