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
data['f3_1'] = fn.set_field_value_to_new_value(raw_data, 'f3_1', 0, 8)
data['f3_2'] = fn.set_field_value_to_new_value(raw_data, 'f3_2', 0, 8)
data['f3_3'] = fn.set_field_value_to_new_value(raw_data, 'f3_3', 0, 8)
data['f3_4'] = fn.set_field_value_to_new_value(raw_data, 'f3_4', 0, 8)
data['f3_5'] = fn.set_field_value_to_new_value(raw_data, 'f3_5', 0, 8)
data['f3_6'] = fn.set_field_value_to_new_value(raw_data, 'f3_6', 0, 8)
data['f3_7'] = fn.set_field_value_to_new_value(raw_data, 'f3_7', 0, 8)
data['f3_8'] = fn.set_field_value_to_new_value(raw_data, 'f3_8', 0, 8)
data['f3_9'] = fn.set_field_value_to_new_value(raw_data, 'f3_9', 0, 8)
data['f3_10'] = fn.set_field_value_to_new_value(raw_data, 'f3_10', 0, 8)
data['f3_11'] = fn.set_field_value_to_new_value(raw_data, 'f3_11', 0, 8)

# f4_1 - f4_11 - set zero values to 8 --> not answered
data['f4_1'] = fn.set_field_value_to_new_value(raw_data, 'f4_1', 0, 8)
data['f4_2'] = fn.set_field_value_to_new_value(raw_data, 'f4_2', 0, 8)
data['f4_3'] = fn.set_field_value_to_new_value(raw_data, 'f4_3', 0, 8)
data['f4_4'] = fn.set_field_value_to_new_value(raw_data, 'f4_4', 0, 8)
data['f4_5'] = fn.set_field_value_to_new_value(raw_data, 'f4_5', 0, 8)
data['f4_6'] = fn.set_field_value_to_new_value(raw_data, 'f4_6', 0, 8)
data['f4_7'] = fn.set_field_value_to_new_value(raw_data, 'f4_7', 0, 8)
data['f4_8'] = fn.set_field_value_to_new_value(raw_data, 'f4_8', 0, 8)
data['f4_9'] = fn.set_field_value_to_new_value(raw_data, 'f4_9', 0, 8)
data['f4_10'] = fn.set_field_value_to_new_value(raw_data, 'f4_10', 0, 8)
data['f4_11'] = fn.set_field_value_to_new_value(raw_data, 'f4_11', 0, 8)
data['f4_12'] = fn.set_field_value_to_new_value(raw_data, 'f4_12', 0, 8)
data['f4_13'] = fn.set_field_value_to_new_value(raw_data, 'f4_13', 0, 8)
data['f4_14'] = fn.set_field_value_to_new_value(raw_data, 'f4_14', 0, 8)

# f5_1 - f5_14 - set zero values to 8 --> not answered
data['f5_1'] = fn.set_field_value_to_new_value(raw_data, 'f5_1', 0, 8)
data['f5_2'] = fn.set_field_value_to_new_value(raw_data, 'f5_2', 0, 8)
data['f5_3'] = fn.set_field_value_to_new_value(raw_data, 'f5_3', 0, 8)
data['f5_4'] = fn.set_field_value_to_new_value(raw_data, 'f5_4', 0, 8)
data['f5_5'] = fn.set_field_value_to_new_value(raw_data, 'f5_5', 0, 8)
data['f5_6'] = fn.set_field_value_to_new_value(raw_data, 'f5_6', 0, 8)
data['f5_7'] = fn.set_field_value_to_new_value(raw_data, 'f5_7', 0, 8)
data['f5_8'] = fn.set_field_value_to_new_value(raw_data, 'f5_8', 0, 8)
data['f5_9'] = fn.set_field_value_to_new_value(raw_data, 'f5_9', 0, 8)
data['f5_10'] = fn.set_field_value_to_new_value(raw_data, 'f5_10', 0, 8)
data['f5_11'] = fn.set_field_value_to_new_value(raw_data, 'f5_11', 0, 8)


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
