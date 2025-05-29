import unittest
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sts

#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()


#%store -r data
data = pd.read_csv('../data/final.csv')
dataa = data[['score', 'scored_by', 'volumes', 'chapters']]
print(dataa)

x = np.power(dataa['volumes'], 1 / 2)
y = dataa['score']
plt.scatter(x, y)
#plt.hold


k, b, rv, pv, k_err = sts.linregress(x, y)#, b_err
xx = np.linspace(0, 8, 100)

plt.plot(xx, k * xx + b)

plt.show()

xs = np.log10(dataa['scored_by'])
plt.figure()
ks, bs, rvs, pvs, k_errs = sts.linregress(xs, y)
xxs = np.linspace(2, 5, 10)#0
plt.scatter(xs, y)#, yy
plt.plot(xxs, xxs * ks + bs, color='red')
plt.show()