import math
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['savefig.dpi'] = 300

use_latex = True
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

set_latex(use_latex)

debug = False # True prints output

p  = 0.4
ne = 10000  # Number of experiments
nt = 100    # Number of trials per experiment

def p_exact(x, nt, p):
  nCk = math.factorial(nt)/(math.factorial(nt-x)*math.factorial(x))
  return nCk*(1-p)**(nt-x)*p**x

def p_gauss(x, nt, p):
  return (1/np.sqrt(2*np.pi*nt*p*(1-p)))*np.exp(-(x-nt*p)**2/(2*nt*p*(1-p)))

def p_expmt(x, nt, p, ne):
  # Could do this using np.histogram()
  nx = 0
  for i in range(ne):
    # Count the number of successes in this experiment
    n_success = np.sum(np.random.rand(nt) < p)
    if n_success == x:
      nx += 1

  return nx/ne
import numpy as np

xbars = []
nbig = 0
for i in range(0, 1000):
  sample = np.random.normal(0, 1, 10)
  xbar = np.mean(sample)
  xbars.append(xbar)
  if xbar > 0.1:
    nbig = nbig + 1
print(nbig)

P_exact = np.empty(nt)
P_gauss = np.empty(nt)
P_expmt = np.empty(nt)
for x in range(nt):
  P_exact[x] = p_exact(x, nt, p)
  P_gauss[x] = p_gauss(x, nt, p)
  P_expmt[x] = p_expmt(x, nt, p, ne)


plt.plot(np.arange(len(P_expmt)), P_expmt, marker='o', linestyle='none', fillstyle='none', markeredgecolor='green', markersize=3, label='Experimental')
plt.bar(np.arange(len(P_exact)), P_exact, width=0.5, label='$\\binom{n}{x}(1-p)^{n-x}p^x$')
plt.plot(np.arange(len(P_gauss)), P_gauss, 'r', marker='o', linestyle='None', markersize=3, label='$e^{-(x-np)^2/2npq}/\\sqrt{2\\pi npq}$')


plt.grid(axis='y', color=3*[0.5], ls=':')
plt.grid(axis='x')
plt.xlabel('$x$  (num. of $1$s in experiment)')
plt.ylabel('$P(x)$')
plt.title(f'num. trials per experiment = {nt}; num. experiments = {ne}')
plt.xlim([10, 70])
plt.ylim([0, 0.09])
plt.legend(fontsize=11)

plt.savefig('HW2_4.png')
plt.savefig('HW2_4.svg', transparent=True)
