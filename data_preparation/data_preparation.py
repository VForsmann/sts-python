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


