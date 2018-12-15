import pandas as pd
import functions as fn
from sklearn import linear_model
import statsmodels.api as sm

data = fn.load_data('../data_preparation/data_preparation.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
X = data[['f4_13', 'f8', 'f9', 'f10_1', 'f10_2', 'f15_8', 'f16_3', 'f16_8', 'f18_2']]
Y = data['f18_7']
# sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# statsmodels
X = sm.add_constant(X)

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)
# test = skl.matthews_corrcoef([data['f4_13'], data['f8'], data['f9'], data['f10_1'], data['f10_2'], data['f15_8'], data['f16_3'], data['f16_8'], data['f18_2']], [data['f18_7']])

print()