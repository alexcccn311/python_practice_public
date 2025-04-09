# 作者：Alex
# 2024/10/13 14:53
s = 'helloworld'
b='我是1'
c='我是2'
print('{0:*<30}\n{1:->30}\n{2:-^30}'.format(s,b,c))

e = 123789.456213
print('{0:,}'.format(e))
print('{0:,.2f}'.format(e))
print('{0:.2}'.format(c))
int_example = 73
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x}'.format(int_example))
print('{0:.2f},{0:E},{0:.3e},{0:.1%}'.format(e))