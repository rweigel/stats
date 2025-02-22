import numpy as np
from scipy.stats import chi2
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['mathtext.default'] = 'regular'

use_latex = True  # Set to False if you don't want to use LaTeX
n  = 10    # Number of samples per experiment
nb = 50000 # Number of bootstrap resamples

def pmf(bin_edges, data, color='k'):
  import warnings

  if np.min(data) < bin_edges[0]:
    warnings.warn(f'Minimum data value {np.min(data)} is less than minimum bin edge {bin_edges[0]}.', stacklevel=2)
  if np.max(data) > bin_edges[-1]:
    warnings.warn(f'Maximum data value {np.max(data)} is greater than maximum bin edge {bin_edges[-1]}.', stacklevel=2)

  db = bin_edges[1:] - bin_edges[0:-1]
  bin_centers = bin_edges[0:-1] + db/2

  n, _ = np.histogram(data, bins=bin_edges)
  pmf = n/len(data)
  plt.grid(axis='y', color=[0.5, 0.5, 0.5], ls=':')
  plt.bar(bin_centers, pmf, width=db, color=color, edgecolor='w', linewidth=0.5)

  return pmf, bin_centers

def set_latex(use_latex):

  import shutil
  import matplotlib

  if use_latex and shutil.which("latex"):
      print("LaTeX is installed")
      use_latex = True
      matplotlib.rcParams['text.usetex'] = True
      matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
  else:
      print("LaTeX is not installed")
      matplotlib.rcParams['text.usetex'] = False
      use_latex = False

  return use_latex

S2 = np.full(nb, np.nan)
for i in range(nb):
  X = np.random.normal(loc=0.0, scale=1.0, size=(n, ))
  S2[i] = (1/(n-1))*np.sum( np.power(X - np.mean(X), 2))
  #S2[i] = np.var(X, ddof=0)

db = 0.1
bin_edges = np.arange(0, 4.0, db)

pmf(bin_edges, S2)

if True:
  x = np.arange(0, 4.0, db/10)
  #https://online.stat.psu.edu/stat414/lesson/26/26.3
  # (n-1)/sigma^2 S^2 ~ chi^2(n-1)
  chi2 = chi2.pdf(x*(n-1), df=n-1)
  plt.plot(x, 10*chi2/sum(chi2), '.', ms=1, color=3*[0.5], label=f'$\\chi^2_{n-1}$')

eqn = '\n\n$\\displaystyle S^2 = (1/n)\\sum_{i=1}^{n} (x_i - \\overline{x})^2$'
if not set_latex(use_latex):
  eqn = eqn.replace('\\displaystyle ', '')
plt.text(2.0, 0.062, eqn, fontsize=16)

plt.axvline(x=1, color=[0,0,1], ls='-', label='$\\sigma^2 = 1$')
plt.axvline(x=np.mean(S2), color=[0,1,0], ls='--', label=f'mean($S^2$) = {np.mean(S2):.3f}')

title = f'Bootstrap sampling distribution of $S^2$; $N_b = {nb}$'
title += f'\n$n={n}$ values of $x$ drawn from Gaussian with $\\mu = 0$ and $\\sigma^2 = 1$'
plt.title(title)
plt.legend()
plt.ylabel('Probability')
plt.savefig("HW4_2.svg", transparent=True)
plt.savefig("HW4_2.png")
