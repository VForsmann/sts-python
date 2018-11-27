#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Assign filename to variable: file
file = 'daten_robinson.csv'

data = pd.read_csv(file,sep=';' ,na_values=('Nothing'), error_bad_lines=False)
# range as bins
lower = pd.DataFrame.min(data[['f12_2']])
upper = pd.DataFrame.max(data[['f12_2']])

graphRange = upper - lower
print(graphRange)
pd.DataFrame.hist(data[['f12_2']], bins=np.arange(int(graphRange) + 2) - 0.25,  width=0.5)
plt.xticks(range(int(graphRange) + 1))

plt.ylabel('Anzahl')
plt.xlabel("Ausprägung")
plt.show()
print(data.head())