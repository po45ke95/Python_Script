import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data = pd.read_csv('newcode02.csv',index_col='Item')
#print(data.head(10))
gender = data.groupby('PRO1Gender')
plt.ylabel('People')
gender.size().plot.bar()
plt.ylim(520,560)
plt.grid(True)

plt.show()

#git test