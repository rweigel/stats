import numpy as np
from matplotlib import pyplot as plt

n     = 5
mu    = 10
sigma = 20

# n x 10,000 matrix
X = mu + sigma*np.random.randn(n, 10000)

# Compute 10,000 averages of n values
Xbar = np.mean(X, axis=0)

# Histogram is not centered on the origin and has
# standard deviation != 1
plt.figure()
plt.hist(Xbar, bins=np.linspace(-60,70,100))
plt.grid()
plt.xlabel('$\overline{X}$')
plt.ylabel('# in bin')

# Compute standardized variable
z = (Xbar - mu)/(sigma/np.sqrt(n))
plt.figure()
plt.hist(z, bins=np.linspace(-3.5,3.5,100))
plt.grid()
plt.xlabel('$z = (\overline{X}-\mu)/(\sigma/\sqrt{n})$')
plt.ylabel('# in bin')

V = np.var(X, axis=0, ddof=1)
S = np.sqrt(V)

t = (Xbar - mu)/(S/np.sqrt(n))
plt.figure()
plt.hist(z, bins=np.linspace(-3.5,3.5,100))
plt.xlabel('$t = (\overline{X}-\mu)/(S/\sqrt{n})$')
plt.ylabel('# in bin')


plt.legend(['t distribution','z distribution'])

X2 = np.power(X,2)

e2 = np.sum(X2, axis=0)

plt.hist(e2)
plt.xlabel('e2')
