import torch
import visdom
from torch import nn
from torchvision import datasets, transforms
import torch.nn.init as init
from CNN_restnet import RestNet18
import time


class CNN_2(torch.nn.Module):
    def __init__(self):
        super(CNN_2, self).__init__()
        self.conv_unit = torch.nn.Sequential(
            #in_data= [batch_size, 3(RGB),32(H),32(W)]
            #out_data = [batch_size,6(out_channels),32((H+2*padding-(kernel_size - 1))/stride),32((W+2*padding-(kernel_size - 1))/stride)]
            torch.nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=1),
            #平均池化,in_data= [b,6,32,32]
            # output = [b,6,16((32 + 2 * padding)/stride),16((32 + 2 * padding)/stride)]
            torch.nn.AvgPool2d(kernel_size=2, stride=2, padding=0),
            # in_data= [b,6,16,16]
            # output = [b,16,8,8]
            torch.nn.Conv2d(in_channels=6, out_channels=16, kernel_size=3, stride=2, padding=1),
            # input = [b,16,8,8]
            # output = [b,16,4,4]
            torch.nn.AvgPool2d(kernel_size=2, stride=2, padding=0),
        )
        self.fc_unit = torch.nn.Sequential(
            torch.nn.Linear(in_features=16 * 4 * 4, out_features=128),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.2),
            torch.nn.Linear(in_features=128, out_features=64),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.2),
            torch.nn.Linear(in_features=64, out_features=32),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.2),
            torch.nn.Linear(in_features=32, out_features=10),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.2),
        )


    def forward(self, x):
        x = self.conv_unit(x)
        x = x.view(x.size(0), -1)
        x = self.fc_unit(x)
        return x

def initialize_weights(m):
    if isinstance(m, nn.Linear):
        init.kaiming_uniform_(m.weight, nonlinearity='relu')  # Kaiming 均匀分布初始化,专门为relu激活函数设计的一种初始化方式
        if m.bias is not None:
            init.zeros_(m.bias)  # 偏置初始化为 0


def main():
    torch.autograd.set_detect_anomaly(True)
    loss = 100
    learning_rate = 1e-3
    weight_decay = 1e-2
    batch_size = 128
    epochs = 1000
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    start_time = time.time()
    print(f"start time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

    model = RestNet18().to(device)
    model.apply(initialize_weights)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(),
                                 lr=learning_rate,
                                 betas=(0.9, 0.999),  # 一阶和二阶矩的衰减率
                                 weight_decay=weight_decay  # L2 正则化项 (权重衰减)
                                 )
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer,  # 目标学习率的优化器
        mode='min',  # 优化模式
        factor=0.1,  # 优化比例,每次优化方式为 lr *= factor
        patience=10,  # 耐心度, 等待多少次loss没有变化之后进行优化
    )

    # model.load_state_dict(torch.load("examples/RestNet18/model_epoch_10.pth"))
    # optimizer.load_state_dict(torch.load("examples/RestNet18/optimizer_epoch_10.pth"))
    # scheduler.load_state_dict(torch.load("examples/RestNet18/scheduler_epoch_10.pth"))



    print(model)
    transform = transforms.Compose([
        transforms.RandomResizedCrop(32), #随机缩放一部分图像,输出图像为32*32
        transforms.RandomHorizontalFlip(),  #以 50% 的概率将输入图像进行水平翻转
        transforms.RandomRotation(30),  #随机旋转图像的角度，旋转角度范围是 -30 到 30 度之间
        transforms.RandomVerticalFlip(),  #以 50% 的概率将输入图像进行垂直翻转
        transforms.ToTensor(),  #tensor化
        transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])  #均值和方差
    ])
    cifar10_train_loader = torch.utils.data.DataLoader(datasets.CIFAR10(root='./CIFAR10', train=True, transform=transform, download=True),
                                                       batch_size=batch_size, shuffle=True,
                                                       num_workers=4,
                                                       pin_memory=True)
    cifar10_test_loader = torch.utils.data.DataLoader(datasets.CIFAR10(root='./CIFAR10', train=False, transform=transform, download=True),
                                                      batch_size=batch_size, shuffle=True)

    # Visdom
    # 启动visdom命令 python -m visdom.server
    viz = visdom.Visdom()
    win = viz.line(
        Y=[0.],  # 初始值
        X=[0.],  # 初始步数
        win='Accuracy',
        opts=dict(
            env='test_train',
            title='Training Loss and Accuracy',
            xlabel='epoch',
            ylabel='Accuracy',
            Label=['accuracy']
        )
    )

    for epoch in range(epochs):
        model.train()
        for batch_idx, (data, labels) in enumerate(cifar10_train_loader):
            data = data.to(device)
            labels = labels.to(device)
            loss = criterion(model(data), labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            if batch_idx % 100 == 0:
                print(f'epoch:{epoch} batch_idx: {batch_idx} loss:{loss}')
                execution_time = time.time() - start_time
                hours = execution_time // 3600
                minutes = (execution_time % 3600) // 60
                seconds = execution_time % 60
                print(f"time: {int(hours)}小时 {int(minutes)}分钟 {int(seconds)}秒")
        scheduler.step(loss)
        val_loss = 0
        correct = 0
        total = 0
        if epoch % 5 == 0:
            model.eval()  # 设置模型为评估模式（禁用dropout等）
            with torch.no_grad():
                for test_data, test_labels in cifar10_test_loader:
                    test_data,test_labels = test_data.to(device), test_labels.to(device)
                    logit = model(test_data)
                    loss = criterion(logit, test_labels)
                    val_loss += loss.item()
                    pred = logit.argmax(dim=1)
                    correct += pred.eq(test_labels).sum().item()
                    total += test_labels.size(0)
                    # 输出验证集的损失和准确率
                val_loss /= len(cifar10_test_loader)
                val_accuracy = 100 * correct / total
                print(f'Validation Loss after epoch {epoch}: {val_loss:.4f}')
                print(f'Validation Accuracy after epoch {epoch}: {val_accuracy:.2f}%')
                # 使用 ReduceLROnPlateau 调度器更新学习率
                scheduler.step(val_loss)  # 调用调度器并传入验证损失
                torch.save(model.state_dict(), f"examples/RestNet18/model_epoch_{epoch}.pth")
                torch.save(optimizer.state_dict(), f"examples/RestNet18/optimizer_epoch_{epoch}.pth")
                torch.save(scheduler.state_dict(), f"examples/RestNet18/scheduler_epoch_{epoch}.pth")

            viz.line(
                Y=[val_accuracy],
                X=[epoch],
                win=win,
                update='append',
                opts=dict(
                    title='Accuracy',
                    xlabel='epoch',
                    ylabel='Accuracy',
                    legend=['Accuracy'],
                    ),
                )


if __name__ == "__main__":
    main()
