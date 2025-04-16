import torch
import numpy as np
import matplotlib.pyplot as plt
import random

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# a = np.array([1,2,3,4,5])
# a= torch.from_numpy(a)
# a= a.to(device)

# a = torch.randn(4, 5).to(device)

a = torch.rand(500,3,28,28).to(device)





print(a)
print(a.type())
print(f'FloatTensor: {isinstance(a, torch.FloatTensor)}')
print(f'cuda.FloatTensor: {isinstance(a, torch.cuda.FloatTensor)}')
print(f'cuda.DoubleTensor: {isinstance(a, torch.cuda.DoubleTensor)}')
print(f'cuda.HalfTensor: {isinstance(a, torch.cuda.HalfTensor)}')
print(f'cuda.ByteTensor: {isinstance(a, torch.cuda.ByteTensor)}')
print(f'cuda.CharTensor: {isinstance(a, torch.cuda.CharTensor)}')
print(f'cuda.ShortTensor: {isinstance(a, torch.cuda.ShortTensor)}')
print(f'cuda.LongTensor: {isinstance(a, torch.cuda.LongTensor)}')
print(f'cuda.IntTensor: {isinstance(a, torch.cuda.IntTensor)}')
print(a.shape)
print(a.size(0))
print(a.size(1))
print(a.shape[1])
print(a[0])
print(a[0].shape)
print(list(a[0].size()))
print(a.numel())
print(a.dim())

# random.seed(33)
# image= (a[random.randint(0,499)]).permute(1,2,0)
# image = image.cpu().numpy()
# plt.imshow(image)
# plt.axis('off')
# plt.show()
