# 作者：Alex
# 2025/1/10 10:45
import torch
import torch.nn.functional as F

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
a = torch.linspace(-10, 10, 11,device=device,requires_grad=True)    #创建张量时,只有设定为required_grad才能进行求导计算,否则会报错.也可以在创建后通过.required_grad_()方法来补充梯度计算图
# b = F.sigmoid(a)    #也可以直接通过torch.sigmoid直接使用sigmoid函数
c = F.tanh(a)   #也可以直接通过torch.tanh直接使用tanh函数
d = F.relu(a)        #Relu函数.也可以直接通过torch.relu直接使用relu函数
# e = F.mse_loss(b, c, reduction='mean')

# grad_outputs = torch.ones_like(b)
# f = torch.autograd.grad(b,a,grad_outputs=grad_outputs, create_graph=True) #如果outputs为张量,必须有一个与outputs形状相同的矩阵来描述权重.pytorch会根据权重将outputs这个张量转换为一个标量与每个x进行计算.
#本质上来说就是y=f(x),第一个值是y,第二个值是x(可以为张量)然后对x求导


# b = a.sum()
# b.backward()    #backward只能对标量使用  y=f(x),将b设定为y,然后它的所有变量都会附带它的导数(隐藏显示,需要通过.grad方法查看)


b = F.softmax(a,dim=0)  #必须指定维度,即使只有一维.  概率分布的首选激活函数
# b.backward()
for x in range(11):
    loss = torch.autograd.grad(b[x],a,retain_graph=True)
    print(loss)     #所有的loss加起来就是一个雅可比矩阵
# b = b.sum()







# print(a)
# print(a.grad)
print(b)
# print(b.grad)
# print(c)
# print(d)
# print(e)
# print(f)
print(loss)