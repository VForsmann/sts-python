import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import functions as fn

# Start script
data = fn.load_data('daten_robinson.csv')

# example for vitus
logos = data[['f12_1', 'f12_2', 'f12_3', 'f12_4', 'f12_5', 'f12_6', 'f12_7', 'f12_8', 'f12_9']].replace(' ', '0')
sum_logos = fn.sum_characteristics(np.array(logos[1:]))

pd_logos = pd.DataFrame(sum_logos)
print(sum_logos)
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], sum_logos)
plt.grid()
plt.show()
