import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sts
from statsmodels.formula.api import ols
import statsmodels.api as sm

data = pd.read_csv('../data/final.csv')
print(data.columns)
print(len(data))
#%Xdata
data['scored_by'] = np.log10(data['scored_by'])
data['chapters'] = np.power(data['chapters'], 0.5)
X = data[['scored_by', 'volumes', 'chapters',  'has Romance', 'has Comedy', 'has Hentai', 'has Fantasy',
       'has Boys Love', 'has School', 'has Historical', 'has Harem',
       'has Psychological', 'has Isekai']].to_numpy()
X = np.hstack((np.ones((X.shape[0], 1)), X))
Y = data[['score']].to_numpy()
data_x = data[['score' ,'scored_by', 'volumes', 'chapters',  'has Romance', 'has Comedy', 'has Hentai', 'has Fantasy',
       'has Boys Love', 'has School', 'has Historical', 'has Harem',
       'has Psychological', 'has Isekai']]
corr = data_x.corr().round(2)
f = open('coor.txt', 'w')
f.write(str(corr))#
f.close()

#X.corr#C
print(str(corr.to_string()))
#B = np.linalg.inv(X.T @ X) @ X.T @ Y
##########################
##########################
#преобразованные chapters, scored_by; volumes убираем(корреляция с chapters), наибольшая корреляция среди категориальных у
#has Boys Love, Hentai
#############################
#############################


#print(B)

