# Useful for data processing and analysis
# panadas dataframe is 2d tabular data structure with labeled axes(rows and column)

import pandas as pd
import numpy as np

# create pandas dataframe
# pd.Dataframe(dataset.data, colums = datasets.feature_names)

# read csv file - csv file to pandas dataframe
df = pd.read_csv("diabetes.csv")
print(type(df), df.shape)

# print first 5 rows from dataset
print(df.head())

# export dataframe to csv file
# df.to_csv("diabetesExport.csv")

# export dataframe to exel
# df.to_excel("filename")

# create dataframe with random values
random_df = pd.DataFrame(np.random.rand(20, 10))
print(random_df.head())
print(random_df.shape)

# last 5 rows
print(random_df.tail())

# information about dataframe
print(random_df.info())

# find number of missing value 
print(random_df.isnull().sum())

# count the number of specific value - based on the labels
print(df.value_counts('Outcome'))

# group the values based on the mean
print(df.groupby('Outcome').mean())

# statistical data based on column
print(df.count())
print(df.mean())
print(df.std())
print(df.min())
print(df.max())

# all the statistic data
print(df.describe())

# manipulate dataframe

# add column to dataframe
df['columnname'] = "value"
print(df)

# remove a row
df.drop(index=0, axis=0)
# drop a column
df.drop(columns='columnname')

# locating a row using index value
print(df.iloc[1])

# locate a prticular column
print(df.iloc[:, 0]) # first column with all the rows

# Correlation
# positive correlation
# negative correlation

print(df.corr())

