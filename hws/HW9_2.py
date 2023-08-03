import numpy as np
from numpy.fft import fft, ifft

def dft(y):
    N = len(y)
    q = int(N/2)
    a = np.full(q+1, np.nan)
    b = np.full(q+1, np.nan)
    f = np.full(q+1, np.nan)
    t = np.arange(N)
    a[0] = np.mean(y)
    b[0] = 0
    f[0] = 0
    for i in range(1, q+1):
        f[i] = i/N
        a[i] = np.sum(y*np.cos(2*np.pi*f[i]*t))
        b[i] = np.sum(y*np.sin(2*np.pi*f[i]*t))
    return f, 2*a/N, 2*b/N

# Verify dft function using class example
y = [0, 1, 0, -1]
N = len(y)
t = np.arange(N)
f, a, b = dft(y)
eps = np.finfo(np.double).eps;
assert(np.allclose(f, [0, 0.25, 0.5], atol=3*eps, rtol=0.0))
assert(np.allclose(a, [0, 0, 0], atol=3*eps, rtol=0.0))
assert(np.allclose(b, [0, 1, 0], atol=3*eps, rtol=0.0))

# 8.2.1
N = 1000
y = np.random.randn(N)
f, a, b = dft(y)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(y)
plt.ylabel('$y$')
plt.xlabel('time index')
plt.grid()
plt.savefig('figures/HW9_2_1.svg', transparent=True)
plt.savefig('figures/HW9_2_1.png', transparent=True, dpi=300)

plt.figure()
plt.plot(N*0.5*(a**2 + b**2))
plt.ylabel('$I$')
plt.xlabel('freq. index')
plt.grid()
plt.savefig('figures/HW9_2_2.svg', transparent=True)
plt.savefig('figures/HW9_2_2.png', transparent=True, dpi=300)

# 8.2.2
Nb = 1000
I2 = np.full(Nb, np.nan)
for i in range(0, Nb):
    y = np.random.randn(N)
    f, a, b = dft(y)
    I2[i] = N*0.5*(a[2]**2 + b[2]**2)

bin_edges = np.linspace(0, 10, 21)
dx = (bin_edges[1]-bin_edges[0])
bin_cents = bin_edges[0:-1] + dx/2;
hist, _ = np.histogram(I2, density=False, bins=bin_edges)

from scipy.stats import chi2

plt.figure()
plt.plot(bin_cents, hist/Nb, 'k.')
plt.plot(bin_cents, dx*chi2.pdf(bin_cents, df=2),'r.')
plt.grid()
plt.title('Parametric bootstrap sampling dist of $I(f_2)$')
plt.xlabel('$I(f_2)$')
plt.legend(['Bootstrap', '$\chi_2^2$'])
plt.ylabel('p')

plt.savefig('figures/HW9_2_3.svg', transparent=True)
plt.savefig('figures/HW9_2_3.png', transparent=True, dpi=300)

# CI can be found using method in HW 8.
