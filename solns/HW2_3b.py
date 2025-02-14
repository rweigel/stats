import numpy as np
from matplotlib import pyplot as plt

np.random.seed(3)

debug = False

Ns = 100    # Number of samples per experiment
Ne = 10000  # Number of experiments

# 1

X = np.random.randn(Ns, Ne)
Xbar = np.mean(X, axis=0) # Compute average of each column
eps = 0.01
idx = np.abs(Xbar) < eps
f = np.sum(idx)/Ne

print('Fraction between [-%.2g,%.2g] = %.2g' % (eps, eps, f))
# Fraction between [-0.01,0.01] = 0.076

# 2

F = []
Ns = 10**np.arange(0, 4, 1)
F = np.zeros(Ns.shape)

i = 0
for n in Ns:
    X = np.random.randn(n,Ne) 
    Xbar = np.mean(X, axis=0)
    eps = 0.01
    idx = np.abs(Xbar) < eps
    f = np.sum(idx)/Ne
    F[i] = f
    i = i + 1

plt.figure()
plt.grid(which='minor', color=(0.9, 0.9, 0.9))
plt.grid(which='major', color=(0.2, 0.2, 0.2))
plt.loglog(Ns, F, marker=".")
plt.xlabel('n')
plt.title('Fraction of %d $\\bar{X}$s in range [-0.01,0.01]' % Ne)
plt.savefig("HW2_3b2.png", format="png", transparent=True)
plt.savefig("HW2_3b2.svg", format="svg", transparent=True)

# 3
Ns = 100    # Number of samples per experiment
Ne = 10000  # Number of experiments
X = np.random.randn(Ns, Ne)
Xbar = np.mean(X, axis=0) # Compute average of each column

flast = np.nan
for eps in np.arange(np.min(Xbar), np.max(Xbar), 0.01):
    idx = np.abs(Xbar) < eps
    f = np.sum(idx)/Ne
    if debug:
        print('Fraction between [-%.4g,%.4g] = %.4g' % (eps, eps, f)) 
    if f >= 0.99 and flast < 0.99:
        # Could use linear interpolation to get better estimate
        print('Fraction between [-%.4g,%.4g] = %.4g' % (eps, eps, f)) 
        # Fraction between [-0.258,0.258] = 0.9901
        break
    flast = f

# 4
import time as time
np.random.seed(int(time.time()))

Ns = 100    # Number of samples per experiment
Ne = 10000  # Number of experiments

Eps = []
Ns = 10**np.arange(0, 4, 1)
Eps = np.zeros(Ns.shape)

i = 0
for n in Ns:
    X = 10*np.random.randn(n, Ne)
    #X = np.random.uniform(-1.0, 1.0, size=(n,Ne))
    Xbar = np.mean(X, axis=0) # Compute average of each column

    flast = np.nan
    for eps in np.arange(np.min(Xbar), np.max(Xbar), 0.001):
        idx = np.abs(Xbar) < eps
        f = np.sum(idx)/Ne
        if debug:
            print('Fraction between [-%.4g,%.4g] = %.4g' % (eps, eps, f)) 
        if f >= 0.99 and flast < 0.99:
            # Could use linear interpolation to get better estimate
            print('n = %d; Fraction between [-%.4g,%.4g] = %.4g' % (n, eps, eps, f)) 
            # Fraction between [-0.08646,0.08646] = 0.9937
            break
        flast = f

    Eps[i] = eps
    i = i + 1

plt.figure()
plt.grid(which='minor', color=(0.9, 0.9, 0.9))
plt.grid(which='major', color=(0.2, 0.2, 0.2))
plt.loglog(Ns, Eps, marker=".")
plt.xlabel('$n$ values used for each $\\bar{X}$ calculation')
plt.ylabel('$\\epsilon$')
plt.title('99% of $\\bar{X}s$ in range [-$\\epsilon$,$\\epsilon$]')
plt.savefig("HW2_3b4.png", format="png", transparent=True)
plt.savefig("HW2_3b4.svg", format="svg", transparent=True)

# 5

"""
If a distribution is selected that has a zero mean, the general trend
is the same. This is expected based on the Central Limit Theorem.
"""
