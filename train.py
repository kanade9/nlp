import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision
import numpy as np
import model

model = model.Model()

optimizer = optim.SGD(model.parameters(), lr=0.1)