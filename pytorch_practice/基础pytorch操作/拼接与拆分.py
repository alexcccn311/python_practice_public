# 作者：Alex
# 2025/1/9 09:05
import torch

a = torch.randn(3,3,28,28)
b = torch.randn(3,3,28,28)
c = torch.randn(6,3,28,28)

d = torch.cat([a,b,c],dim=0) #直接拼接
d = torch.stack([a,b],dim=1)  #将多个形状完全相同的张量组成一个新的张量,新建一个维度,该维度的每一个元素对应一个原张量,dim来指定新建维度的位置.
d,e,f = c.split(2,dim=0)    #split拆分命令,可以将张量在指定维度上按照这个部分指定的数量进行拆分.
d,e = c.split([2,1],dim=1)  #split也可以通过列表详细指定拆分的分布
d,e = c.chunk(2,dim=1)  #chunk命令与split类似,chunk命令是直接指定拆分的数量在指定维度上进行平均拆分,即使数量不能整除也可以依次添加.

print(d.shape)