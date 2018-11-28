import numpy as np
import pandas as pd


def sum_characteristics(data: np.numarray):
    int_data = data.astype(np.int)
    sum_data = sum(int_data)
    return sum_data


def load_data(file):
    return pd.read_csv(file, sep=';', na_values='Nothing', error_bad_lines=False)
