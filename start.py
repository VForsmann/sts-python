import data_preparation.csv_import as csv
import functions as fn
import numpy as np
import pandas as pd

# Start script
data = csv.load_data()

# example for vitus
logos = data[['f12_1', 'f12_2', 'f12_3', 'f12_4', 'f12_5', 'f12_6', 'f12_7', 'f12_8', 'f12_9']].replace(' ', '0')
sum_logos = fn.sum_characteristics(np.array(logos[1:]))
print(sum_logos)
