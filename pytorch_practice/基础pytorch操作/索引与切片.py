import torch
a = torch.rand(4,3,28,28)

# b= a[0]
# b= a[0,0]
# b= a[0,1,27,27]
# b= a[:2]
# b= a[:2,:1]
# b= a[3:,-1:,:28,:]
# b= a[:,:,0:28:2,0:28:4]
# b= a[:,:,::2,0:28:3]
# b= a.index_select(3,torch.arange(0,28,4))
# b = a[...,::3,:,torch.arange(0,28,4)]
# mask = a.ge(0.5)    #ge为新建一个形状与目标张量相同的张量,大于等于给定值的元素变为1,其余元素变为0
# b = torch.masked_select(a, mask)   #masked_select之后只剩下一个维度
b = torch.take(a, torch.arange(0,28,4)) #take会将目标元素转换为1维之后再按给定的序号取元素



print(b)
print(b.type())
print(b.shape)