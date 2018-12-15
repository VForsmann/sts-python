import pandas as pd
import statsmodels.api as sm
from sklearn import linear_model
from statsmodels.stats.outliers_influence import variance_inflation_factor

import functions as fn

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

factor = []
header = []
for i in range(0, X.shape[1]):
    factor.append(variance_inflation_factor(X.values, i))
    header = X.columns
vif = pd.DataFrame()
vif = vif.append(pd.Series(factor), ignore_index=True)
vif.columns = pd.Series(header)
vif.rename(index={0: 'VIF Factor', 1: 'Header'}, inplace=True)
print(vif.transpose())

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)
