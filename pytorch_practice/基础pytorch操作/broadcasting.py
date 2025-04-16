import torch

a = torch.randn(4,3, 28,28)

# b = torch.randn(28)
# b = b.unsqueeze(-1).unsqueeze(-1)

b = torch.randn(2)
c = b.expand(4,4,2)

print(b)
print(c)
print(c.shape)
