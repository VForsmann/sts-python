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
