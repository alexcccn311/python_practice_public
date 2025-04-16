import torch


def entropy_1(p):
    return -(p * torch.ln(p)).sum()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
a = torch.full([4,4],0.0000001,device=device)
a[3,3] = 0.9999985
b = torch.ln(a)
c = a * b
d = -c.sum()

# print(f'a: {a}')
# print(f'b: {b}')
# print(f'c: {c}')
# print(f'd: {d}')

#双参数熵
def entropy_2(p,q):
    return -(p * torch.ln(q)).sum()

def dkl(p,q):
    return (p * torch.ln(p)).sum() - (p * torch.ln(q)).sum()

def entropy_3(p,q):
    h_p = entropy_1(p)
    dkl_p_q = dkl(p,q)
    return h_p + dkl_p_q

e = torch.ones(4,4,device=device)
f = torch.full([4,4],1,device=device)
g = torch.full([4,4],0.0000001,device=device)
g[3,3] = 0.9999985
entropy_e_f_1 = -(e * torch.ln(f)).sum()
h_e = -(e * torch.ln(e)).sum()
d_kl = (e * torch.ln(e)).sum() - (e * torch.ln(f)).sum()
entropy_e_f_2 = h_e + d_kl
entropy_f_g_1 = entropy_2(f,g)
entropy_f_g_2 = entropy_3(f,g)
test_result = torch.allclose(entropy_f_g_1,entropy_f_g_2)
test_result_2 = torch.equal(entropy_f_g_1,entropy_f_g_2)


# print(f'e: {e}')
# print(f'f: {f}')
# print(f'entropy_e_f_1: {entropy_e_f_1}')
# print(f'h_e: {h_e}')
# print(f'd_kl: {d_kl}')
# print(f'entropy_e_f_2: {entropy_e_f_2}')
# print(f'entropy_e_g_1: {entropy_f_g_1}')
# print(f'entropy_e_g_2: {entropy_f_g_2}')
# print(f'test_result: {test_result}')
# print(f'test_result_2: {test_result_2}')


cat_possibility = torch.rand(4,4,device=device,requires_grad=True)
dog_possibility = 1 - cat_possibility
cat_true = torch.randint(0,2,(4,4),device=device)
dog_true = torch.where(cat_true == 1,0,1)
entropy_cat_1 = (-cat_true * torch.ln(cat_possibility)).sum()
entropy_dog_1 = (-(1 -cat_true) * torch.ln(1 - cat_possibility)).sum()
entropy_cat_dog_1 = entropy_cat_1 + entropy_dog_1

clone_cat_possibility = cat_possibility.clone()

# cat_possibility.requires_grad_(True)
# print(dog_possibility)
# print(cat_true)
# print(entropy_cat_1)

optimizer= torch.optim.SGD([cat_possibility], lr=0.1)
current_cat_possibility = torch.zeros_like(clone_cat_possibility)

for epoch in range(100000):
    optimizer.zero_grad()
    current_cat_possibility = torch.sigmoid(cat_possibility)
    loss = ((-cat_true * torch.ln(current_cat_possibility)).sum()) ** 2
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 10000 == 0:
        print(f"Epoch {epoch + 1}\nLoss: {loss.item()}\ncat_possibility: {current_cat_possibility}")

print(f'original cat_possibility: {clone_cat_possibility}')
print(f'final cat_possibility: {current_cat_possibility}')
print(f'cat_true: {cat_true}')
