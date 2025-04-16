import torch
import torchvision

from pytorch_practice.utils import plot_curve


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # self.conv1 = torch.nn.Conv2d(1, 10, kernel_size=5)
        # self.conv2 = torch.nn.Conv2d(10, 20, kernel_size=5)
        self.fc1 = torch.nn.Linear(784, 512)
        self.fc2 = torch.nn.Linear(512, 256)
        self.fc3 = torch.nn.Linear(256, 64)
        self.fc4 = torch.nn.Linear(64, 10)
        self.relu = torch.nn.ReLU()
        # self.pool = torch.nn.MaxPool2d(2, 2)
        self.dropout = torch.nn.Dropout(0.5)
        self.softmax = torch.nn.LogSoftmax(dim=1)
        self.loss = torch.nn.CrossEntropyLoss()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.to(self.device)
        self.optimizer = torch.optim.Adam(self.parameters(),lr=0.001)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.relu(self.fc3(x))
        x = self.fc4(x)
        return x


if __name__ == '__main__':
    batch_size = 512
    epochs = 20
    train_loss = []
    total_correct = 0
    train_data = torch.utils.data.DataLoader(
        torchvision.datasets.MNIST('../numpy_practice/mnist_data', train=True, download=True,
                                   transform=torchvision.transforms.Compose([
                                       torchvision.transforms.ToTensor(),
                                       torchvision.transforms.Normalize((0.1307,), (0.3081,))
                                   ])),
        batch_size=batch_size, shuffle=True)
    test_data = torch.utils.data.DataLoader(
        torchvision.datasets.MNIST('../numpy_practice/mnist_data', train=False, download=True,
                                   transform=torchvision.transforms.Compose([
                                       torchvision.transforms.ToTensor(),
                                       torchvision.transforms.Normalize((0.1307,), (0.3081,))
                                   ])),
        batch_size=batch_size, shuffle=True)
    net = Net()
    for epoch in range(epochs):
        for batch_idx,(x,y) in enumerate(train_data):
            x = x.view(x.size(0),28*28)
            x,y = x.to(net.device),y.to(net.device)
            out = net(x)
            net.optimizer.zero_grad()
            loss = net.loss(out, y)
            loss.backward()
            net.optimizer.step()
            train_loss.append(loss.item())

            if batch_idx % 10 == 0:
                print(epoch,batch_idx,loss.item())

    plot_curve(train_loss)


    net.eval()
    with torch.no_grad():
        for x,y in test_data:
            x = x.view(x.size(0),28*28)
            x, y = x.to(net.device), y.to(net.device)
            out = net(x)
            predict = out.argmax(dim=1, keepdim=True)
            correct = predict.eq(y.view_as(predict)).sum().item()
            total_correct += correct

    total_num = len(test_data.dataset)
    acc = total_correct / total_num
    print(f"test acc:{acc}")