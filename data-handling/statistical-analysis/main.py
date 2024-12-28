


import numpy as np
import pandas as pd

import statsmodels.api as sm
from scipy import stats
import pingouin as pg



def linear_regression_using_statsmodels(x, y):
    # Statsmodels: Linear Regression
    X = sm.add_constant(x)  # Adds a constant term to the predictor
    model = sm.OLS(y, X).fit()
    print("Statsmodels Linear Regression Results:")
    
    return model.summary()


# sample data for regression
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)


print(linear_regression_using_statsmodels(x, y))


# def t_test_using_scipy(group1, group2):
#     # Scipy: T-test
#     t_stat, p_value = stats.ttest_ind(group1, group2)
#     return t_stat, p_value

# group1 = np.random.normal(0, 1, 100)
# group2 = np.random.normal(0.5, 1, 100)
# t_stat, p_value = t_test_using_scipy(group1, group2)
# print("Scipy T-test Results:")
# print(f"t-statistic = {t_stat}, p-value = {p_value}")

def correlation_using_pingouin(data):
    # Pingouin: Correlation
    data = pd.DataFrame({'x': x, 'y': y})
    correlation = pg.corr(data['x'], data['y'])
    return correlation

data = pd.DataFrame({'x': x, 'y': y})
correlation = correlation_using_pingouin(data)
print("Pingouin Correlation Results:")
print(f"r = {correlation['r'].values[0]}, p-val = {correlation['p-val'].values[0]}")
