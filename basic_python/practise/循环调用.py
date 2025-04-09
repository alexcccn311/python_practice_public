# 作者：Alex
# 2024/8/29 上午10:59
import math
def f(x):
    if x == 1:
        s =1
    else:
        s=f(x-1)*x
    return s

n=int(input('请输入一个大于1的整数:'))
print(f(n)+f(n-1))

def jiecheng(x):
    y = math.factorial(x)
    return y

print(jiecheng(3))