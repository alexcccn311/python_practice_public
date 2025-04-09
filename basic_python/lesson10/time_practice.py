# 作者：Alex
# 2024/10/27 05:32
import time
import datetime

# print(round(time.time(),2))
# print(time.localtime())

today = datetime.datetime.now()
# print(today)

gap1 = datetime.timedelta(10,hours=10,minutes=30,seconds=11,microseconds= 23)

print(today + gap1)