import numpy as np
from matplotlib import pyplot as plt

from lib.savefig import savefig
from lib.conffig import conffig
from lib.pdf import pdf


np.random.seed(1)

n = 100     # Number of samples per experiment
Ne = 10000  # Number of experiments

X = np.random.normal(loc=0.0, scale=1.0, size=(n, Ne))

Xbar = np.mean(X, axis=0) # Compute average of each column

a = -0.5
dx = 0.1
e_pdf, bin_centers, bin_edges = pdf(Xbar, dx=dx, a=a)

conffig()
plt.bar(bin_centers, e_pdf, width=dx*0.97, align='center', color='black')
plt.xlim([a, -a])
plt.title(f'$n$ = {n:d} | Average of $\\bar{{X}}$ = {np.mean(Xbar):.2g}')
plt.xlabel('$\\bar{X}$')
plt.ylabel('Probability Density')
plt.gca().set_axisbelow(True) # Put grid lines in back.
plt.grid()
savefig("HW3_2_1")
