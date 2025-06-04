import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import scipy.stats as sts
import scipy.stats as sts##
from statsmodels.formula.api import ols
import statsmodels.api as sm


data = pd.read_csv('../data/final.csv')
print(data.columns)

x = np.log10(data['scored_by']) #
y = data['score']
n = len(x)
t_table = 1.9734#0.0
#Поле корреляции
plt.scatter(x, y)
plt.show() # надо преобразовывать (сделано)
print(n)

k, b, cor, k_pval, k_err = sts.linregress(x, y)
s = np.power(y - (b + k * x), 2).sum() / (len(x) - 2)
print("параметры: b1, b0")

#;
print(k, b)#
print("коэффициент корреляцмм и коэффициент детерминации:")
print(cor, cor ** 2)
print('критерий Стьюдента для b1: p-value, tрасч')
print(k_pval, k / k_err)
print('критерий Стьюдента для b0: tтабл, tрасч')
b_err = (s * np.power(x, 2).sum() / n / np.power(x - x.mean(), 2).sum()) ** 0.5
print(t_table, b / b_err)
print('интервальная оценка для b1')
print("b1 =", k, "+-", t_table * k_err)
print('интервальная оценка для b0')
print('b0 =', b, '+-', t_table * b_err, '\n')
modell = sm.OLS(x, y).fit()
modell = ols('Y ~ X', pd.DataFrame({'X' : x, 'Y' : y})).fit()
ta = sm.stats.anova_lm(modell, typ=2)
print(ta)#еф
gq_f, gq_p, gq_ord = sm.stats.diagnostic.het_goldfeldquandt(y, sm.add_constant(x))##
print('\nТест Голдфелда-Квандта: F-статистика, p-value')
print(gq_f, gq_p)#dq
#modell.predict
print('предсказание')
yp = b + k * x.mean() * 1.05
print('yp =', yp)
print('оверительный интервал:')

print('yp =', yp, '+-', t_table * (s * (1 / n + 1 + (0.05 * x.mean()) ** 2) / np.power(x - x.mean(), 2).sum()) ** 0.5)#, '+='
#print((s / np.power(x - x.mean(), 2).sum()) ** 0.5, k_err)



#print(k_err)


