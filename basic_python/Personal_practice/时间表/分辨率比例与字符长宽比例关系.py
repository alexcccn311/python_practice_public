import os
import shutil


def measure_terminal_size():
    columns, rows = shutil.get_terminal_size()
    return columns, rows


def calculate_char_aspect_ratio():
    columns, rows = measure_terminal_size()

    # 假设显示器的分辨率（以像素为单位）
    screen_width_pixels = 1920
    screen_height_pixels = 1080

    # 计算每个字符的宽度和高度（以像素为单位）
    char_width_pixels = screen_width_pixels / columns
    char_height_pixels = screen_height_pixels / rows

    # 计算字符的长宽比例
    aspect_ratio = char_height_pixels / char_width_pixels
    return aspect_ratio


aspect_ratio = calculate_char_aspect_ratio()
print(f"字符的长宽比例: {aspect_ratio:.2f}")

print(16*1.88)
