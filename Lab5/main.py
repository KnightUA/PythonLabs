import numpy as np
from pandas import read_csv
from sklearn import preprocessing

dataset = read_csv("VideoHost.txt","\t")
print(dataset.iloc())
