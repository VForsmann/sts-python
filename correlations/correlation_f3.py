import numpy as np
import pandas as pd

import plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

import functions as fn

data = fn.load_data('../data_preparation/data_preparation.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

x = pd.crosstab(data['f3_2'], data['f3_1'], rownames=['f2'], colnames=['f1'])
corr = data.corr()
corr = corr[(corr[:] > 0.5) & (corr[:] < 1)].dropna(how='all').dropna(axis='columns', how='all')
print(corr)
# table = go.Table(
#     header=dict(values=corr.columns,
#                 line=dict(color='#7D7F80'),
#                 fill=dict(color='#a1c3d1'),
#                 align=['left'] * 5),
#     columnwidth=50,
#     cells=dict(values=corr.values,
#                line=dict(color='#7D7F80'),
#                fill=dict(color='#EDFAFF'),
#                align=['left'] * 5))
# table = [table]

corr.to_html('pandas_table.html')

# py.offline.plot(table, filename='pandas_table.html')

