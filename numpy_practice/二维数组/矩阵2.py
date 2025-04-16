import numpy as np
a = np.array([[1,2],[3,4]])
b = np.ones((1,2))
c = np.eye(2)
d = np.random.randint(1,100, size=(2,2))
#print(a)
#print(b)
#print(c)
print('-'*50)

"""d= np.concatenate((a,b,c),0)
print(d)

print(np.hstack((a,b.T,c)))
print(np.vstack((a,b,c)))
print(np.split(np.array([2,5,28,3]),2,0))
print(np.split(a,2))
print(np.hsplit(a,2))
print(np.vsplit(a,2))
print(a+np.arange(1,5).reshape(2,2))"""

print(d)
e = np.dot(a,d)
print(e)
print(np.linalg.det(e))
print(np.linalg.inv(e))
