import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import statsmodels.api as sma

#the pca function is written for you, call this from your code to calculate the 1st PC
def pca_function(stdata):
    """Returns the sign identified 1st principal component of a data set.
    input: stdata - a n x t pandas data frame
    output: 1st principal component, standardised to s.d = 1 and
    signed to have the same sign as the cross sectional mean of the variables"""
    factor1_us = sma.PCA(stdata, 1).factors
    factor1 = (factor1_us - factor1_us.mean()) / factor1_us.std()
    sgn = np.sign(pd.concat([stdata.mean(1), factor1], axis=1).corr().iloc[1, 0])
    return factor1 * sgn

#produce your analysis for the following five variables
my_srs = ['INDPRO', 'UNRATE', 'PAYEMS', 'CPIAUCSL', 'BUSINVx']

df = pd.read_csv('2021-12.csv',  parse_dates=['sasdate'], dayfirst=True, index_col='sasdate')
df.head()

df.isna().sum()

df = df.dropna()

df.index

#making a copy of the dataframe

transformation_column = df.iloc[0]

#renaming the column keys to the transformations
df.rename(columns=transformation_column, inplace=True)

df.head()

df = df.drop(df.index[0])
df.head()

df = df.reset_index()

df.columns

df.dtypes

mask = (df['sasdate'] >= '01-01-1992') & (df['sasdate'] < '01-01-2020')

df1 = df.loc[mask]
df1.head()

column_names = df1.keys()

# The data description file
df_desc = pd.read_csv("fred_md_desc.csv", index_col='id')

df_clean = df_desc.dropna()

df_clean = df_clean.drop(df_clean.columns[0], axis=1)

df_clean = df_clean.reset_index()

keys = df_clean['id']

# A dictionary that maps keys to column names
key_to_column = {key: column for key, column in zip(keys, column_names)}

# The resulting dictionary
print(key_to_column)

# Renaming columns of the dataframe using the key_to_column dictionary
df1.rename(columns=key_to_column, inplace=True)