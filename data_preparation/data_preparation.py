import numpy as np
import pandas as pd
import csv_import as csv
import matplotlib.pyplot as plt
data = csv.load_data()


# count the values and how often they appear
def count_values(field):
    unique, counts = np.unique(data[field], return_counts=True)
    rows = dict(zip(unique, counts))
    print(rows)


# replace its given value with zero
def set_empty_values_new(field, replace_value=' '):
    data[field] = data[field].replace(replace_value, '0')
    print(data[field])


# replace a value zero to median of the field
def set_zero_to_median(field):
    median = data[data != 0].median(skipna=True)
    data[field] = data[field].mask(data[field] == 0, median[field])
    print(data[field])


# replace every zero value with the median
def clean_years():
    f22_data = np.array(data[['f22']])
    median = np.median(f22_data[f22_data > 0])
    f22_data[f22_data == 0] = median
    pd.DataFrame.hist(pd.DataFrame(f22_data))


def descriptive_statistics():
    print(data.describe())


def boxplot():
    plt.boxplot(data['f17'])


#set_empty_values_new('f17_Comment')
#set_empty_values_new('f17', replace_value='-99')
descriptive_statistics()
