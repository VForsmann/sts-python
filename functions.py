import numpy as np


def sum_characteristics(data: np.numarray):
    int_data = data.astype(np.int)
    sum_data = sum(int_data)
    return sum_data
