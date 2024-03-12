import cv2
import numpy as np

# 读入图像
image = cv2.imread('imagee.jpg')

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用高斯模糊
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 边缘检测
edges = cv2.Canny(blurred, 50, 100)

# 寻找轮廓
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 检测并绘制圆或椭圆轮廓
for contour in contours:
    # 跳过小轮廓，减少噪声影响
    if cv2.contourArea(contour) > 30:  # 设定一个面积阈值来避免过小的轮廓
        # 拟合轮廓
        # 计算轮廓的近似
        perimeter = cv2.arcLength(contour, True)
        epsilon = 0.01 * perimeter
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # 检查轮廓是不是圆
        area = cv2.contourArea(approx)
        (x, y), radius = cv2.minEnclosingCircle(approx)
        circle_area = np.pi * (radius ** 2)

        # 判断实际轮廓面积和圆形面积之间的比率
        if area / circle_area > 0.4:
            # 绘制圆形轮廓
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(image, center, radius, (0, 255, 0), 2)

# 显示结果图像
cv2.imshow('Circles Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()