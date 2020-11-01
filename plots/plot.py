import pandas as pd
import matplotlib.pyplot as plt

test1 = pd.read_csv('newcode02.csv', names=['PRO1Gender', 'PRO2City', 'PRO3Age'])
print(test1.groupby('PRO2City').PRO1Gender.sum())
