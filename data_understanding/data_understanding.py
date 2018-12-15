import pandas as pd
import functions as fn
import numpy as np
import matplotlib.pyplot as plt

data = fn.load_data('../daten_robinson.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


countID1 = data['Ort'][data['Ort'] == 1].value_counts().sum()
percentageID1 = countID1/219*100
countID2 = data['Ort'][data['Ort'] == 2].value_counts().sum()
percentageID2 = countID2/219*100

# matplotlib style
plt.style.use('seaborn-bright')

# data to plot
labels = 'Österreich', 'Türkei'
sizes = [percentageID1, percentageID2]
colors = ['green', 'blue']

# plot
plt.pie(sizes,              # data
        labels=labels,      # slice labels
        colors=colors,      # array of clors
        autopct='%1.1f%%',  # print the values inside the wedges
        shadow=True,        # enable shadow
        startangle=140)     # startin angle

plt.axis('equal')
plt.show()


# Gibt die Ausprägung von einer Spalte an
for c in data.columns:
    print("---- %s ---" % c)
    print(data[c].value_counts())

# ab Frage 11 sind alle Werte numerischen Werte Strings, diese werden im data_preparation behandelt
print(data.describe())

