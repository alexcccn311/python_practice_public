# 作者：Alex
# 2024/10/13 15:22
s = '213123阿第三方'
s_uft = s.encode('utf-8',errors='ignore') #UTF-8中一个汉字占3个字节
print('UTF-8:',s_uft,'UTF-8')

try:
    s_gbk = s.encode('gbk', errors='strict')
    print('GBK:', s_gbk, 'GBK')
    s_gbk_de = s_gbk.decode('gbk', errors='strict')  # 只在编码成功时解码
    print('GBK:', s_gbk_de, 'GBK')
except UnicodeEncodeError:
    print('UnicodeEncodeError')

s_utf_de = s_uft.decode('utf-8',errors='ignore')
print('UTF-8:',s_utf_de,'UTF-')