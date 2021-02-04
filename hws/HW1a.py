import numpy as np
from matplotlib import pyplot as plt

np.random.seed(1)

Ns = 100    # Number of samples per experiment
Ne = 10000  # Number of expriments

# 1
X = np.random.randn(Ns)

#2

print('Xbar = %.2f' % np.mean(X))

# 3

# Create 100 x 10000 matrix of numbers drawn from N(0, 1) distribution
#X = np.random.randn(Ns,Ne) 
X = np.random.uniform(-1.0, 1.0, size=(Ns,Ne))

print("X.shape = (%d,%d)" % X.shape) # (100, 1000)

Xbar = np.mean(X, axis=0) # Compute average of each column

print("Xbar.shape = (%d,)" % Xbar.shape) # (10000,) 

plt.figure()
# Choose bins so symmetric about 0
bins = np.arange(-0.425,0.425,0.05)
print(bins)
plt.grid(axis='y', color=[0.2,0.2,0.2], linewidth=0.2)
plt.hist(Xbar, bins=bins)
plt.title('$\mu= 0$, $n=%d$, $mean(\overline{X}) = $ %.2g' % (Ne, np.mean(Xbar)))
plt.xlabel('$\overline{X}$')
plt.ylabel('# in bin')

plt.savefig("figures/HW1a.svg", format="svg", transparent=True)