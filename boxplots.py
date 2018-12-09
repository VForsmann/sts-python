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
plotly.offline.plot(data, filename='pandas-box-plot.html')
