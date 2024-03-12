import cv2
import numpy as np

# 读入图像
image = cv2.imread('imagee.jpg')

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用高斯模糊
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 边缘检测
edges = cv2.Canny(blurred, 10, 200)

# 寻找轮廓
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 找到最大的轮廓（假设最大的轮廓是整体外轮廓）
max_contour = max(contours, key=cv2.contourArea)

# 绘制整体外轮廓
cv2.drawContours(image, [max_contour], -1, (255, 0, 0), 2)

# 检测圆形并绘制
for contour in contours:
    # 跳过小轮廓，减少噪声影响
    if cv2.contourArea(contour) > 50:
        # 计算轮廓的近似
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)

        # 检查轮廓是不是圆形
        area = cv2.contourArea(approx)
        (x, y), radius = cv2.minEnclosingCircle(approx)
        circle_area = np.pi * (radius ** 2)

        # 判断实际轮廓面积和圆形面积之间的比率
        if area / circle_area > 0.5:  # 设定一个阈值来确定形状的“圆形度”
            # 绘制圆形轮廓
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(image, center, radius, (0, 255, 0), 2)

# 显示图像
cv2.imshow('Circles and Outer Contour Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()