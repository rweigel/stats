import numpy as np
from scipy.stats import chi2
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['mathtext.default'] = 'regular'

use_latex = True  # Set to False if you don't want to use LaTeX
n  = 100    # Number of samples per experiment
nb = 10000 # Number of bootstrap resamples
sigma = 1
max_x = 2.5

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
X = np.random.normal(loc=0.0, scale=sigma, size=(n, ))
S2o = np.var(X, ddof=1)
for i in range(nb):
  Xb = np.random.choice(X, size=(n, ), replace=True)
  S2[i] = np.var(Xb, ddof=1)

db = 0.05
bin_edges = np.arange(0, max_x, db)

use_latex = set_latex(use_latex)

plt.hist(S2, bins=bin_edges, color='black', edgecolor='w', linewidth=0.5, density=True)
#pmf(bin_edges, S2)
if True:
  x = np.arange(0, 3.0, db/10)
  #https://online.stat.psu.edu/stat414/lesson/26/26.3
  # (n-1)/sigma^2 S^2 ~ chi^2_{n-1}
  bin_centers = bin_edges[0:-1] + db/2
  chi2 = chi2.pdf(bin_centers*(n-1)/sigma**2, df=n-1)
  plt.stairs(chi2/(db*sum(chi2)), bin_edges, color=3*[0.5], label=f'Exact sampling dist: $\\chi^2_{{{n-1}}}$')

eqn = '\n\n$\\displaystyle S^2 = \\frac{1}{n-1}\\sum_{i=1}^{n} (x_i - \\overline{x})^2$'
if not use_latex:
  eqn = eqn.replace('\\displaystyle ', '')
plt.text(max_x, 1.2, eqn, fontsize=14, ha='right')

plt.axvline(x=1, color=3*[0.5], ls=':', label='$\\sigma^2 = 1$')
plt.axvline(x=S2o, color=[1,0,0], ls='-', lw=3, label=f'$S^2$ = {S2o:.3f}')
plt.axvline(x=np.mean(S2), color=[0,1,0], ls='--', label=fr'$\langle S^{{*2}}\rangle$ = {np.mean(S2):.3f}')

title = f'Bootstrap sampling distribution of $S^2$; $n_b = {nb}$'
title += f'\n$n={n}$ values of $x$ drawn from Gaussian with $\\mu = 0$ and $\\sigma^2 = 1$'
plt.title(title)
plt.grid(ls=':')
plt.legend()
plt.ylabel('Probability Density')
plt.xlabel('$S^2$')
plt.savefig("HW4_2.svg", transparent=True)
plt.savefig("HW4_2.png")
