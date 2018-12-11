import pandas as pd
import functions as fn
import sklearn.metrics as skl

data = fn.load_data('../data_preparation/data_preparation.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
# reg = linear_model.Ridge(alpha=.5)
# reg.fit([data['f4_13'], data['f8'], data['f9'], data['f10_1'], data['f10_2'], data['f15_8'], data['f16_3'], data['f16_8'], data['f18_2']], [data['f18_7']])
#
# res1 = reg.coef_
# res2 = reg.intercept_
#
# print(res1)
# print(res2)

test = skl.matthews_corrcoef([data['f4_13'], data['f8'], data['f9'], data['f10_1'], data['f10_2'], data['f15_8'], data['f16_3'], data['f16_8'], data['f18_2']], [data['f18_7']])

print(test)