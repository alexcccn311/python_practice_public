import torch


# a = np.array([1,2,3,4.3,5])
# a = torch.from_numpy(a)


#大写Tensor接受维度,小写tensor接受数据.
# a = torch.tensor([1,2,3,4.2,5])
# a = torch.FloatTensor([2,2.2])
# a = torch.tensor([[2,3.2],[1.2,2.3]])
# a = torch.Tensor(2, 2)

# a = torch.empty(2,3)  #元素随机
# a = torch.FloatTensor(2,3)  #元素随机浮点数
# a = torch.randn(2, 3) #生成标准正态分布（均值为 0，标准差为 1）的随机数。
# a = torch.rand(2, 3) #生成 [0, 1] 区间内的 均匀分布随机数
# b = torch.rand_like(a)
# a = torch.randint(1, 10, [3,3])

#mean:均值 std:方差 torch.full([10],0): 创建一个长度为 10 的张量，其所有值都为 0  torch.arange(1,0,-0.1): 创建一个从 1 递减到 0（不包含 0），步长为 -0.1 的张量
# a = torch.normal(mean= torch.full([10],0,dtype=torch.float32),std= torch.arange(1,0,-0.1))

# a = torch.full([2,3],7,dtype=torch.float32)
# a = torch.full([],7,dtype=torch.float32)
# a = torch.full([1],7,dtype=torch.float32)
# a = torch.arange(-5, 5,1)
# a = torch.range(-5,5,1)
# a = torch.linspace(-5,5,11)
# a = torch.logspace(1,5,5)

# a = torch.ones(2, 3)
# a =  torch.zeros(2,3)   #元素全为0
# a = torch.eye(3)

b= torch.randperm(2)
a = torch.tensor([[1,2],[3,4]])
c = a[b]

print(a)
print(a.type())
# print(b.type())
# print(b)
print(c)
print(c.type())