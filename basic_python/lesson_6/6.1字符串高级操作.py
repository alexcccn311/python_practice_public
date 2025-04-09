# 作者：Alex
# 2024/10/13 13:40
str_1 = "I'm Alex"
str_2 = str_1.lower()
print(str_2)
str_3 = str_2.upper()
print(str_3)

list_1 = '1,2,3,我,5,c,7,我,9'
list_2 = list_1.split(',')
print(list_2)
"""list_count = list_1.count(',')
print(list_count)
list_int_count = sum(1 for item in list_1 if item.isdigit())
print(list_int_count)

print(list_1.find('我'))
print(list_1.find('你'))

print(list_1.index('3'))
try:
    print(list_1.index('你'))
except ValueError:
    print('没找到')

print('demo.py'.endswith('.py'))
print('demo.py'.endswith('.php'))
print('demo.py'.startswith('.py'))
print('demo.py'.startswith('de'))

s= 'hello world'
s1 = s.replace('o','你',1)
print(s1)

print(s.center(20,'*'))

s ='    Hello World    '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s1 ='lll-hello-world'
print(s1.strip('rld'))
print(s1.rstrip('rld'))
print(s1.lstrip('rld'))"""