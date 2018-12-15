import pandas as pd
import statsmodels.api as sm
from sklearn import linear_model
from statsmodels.stats.outliers_influence import variance_inflation_factor

import functions as fn


def reg_for_prep_data(x, y):
    data = fn.load_data('../data_preparation/data_preparation.csv')
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    x = data[x]
    y = data[y]

    # sklearn
    regr = linear_model.LinearRegression()
    regr.fit(x, y)

    print('Intercept: \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)

    # statsmodels
    x = sm.add_constant(x)

    factor = []
    header = []
    for i in range(0, x.shape[1]):
        factor.append(variance_inflation_factor(x.values, i))
        header = x.columns
    vif = pd.DataFrame()
    vif = vif.append(pd.Series(factor), ignore_index=True)
    vif.columns = pd.Series(header)
    vif.rename(index={0: 'VIF Factor'}, inplace=True)
    print(vif.transpose())

    model = sm.OLS(y, x).fit()
    predictions = model.predict(x)

    print_model = model.summary()
    print(print_model)


# regression for assigment 1
food = ['f4_13', 'f8', 'f9', 'f10_1', 'f10_2', 'f15_8', 'f16_3', 'f16_8', 'f18_2']
well_being = 'f18_7'
# reg_for_prep_data(food, well_being)
sport = ['f3_3', 'f3_9']
well_being = 'f3_2'
reg_for_prep_data(sport, well_being)
