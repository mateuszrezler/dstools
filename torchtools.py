def from_np(tensor):
    if len(tensor.shape) == 1:
        tensor = tensor.reshape(-1, 1)
    return from_numpy(tensor.astype(float32))

