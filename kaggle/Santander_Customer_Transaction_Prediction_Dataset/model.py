import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    '''
    A simple neural network based on troch. There is no backpropagation 
    at the moment, may come at a later date.
    '''
    def __init__(self, input_size, hidden_dimentions):
        super(Net, self).__init__()
        self.batch_norm = nn.BatchNorm1d(input_size)
        self.layer_1 = nn.Linear(2, hidden_dimentions)
        self.layer_2 = nn.Linear(input_size // 2 * hidden_dimentions, 1)

    def forward(self, x):
        x = self.batch_norm(x)
        N = x.shape[0]
        # set the shape (N, 200, 1)
        original_features = x[:, :200].unsqueeze(2)
        new_features = x[:, :200].unsqueeze(2)

        x = torch.cat([original_features, new_features], dim=2)
        x = F.relu(self.layer_1(x)).reshape(N, -1)
        x = torch.sigmoid(self.layer_2(x)).view(-1)
        return x