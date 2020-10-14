import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.pivot(index="A", columns='B', values='C').plot(kind='bar')

plt.show()