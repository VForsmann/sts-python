import pandas as pd
import functions as fn
import numpy as np

raw_data = fn.load_data('../daten_robinson.csv')
tmp_field = []
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
# print(fn.descriptive_statistics(raw_data)['f22'])

# Selektieren und löschen von der Person mit der ID 88 der nichts mehr ausgefüllt hat
data = raw_data.drop(index=87)

# Ersetzen von leeren Strings der Ankreuzmöglichkeiten zu -> gar nichts angekreuzt
data[['f11_7', 'f12_4', 'f15_8']] = data[['f11_7', 'f12_4', 'f15_8']].replace(' ', 0)

# Ersetzt alle Leerstrings von allen Textfeldern mit 'nicht ausgefuellt'
tmp = ['f3_txt_val', 'f3_txt', 'f4_txt_val', 'f4_txt', 'f5_txt_val', 'f5_txt',
      'f6_txt', 'f7_txt', 'f11_txt', 'f14_txt', 'f15_txt_val', 'f15_txt', 'f17_Comment', 'f24', 'f25_1']
data[tmp] = data[tmp].replace(' ', 'nicht ausgefuellt')

data[['f23_1', 'f23_2', 'f23_3', 'f23_4']] = data[['f23_1', 'f23_2', 'f23_3', 'f23_4']].replace(' ', 0)

# Wenn jemand nichts auszusetzen hatte oder aehnliches ersetzt durch "nicht ausgefuellt"
data['f7_txt'] = data['f7_txt'].replace(['-', './.', 'Nichts', 'Nichts!', 'nichts', 'eigentlich nichts', 'Keine Wünsche', 'Alles prima - super Auswahl', 'Absolut gar nichts', 'Überhaupt nichts', 'Nichts, fast zu üppig und verschwenderisch', 'keine Ahnung', 'Uns fehlt nichts.'], 'nicht ausgefuellt')

# Ausreißer und ungueltige Werte behandeln und ersetzen
data['f16_8'] = data['f16_8'].replace('77', 8)
data['f19_6'] = data['f19_6'].replace('22', 8)
data['f18_3'] = data['f18_3'].replace('9', 8)
data['f26'] = data['f26'].replace('0', 7)

# neue Variable Altersklassen Skalierung ordinal 0 = keine Angabe, 1 = junger Erwachsener (bis 25), 2 = mittlerer Erwachsener (bis 45), 3 = alter Erwachesener (>45)
data = fn.create_age(data)


# Gibt die Ausprägung von einer Spalte an
for c in data.columns:
    print("---- %s ---" % c)
    print(data[c].value_counts())

# # f1 - set zero values to median
# data['f1'] = fn.set_zero_to_median(raw_data, 'f1')
#
# # f2 - set zero values to median
# data['f2'] = fn.set_zero_to_median(raw_data, 'f2')
#
# # f3_1 - f3_11 - set zero values to 8 --> not answered
# tmp_field = ['f3_1', 'f3_2', 'f3_3', 'f3_4', 'f3_5', 'f3_6', 'f3_7', 'f3_8', 'f3_9', 'f3_10', 'f3_11', ]
# data[tmp_field] = fn.question_cleaning(data, tmp_field, '0', 8)
#
#
# # f4_1 - f4_11 - set zero values to 8 --> not answered
# tmp_field = ['f4_1', 'f4_2', 'f4_3', 'f4_4', 'f4_5', 'f4_6', 'f4_7', 'f4_8', 'f4_9', 'f4_10', 'f4_11', 'f4_12', 'f4_13',
#              'f4_14']
# data[tmp_field] = fn.question_cleaning(data,tmp_field, '0', 8)
#
#
# # f5_1 - f5_14 - set zero values to 8 --> not answered
# tmp_field = ['f5_1', 'f5_2', 'f5_3', 'f5_4', 'f5_5', 'f5_6', 'f5_7', 'f5_8', 'f5_9', 'f5_10', 'f5_11']
# data[tmp_field] = fn.question_cleaning(data, tmp_field, '0', 8)
#
# # f6 - set zero values to 8
# data['f6_1'] = fn.set_field_value_to_new_value(raw_data, 'f6_1', 0, 8)
# data['f6_2'] = fn.set_field_value_to_new_value(raw_data, 'f6_2', 0, 8)
# data['f6_3'] = fn.set_field_value_to_new_value(raw_data, 'f6_3', 0, 8)
# data['f6_4'] = fn.set_field_value_to_new_value(raw_data, 'f6_4', 0, 8)
# data['f6_5'] = fn.set_field_value_to_new_value(raw_data, 'f6_5', 0, 8)
# data['f6_6'] = fn.set_field_value_to_new_value(raw_data, 'f6_6', 0, 8)
# data['f6_7'] = fn.set_field_value_to_new_value(raw_data, 'f6_7', 0, 8)
# data['f6_8'] = fn.set_field_value_to_new_value(raw_data, 'f6_8', 0, 8)
# data['f6_9'] = fn.set_field_value_to_new_value(raw_data, 'f6_9', 0, 8)
#
# # f7 - we do not use this question because of too large variations
#
# # f8 - set zero value to median
# data['f8'] = fn.set_zero_to_median(raw_data, 'f8')
#
# # f9 - there is nothing to do here.
#
# # f10 - set zero values to 8
# data['f10_1'] = fn.set_field_value_to_new_value(raw_data, 'f10_1', 0, 8)
# data['f10_2'] = fn.set_field_value_to_new_value(raw_data, 'f10_2', 0, 8)

# f11 - categorize
# catalogue
raw_catalogue = data[['f11_1', 'f11_2', 'f11_3', 'f11_4', 'f11_5', 'f11_6', 'f11_7']].replace(' ', '0')
trans_catalogue = raw_catalogue.transpose()
sum_catalogue = fn.sum_characteristics(trans_catalogue.values)
catalogue = pd.DataFrame(sum_catalogue).replace(2, 1).rename(index=str, columns={0: 'catalogue'})
