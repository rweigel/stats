import numpy as np
from matplotlib import pyplot as plt

from lib.conffig import conffig
from lib.savefig import savefig

np.random.seed(3)

debug = False
dist = 'normal'

Ns = 100    # Number of samples per experiment
Ne = 10000  # Number of experiments

# 1

if dist == 'uniform':
  X = np.random.uniform(-1.0, 1.0, size=(Ns, Ne))
else:
  X = np.random.randn(Ns, Ne)

Xbar = np.mean(X, axis=0) # Compute average of each column

eps = 0.01
idx = np.abs(Xbar) < eps
f = np.sum(idx)/Ne

print(f'Fraction between [-{eps:.2g},{eps:.2g}] = {f:.2g}')
# Fraction between [-0.01, 0.01] = 0.076

# 2

F = []
ns = 10**np.arange(0, 5, 1)
F = np.zeros(ns.shape)

i = 0
eps = 0.01
for n in ns:
    X = np.random.randn(n, Ne)
    if dist == 'uniform':
        X = np.random.uniform(-1.0, 1.0, size=(n, Ne))
    Xbar = np.mean(X, axis=0)
    idx = np.abs(Xbar) < eps
    f = np.sum(idx)/Ne
    F[i] = f
    i = i + 1

# Remove zero F values to avoid log(0) error
ns = ns[F > 0]
F = F[F > 0]

conffig()

plt.figure()
plt.grid(which='minor', color=(0.8, 0.8, 0.8))
plt.grid(which='major', color=(0.3, 0.3, 0.3))
plt.loglog(ns, F, "k.")
plt.xlabel('$n$')
plt.ylabel('$f$')
plt.title(r'Fraction, $f$, of $\overline{X}$s in range $[-0.01,0.01]$')
savefig("HW3_2_2a")

# 3
X = np.random.randn(Ns, Ne)
Xbar = np.mean(X, axis=0) # Compute average of each column

flast = np.nan
for eps in np.arange(np.min(Xbar), np.max(Xbar), 0.01):
    idx = np.abs(Xbar) < eps
    f = np.sum(idx)/Ne
    if debug:
        print(f'Fraction between [-{eps:.4g},{eps:.4g}] = {f:.4g}')
    if f >= 0.99 and flast < 0.99:
        # Could use linear interpolation to get better estimate
        print(f'Fraction between [-{eps:.4g},{eps:.4g}] = {f:.4g}')
        # Fraction between [-0.258,0.258] = 0.9901
        break
    flast = f

# 4

Ns = 100    # Number of samples per experiment
Ne = 10000  # Number of experiments

Eps = []
Ns = 10**np.arange(0, 4, 1)
Eps = np.zeros(Ns.shape)

i = 0
for n in Ns:
    X = 10*np.random.randn(n, Ne)
    if dist == 'uniform':
        X = np.random.uniform(-1.0, 1.0, size=(n,Ne))
    Xbar = np.mean(X, axis=0) # Compute average of each column

    flast = np.nan
    for eps in np.arange(np.min(Xbar), np.max(Xbar), 0.001):
        idx = np.abs(Xbar) < eps
        f = np.sum(idx)/Ne
        if debug:
            print(f'Fraction between [-{eps:.4g},{eps:.4g}] = {f:.4g}') 
        if f >= 0.99 and flast < 0.99:
            # Could use linear interpolation to get better estimate
            print(f'n = {n:d}; Fraction between [-{eps:.4g},{eps:.4g}] = {f:.4g}') 
            # Fraction between [-0.08646,0.08646] = 0.9937
            break
        flast = f

    Eps[i] = eps
    i = i + 1

plt.figure()
plt.grid(which='minor', color=(0.8, 0.8, 0.8))
plt.grid(which='major', color=(0.2, 0.2, 0.2))
plt.loglog(Ns, Eps, 'k.', markersize=10, label='Computed values')
coefficients = np.polyfit(np.log10(Ns), np.log10(Eps), 1)
best_fit_line = np.poly1d(coefficients)
label = f"Best fit line: $\\epsilon$ = {10**coefficients[1]:.1f}n$^{{{coefficients[0]:.3f}}}$"
plt.loglog(Ns, 10**best_fit_line(np.log10(Ns)), "k--", label=label)
plt.legend()
plt.xlabel('$n$ values used for each $\\overline{X}$ calculation')
plt.ylabel('$\\epsilon$')
plt.title('99% of $\\overline{X}s$ in range [-$\\epsilon$,$\\epsilon$]')
savefig("HW3_2_2b")

# 5

"""
If a distribution is selected that has a zero mean, the general trend
is the same.
"""
