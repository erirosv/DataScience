import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torch.nn.functional as F
from sklearn import metrics
from tqdm import tqdm

from data import get_tensordata

class Net(nn.Module):
    def __init__(self, input_size, hidden_dimentions):
        super(Net, self).__init__()
        self.batch_norm = nn.BatchNorm1d(input_size)
        self.layer_1 = nn.Linear(2, hidden_dimentions)
        self.layer_2 = nn.Linear(input_size // 2 * hidden_dimentions, 1)

    def forward(self, x):
        pass