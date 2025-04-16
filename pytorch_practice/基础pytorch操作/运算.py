import torch

a = torch.randn(3,2,3)
b = torch.ones(2,3)
c = torch.randn(3,4)
d = torch.randn(1,3,4)

#不改变矩阵形状,只适用于元素之间的运算
# c = a+b
# c = a-b
# c = a*b
# c = a/b
# c = a//b
# c = a.pow(2)    #次方指令,等价于**
# c = c.sqrt()    #开平方根
# c = c.rsqrt()   #平方根分之一
# e = torch.exp(b)  #以e为底数,每个元素为指数进行计算
# e = torch.log(e)    #log运算,log默认以e为底
# e = torch.log10(b)  #log后面接数字可以修改底数

f = torch.tensor(3.1415926)
# e = f.floor() #向下取整
# e = f.ceil()    #向上取整
# e = f.trunc()   #裁剪整数部分
# e = f.frac()    #裁剪小数部分
# e = f.round()   #四舍五入

# e = torch.mm(b,c)  #mm矩阵相乘只适用于二维矩阵
# e = torch.matmul(a,d)  #matmul可以适用于多维矩阵,但除最后两个维度外的其他维度必须相等,最后两个维度按照普通矩阵乘法规则相乘
# e = a@d   #matmul的简写,  matmul适用于broadingcasting规则,可以自动扩展维度

grad = torch.randn(2,3)*15
# e = grad.max() #最大的一个元素
# e = grad.min()    #最小的一个元素
# e = grad.median()   #中间值
# e = grad.abs()  #所有元素进行绝对值运算并生成新的矩阵
# e = grad.clamp(10)  #将所有小于参数的元素变为该参数
# e = grad.clamp(0,10)    #同时规定所有元素的最大值和最小值



print(grad)
print(e)
# print(e.shape)

