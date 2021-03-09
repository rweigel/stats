# HW 6.1 Bootstrapping a Sample Distribution
# PHYS 590
# James K. Williams
# 8 March 2021

import numpy as np
import matplotlib.pyplot as plt

N = 10    # number of trials
B = 10000  # number of experiments
mu = 1.0
sigma = 1.0

# Arrays:
# a = E*N random numbers from a standard normal distributio.
#     in E rows and N columns
# y = sum of the squares of each row

a = np.empty(B*N)
Y = np.empty(B)
Ystar = np.empty(B)
rng = np.random.default_rng()

# Part 1

a = rng.normal(loc=mu, scale=sigma, size=B*N).reshape((B,N))
a2 = a**2
Y = a2.sum(axis=1)  # Sum the columns.

# Part 2

# Draw with replacement N values from each row of a.
for i in range(B):
    b = rng.choice(a[i], size=N, replace=True)
    b2 = b**2
    Ystar[i] = b2.sum()

# Plot the results

binmin = min(np.min(Y), np.min(Ystar)) - 0.5
binmax = max(np.max(Y), np.max(Ystar)) + 0.5
# binmin = np.min(Ystar) - 0.5
# binmax = np.max(Ystar) + 0.5
xlim = [np.floor(binmin), np.ceil(binmax)]
bin_edges = np.linspace(np.floor(binmin), np.ceil(binmax), 50)

pdf, _ = np.histogram(Y, density=True)
pdf_star, _ = np.histogram(Ystar, density=True)

fig, ax = plt.subplots(1, 1, figsize=(6,4))
fig.tight_layout(pad=3)
ax.set_title('Bootstrapping Trials')

print('min, max Y', Y.min(), Y.max())
print('min, max Y*', Ystar.min(), Ystar.max())

#ax.plot(pdf, pdf_star, '.')
kwargs = {'alpha':0.5, 'color':'tab:blue'}
ax.hist(Y, bins = bin_edges, density=True, label='Y', **kwargs)
kwargs = {'alpha':0.3, 'color':'tab:brown'}
ax.hist(Ystar, bins= bin_edges, density=True, label='Y*', **kwargs)
ax.set_xlabel('Y')
ax.set_ylabel('Probability density')
ax.legend()
kwargs = {'color':'tab:gray', 'lw':0.3}
ax.grid(**kwargs)

fig.savefig('junk.png', format='png')
plt.show()