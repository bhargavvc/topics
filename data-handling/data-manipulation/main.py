# plotly gives the best visualization it gives web ui
# before running these function install dependecies 
# pipenv install matplotlib seaborn plotly pandas


import pandas as pd
import numpy as np
import polars as pl

import pdb


############ using Pandas ###########


def panads_clean_filter():
    data = {'Name': ['John', 'Jane', 'Doe'], 'Age': [28, 34, None], 'Salary': [70000, None, 45000]}
    df = pd.DataFrame(data)
    
    # df = df.dropna()  # Remove rows with missing values either of column (name, age, salary
    
    #alternative ways to keep the rows
    # df['Age'].fillna(df['Age'].mean(), inplace=True) # Fill missing age values with the mean age
    
    # df = df.fillna("This is empty value")  # Insated of removing we can fill with some value to keep the data rows
    
    return df
    
# print(panads_clean_filter())


def numpy_operations():
    
    arr = np.array([1, 2, 3, 4, 5])
    return np.mean(arr), np.median(arr), np.std(arr), np.var(arr)

# print(numpy_operations())


def polars_better_than_pandas():
    
    df = pl.DataFrame({'Name': ['John', 'Jane', 'Doe'], 'Age': [28, 34, None], 'Salary': [70000, None, 45000]})
    
    # return df.filter(pl.col('Age').is_not_null())  # Remove rows with missing values in the Age column
    return df  

print(polars_better_than_pandas())