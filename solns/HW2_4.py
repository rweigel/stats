import numpy as np
from matplotlib import pyplot as plt

#np.random.seed(1)

n = 100  # Number of samples per experiment
ne = 10000 # Number of experiments
X = np.random.randn(n, ne)

Xbar = np.mean(X, axis=0)
bin_c = np.linspace(-0.5, 0.5, 11, endpoint=True)
print("Bin centers:")
print(bin_c)

dx = bin_c[1]-bin_c[0]
print(f"Bin width: {dx}")

bin_e = bin_c - dx/2 # Bin edges
print("Bin edges:")
print(bin_e)

nXbar, _ = np.histogram(Xbar, bins=bin_e)
bin_c = bin_c[0:-1]

print("Mean of X_bar = {:.8f}".format(np.mean(Xbar)))
print("(std of X_bar)*sqrt(n) = {:.8f}".format(np.std(Xbar)*np.sqrt(n)))

fig, ax = plt.subplots(2, 1, figsize=(5, 9))
plt.subplots_adjust(hspace=0.4)

ax[0].bar(bin_c, nXbar, width=dx*0.99, color='k')
ax[0].set_xlabel('$\\bar{X}$')
ax[0].set_ylabel('# in bin')
ax[0].set_title(f'Histogram of {ne} $\\bar{{X}}$ values\nEach computed by sampling {n} values from $N(0,1)$')
ax[0].set_xlim(-0.5, 0.5)
ax[0].set_xticks(bin_c)

n_out = 0
for i in range(0, ne):
  delta = 1.96/np.sqrt(n)
  r = [Xbar[i] - delta, Xbar[i] + delta]
  if r[0] > 0 or r[1] < 0:
    n_out += 1
    if i < 100:
      ax[1].plot(r, [i+1, i+1], color='r')
  else:
    if i < 100:
      ax[1].plot(r, [i+1, i+1], color='k')

ax[1].grid()
ax[1].axvline(x=0, color='k', linestyle='--')
title = f'Fraction of {ne} experiments where\nrange does not contain 0: {n_out/ne:.4f}'
print(title)
ax[1].set_title(title)
ax[1].set_ylabel('Experiment number')
#ax[1].set_xlabel('Range of $\\bar{X}$')

fig.savefig("HW2_4.svg")
fig.savefig("HW2_4.png", dpi=300)

