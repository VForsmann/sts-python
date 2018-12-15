import correlations.regression as regr
import functions as fn

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


