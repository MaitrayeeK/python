import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Seaborn built in dataset

# bill vs tip dataset
tips = sns.load_dataset('tips')
print(tips.head())

# Visualization of data
sns.set_theme()
sns.relplot(data=tips, x='total_bill', y='tip', col='time', hue='smoker', style='smoker', size='size')
plt.show()

# load iris dataset
iris = sns.load_dataset('iris')
print(iris.head())

# Scatter plot
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=iris)
plt.show()

# Titanic dataset
titanic = sns.load_dataset('titanic')

# Count plot
sns.countplot(x='class', data=titanic)
plt.show()

sns.countplot(x='survived', data=titanic)
plt.show()

# Bar plot
sns.barplot(x='sex', y='survived', hue='class', data=titanic)
plt.show()