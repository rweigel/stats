import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.default'] = 'regular'

from lib.savefig import savefig
from lib.pdf import pdf

np.random.seed(1)

n = 10    # Number of samples per experiment
ne = 100  # Number of experiments

# Create 100 x 10000 matrix of numbers drawn from N(0, 1) distribution
X = np.random.randn(n, ne)
S2b = np.var(X, axis=0, ddof=0) # Compute sample variance of each column

dx = 0.1
e_pdf, bin_centers, bin_edges = pdf(S2b, dx=dx, a=dx/2)
plt.bar(bin_centers, e_pdf, width=dx*0.93, align='center', color='black')
plt.xlim([0.0, 3])
plt.title(f'$n$ = {n:d}, $\\sigma^2=1$, mean($S^2_b$) = {np.mean(S2b):.3f}')
plt.axvline(np.mean(S2b), color='red', linestyle='dashed', linewidth=1)
plt.xlabel('$S^2_b$')
plt.ylabel('Probability Density')
plt.gca().set_axisbelow(True) # Put grid lines in back.
plt.grid()
savefig("HW3_3_2")
