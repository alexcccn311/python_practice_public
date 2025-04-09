# 作者：Alex
# 2024/9/28 上午1:49
import json


class Person:
    def __init__(self, name, age, profession, gender,permissions,identity):
        self.name = name
        self.age = age
        self.profession = profession
        self.gender = gender
        self.permissions = permissions
        self.identity = identity

    def to_dict(self):
        """将 Person 对象转换为字典格式"""
        return {
            'name': self.name,
            'age': self.age,
            'profession': self.profession,
            'gender': self.gender,
            'permissions': self.permissions,
            'identity': self.identity
        }

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, profession={self.profession}, gender={self.gender}, permissions={self.permissions}, identity={self.identity})"

    def is_named(self, name):
        """检查此人是否有给定的名字"""
        return self.name == name

