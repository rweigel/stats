import numpy as np
from matplotlib import pyplot as plt

debug = False # True -> prints output

Ne = 10000  # Number of experiments
Nt = 100    # Number of trials per experiment
po = 0.4

lamb = po
import math
def nCk(n,k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
                    
P = np.empty(Nt)    
for k in range(Nt):
    P[k] = nCk(Nt, k)*(1-po)**(Nt-k)*po**k

n  = np.empty(Ne)
n2 = np.empty(Ne)
for j in range(n.size):   # Loop over experiments
    k  = 0                 # Number of heads in experiment
    k2 = 0                 # Number of heads in experiment
    p  = np.empty(Nt)
    p2 = np.empty(Nt)
    x = np.empty(Nt)
    for i in range(Nt):  # Loop over trials
        p[i] = po
        p2[i] = po
        if i > 1 and x[i-1] <= po and x[i-2] <= po:
            p2[i] = 0.44
        x[i] = np.random.uniform()
        if x[i] <= p[i]:
            k = k + 1
        if x[i] <= p2[i]:
            k2 = k2 + 1
            if debug:
                print('j = {0:03d}  p = {1:.2f} H'.format(i, p2[i]))
        else:
            if debug:
                print('j = {0:03d}  p = {1:.2f} T'.format(i, p2[i]))
            
    n[j]  = k
    n2[j] = k2

bin_centers = np.arange(102)    # 0, ..., 101
bin_edges = bin_centers - 0.5   # -0.5, 0.5, ..., 100.5
bin_centers = bin_centers[0:-1] # remove last element

x_lim = [np.min(n) - 0.5, np.max(n) + 0.5]
    
plt.figure()
plt.grid(axis='y', color='k')
plt.plot(P,'k*')
plt.hist(n,bins=bin_edges,density=True)
hist = np.histogram(n, bins=bin_edges)
plt.step(bin_centers, hist[0]/np.sum(hist[0]), where='mid')

hist2 = np.histogram(n2, bins=bin_edges)
plt.step(bin_centers, hist2[0]/np.sum(hist2[0]), where='mid')

plt.xlabel('# heads in experiment')
plt.ylabel('P of # heads in experiment')
plt.title('# trials/experiment = {0:d}; # experiments = {1:d}'.format(Nt, Ne))
plt.xlim(x_lim)
plt.legend(['Binomial Formula','Experiment 1. p=0.4','Experiment 2. p varies'])

plt.savefig("figures/HW4_2.png", format="png", transparent=True)
plt.savefig("figures/HW4_2.svg", format="svg", transparent=True)
    