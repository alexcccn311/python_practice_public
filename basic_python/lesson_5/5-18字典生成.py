# 作者：Alex
# 2024/9/27 下午11:12
import random

d = {item: random.randint(1, 100) for item in range(1, 11)}
print(d)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = ['性奴', '主人', '母狗', '厕奴', '狗奴', '男奴', '鞋奴', '脚奴', '贱奴', '婊子']
d = {key: value for value, key in zip(lst2, lst)}
print('d',d)

e = {item: random.choice(lst2) for item in range(1, len(lst2) + 1)}
print('e1',e)

e[11] = '贱奴'
print(e)
keys = e.keys()
print(list(keys))
print(tuple(e.values()))
print(list(e.items()))
print(dict(list(e.items())))
print(e.pop(8))
print(e)
print(e.pop(14, '不存在'))
print(e.popitem())
print(e.pop(random.choice(list(e.keys()))))
print(e)