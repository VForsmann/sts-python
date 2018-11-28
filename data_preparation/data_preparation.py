import numpy as np
import pandas as pd
import csv_import as csv

data = csv.load_data()


# count the values and how often they appear
def count_values(field):
    unique, counts = np.unique(data[field], return_counts=True)
    rows = dict(zip(unique, counts))
    print(rows)


# replace its given value with zero
def set_empty_values_new(field, replace_value=' '):
    data[field] = data[field].replace(replace_value, 0)
    print(data[field])


# replace a value zero to median of the field
def set_zero_to_median(field):
    median = data[data != 0].median(skipna=True)
    data[field] = data[field].mask(data[field] == 0, median[field])
    print(data[field])


# replace a field value with a given new value
def set_field_value_to_new_value(field, replace_value, new_value):
    data[field] = data[field].replace(replace_value, new_value)
    print(data[field])


set_empty_values_new('f17_Comment')
set_empty_values_new('f17', replace_value='-99')

set_field_value_to_new_value('f1', 0, 1)
