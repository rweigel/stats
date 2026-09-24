import numpy as np
np.random.seed(0)
n = 10
μ = 0
σ = 2
x = np.random.normal(loc=μ, scale=σ, size=n)

print(x)
# [ 3.52810469  0.80031442  1.95747597  4.4817864   3.73511598 
#  -1.95455576  1.90017684 -0.30271442 -0.2064377   0.821197  ]

print(np.mean(x))
# 1.4760463414576694

Z = (np.mean(x)-μ)/(σ/np.sqrt(n))
print(Z)
# 2.3338341854824276

# Hard way
z = np.linspace(-3, 3, 1000)
f = (1/(np.sqrt(2*np.pi)))*np.exp(-z**2/2)
dz = z[1] - z[0]
print(np.sum(f)*dz)
import matplotlib.pyplot as plt
plt.plot(z, f, label='Gaussian PDF')
plt.xlabel('z')
plt.legend()
plt.grid(True)
plt.show()

import scipy.stats
# Use the percent point function (inverse of the CDF) to find critical z-values
print(scipy.stats.norm.ppf(.025))
# -1.9599639845400545
print(scipy.stats.norm.ppf(.975))
# 1.959963984540054

scipy.stats.t.ppf(.025, df=n-1)
# -2.2621571627409915
scipy.stats.t.ppf(.975, df=n-1)
# 2.2621571627409915