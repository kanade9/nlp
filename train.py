import torch
import os, sys
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision
import numpy as np
import torch.autograd as autograd

# batchの中には batch.text , batch.label

# あとで修正
# train_iter と　args そしてargs. xx_intervalってなんだ???
train_iter = data.BucketIterator(dataset=pos, batch_size=3, device=-1,
                                 repeat=False)


def train(model):
    epoch = 50
    steps = 0
    progress_show = 50
    # ロスを計算する
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    model.train()

    for e in range(epoch):
        for batch in train_iter:
            feature, target = batch.text, batch.label
            # これはbatchの最初と揃えたindexを表す??
            feature.data.t_(), target.data.sub_(1)

            optimizer.zero_grad()
            logit = model(feature)

            loss = F.cross_entropy(logit, target)
            loss.backward()
            optimizer.step()

            steps += 1

            if steps % progress_show == 0:
                corrects = (torch.max(logit, 1)[1].view(target.size()).data == target.data).sum()
                accuracy = 100.0 * corrects / batch.batch_size
                sys.stdout.write('\rBatch[{}] - loss: {:.6f} acc: {:.4f}%({}/{})'
                                 .format(steps, loss.data[0], accuracy, corrects, batch.batch_size))




model.train()
