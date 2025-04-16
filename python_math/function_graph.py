import numpy as np
import matplotlib.pyplot as plt

# 1. 定义 x 的取值范围
def f(x):
    return 1.0/(1.0+np.exp(-x))

x = np.linspace(-10, 10, 1000)
y = f(x)

# 3. 绘制函数图像
plt.plot(x, y, label=r'$label$', color='blue')  # 绘制曲线，添加标签和颜色

# 4. 添加辅助线（x轴和y轴）
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # 水平线（x轴）
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # 垂直线（y轴）

# 5. 添加标题和坐标轴标签
plt.title("tittle$")  # 图像标题
plt.xlabel("x")  # x轴标签
plt.ylabel("$y$")  # y轴标签

# 6. 添加网格和图例
plt.grid(alpha=0.3)  # 设置网格线的透明度
plt.legend()  # 显示图例

# 7. 显示图像
plt.show()
