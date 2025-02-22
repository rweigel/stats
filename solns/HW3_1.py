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

Ne = 10000  # Number of experiments
Nt = 100    # Number of trials per experiment
po = 0.4
px = 0.44

def nCk(n,k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

# Exact solution
P = np.empty(Nt)
for k in range(Nt):
    P[k] = nCk(Nt, k)*(1-po)**(Nt-k)*po**k

##############################################################################
# Solution without using np.random.binomial()
##############################################################################

n1 = np.empty(Ne)
n2 = np.empty(Ne)
for j in range(n1.size):   # Loop over experiments
    k1 = 0                 # Number of heads in p = 0.4 experiment
    k2 = 0                 # Number of heads in variable p experiment
    p1 = np.empty(Nt)
    p2 = np.empty(Nt)
    x = np.empty(Nt)
    for i in range(Nt):    # Loop over trials
        p1[i] = po
        p2[i] = po
        if i > 1 and x[i-1] <= po and x[i-2] <= po:
            p2[i] = px
        x[i] = np.random.uniform()
        if x[i] <= p1[i]:
            k1 = k1 + 1
        if x[i] <= p2[i]:
            k2 = k2 + 1
            if debug:
                print('j = {0:03d}  p = {1:.2f} H'.format(i, p2[i]))
        else:
            if debug:
                print('j = {0:03d}  p = {1:.2f} T'.format(i, p2[i]))

    n1[j] = k1
    n2[j] = k2

bin_centers = np.arange(102)    # 0, ..., 101
bin_edges   = bin_centers - 0.5 # -0.5, 0.5, ..., 100.5
bin_centers = bin_centers[0:-1] # remove last element

x_lim = [np.min([np.min(n1), np.min(n2)]) - 0.5,
         np.max([np.min(n1), np.max(n2)]) + 0.5]

plt.figure()
plt.grid(axis='y', color='k')

plt.hist(n1, bins=bin_edges, density=True)
hist1 = np.histogram(n1, bins=bin_edges)
plt.step(bin_centers, hist1[0]/np.sum(hist1[0]), where='mid', color='k')

hist2 = np.histogram(n2, bins=bin_edges)
plt.step(bin_centers, hist2[0]/np.sum(hist2[0]), where='mid', color='r')

plt.bar(np.arange(len(P)), P, width=0.96)

plt.xlabel('num. heads in experiment')
plt.ylabel('P of num. heads in experiment')
plt.title('num. trials/experiment = {0:d}; num. experiments = {1:d}'.format(Nt, Ne))
plt.xlim(x_lim)
plt.legend(['Experiment 1. p=0.4','Experiment 2. p varies','Binomial Formula'])

plt.savefig("HW3_1.png")
plt.savefig("HW3_1.svg", transparent=True)

##############################################################################
# Solution using np.random.binomial()
##############################################################################

n1 = np.empty(Ne) # Number of success trials for p = 0.4
n2 = np.empty(Ne) # Number of success trials for variable p
r1 = np.empty(Nt) # Trial results for p = 0.40
r2 = np.empty(Nt) # Trial results for variable p

for j in range(n1.size):  # Loop over experiments
    r1 = np.random.binomial(n=1, p=0.4, size=Nt)
    n1[j] = np.sum(r1)
    for i in range(Nt):  # Loop over trials
        if i > 1 and r2[i-1] == 1 and r2[i-2] == 1:
            r2[i] = np.random.binomial(n=1, p=px)
        else:
            r2[i] = np.random.binomial(n=1, p=po)
    n2[j] = np.sum(r2)

plt.close()
plt.figure()

hist1 = np.histogram(n1, bins=bin_edges)
plt.step(bin_centers, hist1[0]/np.sum(hist1[0]),
         where='mid', color='k', label='Experiment 1. $p = 0.4$')

hist2 = np.histogram(n2, bins=bin_edges)
plt.step(bin_centers, hist2[0]/np.sum(hist2[0]),
         where='mid', color='r', label='Experiment 2. $p$ varies')

xg = np.arange(x_lim[0], x_lim[1]+1)
Pg = (1/np.sqrt(2*np.pi*Nt*po*(1-po)))*np.exp(-(xg-Nt*po)**2/(2*Nt*po*(1-po)))
plt.plot(xg, Pg, 'k--', label='$e^{-(x-np)^2/2npq}/\\sqrt{2\\pi npq}$')

plt.bar(np.arange(len(P)), P, width=0.95, label='$\\binom{n}{k}(1-p)^{n-k}p^k$')

plt.grid(axis='y', color=3*[0.5], ls=':')
plt.xlabel('$k$')
plt.ylabel('P(k) (prob. of num. of $1$s in experiment)')
plt.title('num. trials/experiment = {0:d}; num. experiments = {1:d}'.format(Nt, Ne))
plt.xlim(x_lim)
plt.legend(fontsize=10)

plt.savefig('HW3_1.png')
plt.savefig('HW3_1.svg', transparent=True)
