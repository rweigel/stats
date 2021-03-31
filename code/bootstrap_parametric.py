import numpy as np
from matplotlib import pyplot as plt

n = 5     # Number of samples per experiment
N = 10000 # Number of experiments
X = np.random.normal(loc=0, scale=1, size=(N, n))

bins = np.arange(0, 30, 0.5)
Y = np.sum( np.power(X, 2), axis=1)

plt.hist(Y, bins=bins, density=True)
plt.xlabel('$Y$')
plt.ylabel('pdf($Y$)')
plt.title('$Y=\sum_{i=1}^{' + str(n) + '} X_i^2$ ;   $X \sim{\mathcal{N}(0, 1)}$')

plt.savefig('figures/bootstrap_parametric.svg', transparent=True)
plt.savefig('figures/bootstrap_parametric.png', transparent=True)
