from pandas import read_csv
import pandas
from sklearn import preprocessing

df = read_csv("Base.txt","\t")
df.fillna(df.mean()).to_csv(r'TabSA.txt', index = False, header=True)
df.fillna(df.mode()).to_csv(r'TabMODA.txt', index = False, header=True)
df.fillna(df.median()).to_csv(r'TabMD.txt', index = False, header=True)
# Something going wrong
#x = df.values
#min_max_scaler = preprocessing.MinMaxScaler()
#x_scaled = min_max_scaler.fit_transform(x)
#df = pandas.DataFrame(x_scaled)

#df.to_csv(r'TabNorm.txt', index = False, header=True)