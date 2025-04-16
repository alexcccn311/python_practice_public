import torch
import torch.nn.functional as F
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from visdom import Visdom

class Res_Blk(nn.Module):
    def __init__(self,ch_in,ch_out):
        super(Res_Blk, self).__init__()
        self.conv1 = nn.Conv2d(ch_in,ch_out,kernel_size=5, stride=1, padding=2)
        self.bn1 = nn.BatchNorm2d(ch_out)
        self.conv2 = nn.Conv2d(ch_out,ch_out,kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(ch_out)

        self.extra = nn.Sequential()
        if ch_in != ch_out:
            self.extra = nn.Sequential(
                nn.Conv2d(ch_in,ch_out,kernel_size=1, stride=1),
                nn.BatchNorm2d(ch_out),
            )

    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)), inplace=False)
        out = F.relu(self.bn2(self.conv2(out)), inplace=False)
        out = self.extra(x) + out
        return out

class RestNet18(nn.Module):
    def __init__(self):
        super(RestNet18, self).__init__()
        self.conv1 =nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1),
            nn.BatchNorm2d(64),
        )
        self.block1 = Res_Blk(64,128)
        self.block2 = Res_Blk(128,256)
        self.block3 = Res_Blk(256,512)
        self.block4 = Res_Blk(512,1024)
        # self.pool = nn.AdaptiveAvgPool2d(1)
        self.out_layer = nn.Linear(1024 * 30 * 30, 10)

    def forward(self, x):
        out = self.conv1(x)
        out = self.block1(out)
        out = self.block2(out)
        out = self.block3(out)
        out = self.block4(out)
        out = out.view(out.size(0), -1)
        out = self.out_layer(out)
        return out

def main():
    # tmp = torch.randn(2,64,32,32)
    # blk = Res_Blk(64,128)
    # out = blk(tmp)
    # print(out.size())

    model = RestNet18()
    tmp = torch.randn(2,3,32,32)
    out = model(tmp)
    print(out.size())

if __name__ == '__main__':
    main()

