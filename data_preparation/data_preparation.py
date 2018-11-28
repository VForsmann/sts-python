import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as fn

data = fn.load_data('../daten_robinson.csv')
print(fn.set_zero_to_median(data, 'f22'))
# set_empty_values_new('f17_Comment')
# set_empty_values_new('f17', replace_value='-99')
# set_field_value_to_new_value('f1', 0, 1)
