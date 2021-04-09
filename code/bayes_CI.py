import numpy as np
from matplotlib import pyplot as plt

def count(condition):
    return np.sum(condition)

N_T = 3  # Number of tosses/experiment
N_H = 2  # Number of heads in an experiment

N_E = 10000 # Number of experiments to run for each p_H.

dtheta = 0.01 

thetas = np.arange(0, 1 + dtheta, dtheta)
#ps = np.arange(0.4, 0.6 + dtheta, dtheta)
n_B = np.full(thetas.size, np.nan)
p_theta = np.full(thetas.size, np.nan)
for i in range(thetas.size):
    x = np.random.binomial(N_T, thetas[i], size=N_E)
    n_B[i] = count(x == N_H)

p_B = n_B/N_E
#print(np.sum(p_B))

# Bayesian
plt.bar(thetas, p_B*p_theta, width=dtheta/2, color='b', align='center')
plt.bar(thetas, p_B, width=dtheta/2, color='k', alpha=0.5, align='center')
plt.xlabel('$\\theta$ of coin')
plt.ylabel('P(experiment yields {0:d} heads)'.format(N_H))
plt.title('Experiment: Toss coins with different $\\theta$ {0:d}x; Each bin is\n' \
          ' result from 10k reps of experiment for given $\\theta$.' \
          .format(N_T))
plt.xticks(np.arange(0,11,1)/10)

# Frequentist
P_H = N_H/N_T
n_H = np.random.binomial(N_T, P_H, size=N_E)

plt.figure()
binsc = np.arange(0, N_T + 2)
n_F, _ = np.histogram(n_H, bins=binsc-0.5)
plt.bar(binsc[0:-1]/N_T, n_F/N_E, width=1/(2*N_T), color='r')
if N_T <= 10:
    plt.xticks(binsc[0:-1]/N_T)
plt.xlabel('$F_H$ (fraction of heads in experiment)')
plt.ylabel('$P(F_H)$')
plt.title('Experiment: Toss coin {0:d}x; coin has $p_H=${1:d}/{2:d}'.format(N_T, N_H, N_T) + \
          '\nAll bins represent results from 10k experiments')


# Check CLT. F_H is the sum of iid random variables:
# F_H = (1/N_T)(x1 + x2 + ... + x_{N_T})
# CLT says that as N_T -> infinity, pdf of F_H should approach Gaussian with
# std = (std of pdf of x)/sqrt(N_T). The variance of the pdf of x (which takes
# on values of 0 or 1 with equal probability) is, for p_H = 0.5
# var = (0 - 0.5)^2/2 + (1 - 0.5)^2/2 = 1/4, so
# (std of pdf of x) = 0.5. For arbitrary p_H, it is
# var = (0 - xbar)^2/2 + (1 - xbar)^2/2, where xbar = p_H

xbar = 2/3
var = (0 - xbar)**2/2 + (1 - xbar)**2/2
std = np.sqrt(var)

tmp = n_F/N_E
ci1 = [np.percentile(n_H, 2.5)/N_T, np.percentile(n_H, 97.5)/N_T]
ci2 = [N_H/N_T-1.96*std/np.sqrt(N_T), N_H/N_T+1.96*std/np.sqrt(N_T)]
print('CI from numerical experiment histogram: [{0:.2f}, {1:.2f}]'.format(ci1[0], ci1[1]))
print('CI predicted by CLT                   : [{0:.2f}, {1:.2f}]'.format(ci2[0], ci2[1]))
