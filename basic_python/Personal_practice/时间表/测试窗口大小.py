import tkinter as tk  # 导入 tkinter 库用于显示弹窗
from tkinter import font  # 导入 font 模块用于设置字体

def show_popup():
    """
    显示弹窗提示的函数。
    """
    root = tk.Tk()
    root.title("测试窗口")  # 设置弹窗标题

    # 设置窗口总是置顶
    root.attributes("-topmost", True)

    # 设置窗口大小
    window_width = 350
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")  # 设置窗口大小

    # 获取屏幕尺寸以计算窗口居中的位置
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"+{position_x}+{position_y}")  # 设置窗口位置

    # 创建一个包含标签和按钮的框架
    frame = tk.Frame(root)
    frame.pack(expand=True)

    # 设置自定义字体
    custom_font = font.Font(family="Helvetica", size=13, weight="bold")

    label = tk.Label(frame, text="这是一个测试窗口", padx=20, pady=5, font=custom_font)  # 创建显示消息的标签，并设置字体
    label.pack(pady=10)  # 设置标签与框架边界的垂直外边距

    button = tk.Button(frame, text="确定", command=root.destroy, padx=20, pady=5, font=custom_font)  # 创建关闭弹窗的按钮，并设置字体
    button.pack(pady=2)  # 设置按钮与标签之间的垂直外边距

    root.mainloop()  # 进入 tkinter 的主循环

# 立即显示弹窗
show_popup()