import plotly
import plotly.graph_objs as go
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
file = 'daten_robinson.csv'
raw_data = pd.read_csv(file, sep=';', na_values=('Nothing'), error_bad_lines=False)
# Erstellen von allen Boxplots außer von ID, f25_2, f22, f17. Die werte Sind zu hoch und man würde nichts mehr erkennen
data = []
raw_data['f23_1'] = raw_data['f23_1'].replace(' ', '0')
raw_data['f23_1'] = pd.to_numeric(raw_data['f23_1'].astype('str').str.replace(',', '.'), errors='coerce')
raw_data['f23_2'] = pd.to_numeric(raw_data['f23_2'].astype('str').str.replace(',', '.'), errors='coerce')
raw_data['f23_3'] = pd.to_numeric(raw_data['f23_3'].astype('str').str.replace(',', '.'), errors='coerce')
raw_data['f23_4'] = pd.to_numeric(raw_data['f23_4'].astype('str').str.replace(',', '.'), errors='coerce')
for col in raw_data.columns:
    if col != "f25_2" and col != "f22" and col != "ID" and col != "f17":
        data.append(go.Box(y=raw_data[col], name=col, showlegend=False))
# IPython notebook
# py.iplot(data, filename='pandas-box-plot')
plotly.offline.plot(data, filename='./graphs/html/htmlGraphs/pandas-box-plot.html')



data[['f18_7', 'f8', 'f9', 'f18_2', 'f3_1', 'f3_2', 'f3_3', 'f3_4', 'f3_5', 'f3_6', 'f3_7', 'f3_8',
                  'f3_9', 'f3_10', 'f3_11', 'age', 'f17', 'f1', 'f4_1', 'f4_2', 'f4_3', 'f4_4', 'f4_5', 'f4_6',
      'f4_7', 'f4_8', 'f4_9', 'f4_10', 'f4_11', 'f4_12', 'f4_13', 'f4_14',
      'f19_1', 'f19_2', 'f19_3', 'f19_4', 'f19_5', 'f19_6',
      'f19_7', 'f19_8', 'f19_9', 'f19_10']] \
    = sst.zscore(data[['f18_7', 'f8', 'f9', 'f18_2', 'f3_1', 'f3_2', 'f3_3', 'f3_4', 'f3_5', 'f3_6', 'f3_7', 'f3_8',
                  'f3_9', 'f3_10', 'f3_11', 'age', 'f17', 'f1', 'f4_1', 'f4_2', 'f4_3', 'f4_4', 'f4_5', 'f4_6',
                       'f4_7', 'f4_8', 'f4_9', 'f4_10', 'f4_11', 'f4_12', 'f4_13', 'f4_14',
                       'f19_1', 'f19_2', 'f19_3', 'f19_4', 'f19_5', 'f19_6',
                       'f19_7', 'f19_8', 'f19_9', 'f19_10']])