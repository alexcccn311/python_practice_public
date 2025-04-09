# 作者：Alex
# 2025/1/9 23:21
import torch

# a = torch.full([8],-2.0)
# b = a.view(-1,4)
# c = a.view(-1,2,2)
# d = torch.arange(1,9).view(-1,2).float()

# print(a)
# print(a.norm(1))    #一范数:所有元素的绝对值求和
# print(b.norm(2))    #二范数:所有元素的平方和再开根号
# print(c.norm(2))    #三范数:所有元素的三次方和再开三次根
#
# print(b.norm(1,1))  #对第一个(从0开始算是第二个维度)维度求一次范数,然后再将范数以剩余的维度作为张量返回
# print(c.norm(1,1))

# print(d)
# print(d.sum())  #累加
# print(d.prod()) #累乘
# print(d.mean()) #平均值
# print(d.std())  #方差
# print(d.argmin())   #先将张量降维成一个列表,再返回最小值的序号
# print(d.argmin(dim=0))  #先将张量中指定的维度降维成一个列表,直接返回该维度中最小值的序号
# print(d.argmax(dim=0))   #先将张量中指定的维度降维成一个列表,直接返回该维度中最大值的序号
# print(d.max(dim=0))
# print(d.argmax())   #先将张量降维成一个列表,再返回最大值的序号


# a = torch.randn(3,500,3,28,28)
# max_values, max_indices = a.max(dim=0)  #沿每个维度取最大值,这里选择了第0维度就会依次从[x,0,0,0,0]中遍历x取最大的那个元素,然后继续从[x,0,0,0,1]中遍历取最大值,直到遍历完所有的x.最后会得出一个由各个最大值组成的形状为[500, 3, 28, 28]的张量.max_indices是这些最大值元素的位置也就是x.
# print(max_values.shape)
# b, c = a.max(dim=-1, keepdim=True)  #keepdim:在求最值的同时避免降维,将目标维度作为一维保留维持张量的维度不变.等价于求最值之后再通过unsqueeze(x)在消去的原维度上扩充回来一个维度
# print(b.shape)
# b, c = a.topk(3,1,largest=True)  #类似于max,不过从只求最大值改为求最大的k个值了.可以通过largest来调整求最大值还是最小值
# b ,c = a.kthvalue(3,1,keepdim=False)    #类似于topk,默认largest为fail且不能修改,只选择第x小的那一个对象张量.
# print(b.shape)
# print(c.shape)


a = torch.randn(2,3)
#直接对张量使用比较运算符,是分别将张量中的每一个元素进行比较然后再返回布尔值放入元素原本的位置.python中所有的比较运算符都可以使用
# b = a>0
# b = a==0
b = torch.gt(a,0)   # torch.gt等价于a>0
c = torch.eq(a,b)   #eq是将两个张量中每个相同位置的元素进行比较然后再返回布尔值放入原本的位置
d = torch.equal(a,b)   #只有两个张量的形状完全相同,且每个位置的元素完全相等才返回True,否则返回False

# print(a)
# print(b)
# print(b.dtype)
print(c)
print(d)