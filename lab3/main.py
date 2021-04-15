import matplotlib
import matplotlib.pyplot as plt


import numpy as np
import pandas as pd
import os
import seaborn as sns

from matplotlib import colors



#PART1

#step1
brainFile = './brainsize.txt'
brainFrame = pd.read_csv(brainFile)

#step2
brainFrame.head()


#PART 2

#step 1
brainFrame.describe()

# #step2 b
menDf = brainFrame[(brainFrame.Gender == 'Male')]
womenDf = brainFrame[(brainFrame.Gender == 'Female')]


#step2 c
menMeanSmarts = menDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)
plt.scatter(menMeanSmarts, menDf["MRI_Count"])

womenMeanSmarts = womenDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)
plt.scatter(womenMeanSmarts, womenDf["MRI_Count"])
# plt.show()

# #PART 3
# #step1

brainFrame.corr(method='pearson')

# print('women')
womenDf.corr(method='pearson')
# print('men')
menDf.corr(method='pearson')


# #PART 4
# #step 2
wcorr = womenDf.corr()
sns.heatmap(wcorr)
plt.savefig('women_correlations.png', tight_layout=True)

mcorr = menDf.corr()
sns.heatmap(mcorr)
plt.savefig('men_correlations.png', tight_layout=True)



