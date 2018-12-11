import numpy as np
import pandas as pd


def sum_characteristics(data: np.numarray):
    int_data = data.astype(np.int)
    sum_data = sum(int_data)
    return sum_data


def load_data(file):
    return pd.read_csv(file, sep=';', na_values='Nothing', error_bad_lines=False)


# count the values and how often they appear
def count_values(data, field):
    unique, counts = np.unique(data[field], return_counts=True)
    rows = dict(zip(unique, counts))
    return rows


# replace its given value with zero
def set_empty_values_new(data, field, replace_value=' '):
    data[field] = data[field].replace(replace_value, '0')
    return data[field]


# replace a value zero to median of the field
def set_zero_to_median(data, field):
    answer = np.array(data[[field]])
    median = np.median(answer[answer > 0])
    answer[answer == 0] = median
    data[field] = answer
    return data[field]


def descriptive_statistics(data):
    return data.describe()


# replace a field value with a given new value
def set_field_value_to_new_value(data, field, replace_value, new_value):
    data[field] = data[field].replace(replace_value, new_value)
    return data[field]


# helper method for filling in empty values, replace them and convert them into int
def question_cleaning(data, field, rep_value, rep_with):
    data[field] = set_empty_values_new(data, field)
    data[field] = set_field_value_to_new_value(data, field, rep_value, rep_with)
    # to int, if numbers are strings
    if isinstance(rep_value, str):
        data[field] = data[field].astype(np.int)
    return data[field]


# creates new variable Altersklasse which is clustered
def create_age(data):
    data['Alter'] = 2018 - data['f22']
    data['Alter'] = data['Alter'].replace(2018, 0)
    data['Altersklasse'] = 0
    data.loc[(data['Alter'] <= 30) & (data['Alter'] > 0), ['Altersklasse']] = 1
    data.loc[(data['Alter'] >= 30) & (data['Alter'] <= 50), ['Altersklasse']] = 2
    data.loc[(data['Alter'] >= 50) & (data['Alter'] <= 2017), ['Altersklasse']] = 3
    return data

# creates new variable income_class which is clustered
def create_income_class(data):
    data['income_class'] = 0
    data.loc[(data['f26'] == 1) | (data['f26'] == 2), ['income_class']] = 1
    data.loc[(data['f26'] == 3) | (data['f26'] == 4), ['income_class']] = 2
    data.loc[(data['f26'] == 5) | (data['f26'] == 6), ['income_class']] = 3
    return data

def difference(data):
    data['difference'] = 99
    data['f18_2'] = pd.to_numeric(data['f18_2'], errors='coerce')
    data['f18_2'] = pd.to_numeric(data['f18_9'], errors='coerce')
    data['difference'] = data['f18_2'](([data['f18_2'].isin([1]) | data['f18_2'].isin([2]) | data['f18_2'].isin([6])| data['f18_2'].isin([7])]) & (data['f18_9'][data['f18_9'].isin([1]) | data['f18_9'].isin([2]) | data['f18_9'].isin([6]) | data['f18_9'].isin([7]))]))
    return data


#data['f26'] = pd.to_numeric(data['f26'].astype('str').str.replace(',', '.'), errors='coerce')
