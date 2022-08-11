import pandas as pd
from sklearn.preprocessing import MinMaxScaler

filename = input("Enter the .csv file: ")

data = pd.read_csv(filename)
nameColumn = data.pop("name")
#permissionColumn = data.pop("permissions")

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

df = pd.DataFrame(scaled_data, columns=data.columns, index=data.index)

df.insert(0, "name", nameColumn)
#df.insert(71,"permissions",permissionColumn)

df.to_csv("normalized_data.csv")

print('Data has been normalized to "normalized_data.csv"')


