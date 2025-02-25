# py -m venv myenv will create a virtual environment
# myenv\Scripts\activate will activate the virtual environment
# pip install pandas, numpy, matplotlib, seaborn, scikit-learn will install the given libraries as well as some additional libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')

df = pd.read_csv('air quality data.csv')

print(df.head()) # top 5 rows and columns
print('\n')
print(df.shape) # gives total number of rows and columns
print('\n')
print(df.info()) # information about dataset
print('\n')
print(df.describe())  # summary of statistics
print('\n')
print(df.describe().T) # summary of statistics i.e, transpose of the original output
print('\n')
print(df.duplicated()) # to know the duplicate values for each row
print('\n')
print(df.duplicated().sum()) # to know duplicate values for overall dataset
print('\n')
print(df.isnull()) # to check missing values
print('\n')
df.dropna(subset='AQI', inplace=True) # drop the rows where 'AQI' has missing values
print(df.isnull().sum().sort_values(ascending=False))
print('\n')
print(df.shape) # updated rows and columns adter dropping 'AQI' null values
print('\n')
null_val = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending=False)
print(null_val) # null values percentage
