from numpy.random import randn, random


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

