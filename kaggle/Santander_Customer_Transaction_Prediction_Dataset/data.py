import pandas as pd
from math import ceil

import torch
from torch.utils.data import TensorDataset
from torch.utils.data.dataset import random_split

def get_tensordata() -> TensorDataset:
    train = pd.read_csv('data/train.csv')
    test = pd.read_csv('data/test.csv')

    y_train = train['target']
    X_train = train.drop(['ID_code', 'target'], axis=1)
    
    test_id = test['ID_code']
    X_test = test.drop(['ID_code'])

    X_train_tensor = torch.tensor(X_train.values, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32)
    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    train_dataset, val_dataset = random_split(train_dataset, [int(0.8 * len(train_dataset)), 
                                                              ceil(0.2 * len(train_dataset))])
    
    X_test_tensor = torch.tensor(X_test.values, dtype=torch.float32)
    test_dataset = TensorDataset(X_test_tensor, y_train_tensor)

    return train_dataset, val_dataset, test_dataset, test_id
