import plotly
import plotly.graph_objs as go
import pandas as pd

file = 'daten_robinson.csv'
raw_data = pd.read_csv(file, sep=';', na_values=('Nothing'), error_bad_lines=False)
# raw_data['f16_8'] = raw_data['f16_8'].replace('77', 8)
# raw_data['f19_6'] = raw_data['f19_6'].replace('22', 8)
# Erstellen von allen Boxplots außer von ID, f25_2, f22, f17. Die werte Sind zu hoch und man würde nichts mehr erkennen
data = []
for col in raw_data.columns:
    if col != "f25_2" and col != "f22" and col != "ID" and col != "f17":
        data.append(go.Box(y=raw_data[col], name=col, showlegend=False))

# IPython notebook
# py.iplot(data, filename='pandas-box-plot')
plotly.offline.plot(data, filename='pandas-box-plot.html')
