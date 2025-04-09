# 作者：Alex
# 2025/1/16 04:15
import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, TensorDataset, random_split
import torch.nn.init as init
# from torch.utils.tensorboard import SummaryWriter
from visdom import Visdom
import numpy as np


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
batch_size = 10
learning_rate = 3e-3
epoch = 10000
input_data = torch.randn(500, 3, 28, 28, device= device)
target_data = torch.randint(0, 10, (500,),device= device)
dataset = TensorDataset(input_data, target_data)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_data, test_data = random_split(dataset, [train_size, test_size])
train_dataloader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=batch_size, shuffle=True)
loss = 0

class FullyConnectedModel1(nn.Module):
    def __init__(self):
        super(FullyConnectedModel1, self).__init__()
        # self.model = nn.Sequential(     #nn.Sequential写起来更方便快捷,但可维护性不高,出现问题或者模型效果不好难以定位那一层出现问题
        #     nn.Linear(28 * 28, 100),
        #     nn.ReLU(inplace=True),
        #     nn.Linear(100, 10),
        #     nn.ReLU(inplace=True),
        #     nn.Linear(10, 10),
        #     nn.ReLU(inplace=True),
        # )
        self.fc1 = nn.Linear(3 * 28 * 28, 512,bias=True)
        self.fc2 = nn.Linear(512, 128,bias=True)
        self.fc3 = nn.Linear(128, 32,bias=True)
        self.fc4 = nn.Linear(32, 10,bias=True)
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        x1 = F.relu(self.fc1(x),inplace=True)
        x1 = self.dropout(x1)
        x2 = F.relu(self.fc2(x1),inplace=True)
        x2 = self.dropout(x2)
        x3 = F.relu(self.fc3(x2),inplace=True)
        x3 = self.dropout(x3)
        x4 = F.relu(self.fc4(x3),inplace=True)
        return x4
def initialize_weights(m):
    if isinstance(m, nn.Linear):
        init.kaiming_uniform_(m.weight, nonlinearity='relu')  # Kaiming 均匀分布初始化,专门为relu激活函数设计的一种初始化方式
        if m.bias is not None:
            init.zeros_(m.bias)  # 偏置初始化为 0

model = FullyConnectedModel1().to(device)
model.apply(initialize_weights)
optimizer = torch.optim.SGD(
    model.parameters(), #需要优化的参数
    lr=learning_rate,
    weight_decay= 0.01, #weight_decay默认进行L2正则来降低网络复杂度防止过拟合
    momentum= 0.9
)
# scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=100, gamma=0.1) #每多少次更新一次学习率,根据scheduler.step()来确定次数的单位(scheduler.step()每运行一次记作一次)
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
    optimizer,  #目标学习率的优化器
    mode='min', #优化模式
    factor=0.1, #优化比例,每次优化方式为 lr *= factor
    patience=10,    #耐心度, 等待多少次loss没有变化之后进行优化
)

criterion = nn.CrossEntropyLoss()

#可视化
#TensorBoard
# # 初始化 TensorBoard
# writer = SummaryWriter(log_dir='runs/example')
#
# # 记录模型结构
# dummy_input = torch.randn(1, 3 * 224 * 224, device=device)
# writer.add_graph(model, dummy_input)
# global_step = 0

#Visdom
#启动visdom命令 python -m visdom.server
global_step = 0
viz = Visdom()
win = viz.line(
    Y=[0.],  # 初始值
    X=[0.],  # 初始步数
    win='loss and accuracy',
    opts=dict(
        env = 'test_train',
        title='Training Loss and Accuracy',
        xlabel='epoch',
        ylabel='Loss/Accuracy',
        Label = ['loss','accuracy']
    )
)
for epoch in range(epoch):
    model.train()  # 设置模型为训练模式
    for batch_idx, (data, target) in enumerate(train_dataloader):
        data = data.view(-1, 3 * 28 * 28)
        logit = model(data)
        loss = criterion(logit, target)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # scheduler.step()
        if batch_idx % 100 == 0:
            print(f'epoch: {epoch}, batch: {batch_idx}, loss: {loss.item():.4f}')
    # 验证过程
    model.eval()  # 设置模型为评估模式（禁用dropout等）
    val_loss = 0
    correct = 0
    total = 0
    if epoch%5 == 0:
        with torch.no_grad():  # 禁用梯度计算，以节省内存
            for data, target in test_dataloader:
                data = data.view(-1, 3 * 28 * 28)
                logit = model(data)
                loss = criterion(logit, target)
                val_loss += loss.item()

                # 计算准确率
                _, predicted = torch.max(logit, 1)
                total += target.size(0)
                correct += (predicted == target).sum().item()

        # 输出验证集的损失和准确率
        val_loss /= len(test_dataloader)
        val_accuracy = 100 * correct / total
        print(f'Validation Loss after epoch {epoch}: {val_loss:.4f}')
        print(f'Validation Accuracy after epoch {epoch}: {val_accuracy:.2f}%')
        # 使用 ReduceLROnPlateau 调度器更新学习率
        scheduler.step(val_loss)  # 调用调度器并传入验证损失

        # 保存模型参数
        torch.save(model.state_dict(), f"examples/model_epoch_{epoch}.pth")  # 保存模型参数文件

        # 更新验证损失的可视化
        # 记录损失
        # writer.add_scalar('Loss/train', loss.item(), global_step)
        # 更新 Visdom 曲线
        viz.line(
            Y=[val_loss],
            X=[epoch],
            win=win,
            update='append',
            opts=dict(
                name='Validation Loss',
                linecolor= np.array([[1, 0, 0]])
            )  # 红色
        )
        viz.line(
            Y=[val_accuracy],
            X=[epoch],
            win=win,
            update='append',
            opts=dict(
                name= 'Validation Accuracy',
                linecolor= np.array([[0, 1, 0]])
            )  # 绿色
        )


# writer.close()
print(loss)