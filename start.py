import data_preparation.csv_import as csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Start script
data = csv.load_data()

f22_data = np.array(data[['f22']])
median = np.median(f22_data[f22_data > 0])
f22_data[f22_data == 0] = median
print(f22_data)
pd.DataFrame.hist(pd.DataFrame(f22_data))
plt.show()
