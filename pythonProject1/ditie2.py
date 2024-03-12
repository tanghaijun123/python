# import cv2
# import numpy as np
#
# def find_and_draw_contours(image, lower_color, upper_color, color, color_name):
#     # 转换颜色空间到HSV
#     hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     # 根据颜色阈值创建掩码
#     mask = cv2.inRange(hsv_image, lower_color, upper_color)
#     # 查找轮廓
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
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
#     # 计算矩形对角线长度作为线段的近似长度
#     diagonal_length = np.sqrt(w**2 + h**2)
#     print(f"Approximate length of {color_name} line based on diagonal: {diagonal_length} pixels.")
#
#     # 根据给定的比例计算段数
#     # 注意：如果之前的比例基于实际的长度估计，可能需要调整这里的基准长度
#     average_length_per_segment = 495/16  # 示例中的基准比例
#     estimated_segments = round(diagonal_length / average_length_per_segment)
#     print(f"Estimated number of segments in {color_name} line: {estimated_segments}")
#
#     return image
#
# # 主程序部分
# def main():
#     # 替换为你的图像路径
#     image_path = 'ditie.jpg'
#     image = cv2.imread(image_path)
#
#     # 定义颜色的HSV阈值及名称
#     colors_info = [
#         (np.array([0, 120, 70]), np.array([10, 255, 255]), (0, 0, 255), "red"),
#         (np.array([103, 50, 50]), np.array([175, 255, 255]), (255, 0, 0), "blue"),
#         (np.array([50, 100, 100]), np.array([70, 255, 255]), (0, 255, 0), "green")
#     ]
#
#     # 分别处理每种颜色的线条
#     for lower_color, upper_color, color, color_name in colors_info:
#         image = find_and_draw_contours(image, lower_color, upper_color, color, color_name)
#
#     # 显示结果图像
#     cv2.imshow('Detected Lines', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# if __name__ == "__main__":
#     main()
