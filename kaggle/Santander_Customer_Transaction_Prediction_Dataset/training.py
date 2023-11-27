import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from sklearn import metrics
from tqdm import tqdm

from model import Net
from data import get_tensordata

DEVICE = 'cpu'
if torch.cuda.is_available(): DEVICE = 'cuda'
elif torch.backends.mps.is_available(): DEVICE = 'mps'
else: DEVICE

model = Net(input_size=400, hidden_dimentions=100).to(DEVICE)
optimizer = optim.Adam(model.parameters(), lr=1e-2, weight_decay=1e-5)
loss_function = nn.BCELoss()
train_dataset, validation_dataset, test_dataset, test_id = get_tensordata()
train_loader = DataLoader(train_dataset, batch_size=1024, shuffle=True)
