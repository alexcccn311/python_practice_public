import torch
import random

# 定义函数
def func(x):
    return (x - 13)**2 + torch.sin(x - torch.pi)

# 初始化参数
gap = 0.1
final_x = 0
final_prime_value = float('inf')

# 设置随机种子以保证结果可复现
random.seed(42)
torch.manual_seed(42)

for times in range(1000):
    now_x = torch.tensor(random.uniform(-1, 1), requires_grad=True)
    last_symbol = None

    for time in range(1000):
        # 计算函数值和导数
        y = func(now_x)
        y.backward()  # 自动求导
        f_prime_value = now_x.grad.item()

        if f_prime_value < 0:
            if last_symbol == "positive":
                gap *= 0.5
            now_x = now_x + gap
            last_symbol = 'negative'
        elif f_prime_value > 0:
            if last_symbol == "negative":
                gap *= 0.5
            now_x = now_x - gap
            last_symbol = 'positive'
        else:
            break

        # 清除梯度
        now_x = now_x.detach().requires_grad_(True)

    if abs(f_prime_value) < abs(final_prime_value):
        final_x = now_x.item()
        final_prime_value = f_prime_value

    if abs(final_prime_value) < 1e-3:  # 停止条件
        break

    print(f"当前最低点为 {final_x}, 当前导数为 {final_prime_value}")

print(f"在 x = {final_x} 处，导数值为: {final_prime_value} 为最低点")
