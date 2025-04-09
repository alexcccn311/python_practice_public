# 作者：Alex
# 2024/9/28 上午5:17
Female_Slave = {'性奴', '母狗', '狗奴', '女奴', '脚奴', '贱奴', '婊子'}
Male_Slave = {'性奴', '公狗', '厕奴', '狗奴', '男奴', '鞋奴', '脚奴', '贱奴'}

print(Female_Slave & Male_Slave)
Salve_profession = Female_Slave | Male_Slave
print(Salve_profession)
print(Female_Slave - Male_Slave)
print(Female_Slave ^ Male_Slave)

Salve_profession.add('家具奴')
print(Salve_profession)
Salve_profession.remove('脚奴')
print(Salve_profession)
# Salve_profession.clear()
# print(Salve_profession)

for item in Female_Slave:
    print(item)

for index, item in enumerate(Female_Slave):
    print(index, '>>', item)

s = {index for index in range(len(Salve_profession)) if index}
print(s)
