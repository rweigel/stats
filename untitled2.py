import numpy as np
from matplotlib import pyplot as plt

n     = 5
mu    = 10
sigma = 20

# n x 10,000 matrix
X = mu + sigma*np.random.randn(n, 10000)

# Compute 10,000 averages of n values
Xbar = np.mean(X, axis=0)

V = np.var(X, axis=0, ddof=1)
S = np.sqrt(V)

z = (Xbar - mu)/(sigma/np.sqrt(n))
t = (Xbar - mu)/(S/np.sqrt(n))
plt.figure()
plt.grid()
plt.hist(t, bins=np.linspace(-5,5,50), edgecolor='k', facecolor='k')
plt.hist(z, bins=np.linspace(-5,5,50), edgecolor='b', facecolor='b')
plt.xlabel('$t$ or $z$')
plt.ylabel('# in bin')
plt.title('$10^4$ t and z values using $n=4$')
plt.legend(['$t$','$z$'])

plt.savefig("hws/figures/compare_gaussian_and_t.png", format="png", transparent=True)
plt.savefig("hws/figures/compare_gaussian_and_t.svg", format="svg", transparent=True)

