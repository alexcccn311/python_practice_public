# 作者：Alex
# 2024/10/13 18:01
"""
方法:
    re.findall: 所有符合条件的目标
    re.search: 第一个符合条件的匹配对象,如果找不到则返回 None。
    re.match: 只匹配字符串的开头部分。如果开头没有匹配项，则返回 None。
    re.split: 按照匹配目标进行拆分,拆分后的每一个部分作为一个对象放入列表.
    re.sub: 将传入的字符串替换符合条件的字符串
    re.compile: 将正则表达式编译成正则对象(类似于将某种检索方式变为一个实例)，供多次使用，提升效率。
    re.fullmatch: 如果整个字符串与正则表达式完全匹配，则返回匹配对象；否则返回 None
    re.finditer: 返回一个迭代器，包含所有匹配对象（包含详细的位置信息）。

目标:
    'd': 数字, 's': 空格 字母、'w': 数字和下划线
    'D':非数字, 'S':非空格, 'W':非字母,数字和下划线, [word]: []中的任意字符都是目标, (ab):将括号内作为一个整体去进行匹配
数量:
    '+':一个或多个, '.':任意字符, '?': 0个或1个, '*': 0个或多个, {int}: 连续几个, {int,}:至少连续几个, {int,int}: 连续几个到几个的范围
结构:
    ^:开头,  |: 或,
特殊:
    '\.':匹配转义字符.,该方法只能匹配转义字符., [\u4e00-\u9fa5]: UTF8中文编码范围
"""
import re


result = re.findall(r'a.c', 'abc adc aec') #匹配 a 后跟任意字符，再跟 c
print(result)  # 输出 ['abc', 'adc', 'aec']

result = re.findall(r'\w+', 'Hello_123!')  #匹配所有字母、数字和下划线组成的字符序列。
print(result)  # 输出 ['Hello_123']

result = re.findall(r'\W+', 'Hello_123!')  #匹配非字母、数字或下划线的字符。
print(result)  # 输出 ['!']

result = re.findall(r'\s', 'Hello World')  #匹配空格或其他空白字符。
print(result)  # 输出 [' ']

result = re.findall(r'\S+', 'Hello World')  #匹配非空白字符的序列。
print(result)  # 输出 ['Hello', 'World']

result = re.findall(r'\d+', 'My age is 25')  #匹配数字字符。
print(result)  # 输出 ['25']

result = re.findall(r'colou?r', 'color colour') #匹配color或colour，因为u出现0次或1次。
print(result)  # 输出 ['color', 'colour']

result = re.findall(r'ab+', 'abb bbb a abbbb aa') #匹配a+一个或多个b。
print(result)  # 输出 ['abb', 'abbbb']

result = re.findall(r'ab*', 'abb a abbbb aa') #匹配0次或多次b。
print(result)  # 输出 ['abb', 'abbbb', 'a']

result = re.findall(r'\d{3}', 'My phone number is 1234567890') #匹配3个连续的数字。
print(result)  # 输出 ['123', '456', '789']

result = re.findall(r'a{2,}', 'aaa a aa') #匹配两个或更多的a。
print(result)  # 输出 ['aaa', 'aa']

result = re.findall(r'a{2,3}', 'aaa a aa aaaa') #匹配2到3次a
print(result)  # 输出 ['aaa', 'aa']

result = re.findall(r'[aeiou]', 'hello world') #匹配[aeiou]中的任意字母。
print(result)  # 输出 ['e', 'o', 'o']

result = re.findall(r'^Hello', 'Hello world') #匹配字符串以Hello开头。
print(result)  # 输出 ['Hello']

result = re.findall(r'cat|dog', 'I love my cat and dog') #匹配cat或dog。
print(result)  # 输出 ['cat', 'dog']

result = re.findall(r'\.', 'www.example.com') #\. 匹配真实的句点，而不是任意字符。
print(result)  # 输出 ['.', '.']

result = re.findall(r'[\u4e00-\u9fa5]+', '你好，world') #匹配中文字符。
print(result)  # 输出 ['你好']

result = re.findall(r'(ab)+', 'abababc') #匹配一个或多个ab的组合
print(result)  # 输出 ['ab']
