import functions as fn
import correlations.regression as regr
data = fn.load_data('../data_preparation/data_preparation.csv')


# 1. Assignment
# regression for assigment 1
food = ['f4_13', 'f8', 'f9', 'f10_1', 'f10_2', 'f15_8', 'f16_3', 'f16_8', 'f18_2']
well_being = 'f18_7'
regr.reg_for_prep_data(food, well_being, data)
sport = ['f3_3', 'f3_9']
well_being = 'f3_2'
regr.reg_for_prep_data(sport, well_being, data)

# 2. Assignment
print(data['f4_13'].describe())
