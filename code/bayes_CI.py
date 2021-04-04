import numpy as np
from matplotlib import pyplot as plt

def count(condition):
    return np.sum(condition)

N_T = 3  # Number of tosses/experiment
N_H = 2  # Number of heads in an experiment

N_E = 10000 # Number of experiments to run for each p_H.

dtheta = 1/N_T
ps = np.arange(0, 1 + dtheta, dtheta)
#ps = np.arange(0.4, 0.6 + dtheta, dtheta)
n_B = np.full(ps.size, np.nan)
p_theta = np.full(ps.size, np.nan)
for i in range(ps.size):
    x = np.random.binomial(N_T, ps[i], size=N_E)
    n_B[i] = count(x == N_H)

p_B = n_B/N_E
#print(np.sum(p_B))

plt.bar(ps, p_B*p_theta, width=dtheta/2, color='b', align='center')
plt.bar(ps, p_B, width=dtheta/2, color='k', alpha=0.5, align='center')
plt.xlabel('$p_{H}$ of coin')
plt.ylabel('P(experiment yields {0:d} heads)'.format(N_H))
plt.title('Experiment: Toss coins with different $p_H$ {0:d}x; Each bin is\n' \
          ' result from 10k reps of experiment for given $p_H$.' \
          .format(N_T))
plt.xticks(np.arange(0,11,1)/10)

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

# Check CLT

tmp = n_F/N_E
p = tmp.copy()
ci1 = [np.percentile(n_H, 2.5)/N_T, np.percentile(n_H, 97.5)/N_T]
ci2 = [N_H/N_T-1.96*0.5/np.sqrt(N_T), N_H/N_T+1.96*0.5/np.sqrt(N_T)]
print('CI from numerical experiment histogram: [{0:.2f}, {1:.2f}]'.format(ci1[0], ci1[1]))
print('CI predicted by CLT                   : [{0:.2f}, {1:.2f}]'.format(ci2[0], ci2[1]))

#print("p_H = {0:.2f} +/- {1:.2f}".format(N_H/N_T, 1.96*0.5/np.sqrt(N_T)))
