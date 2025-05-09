import torch
from torch import nn

class Net(nn.Module):
    def __init__(self, inputs, outputs):
        super(Net, self).__init__()

        self.fc = nn.Sequential(
            nn.Linear(inputs, inputs*outputs),
            nn.ReLU(inplace=True),
            nn.Linear(inputs*outputs, inputs*outputs),
            nn.ReLU(inplace=True),
            nn.Linear(inputs*outputs, outputs)
        )


    def forward(self, x):
        x = self.fc(x)

        return x