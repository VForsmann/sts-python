import pandas as pd
import functions as fn
import numpy as np
import matplotlib.pyplot as plt

raw_data = fn.load_data('../daten_robinson.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
# print(fn.descriptive_statistics(raw_data)['f22'])

# Selektieren und löschen von der Person mit der ID 88 der nichts mehr ausgefüllt hat
data = raw_data.drop(index=87)

# Ausreißer und ungueltige Werte behandeln und ersetzen
data['f16_8'] = data['f16_8'].replace('77', 8)
data['f19_6'] = data['f19_6'].replace('22', 8)
data['f18_3'] = data['f18_3'].replace('9', 8)
data['f26'] = data['f26'].replace('0', 7)

# Ersetzen von leeren Strings der Ankreuzmöglichkeiten zu -> gar nichts angekreuzt
data[['f11_7', 'f12_4', 'f15_8']] = data[['f11_7', 'f12_4', 'f15_8']].replace(' ', 0)

# Ersetzt alle Leerstrings von allen Textfeldern mit 'nicht ausgefuellt'
tmp = ['f3_txt', 'f4_txt', 'f5_txt_val', 'f5_txt',
      'f6_txt', 'f7_txt', 'f11_txt', 'f14_txt', 'f15_txt', 'f17_Comment', 'f24', 'f25_1']
data[tmp] = data[tmp].replace(' ', 'nicht ausgefuellt')

# Inkonsistenzen beheben I
# Bei den Beurteilungsfragen die das Hinzufügen eines eigenen Begriffes erlauben,
# auf 0 = nicht ausgefuellt setzen, wenn nicht gesetzt
tmp = ['f3_txt_val', 'f4_txt_val', 'f5_txt_val', 'f15_txt_val']
data[tmp] = data[tmp].replace(' ', 0)

# Inkonsistenzen beheben II
data.loc[(data['f3_txt_val'] != 0) & (data['f3_txt'] == 'nicht ausgefuellt'), ['f3_txt_val']] = 0
data.loc[(data['f4_txt_val'] != 0) & (data['f4_txt'] == 'nicht ausgefuellt'), ['f4_txt_val']] = 0
data.loc[(data['f5_txt_val'] != 0) & (data['f5_txt'] == 'nicht ausgefuellt'), ['f5_txt_val']] = 0
data.loc[(data['f15_txt_val'] != 0) & (data['f15_txt'] == 'nicht ausgefuellt'), ['f15_txt_val']] = 0

# Kinderalter die einen leeren String enthalten werden auf 0 gesetzt
data[['f23_1', 'f23_2', 'f23_3', 'f23_4']] = data[['f23_1', 'f23_2', 'f23_3', 'f23_4']].replace(' ', 0)

# Wenn jemand nichts auszusetzen hatte oder aehnliches ersetzt durch "nicht ausgefuellt"
data['f7_txt'] = data['f7_txt'].replace(['-', './.', 'Nichts', 'Nichts!', 'nichts', 'eigentlich nichts', 'Keine Wünsche', 'Alles prima - super Auswahl', 'Absolut gar nichts', 'Überhaupt nichts', 'Nichts, fast zu üppig und verschwenderisch', 'keine Ahnung', 'Uns fehlt nichts.'], 'nicht ausgefuellt')


# f11 - categorize
# catalogue
raw_catalogue = data[['f11_1', 'f11_2', 'f11_3', 'f11_4', 'f11_5', 'f11_6', 'f11_7']].replace(' ', '0')
trans_catalogue = raw_catalogue.transpose()
sum_catalogue = fn.sum_characteristics(trans_catalogue.values)
catalogue = pd.DataFrame(sum_catalogue).replace(2, 1).rename(index=str, columns={0: 'catalogue'})
# internet
raw_internet = data[['f11_8', 'f11_9']].replace(' ', '0')
trans_internet = raw_internet.transpose()
sum_internet = fn.sum_characteristics(trans_internet.values)
internet = pd.DataFrame(sum_internet).replace(2, 1).rename(index=str, columns={0: 'internet'})
# other
raw_other = data[['f11_10']].replace(' ', '0')
trans_other = raw_other.transpose()
sum_other = fn.sum_characteristics(trans_other.values)
other = pd.DataFrame(sum_other).replace(2, 1).rename(index=str, columns={0: 'other'})

data['catalogue'] = catalogue.values
data['internet'] = internet.values
data['other'] = other.values


# f12 - sum
logos = data[['f12_1', 'f12_2', 'f12_3', 'f12_4', 'f12_5', 'f12_6', 'f12_7', 'f12_8', 'f12_9']].replace(' ', '0')
sum_logos = fn.sum_characteristics(logos.values)


# f17 Calculate mean of the percentage with zero and without zero
data['f17'] = pd.to_numeric(data['f17'].astype('str').str.replace(',', '.'), errors='coerce')
only_percentages = data['f17'][data['f17'] > 0].describe()
with_zero_percentage = data['f17'][data['f17'] > -1].describe()


# f22 neue Variable Altersklassen Skalierung ordinal 0 = keine Angabe, 1 = junger Erwachsener (bis 25),
# 2 = mittlerer Erwachsener (bis 45), 3 = alter Erwachesener (>45)
data = fn.create_age(data)

# f23 converting object into double and calculate the difference between parents and children
data['f23_1'] = pd.to_numeric(data['f23_1'].astype('str').str.replace(',', '.'), errors='coerce')
data['f23_2'] = pd.to_numeric(data['f23_2'].astype('str').str.replace(',', '.'), errors='coerce')
data['f23_3'] = pd.to_numeric(data['f23_3'].astype('str').str.replace(',', '.'), errors='coerce')
data['f23_4'] = pd.to_numeric(data['f23_4'].astype('str').str.replace(',', '.'), errors='coerce')
data['dif_parent_first_child'] = data['age'][data['age'] > 0] - data['f23_1'][data['f23_1'] > 0]
data['dif_parent_second_child'] = data['age'][data['age'] > 0] - data['f23_2'][data['f23_2'] > 0]
data['dif_parent_third_child'] = data['age'][data['age'] > 0] - data['f23_3'][data['f23_3'] > 0]
data['dif_parent_fourth_child'] = data['age'][data['age'] > 0] - data['f23_4'][data['f23_4'] > 0]

# f25 cleaning up PLZ
data['f25_2'] = pd.to_numeric(data['f25_2'])
data.loc[data['f25_1'] == 0, ['f25_2']] = 0
data.loc[data['f25_1'].isin(['CH', 'A', 'NL', 'LU']) & ((data['f25_2'] <= 1000) | (data['f25_2'] >= 9999)), ['f25_2']] = 0
data.loc[(data['f25_1'].isin(['D'])) & ((data['f25_2'] <= 10000) | (data['f25_2'] >= 99999)), ['f25_2']] = 0
data.loc[(data['f25_1'].isin(['RUS'])) & ((data['f25_2'] <= 100000) | (data['f25_2'] >= 999999)), ['f25_2']] = 0

ger_plz = data['f25_2'][(data['f25_1'].isin(['D']))] / 10000
ger_plz_sum = ger_plz.astype(int).value_counts()

# f26 Get Statistics of income
data['f26'] = pd.to_numeric(data['f26'].astype('str').str.replace(',', '.'), errors='coerce')
income_statistics = data['f26'][data['f26'] < 7].describe()
# create income classes
data = fn.create_income_class(data)

# Inkonsistenzen beheben III
# Wenn ein Aufschlag angegeben wurde, die Frage ob man jedoch bereit wäre einen Aufschlag zu zahlen >= 5 ist
# soll die Frage auf nicht beurteilbar gesetzt werden
data['f18_2'] = pd.to_numeric(data['f18_2'], errors='coerce')
data.loc[(data['f17'] > 0) & (data['f18_2'] >= 5), ['f18_2']] = 8

# Gibt die Ausprägung von einer Spalte an
for c in data.columns:
    print("---- %s ---" % c)
    print(data[c].value_counts())

data.to_csv('data_preparation.csv', sep=';')

print(data['f23_1'])

data['f23_3'] = data['f23_3'].replace(np.NaN, 0)
data['dif_parent_second_child'] = data['dif_parent_second_child'].replace(np.NaN, 0)
data['dif_parent_third_child'] = data['dif_parent_third_child'].replace(np.NaN, 0)
data['dif_parent_fourth_child'] = data['dif_parent_fourth_child'].replace(np.NaN, 0)

# Berechnung durchschnittsalter der Kinder im Robinson Club
first = data['f23_1'].sum()/data['f23_1'][data['f23_1'] > 0].value_counts().sum()
second = data['f23_2'].sum()/data['f23_2'][data['f23_2'] > 0].value_counts().sum()
third = data['f23_3'].sum()/data['f23_3'][data['f23_3'] > 0].value_counts().sum()
fourth = data['f23_4'].sum()/data['f23_4'][data['f23_4'] > 0].value_counts().sum()
mittelwertAge = (first + second + third + fourth)/4
print(mittelwertAge)

# Berechnung durchschnittliche Anzahl an Kindern je Elternteil
countFirstChild = data['f23_1'][data['f23_1'] > 0].value_counts().sum()
countSecondChild = data['f23_2'][data['f23_2'] > 0].value_counts().sum()
countThirdChild = data['f23_3'][data['f23_3'] > 0].value_counts().sum()
countFourthChild = data['f23_4'][data['f23_4'] > 0].value_counts().sum()
sum =(countFirstChild + countSecondChild + countThirdChild + countFourthChild)/218
print(sum)

print(data['f4_13'].describe())

