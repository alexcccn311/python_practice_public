import torch


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
a = torch.randn(2,3,4,device=device)
# b = torch.randn(2,3,4,device=device)

# c = torch.where(a>0.5,a,b)  #三个参数的顺序为condition,if_result,else_result

idx = torch.arange(3,-1,-1,device=device)
idx = idx.expand_like(a)
b = torch.gather(a,2,idx)

print(idx)
print(f'a: {a}')
print(f'b: {b}')
# print(f'd: {c}')
#
# print(c.device)

