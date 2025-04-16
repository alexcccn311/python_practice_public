import torch

a = torch.randn(5,3,28,28)

# b = a.view(5,3,28*28)
b = a.unsqueeze(0).unsqueeze(0).unsqueeze(-1)
# c = b.squeeze()
# c = b.squeeze(-1)
# c = b.expand(2,3,5,3,28,28,4)  #扩展的维度原维度必须为1,但它不会复制数据，而是通过广播（broadcasting）机制共享内存，节省内存。
# c = b.expand(2,3,5,-1,-1,-1,4)  #-1表示该维度不变
# c = b.repeat(3,1,1,1,1,1,1)  #expand是直接给维度赋值,而repeat是维度乘法.repeat用来复制张量的元素。如果你需要精确地复制张量的内容，可以使用 repeat。

# b = torch.randn(5,3)
# c = b.t()  #.t方法只适用于二维矩阵,高维张量无法使用
# c = b.transpose(2, 3)
c = b.permute(0,1,3,2,6,5,4).contiguous()  #permute可以同时交换多个维度  contiguous()不会改变张量中元素的实际位置，它只会 调整数据在内存中的存储位置，以确保数据按顺序存储，从而提升运行效率

# print(b)
print(f'b的形状: {b.shape}')
print(f'c的形状: {c.shape}')