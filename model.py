import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision
import numpy as np

# 入力は200次元の奴が480個??
# kは次元数=200 nは入力の単語数=841

a = np.load('word_vector.npy')
n = len(a)
trans = torchvision.transforms.ToTensor()
trans_vec = trans(a)


class Model(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv_3 = nn.Conv2d(0, 100, (3, 200))
        self.conv_4 = nn.Conv2d(0, 100, (4, 200))
        self.conv_5 = nn.Conv2d(0, 100, (5, 200))

    def forward(self, x):
        x1 = F.tanh(self.conv_3(x))
        x2 = F.tanh(self.conv_4(x))
        x3 = F.tanh(self.conv_5(x))

        x1n = F.max_pool1d(x1, x1.size(2))
        x2n = F.max_pool1d(x2, x2.size(2))
        x3n = F.max_pool1d(x3, x3.size(2))
        x = torch.cat((x1n, x2n, x3n), 1)
        x = F.dropout(x)

        out = self.fc1(x)
        return out
