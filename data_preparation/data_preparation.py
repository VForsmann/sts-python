import pandas as pd

import functions as fn
import numpy as np
raw_data = fn.load_data('../daten_robinson.csv')
tmp_field = []
# print(fn.set_zero_to_median(raw_data, 'f22'))
# set_empty_values_new('f17_Comment')
# set_empty_values_new('f17', replace_value='-99')
# set_field_value_to_new_value('f1', 0, 1)
# print(fn.descriptive_statistics(raw_data)['f22'])


# removes row with empty values
data = raw_data.drop(index=87)

# f1 - set zero values to median
data['f1'] = fn.set_zero_to_median(raw_data, 'f1')

# f2 - set zero values to median
data['f2'] = fn.set_zero_to_median(raw_data, 'f2')

# f3_1 - f3_11 - set zero values to 8 --> not answered
tmp_field = ['f3_1', 'f3_2', 'f3_3', 'f3_4', 'f3_5', 'f3_6', 'f3_7', 'f3_8', 'f3_9', 'f3_10', 'f3_11', ]
data[tmp_field] = fn.question_cleaning(data, tmp_field, '0', 8)


# f4_1 - f4_11 - set zero values to 8 --> not answered
tmp_field = ['f4_1', 'f4_2', 'f4_3', 'f4_4', 'f4_5', 'f4_6', 'f4_7', 'f4_8', 'f4_9', 'f4_10', 'f4_11', 'f4_12', 'f4_13',
             'f4_14']
data[tmp_field] = fn.question_cleaning(data,tmp_field, '0', 8)


# f5_1 - f5_14 - set zero values to 8 --> not answered
tmp_field = ['f5_1', 'f5_2', 'f5_3', 'f5_4', 'f5_5', 'f5_6', 'f5_7', 'f5_8', 'f5_9', 'f5_10', 'f5_11']
data[tmp_field] = fn.question_cleaning(data, tmp_field, '0', 8)

# Clean F15
tmp_field = ['f15_1', 'f15_2', 'f15_3', 'f15_4', 'f15_5', 'f15_6', 'f15_7', 'f15_8', 'f15_9', 'f15_10', 'f15_11',
             'f15_12', 'f15_13', 'f15_14', 'f15_15', 'f15_16']
data[tmp_field] = fn.question_cleaning(data, tmp_field, rep_value='0', rep_with=8)

# Clean F16
tmp_field = ['f16_1', 'f16_2', 'f16_3', 'f16_4', 'f16_5', 'f16_6', 'f16_7', 'f16_8', 'f16_9']
data[tmp_field] = fn.question_cleaning(data, tmp_field, rep_value='0', rep_with=8)

# Clean F18
tmp_field = ['f18_1', 'f18_2', 'f18_3', 'f18_4', 'f18_5', 'f18_6', 'f18_7', 'f18_8', 'f18_9']
data[tmp_field] = fn.question_cleaning(data, tmp_field, rep_value='0', rep_with=8)

# Clean F19
tmp_field = ['f19_1', 'f19_2', 'f19_3', 'f19_4', 'f19_5', 'f19_6', 'f19_7', 'f19_8', 'f19_9', 'f19_10']
data[tmp_field] = fn.question_cleaning(data, tmp_field, rep_value='0', rep_with=8)

# f6 - set zero values to 8
data['f6_1'] = fn.set_field_value_to_new_value(raw_data, 'f6_1', 0, 8)
data['f6_2'] = fn.set_field_value_to_new_value(raw_data, 'f6_2', 0, 8)
data['f6_3'] = fn.set_field_value_to_new_value(raw_data, 'f6_3', 0, 8)
data['f6_4'] = fn.set_field_value_to_new_value(raw_data, 'f6_4', 0, 8)
data['f6_5'] = fn.set_field_value_to_new_value(raw_data, 'f6_5', 0, 8)
data['f6_6'] = fn.set_field_value_to_new_value(raw_data, 'f6_6', 0, 8)
data['f6_7'] = fn.set_field_value_to_new_value(raw_data, 'f6_7', 0, 8)
data['f6_8'] = fn.set_field_value_to_new_value(raw_data, 'f6_8', 0, 8)
data['f6_9'] = fn.set_field_value_to_new_value(raw_data, 'f6_9', 0, 8)

# f7 - we do not use this question because of too large variations

# f8 - set zero value to median
data['f8'] = fn.set_zero_to_median(raw_data, 'f8')

# f9 - there is nothing to do here.

# f10 - set zero values to 8
data['f10_1'] = fn.set_field_value_to_new_value(raw_data, 'f10_1', 0, 8)
data['f10_2'] = fn.set_field_value_to_new_value(raw_data, 'f10_2', 0, 8)

# f11 - categorize
# catalogue
raw_catalogue = data[['f11_1', 'f11_2', 'f11_3', 'f11_4', 'f11_5', 'f11_6', 'f11_7']].replace(' ', '0')
trans_catalogue = raw_catalogue.transpose()
sum_catalogue = fn.sum_characteristics(trans_catalogue.values)
catalogue = pd.DataFrame(sum_catalogue).replace(2, 1).rename(index=str, columns={0: 'catalogue'})
