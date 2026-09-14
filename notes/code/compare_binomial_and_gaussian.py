import numpy as np

n = 6
p = 1/4
x = np.arange(n+1)

import scipy.stats
# SciPy has a function for this PMF.
P_binom = scipy.stats.binom.pmf(x, n, p)

P_gauss = (1/np.sqrt(2*np.pi*n*p*(1-p)))*np.exp(-(x-n*p)**2/(2*n*p*(1-p)))

import matplotlib.pyplot as plt
plt.plot(x-n*p, P_binom, 'o', label='Binomial')
plt.plot(x-n*p, P_gauss, '*', label='Gaussian')
plt.xlabel(r'$x-np$')
plt.ylabel('Probability')
plt.title(f'$n={n}; p={p}$')
plt.legend()
plt.grid(True)
plt.show()