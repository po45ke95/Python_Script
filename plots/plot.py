import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('newcode02.csv',index_col='Item')
#print(data.head(10))
gender = data.groupby('PRO1Gender')
city = data.groupby('PRO2City')
#print(type(gender))
#print(gender.size())
#print(city.size())
gender.get_group(1).head