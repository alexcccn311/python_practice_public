import random
import numpy as np
import torch
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def function(position_):
    return (position_[0] ** 2 + position_[1] - 11) ** 2 + (position_[0] + position_[1] ** 2 - 7) ** 2

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
position = np.meshgrid(x, y)
z = function(position)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(position[0], position[1], z)


current_position = torch.tensor([random.uniform(-5,6),random.uniform(-5,5)],requires_grad=True,device='cuda')
print(f'ini_position: {current_position}')
optimizer = torch.optim.Adam([current_position], lr=1e-2)
for i in range(10000):
    optimizer.zero_grad()
    z1 = function(current_position)
    z1.backward()
    optimizer.step()
    if i % 1000 == 0:
        print(f'x: {current_position[0]} y: {current_position[1]} z: {z1}')
final_position = current_position.detach().cpu().numpy()
final_z = function(final_position)

# 在图中标记最低点
ax.scatter(final_position[0], final_position[1],z = final_z, color='red',s = 50, label='Found Minimum')

# 添加图例和标题
ax.set_zlim(np.min(z), np.max(z))
ax.set_title('3D Surface Plot with Found Minimum')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

# 显示图像
plt.show()
