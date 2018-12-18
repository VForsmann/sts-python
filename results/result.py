import correlations.regression as regr
import functions as fn
import statsmodels.stats.weightstats as tests
import scipy.stats as stat
import numpy as np
data = fn.load_data('../data_preparation/data_preparation.csv')


# 1. Assignment
# regression for assigment 1
print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 1. Assigment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
# TODO hier noch die korrelationen einfügen, aber erst, wenn korrelation eine eigene funktion ist
food = ['f4_13', 'f8', 'f9', 'f10_1', 'f10_2', 'f15_8', 'f16_3', 'f16_8', 'f18_2']
well_being = 'f18_7'
print('---- well being - food regression ----')
regr.reg_for_prep_data(food, well_being, data)
sport = ['f3_3', 'f3_9']
well_being = 'f3_2'
print('---- well being - sport regression ----')
regr.reg_for_prep_data(sport, well_being, data)

# 2. Assignment
print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 2. Assigment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
# TODO hier noch die korrelationen einfügen, aber erst, wenn korrelation eine eigene funktion ist
print(data['f4_13'][(data['f4_13'] < 8) & (data['f4_13'] > 0)].describe())

# 3. Assignment
print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 3. Assigment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
# TODO hier noch ein plot erstellen, der pro frage den Mittelwert darstellt und ggf. irgendwie noch die std
bio_elements = ['f15_1', 'f15_2', 'f15_3', 'f15_4', 'f15_5', 'f15_6', 'f15_7', 'f15_8', 'f15_9', 'f15_10', 'f15_11', 'f15_12', 'f15_13', 'f15_14', 'f15_15', 'f15_16']
print(data[bio_elements][(data[bio_elements] < 8) & (data[bio_elements] > 0)].describe())

# 4. Assignment
print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 4. Assigment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
# TODO  0 reinnehmen und -99 raus. evtl. noch weiteres prep; hier noch ein plot erstellen, der pro frage den Mittelwert darstellt und
#  ggf. irgendwie noch die std
print('Leute, die bereit sind für Bio mehr zu zahlen, würden im Schnitt x mehr zahlen:')
print(data['f17'][(data['f17'] > 0)].describe())
print('Leute, die die Frage beantwortet haben:')
prep_f17 = data['f17'][data['f17'] != 0]
prep_f17 = prep_f17.replace(-99, 0)
print(prep_f17.describe())

# 5. Assignment
print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 5. Assigment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')

# 6. Assignment
print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 6. Assigment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
# TODO prüfen, ob die 0er und 8er rausgennommen werden sollen; hier noch ein plot erstellen, der pro Frage den
#  Mittelwert darstellt und ggf. irgendwie noch die std; hier noch eine Korreltation oder Regression
bio_food = ['f16_1', 'f16_2', 'f16_3', 'f16_4', 'f16_5', 'f16_6', 'f16_7', 'f16_8', 'f16_9']
print(data[bio_food][(data[bio_food] < 8) & (data[bio_food] > 0)].describe())

# 7. Assignment
print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 7. Assigment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
logos = data[['f12_1', 'f12_2', 'f12_3', 'f12_4', 'f12_5', 'f12_6', 'f12_7', 'f12_8', 'f12_9']]
print('So oft wurden die einzelnen Bio-Siegel angekreuzt')
print(fn.sum_characteristics(logos.values))
print('Platz 1:')
print(fn.count_values(data, 'f13_1'))
print('Platz 2:')
print(fn.count_values(data, 'f13_2'))
print('Platz 3:')
print(fn.count_values(data, 'f13_3'))


# Kolgomorov Smirnof Test
# x = np.linspace(data['f9'])
print(stat.kstest(data['f9'], 'norm'))
# 1. Hypothesentest f9
without_child = data['f9'][(data['f2'] == 1) | (data['f2'] == 2)]
with_child = data['f9'][data['f2'] == 3]
print(tests.ztest(without_child, with_child))
without_child = data['f9'][(data['f23_1'] > 0) | (data['f23_2'] > 0) | (data['f23_3'] > 0) | (data['f23_4'] > 0)]
with_child = data['f9'][(data['f23_1'] == 0) & (data['f23_2'] == 0) & (data['f23_3'] == 0) & (data['f23_4'] == 0)]
print(tests.ztest(without_child, with_child))
