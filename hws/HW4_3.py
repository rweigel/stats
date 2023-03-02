import numpy as np
from matplotlib import pyplot as plt

# Average probability of event in each hour
po = 900/(1000*24)
lambda_ = 900/(1000*24)

# Part 1.

# Poisson solution
t = 24
kmax = 10
P_P = []
p = 1
k = 0
while p > 1e-4:
    p = ((lambda_*t)**k)*np.exp(-lambda_*t)/np.math.factorial(k)
    P_P.append(p)
    k = k + 1
x = np.arange(len(P_P))

# Simulated solution
# Use np.random.binomial to create an array n_S containing results of 1000
# experiments where n=24 values are drawn with a probability of success of po.
# Each array element of n_S is the number of success in the n=24 draws.
n_S = np.random.binomial(n=24, p=po, size=1000)

# The above does not create a full list of 1000*24 days, which we need later.
# We can compute an array e_S containing 24*1000 events with a probability
# of success using
e_S = np.random.binomial(n=1, p=po, size=1000*24)
# The number of events in a 24 hour period can be computed using
e_Sr = e_S.reshape((24,1000))
n_S = np.sum(e_Sr,axis=0)

P_S, _ = np.histogram(n_S, density=True, bins=-0.5+np.arange(len(P_P)+1))

# Exact solution
import math
def nCk(n,k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

P_B = np.empty(len(P_P))
for k in range(len(P_B)):
    P_B[k] = nCk(24, k)*(1-po)**(24-k)*po**k

# TODO: When no blue dot, P_S = 0. Add an annotation to make this more obvious.
plt.figure()
plt.grid()
plt.semilogy(x, P_B, 'r.')
plt.semilogy(x, P_P, 'g.')
plt.semilogy(x, P_S, 'b.')
plt.xticks(x)
plt.xlabel('Events per day (k)')
plt.ylabel('PMF')
plt.legend(['Binomial','Poisson: ($\lambda t)^ke^{\lambda t}/k!$','Simulated (1000 days)'])
plt.title('$t=%d$ hrs; $\lambda$=%.3f/hr' % (t, lambda_))

plt.savefig('figures/HW4_3.svg', transparent=True)
plt.savefig('figures/HW4_3.png', transparent=True)

plt.figure()
plt.grid()
plt.semilogy(x, np.abs(P_P-P_B), 'g.')
plt.semilogy(x, np.abs(P_P-P_S), 'b.')
plt.xticks(x)
plt.xlabel('Events per day (k)')
plt.ylabel('PMF difference')
plt.legend(['|Poisson - Binomial|','|Simulated - Binomial|'])
plt.title('$t=%d$ hrs; $\lambda$=%.3f/hr' % (t, lambda_))

plt.savefig('figures/HW4_3-error.svg', transparent=True)
plt.savefig('figures/HW4_3-error.png', transparent=True)


# Part 2.
# Create a list of 1000*24 zeros and ones, with a 1 having probability po.
#n = np.random.binomial(n=1, p=po, size=1000*24)
# Time index from 0 to 1000*24 - 1
t = np.arange(len(e_S))
# Time indices when there was an event
te = np.where(e_S == 1)[0]
dte = np.diff(te)
bin_edges   = np.arange(np.max(dte) + 1) + 0.5
bin_centers = 0.5 + bin_edges[0:-1]
P_dte, _ = np.histogram(dte, density=True, bins=bin_edges)

plt.figure()
plt.grid()
plt.plot(bin_centers, P_dte,'.')
xticks = plt.gca().get_xticks()
xticks = np.arange(25, np.max(dte)+1, 25)
plt.gca().set_xticks([1,*xticks])
plt.ylabel('PMF')
plt.xlabel('hours between flares')

plt.savefig('figures/HW4_3-dt.svg', transparent=True)
plt.savefig('figures/HW4_3-dt.png', transparent=True)
