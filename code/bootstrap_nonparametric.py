import numpy as np
from matplotlib import pyplot as plt

n = 20    # Number of samples per experiment
N = 10000 # Number of experiments
X = np.random.normal(loc=0, scale=1, size=(n))
Y = np.sum(np.power(X, 2))

Ystar = np.full(N, np.nan)
for i in range(Ystar.size):
    Xstar = np.random.choice(X, size=n, replace=True)
    Ystar[i] = np.sum(np.power(Xstar, 2))

bins = np.arange(0, np.max(Ystar), 0.5)
plt.hist(Ystar, bins=bins, density=True)
plt.xlabel('$Y^*$')
plt.ylabel('pdf($Y^*$)')
plt.title('$Y^*=\sum_{i=1}^{' + str(n) + '} X_i^{*2}$ ;   $X^*$ drawn with replacment\nfrom sample $[X_1, X_2, ..., X_{' + str(n) + '}]$   $X \sim{\mathcal{N}(0, 1)}$')

plt.savefig('figures/bootstrap_nonparametric.svg', transparent=True)
plt.savefig('figures/bootstrap_nonparametric.png', transparent=True)
