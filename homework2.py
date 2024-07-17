import pandas as pd
df = pd.read_csv('Machine.csv', sep=';')
print(df.columns)
print(df.shape)
print(df.info())
print(df.head(6))
print(df.describe)
print(df.sample)
print(df.nlargest(2, 'footfall'))
print(df.nsmallest(2,'footfall'))
print(df.iloc[4:7,[1,3]])
mean_values = df.mean()
mask = (df > mean_values)
data = df[mask.all(axis=1)]
print(data)
mean_values_last_two = df.iloc[:, -2:].mean(axis=1)
mask = (df.iloc[:, -2:] > mean_values_last_two.values[:, None])
data = df[mask.all(axis=1)]
print(data)