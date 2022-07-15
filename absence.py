import pandas as pd

df=pd.read_excel("Chronic Absence Rate(%).xlsx",header=2)
print(df.describe())
print(df.head())
print (df.columns)
