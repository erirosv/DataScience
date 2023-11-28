import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from sklearn import metrics
from tqdm import tqdm

from model import Net
from data import get_tensordata
from utils import get_result_to_csv

def available_device():
    DEVICE = 'cpu'
    if torch.cuda.is_available(): DEVICE = 'cuda'
    elif torch.backends.mps.is_available(): DEVICE = 'mps'
    else: DEVICE
    print(f'DEVICE {DEVICE}')
    return DEVICE

def prep_training():
    model = Net(input_size=200, hidden_dimentions=100).to(available_device())
    print('Init...')
    optimizer = optim.Adam(model.parameters(), lr=1e-2, weight_decay=1e-5)
    loss_function = nn.BCELoss()
    train_dataset, validation_dataset, test_dataset, test_id = get_tensordata()
    train_loader = DataLoader(train_dataset, batch_size=1024, shuffle=True)
    validation_loader = DataLoader(validation_dataset, batch_size=1024)
    test_loader = DataLoader(test_dataset, batch_size=1024)
    print('Data components created')
    return model, optimizer, loss_function, train_loader, validation_loader, test_loader

def get_predictions(loader, model, device): 
    model.eval()
    predictions = []
    true_labels = []

    with torch.no_grad():
        for x,y in loader:
            x = x.to(device)
            y = y.to(device)
            scores = model(x)
            predictions += scores.tolist()
            true_labels += y.tolist()
    model.train()
    print('Evalueating result')
    return  predictions, true_labels


def run_training(epoch=10):
    model, optimizer, loss_function, train_loader, validation_loader, test_loader = prep_training()
    probabilities, true_labels = get_predictions(validation_loader, model, device=available_device())
    print(f'Validation ROC: {metrics.roc_auc_score(true_labels, probabilities)}')
    for id, (data, targets) in enumerate(train_loader):
        data = data.to(available_device())
        targets = targets.to(available_device())
        # ugly forwardpass
        scores = model(data)
        loss = loss_function(scores, targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print('Model result saving...')
    get_result_to_csv(model, test_loader, id, available_device())
    print('Complete')