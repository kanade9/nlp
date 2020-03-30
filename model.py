import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision
import numpy as np
from torch.autograd import Variable

# 入力は200次元の奴が480個??
# kは次元数=200 nは入力の単語数=841

a = np.load('word_vector.npy')
n = len(a)
trans = torchvision.transforms.ToTensor()
trans_vec = trans(a)

window_sizes = n


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        # nn.Conv2dの引数は　インプットのチャンネルの数，アウトプットのチャンネルの数，カーネルサイズ
        self.conv_3 = nn.Conv2d(1, 100, (3, 200))
        self.conv_4 = nn.Conv2d(1, 100, (4, 200))
        self.conv_5 = nn.Conv2d(1, 100, (5, 200))

        self.fc = nn.Linear(10 * window_sizes, 10)

    def forward(self, x):

        x1 = torch.tanh(self.conv_3(x))
        x2 = torch.tanh(self.conv_4(x))
        x3 = torch.tanh(self.conv_5(x))

        print('x1 size={}'.format(x1.size()))
        print('x2 size={}'.format(x2.size()))
        print('x3 size={}'.format(x3.size()))

        x1 = x1.squeeze(3)
        x2 = x2.squeeze(3)
        x3 = x3.squeeze(3)

        x1n = F.max_pool1d(x1, x1.size(2))
        x2n = F.max_pool1d(x2, x2.size(2))
        x3n = F.max_pool1d(x3, x3.size(2))
        x = torch.cat((x1n, x2n, x3n), 1)
        x = F.dropout(x)
        out = F.softmax(x)
        return out


input_matrix = torch.zeros(1, 1, 840, 200)  # input = torch.randn(1,3,224,224) #
# torch.zeros(バッジ数,チャネル数,ベクトルの個数(wordの数)(height),次元数(width))
# print(input_matrix)
model = Model()
out = model(input_matrix)
print(out)
#