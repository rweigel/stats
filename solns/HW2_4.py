import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.default'] = 'regular'

#np.random.seed(1)
mu = 0
sigma = 1

n = 100  # Number of samples per experiment
ne = 1000 # Number of experiments

s = 1.96
delta = s/np.sqrt(n)

X = np.random.normal(loc=mu, scale=sigma, size=(n, ne))

Xbar = np.mean(X, axis=0)

# Computing fractions without using a loop:
above = np.where(Xbar + delta > mu, 1, 0)
below = np.where(Xbar - delta < mu, 1, 0)
both = np.logical_and(above, below)
f_below = np.sum(below)/ne
f_above = np.sum(above)/ne
print(f"Fraction of X_bar + σ/√n > μ: {f_above}")
print(f"Fraction of X_bar - σ/√n < μ: {f_below}")
print(f"Fraction where both contraints satisfied: {np.sum(both)/ne}")

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

ax[0].axvline(x=-delta, color=(0.5, 0.5, 0.5), linestyle='--')
ax[0].axvline(x=+delta, color=(0.5, 0.5, 0.5), linestyle='--')

ax[0].bar(bin_c, nXbar, width=dx*0.99, color='k')
ax[0].set_xlabel('$\\overline{X}$')
ax[0].set_ylabel('# in bin')
ax[0].set_title(f'Gray: Range $[\\overline{{X}}-{s:0.2f}/\\sqrt{{n}},\\overline{{X}}+{s:0.2f}/\\sqrt{{n}}]$ does not trap $\\mu$', fontsize=10)
ax[0].set_xlim(-0.5, 0.5)
ax[0].set_xticks(bin_c)
ax[0].legend([f'$\\pm {s:0.2f}/\\sqrt{{n}}$'], loc='upper left')
ax[0].axvspan(-delta, ax[0].get_xlim()[0], color='gray', alpha=0.5)
ax[0].axvspan(+delta, ax[0].get_xlim()[1], color='gray', alpha=0.5)
ax[0].text(0.21, ax[0].get_ylim()[1]*0.7, f'Fraction: {1-f_above:0.3f}', fontsize=10, bbox=dict(facecolor='white', alpha=0.0))
ax[0].text(-0.49, ax[0].get_ylim()[1]*0.7, f'Fraction: {1-f_below:0.3f}', fontsize=10, bbox=dict(facecolor='white', alpha=0.0))

n_out = 0
for i in range(0, ne):
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
#title = f'Fraction of {ne} experiments where\nrange does not contain 0: {n_out/ne:.4f}'
#print(title)
ax[1].set_title(f"Sample of ranges; red => no trapping of $\\mu = {mu}$")
ax[1].set_ylabel('Experiment number')
ax[1].set_xlabel('Value in range')

fig.savefig("HW2_4.svg", transparent=True)
fig.savefig("HW2_4.png", dpi=300)

