import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['savefig.dpi'] = 300

use_latex = True  # Set to False if you don't want to use LaTeX
n  = 10    # Number of samples per experiment
nb = 10000 # Number of bootstrap resamples

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

use_latex = set_latex(use_latex)

Sb2 = np.full(nb, np.nan)
for i in range(nb):
  X = np.random.normal(loc=0.0, scale=1.0, size=(n, ))
  Sb2[i] = (1/n)*np.sum( np.power(X - np.mean(X), 2))
  #Sb2[i] = np.var(X, ddof=0) # Alternative way to compute Sb2

bin_edges = np.arange(0, 4.0, 0.1)
pmf(bin_edges, Sb2)
title = f'Draw $n$ = {n} samples from Gaussian with $\\mu = 0$ and $\\sigma^2 = 1$'
title += f' $N_e$ = {nb} times'
plt.title(title, fontsize=11)

if use_latex:
  eqn = '\n\n$\\displaystyle S_b^2 = (1/n)\\sum_{i=1}^n (x_i - \\bar{x})^2$'
else:
  eqn = '\n\n$S_b^2 = (1/n)\\sum_{i=1}^n (x_i - \\bar{x})^2$'

plt.text(2.0, 0.06, eqn, fontsize=16)
plt.axvline(x=1, color=3*[0.5], ls='--', label='$\\sigma^2 = 1$')
plt.axvline(x=np.mean(Sb2), color=3*[0.5], ls='-', label=f'mean($S_b^2$) = {np.mean(Sb2):.3f}')
plt.legend()
plt.xlabel('$S_b^2$')
plt.ylabel('Probability')
plt.savefig('HW3_3.png', transparent=True)
plt.savefig('HW3_3.svg', transparent=True)
