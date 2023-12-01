import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

# loading census and epa csvs

suffolk_merged = pd.read_csv("C:/Users/Braeden/Documents/Data Science/Erdos Project - EJ Demographics/suffolk_merged_acs+epa_tracts.csv")

# taking population percents

suffolk_merged['White Population'] = suffolk_merged['DP05_0064E'] / suffolk_merged['DP05_0063E']
suffolk_merged['Black Population'] = suffolk_merged['DP05_0065E'] / suffolk_merged['DP05_0063E']
suffolk_merged['Asian Population'] = suffolk_merged['DP05_0067E'] / suffolk_merged['DP05_0063E']
suffolk_merged['Hispanic Population'] = suffolk_merged['DP05_0071E'] / suffolk_merged['DP05_0063E']
suffolk_merged['POC Population'] = suffolk_merged['Black Population'] + suffolk_merged['Asian Population'] + suffolk_merged['Hispanic Population']

# cleaning unused columns

suffolk_merged_clean = suffolk_merged[['White Population','Black Population','Asian Population','Hispanic Population','POC Population','PM25','OZONE','DSLPM','CANCER','RESP','RSEI_AIR','PTRAF','PRE1960','PRE1960PCT','PNPL','PRMP','PTSDF','UST','PWDIS']]

# making the correlation table


plt.figure(figsize=(16,6))
sns.heatmap(suffolk_merged_clean.corr(), annot = True, cmap = 'BrBG')
plt.show()

y = suffolk_merged_clean['Black Population']
x = suffolk_merged_clean['PM25']

plt.scatter(x,y)
plt.show()