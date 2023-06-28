import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Freundlich (C, K, n):
    return K * C**(1/n)

def Langmuir (C, K, qm):
    return qm * K * C / (1 + K * C)

xdata = np.linspace(0, 4, 50)

ydata = Freundlich(xdata, 1, 0.6) + 0.1 * np.random.default_rng().normal(size=xdata.size)

popt_freundlich, pcov_freundlich = curve_fit(Freundlich, xdata, ydata, maxfev = 1000000)

popt_langmuir, pcov_langmuir = curve_fit(Langmuir, xdata, ydata, maxfev = 1000000)

plt.scatter(xdata, ydata, c='b', label='data')

plt.plot(xdata, Freundlich(xdata, *popt_freundlich),
         label='Freundlich: K=%5.3f, n=%5.3f' % tuple(popt_freundlich))
plt.plot(xdata, Langmuir(xdata, *popt_langmuir),
         label='Langmuir: K=%5.3f, qm=%5.3f' % tuple(popt_langmuir))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
print ('done')