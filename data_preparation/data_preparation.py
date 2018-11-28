import pandas as pd

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
