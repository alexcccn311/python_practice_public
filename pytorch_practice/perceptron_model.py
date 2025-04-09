# 作者：Alex
# 2025/1/11 05:19
import torch
from torch.nn import functional as F
import random

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def random_one_hot(numbers, num_classes=10):
    num_list = [random.randint(0, num_classes-1) for _ in range(numbers)]
    numbers_tensor = torch.tensor(num_list, dtype=torch.long)
    random_one_hot_numbers = torch.zeros((len(num_list), num_classes),device = device)
    random_one_hot_numbers[torch.arange(len(num_list)), numbers_tensor] = 1
    return random_one_hot_numbers

loss = 0
learning_rate = 0.01
x1 = torch.randn(10,28,28, requires_grad=True,device=device)
x1 = x1.view(-1,784)
w1 = torch.randn(784, 256, requires_grad=True,device=device)
x2 = torch.ones(10,256,device=device)
w2 = torch.randn(256,10,requires_grad=True,device=device)
x3 = torch.ones(10,10,device=device)
target = random_one_hot(10,10)
optimizer = torch.optim.SGD([w1,w2], lr=learning_rate)
# print(f'w: {w}')

for i in range(10000):
    optimizer.zero_grad()
    x2 = torch.sigmoid(x1@w1)
    x3 = torch.sigmoid(x2@w2)
    loss = F.mse_loss(target, x3)
    loss.backward()
    optimizer.step()
    if (i+1) % 1000 == 0:
        print(f"Iteration {i+1}, Loss: {loss.item():.6f}")

# print(f'x1 = {x1}')
# print(f'w: {w}')
# print(f'x2: {x2}')
# print(x2.shape)
print(f'loss: {loss}')
# print(loss.shape)
# print(w.grad)

