import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
def func(C, K, sCo, n):
    return (K*(np.power(C-sCo, n)))
xdata = np.array([6.952,
                  6.652,
                  6.461,
                  6.311,
                  6.044,
                  5.922,
                  5.527,
                  5.133,
                  4.79,
                  4.584,
                  4.439])

ydata = np.array([2.43733,
                  2.128,
                  1.8552,
                  1.646,
                  1.56343,
                  1.429,
                  1.3012,
                  1.21567,
                  1.14,
                  0.949,
                  0.8682])

plt.scatter(xdata, ydata, s=20, label='data')
print ('test1')
popt, pcov = curve_fit(func, xdata, ydata, p0=[0.5, 0.5, 0.5], maxfev = 1000000)
xdata_t = np.linspace(0, 60, 60)
plt.plot(xdata_t, func(xdata_t, *popt), 'g--',
         label='fit: K=%5.3f, sCo=%5.3f, n=%5.3f' % tuple(popt))
plt.xlabel('Concentration (mg-C/L)')
plt.ylabel('Adsorbed amount (mg-C/g)')
plt.legend()
test_y = func(xdata, *popt)
#print("R2-score: %.2f" % r2_score(ydata , test_y))
plt.show()
print('done')