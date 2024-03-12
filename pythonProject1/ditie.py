# import cv2
# import numpy as np
#
#
# def find_and_draw_contours(image, lower_color, upper_color, color):
#     # 转换颜色空间到HSV
#     hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     # 根据颜色阈值创建掩码
#     mask = cv2.inRange(hsv_image, lower_color, upper_color)
#     # 查找轮廓
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # 如果没有找到轮廓，则直接返回图像
#     if not contours:
#         return image
#
#     # 合并轮廓
#     # 使用 np.vstack 合并轮廓时需要确保轮廓作为列表传入
#     contours = np.vstack(contours).squeeze()
#
#     # 计算合并后轮廓的边界矩形
#     x, y, w, h = cv2.boundingRect(contours)
#
#     # 绘制矩形框
#     cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
#
#     return image
#
#
# # 读取图像
# image = cv2.imread('ditie.jpg')
#
# # 定义颜色的HSV阈值
# # 注意：这里的阈值可能需要根据你的图像进行调整
# lower_red = np.array([0, 120, 70])
# upper_red = np.array([10, 255, 255])
# lower_blue = np.array([100, 50, 50])
# upper_blue = np.array([130, 255, 255])
# lower_green = np.array([50, 100, 100])
# upper_green = np.array([70, 255, 255])
#
# # 分别处理每种颜色的线条
# image = find_and_draw_contours(image, lower_red, upper_red, (0, 0, 255))  # 红色线条用蓝色框
# image = find_and_draw_contours(image, lower_blue, upper_blue, (255, 0, 0))  # 蓝色线条用红色框
# image = find_and_draw_contours(image, lower_green, upper_green, (0, 255, 0))  # 绿色线条用绿色框
#
# # 显示结果图像
# cv2.imshow('Detected Lines', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
#
# def find_and_draw_contours(image, lower_color, upper_color, color, color_name):
#     # 转换颜色空间到HSV
#     hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     # 根据颜色阈值创建掩码
#     mask = cv2.inRange(hsv_image, lower_color, upper_color)
#     # 查找轮廓
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # 如果没有找到轮廓，则直接返回图像
#     if not contours:
#         print(f"No contours found for {color_name}.")
#         return image
#
#     # 合并轮廓
#     all_contours = np.vstack(contours).squeeze()
#
#     # 计算合并后轮廓的边界矩形
#     x, y, w, h = cv2.boundingRect(all_contours)
#
#     # 绘制矩形框
#     cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
#
#     # 计算并打印长度
#     length = cv2.arcLength(all_contours, True)
#     print(f" {color_name} 长度: {length} pixels.")
#
#     return image
#
#
# # 读取图像
# image = cv2.imread('ditie.jpg')
#
# # 定义颜色的HSV阈值及名称
# colors_info = [
#     (np.array([100, 50, 50]), np.array([130, 255, 255]), (255, 0, 0), "1号线"),
#     (np.array([0, 120, 70]), np.array([10, 255, 255]), (0, 0, 255), "2号线"),
#     (np.array([50, 100, 100]), np.array([70, 255, 255]), (0, 255, 0), "4号线")
# ]
#
# # 分别处理每种颜色的线条
# for lower_color, upper_color, color, color_name in colors_info:
#     image = find_and_draw_contours(image, lower_color, upper_color, color, color_name)
#
# # 显示结果图像
# cv2.imshow('Detected Lines', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np


def find_and_draw_contours(image, lower_color, upper_color, color, color_name):
    # 转换颜色空间到HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 根据颜色阈值创建掩码
    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    # 查找轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 如果没有找到轮廓，则直接返回图像
    if not contours:
        print(f"No contours found for {color_name}.")
        return image

    # 合并轮廓
    all_contours = np.vstack(contours).squeeze()

    # 计算合并后轮廓的边界矩形
    x, y, w, h = cv2.boundingRect(all_contours)

    # 绘制矩形框
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

    # 计算并打印长度
    length = cv2.arcLength(all_contours, True)
    print(f"Length of {color_name} line: {length} pixels.")

    # 根据给定的比例计算段数
    average_length_per_segment = 2266 / 21
    estimated_segments = round(length / average_length_per_segment)
    print(f" {color_name}站数: {estimated_segments}")

    return image


# 读取图像
image = cv2.imread('ditie.jpg')

# 定义颜色的HSV阈值及名称
colors_info = [
    (np.array([0, 120, 70]), np.array([10, 255, 255]), (0, 0, 255), "2号线"),
    (np.array([103, 50, 50]), np.array([160, 255, 255]), (255, 0, 0), "1号线"),
    (np.array([50, 100, 100]), np.array([70, 255, 255]), (0, 255, 0), "4号线")
]

# 分别处理每种颜色的线条
for lower_color, upper_color, color, color_name in colors_info:
    image = find_and_draw_contours(image, lower_color, upper_color, color, color_name)

# 显示结果图像
cv2.imshow('Detected Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
