import numpy as np
from matplotlib import pyplot as plt

np.random.seed(1)

n = 100    # Number of samples per experiment
Ne = 100000  # Number of expriments

# 1
X = np.random.randn(n)

#2

print('Xbar = %.2f' % np.mean(X))

# 3

# Create 100 x 10000 matrix of numbers drawn from N(0, 1) distribution

X = np.random.randn(n, Ne) 
#X = np.random.uniform(-1.0, 1.0, size=(n,Ne))

print("X.shape = (%d,%d)" % X.shape) # (100, 10000)

Xbar = np.mean(X, axis=0) # Compute average of each column

print("Xbar.shape = (%d,)" % Xbar.shape) # (10000,) 

plt.figure()

# Choose bins so symmetric about 0
# Could also use bins = 'sturges', 'fd', etc. The number of bins
# to use is actually a problem considered in the literature. See
# https://arxiv.org/pdf/physics/0605197.pdf and references therein.
bw = 0.05 # bin width
bins = bw/2. + np.arange(-0.4,0.4,0.05)

# Show horizontal gridlines to make reading y-values easier.
plt.grid(axis='y', color=[0.2,0.2,0.2], linewidth=0.2)

if True:
    # To plot histogram
    cnts = plt.hist(Xbar,bins=bins)
    plt.ylabel('# in bin')

if False:
    # To plot probability _density_ function
    plt.hist(Xbar,bins=bins, density=True)
    plt.ylabel('Probability Density')

if False:
    # To plot probability _distribution_ function)
    # (0.99 so that small gap between bars shows)
    plt.bar(bw/2. + bins[0:-1], cnts[0]/np.sum(cnts[0]), width=bw*(0.99))
    plt.ylabel('Probability Distribution')

plt.title('$n=%d$, $mean(\\bar{X}) = $ %.2g' % (n, np.mean(Xbar)))
plt.xlabel('$\\bar{X}$')

plt.savefig("HW2_3a.png", format="png", transparent=True)
plt.savefig("HW2_3a.svg", format="svg", transparent=True)