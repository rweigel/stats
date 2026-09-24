import math

# Average probability of event in each hour
p = 900/(1000*24)
lambda_ = 900/(1000*24)
print(lambda_)

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(25, dtype=int)

# Exact Binomial probability mass function
P_B = np.zeros_like(x, dtype=float)
for i in range(len(x)):
    P_B[i] = math.factorial(24)/(math.factorial(x[i])*math.factorial(24-x[i])) * p**x[i] * (1-p)**(24-x[i])

print(P_B)
# Exact Poisson probability mass function
P_P = np.zeros_like(x, dtype=float)
mu = 900/1000
for i in range(len(x)):
    P_P[i] = mu**x[i] * np.exp(-mu) / math.factorial(x[i])
print(P_P)
exit()
# Simulation

# Each row is an hour and each column a day
cnts = np.random.binomial(n=1, p=p, size=(24, 1000))

# Count the number of events per day
cnts_sum = np.sum(cnts, axis=0) # List of counts on each of 1000 days
unique_vals, counts = np.unique(cnts_sum, return_counts=True)
P_S = counts / len(cnts_sum)

plt.plot(unique_vals, P_S, 'o', label='Simulation')
plt.plot(x, P_B, 's', label='Binomial')
plt.plot(x, P_P, '^', label='Poisson')
plt.xlabel('Number of events per day')
plt.ylabel('Probability')
plt.legend()
plt.show()