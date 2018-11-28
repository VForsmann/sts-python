import functions as fn

raw_data = fn.load_data('../daten_robinson.csv')
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

