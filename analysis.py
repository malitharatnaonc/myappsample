import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

scores = pd.read_csv("collections.csv", header=None, index_col=0, names=['Code','PIPscore'])
lengths = pd.read_csv("proportions.csv", header=None, index_col=0, names=['Code', 'Length'])

data = scores.merge(lengths, left_index=True, right_index=True)
data.reset_index(level=0, inplace=True)

#PIP containing proteins
identified = pd.read_csv("humanpips2.csv", header=None, nrows=27)
identified = np.unique(identified[2])

interact = pd.read_excel('interacts.xlsx')
print(interact)

"""
nuclear = pd.read_csv("nuclear.csv")
nuclear = list(nuclear['Entry'])

data = data[data['Code'].isin(nuclear)]
data = data[data['Length'] < 0.5]

#Adding column with colour labels
def label_row(row):
	if row['Code'] in identified:
		return 'red'
	else:
		return 'black'

def sizing(row):
	if row['Code'] in identified:
		return 10
	else:
		return 1

data['Col'] = data.apply(lambda row: label_row(row), axis=1)
data['Size'] = data.apply(lambda row: sizing(row), axis=1)

#PLOT
plt.scatter(x=data['Length'], y=data['PIPscore'], s=data['Size'], alpha=0.5, c=data['Col'])
plt.show()
"""
