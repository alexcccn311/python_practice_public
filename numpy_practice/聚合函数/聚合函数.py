import numpy as np



random_matrix = np.random.randint(low=0, high=100, size=(10, 13))

"""print(random_matrix.sum(axis=0))
print(np.sum(random_matrix))
print(np.sum(random_matrix, axis=0))
print(np.sum(random_matrix, axis=1))"""

#print(np.amax(random_matrix))
#print(np.amax(random_matrix,axis=0))
#print(np.amin(random_matrix,axis=1))
#print(np.nanmin(random_matrix,axis=0))#忽略非数
#print(np.nanmax(random_matrix, axis=-1))
#print(np.mean(random_matrix)) #平均值
#print(np.nanmean(random_matrix)) #忽略非数平均值
#print(np.std(random_matrix)) #标准差
#print(np.average(random_matrix, axis=0, weights=random_matrix)) #加权平均值 matrix,axis,[权重1,权重2....]

print(random_matrix)