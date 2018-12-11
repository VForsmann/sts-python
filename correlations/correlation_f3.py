import numpy as np
import pandas as pd

import functions as fn

data = fn.load_data('../data_preparation/data_preparation.csv')

x = pd.crosstab(data['f3_2'], data['f3_1'], rownames=['f2'], colnames=['f1'])
print(np.correlate(x))
