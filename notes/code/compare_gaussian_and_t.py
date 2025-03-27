import numpy as np
from matplotlib import pyplot as plt

nx    = 5 # 10^nx experiments
n     = 5 # n samples per experiment
mu    = 10
sigma = 20

# n x nx matrix
X = mu + sigma*np.random.randn(n, 10**nx)

# Compute 10,000 averages of n values
xbar = np.mean(X, axis=0)
s = np.std(X, axis=0, ddof=1)

z = (xbar - mu)/(sigma/np.sqrt(n))
t = (xbar - mu)/(s/np.sqrt(n))
plt.figure()
plt.grid()
plt.hist(t, bins=np.linspace(-5,5,50), edgecolor='k', facecolor='k', histtype='step', linewidth=2)
plt.hist(z, bins=np.linspace(-5,5,50), edgecolor='b', facecolor='b', histtype='step', linewidth=2)
plt.xlabel('$t$ or $z$')
plt.ylabel('# in bin')
plt.title(f'$10^{nx}$ draws of $n={n}$ from $N({mu},{sigma}^2)$')
plt.legend([r'$t=(\overline{x}-\mu)/(s/\sqrt{n})$', r'$z=(\overline{x}-\mu)/(\sigma/\sqrt{n})$'])

plt.savefig("figures/compare_gaussian_and_t.png", format="png")
plt.savefig("figures/compare_gaussian_and_t.svg", format="svg", transparent=True)
