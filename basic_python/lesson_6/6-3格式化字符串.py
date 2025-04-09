# 作者：Alex
# 2024/10/13 14:22
class Slave:
    def __init__(self, name, age, gender, balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance

# 创建实例
Alex = Slave(name='Alex', age=18, gender='male', balance=1.37)
Bob = Slave(name='Bob', age=18, gender='male', balance=1.37)

# 打印属性
print(Alex.name)
print(Alex.age)
print(Alex.gender)
print(Alex.balance)

#占位符
print('姓名:%s, 年龄:%d, 性别:%s, 余额:%.1f'%(Bob.name, Bob.age, Bob.gender, Bob.balance))

# 使用 f-string 打印
print(f'姓名:{Alex.name}, 年龄:{Alex.age}, 性别:{Alex.gender}, 余额:{Alex.balance}')

# 使用 format 方法打印
print('姓名:{0}, 年龄:{1}, 性别:{2}, 余额:{3}'.format(Alex.name, Alex.age, Alex.gender, Alex.balance))

# 使用 vars 方法打印
print('姓名:{name}, 年龄:{age}, 性别:{gender}, 余额:{balance}'.format(**vars(Alex)))

# 使用 __dict__ 方法打印
print('姓名:{name}, 年龄:{age}, 性别:{gender}, 余额:{balance}'.format(**Bob.__dict__))
