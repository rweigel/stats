import numpy as np
from matplotlib import pyplot as plt

debug = False # True prints output

Ne = 10000  # Number of experiments
Nt = 100    # Number of trials per experiment
po = 0.4

import math
def nCk(n,k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

# Exact solution
P = np.empty(Nt)
for k in range(Nt):
    P[k] = nCk(Nt, k)*(1-po)**(Nt-k)*po**k

##############################################################################
# Solution without using np.random.binomial()
##############################################################################

n1 = np.empty(Ne)
n2 = np.empty(Ne)
for j in range(n1.size):   # Loop over experiments
    k1 = 0                 # Number of heads in p = 0.4 experiment
    k2 = 0                 # Number of heads in variable p experiment
    p1 = np.empty(Nt)
    p2 = np.empty(Nt)
    x = np.empty(Nt)
    for i in range(Nt):    # Loop over trials
        p1[i] = po
        p2[i] = po
        if i > 1 and x[i-1] <= po and x[i-2] <= po:
            p2[i] = po*1.1
        x[i] = np.random.uniform()
        if x[i] <= p1[i]:
            k1 = k1 + 1
        if x[i] <= p2[i]:
            k2 = k2 + 1
            if debug:
                print('j = {0:03d}  p = {1:.2f} H'.format(i, p2[i]))
        else:
            if debug:
                print('j = {0:03d}  p = {1:.2f} T'.format(i, p2[i]))

    n1[j] = k1
    n2[j] = k2

bin_centers = np.arange(102)    # 0, ..., 101
bin_edges   = bin_centers - 0.5 # -0.5, 0.5, ..., 100.5
bin_centers = bin_centers[0:-1] # remove last element

x_lim = [np.min([np.min(n1), np.min(n2)]) - 0.5,
         np.max([np.min(n1), np.max(n2)]) + 0.5]

plt.figure()
plt.grid(axis='y', color='k')

plt.hist(n1, bins=bin_edges, density=True)
hist1 = np.histogram(n1, bins=bin_edges)
plt.step(bin_centers, hist1[0]/np.sum(hist1[0]), where='mid', color='k')

hist2 = np.histogram(n2, bins=bin_edges)
plt.step(bin_centers, hist2[0]/np.sum(hist2[0]), where='mid', color='r')

plt.bar(np.arange(len(P)), P)

plt.xlabel('# heads in experiment')
plt.ylabel('P of # heads in experiment')
plt.title('# trials/experiment = {0:d}; # experiments = {1:d}'.format(Nt, Ne))
plt.xlim(x_lim)
plt.legend(['Experiment 1. p=0.4','Experiment 2. p varies','Binomial Formula'])

plt.savefig("figures/HW4_2.png", format="png", transparent=True)
plt.savefig("figures/HW4_2.svg", format="svg", transparent=True)

##############################################################################
# Solution using np.random.binomial()
##############################################################################

n1 = np.empty(Ne) # Number of success trials for p = 0.4
n2 = np.empty(Ne) # Number of success trials for variable p
r1 = np.empty(Nt) # Trial results for p = 0.40
r2 = np.empty(Nt) # Trial results for variable p

for j in range(n1.size):  # Loop over experiments
    r1 = np.random.binomial(n=1, p=0.4, size=Nt)
    n1[j] = np.sum(r1)
    for i in range(Nt):  # Loop over trials
        if i > 1 and r2[i-1] == 1 and r2[i-2] == 1:
            r2[i] = np.random.binomial(n=1, p=po*1.1, size=1)
        else:
            r2[i] = np.random.binomial(n=1, p=po, size=1)
    n2[j] = np.sum(r2)

plt.figure()
plt.grid(axis='y', color='k')

hist1 = np.histogram(n1, bins=bin_edges)
plt.step(bin_centers, hist1[0]/np.sum(hist1[0]), where='mid', color='k')

hist2 = np.histogram(n2, bins=bin_edges)
plt.step(bin_centers, hist2[0]/np.sum(hist2[0]), where='mid', color='r')

plt.bar(np.arange(len(P)), P)

plt.xlabel('# heads in experiment')
plt.ylabel('P of # heads in experiment')
plt.title('# trials/experiment = {0:d}; # experiments = {1:d}'.format(Nt, Ne))
plt.xlim(x_lim)
plt.legend(['Experiment 1. p=0.4','Experiment 2. p varies','Binomial Formula'])

plt.savefig('figures/HW4_2.svg', transparent=True)
plt.savefig('figures/HW4_2.png', transparent=True)