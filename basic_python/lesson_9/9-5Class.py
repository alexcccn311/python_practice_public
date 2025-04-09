# 作者：Alex
# 2024/10/19 02:20
import random


class Person:
    company = 'International Slave management company' #类属性
    def __init__(self, name,age ,gender,nickname, job, salary,address):  #类中自带self的函数称为类方法
        self.name = name #左侧为实例属性,右侧为局部变量
        self.age = age
        self.gender = gender
        self.nickname = nickname
        self.job = job
        self.salary = salary
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "nickname": self.nickname,
            "job": self.job,
            "salary": self.salary,
            "address": self.address
        }



    #静态方法,静态方法和外部函数一样使用静态参数不能调用类方法和类参数
    @staticmethod
    def fun(a):
        a += 1
        return a

    #类方法
    @classmethod
    def class_fun(cls): #cls是class的简写,能访问类变量和类方法，但无法访问实例变量
        pass


    #创建实例
Alex = Person("Alex",18,'male', 'Alex', 'Slave', '3.5', random.randint(1,100))
Bob = Person('Bob',22,'Male',"Bob","Doctor",12000,random.randint(1000,200000))
Mary = Person("Mary",16,"female","Mary","Teacher",random.randint(1000,200000),random.randint(1000,200000))
Cindy = Person("Cindy",17,"Female","Cindy","Teacher",random.randint(1000,200000),random.randint(1000,200000))

"""dic = {}
dic_person = [Alex,Bob,Mary,Cindy]
for person in dic_person:
    dic[person.name] = person.to_dict()
print(dic)
print(Alex.__dict__)
print(Alex.name)
print(Person.fun(10))"""
Alex.level = 12
print(Alex.__dict__)
print(Alex.level)