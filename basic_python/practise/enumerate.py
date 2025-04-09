lst = ['a','b','c','d','e']
for item in lst:
    print(item)
f = len(lst)
print(f)
for i in range(0,len(lst)):
    print(i,'-->',lst[i])
for index,value in enumerate(lst,5):
    print(index,'-->',value)