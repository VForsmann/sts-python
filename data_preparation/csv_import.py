import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Assign filename to variable: file
file = 'daten_robinson.csv'

def load_data():
    return pd.read_csv(file, sep=';', na_values=('Nothing'), error_bad_lines=False)
