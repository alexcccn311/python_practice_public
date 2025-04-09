# 作者：Alex
# 2024/9/28 上午6:12
from datetime import datetime
lst=[ 87, 76, 87, 90, 67, '02', '03', 00, 86, 92, 98]
for index in range (len(lst)):
    if int(lst[index]) < 10:
        lst[index] = str(int(lst[index]) + 2000)
    else:
        lst[index] = str(int(lst[index]) + 1900)
print(lst)

current_year = int(datetime.now().year)
age = []

for index in range (len(lst)):
    age.append(str(current_year - int(lst[index])))
print(age)