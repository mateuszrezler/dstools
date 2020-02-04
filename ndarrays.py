import numpy as np
from print import eprint

def vstack_with_zeros(*vectors):

    """Stack vectors with preceding and following zeros."""

    lengths = np.array([vector.shape[0] for vector in vectors])

    return np.vstack([np.hstack((np.zeros(lengths[:index].sum()),
                                 vector, np.zeros(lengths[index+1:].sum())))
                      for index, vector in enumerate(vectors)])


