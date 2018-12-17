import pandas as pd
import functions as fn
import plotly as py
import plotly.graph_objs as go

data = fn.load_data('../daten_robinson.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


countID1 = data['Ort'][data['Ort'] == 1].value_counts().sum()
percentageID1 = countID1/219*100
countID2 = data['Ort'][data['Ort'] == 2].value_counts().sum()
percentageID2 = countID2/219*100

# Gibt die Ausprägung von einer Spalte an
for c in data.columns:
    print("---- %s ---" % c)
    print(data[c].value_counts())

# ab Frage 11 sind alle Werte numerischen Werte Strings, diese werden im data_preparation behandelt
print(data.describe())

data['f26'] = pd.to_numeric(data['f26'].astype('str'), errors='coerce')

count1 = data['f26'][data['f26'] == 1].value_counts().sum()
percentage1 = count1/219*100
count2 = data['f26'][data['f26'] == 2].value_counts().sum()
percentage2 = count2/219*100
count3 = data['f26'][data['f26'] == 3].value_counts().sum()
percentage3 = count3/219*100
count4 = data['f26'][data['f26'] == 4].value_counts().sum()
percentage4 = count4/219*100
count5 = data['f26'][data['f26'] == 5].value_counts().sum()
percentage5 = count5/219*100
count6 = data['f26'][data['f26'] == 6].value_counts().sum()
percentage6 = count6/219*100
count7 = data['f26'][data['f26'] == 7].value_counts().sum()
percentage7 = count1/219*100

fig = {
  "data": [
    {
      "values": [percentageID1, percentageID2],
      "labels": [
        'Österreich',
        'Türkei'
      ],
      "domain": {"x": [0, .48]},
      "name": "Ort",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },
    {
      "values": [count1, count2, count3, count4, count5, count6, count7],
      "labels": [
        'bis unter 1.500€',
        'bis unter 2.000€',
        'bis unter 3.000€',
        'bis unter 4.000€',
        'bis unter 5.000€',
        '5.000€ oder mehr',
        'keine Angabe'
      ],
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "Einkommensverteilung",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title":"Data Understanding",
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Orte",
                "x": 0.220,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "EV",
                "x": 0.77,
                "y": 0.5
            }
        ]
    }
}

py.offline.plot(fig, filename='../graphs/html/htmlGraphs/tortendiagramme.html')

count1 = data['f26'][data['f26'] == 1].value_counts().sum()

countZero = data['f2'][data['f2'] == 0].value_counts().sum()
countAlone = data['f2'][data['f2'] == 1].value_counts().sum()
countFriend = data['f2'][data['f2'] == 2].value_counts().sum()
countFamily = data['f2'][data['f2'] == 3].value_counts().sum()

trace0 = go.Bar(
    x=['keine Angabe', 'allein', 'mit Ehepartner / Freund/in', 'mit Familie'],
    y=[countZero, countAlone, countFriend, countFamily],
    marker=dict(
        color=['rgba(165, 42, 42, 0.4)', 'rgba(165, 42, 42, 0.7)',
               'rgba(165, 42, 42, 0.6)', 'rgba(165, 42, 42, 1)']),
)

data = [trace0]
layout = go.Layout(
    title='Reisebegleitung',
)

fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename='../graphs/html/htmlGraphs/balkendiagramm.html')
