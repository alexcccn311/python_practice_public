# 作者：Alex
# 2024/9/28 上午12:30
import json


class Person:
    def __init__(self, name, age, profession, gender, permissions, identity):
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


def load_from_jsonl(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            person_data = json.loads(line)  # 解析每一行 JSON 数据
            person_instance = Person(**person_data)  # 创建 Person 实例
            # 使用 globals() 创建一个全局变量，名字为 person_instance.name
            globals()[person_instance.name] = person_instance  # 直接将 Person 实例化为全局变量


a = {'性奴', '主人', '母狗', '厕奴', '狗奴', '男奴', '鞋奴', '脚奴', '贱奴', '婊子'}
print(a)
print(a.issubset(a))

s = {'性奴', '贱奴', '厕奴', '主人', '母狗', '厕奴', '狗奴', '男奴', '鞋奴', '脚奴', '贱奴', '婊子'}
print(s)
print('max:', max(s))
print('min:', min(s))
print('len:', len(s))
print('性奴在集合s中存在么？', ('性奴' in s))

load_from_jsonl('../../data/people_data.jsonl')

print(CC.profession)  # 直接使用 CC 的实例，输出职业
print(张卉晨.profession)  # 直接使用 张卉晨 的实例，输出职业
print(李婷.profession)


def personal_information(name):
    name = eval(name)
    profession_status = "在" if name.profession in s else "不在"
    if name:
        print(
            f"{name.name}是{name.identity}，具体职业为{name.profession}，权限等级为{name.permissions}，{name}的职业{profession_status}职业列表s中")
    else:
        print(f'没有找到名字为{name}的人。')


personal_information('张卉晨')

print(f'{CC.profession}')
if CC:
    if CC.profession in s:
        print(f"CC是{CC.identity}，具体职业为{CC.profession}，权限等级为{CC.permissions}")
    else:
        print(f"CC 是公民")
else:
    print("没有找到名字为 CC 的人。")

del s
try:
    print(s)
except NameError:
    print("s不存在")
