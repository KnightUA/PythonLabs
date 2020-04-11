import numpy as np
import pandas
from pandas import read_csv
from sklearn import preprocessing

dataset = read_csv("VideoHost.txt","\t")
print(dataset.values)
min_max_scaler = preprocessing.MinMaxScaler()
dataset_scaled = min_max_scaler.fit_transform(dataset.values)
print(dataset_scaled)
df = pandas.DataFrame(dataset_scaled)
print(df)
