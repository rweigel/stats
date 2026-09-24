import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.default'] = 'regular'

from lib.savefig import savefig
from lib.pdf import pdf

np.random.seed(1)

n = 100      # Number of samples per experiment
Ne = 100000  # Number of experiments

# 1
X = np.random.randn(n)
#X = np.random.uniform(-1.0, 1.0, size=(n,))

#2

print('Xbar = %.2f' % np.mean(X))

# 3

# Create 100 x 10000 matrix of numbers drawn from N(0, 1) distribution

X = np.random.randn(n, Ne) 
#X = np.random.uniform(-1.0, 1.0, size=(n,Ne))

print(f"X.shape = ({X.shape[0]},{X.shape[1]})") # (100, 10000)

Xbar = np.mean(X, axis=0) # Compute average of each column

print(f"Xbar.shape = ({Xbar.shape[0]},)") # (10000,) 

dx = 0.1
e_pdf, bin_centers, bin_edges = pdf(Xbar, dx=dx, a=-0.4)
plt.bar(bin_centers, e_pdf, width=dx*0.97, align='center', color='black')
plt.xlim([-0.4, 0.4])
plt.title(f'$n$ = {n:d}, mean($\\bar{{X}}$) = {np.mean(Xbar):.2g}')
plt.xlabel('$\\bar{X}$')
plt.ylabel('Probability Density')
plt.gca().set_axisbelow(True) # Put grid lines in back.
plt.grid()
savefig("HW3_2_1")
