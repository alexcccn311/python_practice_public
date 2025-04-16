import torch
import torch.nn.functional as F
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import torch.nn.init as init
# from torchvision import transforms

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
batch_size = 10
learning_rate = 0.01
epoch = 10
input_data = torch.randn(500, 3, 224, 224, device= device)
target_data = torch.randint(0, 10, (500,),device= device)
dataset = TensorDataset(input_data, target_data)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),  # 缩放到 224x224
#     transforms.ToTensor()
# ])

def initialize_weights(m):
    if isinstance(m, nn.Linear):
        init.kaiming_uniform_(m.weight, nonlinearity='relu')  # Kaiming 均匀分布初始化,专门为relu激活函数设计的一种初始化方式
        if m.bias is not None:
            init.zeros_(m.bias)  # 偏置初始化为 0


class FullyConnectedModel(nn.Module):
    def __init__(self):
        super(FullyConnectedModel, self).__init__()
        self.fc1 = nn.Linear(3 * 224 * 224, 8192,bias=True)
        self.fc2 = nn.Linear(8192, 2048,bias=True)
        self.fc3 = nn.Linear(2048, 512,bias=True)
        self.fc4 = nn.Linear(512, 128,bias=True)
        self.fc5 = nn.Linear(128, 32,bias=True)
        self.fc6 = nn.Linear(32, 10,bias=True)
    def forward(self, x):
        x = F.relu(self.fc1(x),inplace=True)
        x = F.relu(self.fc2(x),inplace=True)
        x = F.relu(self.fc3(x),inplace=True)
        x = F.relu(self.fc4(x),inplace=True)
        x = F.relu(self.fc5(x),inplace=True)
        x = self.fc6(x)
        return x

# w1 = torch.randn(8192,224 * 224,requires_grad=True,device= device)
# b1 = torch.randn(8192,requires_grad=True,device= device)
#
# w2 = torch.randn(2048,8192,requires_grad=True,device= device)
# b2 = torch.randn(2048,requires_grad=True,device= device)
#
# w3 = torch.randn(512,2048,requires_grad=True,device= device)
# b3 = torch.randn(512,requires_grad=True,device= device)
#
# w4 = torch.randn(128,512,requires_grad=True,device= device)
# b4 = torch.randn(128,requires_grad=True,device= device)
#
# w5 = torch.randn(32,128,requires_grad=True,device= device)
# b5 = torch.randn(32,requires_grad=True,device= device)
#
# w6 = torch.randn(10,32,requires_grad=True,device= device)
# b6 = torch.randn(10,requires_grad=True,device= device)

model = FullyConnectedModel().to(device)
model.apply(initialize_weights)
optimizer = torch.optim.SGD(model.parameters(),lr = learning_rate)
criterion = nn.CrossEntropyLoss()

for epoch in range(epoch):
    for batch_idx, (data, target) in enumerate(dataloader):
        data = data.view(-1, 3 * 224 * 224)
        logit = model(data)
        loss = criterion(logit, target)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print(f'epoch: {epoch}, batch: {batch_idx}, loss: {loss.item():.4f}')

print(loss)