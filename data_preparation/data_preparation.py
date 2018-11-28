import functions as fn
import numpy as np

raw_data = fn.load_data('../daten_robinson.csv')
# print(fn.set_zero_to_median(raw_data, 'f22'))
# set_empty_values_new('f17_Comment')
# set_empty_values_new('f17', replace_value='-99')
# set_field_value_to_new_value('f1', 0, 1)
# print(fn.descriptive_statistics(raw_data)['f22'])

# removes row with empty values
data = raw_data.drop(index=87)

