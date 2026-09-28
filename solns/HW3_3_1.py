import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.default'] = 'regular'

from lib.savefig import savefig
from lib.pdf import pdf

np.random.seed(1)

n = 10      # Number of samples per experiment
Ne = 10000  # Number of experiments

dist = "normal"
std = 1.0

dist = "uniform"
uniform_a = 0.0 # Problem statement gave 0.0
uniform_a = -1.0 # Problem statement gave 0.0
uniform_b = 1.0
# Standard deviation of the uniform distribution
std = (uniform_b - uniform_a)/np.sqrt(12)

# 1
if dist == "normal":
  X = std * np.random.randn(n)
elif dist == "uniform":
  X = np.random.uniform(uniform_a, uniform_b, size=(n,))

print(f'Xbar = {np.mean(X):.2f}')

# 2

# Create 100 x 10000 matrix of numbers drawn from N(0, 1) distribution

if dist == "normal":
  X = std * np.random.randn(n, Ne)
elif dist == "uniform":
  X = np.random.uniform(uniform_a, uniform_b, size=(n, Ne))

Xbar = np.mean(X, axis=0) # Compute average of each column

f = np.sum(Xbar > std/np.sqrt(n))/Ne
print(f'Fraction of Xbar values greater than sigma/sqrt({n})$: {f}')

a = -1.5
dx = 0.1
e_pdf, bin_centers, bin_edges = pdf(Xbar, dx=dx, a=a)
print(bin_centers)
plt.bar(bin_centers, e_pdf, width=dx*0.97, align='center', color='black')
plt.xlim([a, -a])
plt.title(f'$n$ = {n:d} | mean($\\bar{{X}}$) = {np.mean(Xbar):.2g} | fraction > 1/sqrt(n) = {f:.2g}')
plt.xlabel('$\\bar{X}$')
plt.ylabel('Probability Density')
plt.gca().set_axisbelow(True) # Put grid lines in back.
plt.grid()
savefig(f"HW3_3_1_{dist}")

if dist == "normal":
  ns = [10, 100, 1000, 10000]
  f = np.zeros(len(ns))
  for i, n in enumerate(ns):
    X = std * np.random.randn(n, Ne)
    Xbar = np.mean(X, axis=0) # Compute average of each column
    f[i] = np.sum(Xbar > std/np.sqrt(n))/Ne

  plt.close()
  plt.plot(ns, f, '.')
  plt.xscale('log')
  plt.xlabel('n')
  plt.grid(True)
  plt.title(f'Fraction of Xbar > {std}/sqrt(n)')
  savefig("HW3_3_1_fraction")
