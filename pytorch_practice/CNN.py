import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import visdom
import numpy as np
from torch.utils.data import DataLoader, TensorDataset, random_split

class ConvolutionalNeuralNetwork(nn.Module):
    def __init__(self):
        super(ConvolutionalNeuralNetwork, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)

class Bottleneck(nn.Module):
    def __init__(self, in_channels, mid_channels, out_channels):
        super(Bottleneck, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, mid_channels, kernel_size=1)  # 降维
        self.conv2 = nn.Conv2d(mid_channels, mid_channels, kernel_size=3, padding=1)  # 处理
        self.conv3 = nn.Conv2d(mid_channels, out_channels, kernel_size=1)  # 升维

    def forward(self, x):
        identity = x  # 原始输入
        out = F.relu(self.conv1(x))  # 降维
        out = F.relu(self.conv2(out))  # 3×3 处理
        out = self.conv3(out)  # 升维
        out += identity  # 残差相加
        return F.relu(out)

class ResBlk(nn.Module):
    def __init__(self, in_channels, mid_channels, out_channels):
        self.conv1 = nn.Conv2d(in_channels, mid_channels, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(mid_channels)
        self.conv2 = nn.Conv2d(mid_channels, mid_channels, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(mid_channels)
        self.conv3 = nn.Conv2d(mid_channels, out_channels, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm2d(out_channels)
        self.extra = nn.Sequential
        if out_channels != in_channels:
            self.extra = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
                nn.BatchNorm2d(out_channels),
            )

    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = F.relu(self.bn2(self.conv2(out)))
        out = self.bn3(self.conv3(out))
        out += self.extra(x)
        return F.relu(out)





w = torch.randn(16, 3, 5, 5)
b = torch.randn(16)
x = torch.rand(10,3,28,28)

# out = F.conv2d(x, w, b, stride=2, padding=2)

# layer = nn.ReLU(inplace=True)
# out = layer(x)

# out = F.relu(x)

# layer = nn.BatchNorm2d(num_features= 3, eps=1e-5, momentum=0.1)
# out = layer(x)

# print(out.shape)
print(layer.running_mean)
print(layer.running_var)
