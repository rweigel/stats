import numpy as np
from matplotlib import pyplot as plt

# Average probability of event in each hour
po = 900/(1000*24)
lambda_ = 900/(1000*24)

# Exact solution
t = 24
kmax = 10
P = []
p = 1
k = 0
while p > 1e-4:
    p = ((lambda_*t)**k)*np.exp(-lambda_*t)/np.math.factorial(k)
    P.append(p)
    k = k + 1

P2 = np.random.binomial(n=24, p=po, size=1000)

n2, _ = np.histogram(P2, density=True, bins=-0.5+np.arange(len(P)+1))
x = np.arange(len(P))
plt.figure()
plt.grid()
plt.plot(x, P, 'k*')
plt.bar(x, n2, width=0.1)
plt.xticks(x)
plt.xlabel('Events per day')
plt.ylabel('PDF')
plt.legend(['Poisson: ($\lambda t)^ke^{\lambda t}/k!$','Simulated (1000 days)'])
plt.title('$t=%d$ hrs; $\lambda$=%.3f/hr' % (t, lambda_))

plt.savefig('figures/HW4_3.svg', transparent=True)
plt.savefig('figures/HW4_3.png', transparent=True)