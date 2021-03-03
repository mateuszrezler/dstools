from matplotlib.pyplot import scatter, show
from numpy import float32
from numpy.random import randn, random
from torch import from_numpy
from torch.nn import Linear, MSELoss
from torch.optim import SGD


def from_np(tensor):
    if len(tensor.shape) == 1:
        tensor = tensor.reshape(-1, 1)
    return from_numpy(tensor.astype(float32))


class SyntheticData2D(object):

    def __init__(self,
                 x_min=-10,
                 x_max=10,
                 function=lambda x: x,
                 n_points=10,
                 noise=1):
        self.x = random(n_points)*(x_max-x_min)+x_min
        self.y = function(self.x+randn(n_points)*noise)

    def get_torch(self):
        return from_np(self.x), from_np(self.y)

    def show_scatter(self, fit_line=None):
        scatter(self.x, self.y)
        if fit_line is not None:
            plot(self.x, fit_line)
        show()


class TrainingLoop(object):

    def __init__(self,
                 inputs,
                 targets,
                 model,
                 criterion,
                 optimizer,
                 n_epochs):
        self.inputs = inputs
        self.targets = targets
        self.model = model
        self.criterion = criterion
        self.optimizer = optimizer
        self.n_epochs = n_epochs
        self.losses = []

    def train(self):
        for epoch in range(self.n_epochs):
            self.optimizer.zero_grad()
            outputs = self.model(self.inputs)
            loss = self.criterion(outputs, self.targets)
            self.losses.append(loss.item())
            loss.backward()
            self.optimizer.step()
            print(f'Epoch: {epoch+1}/{self.n_epochs}, loss: {loss.item():.4f}')

