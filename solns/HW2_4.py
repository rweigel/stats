import math
import numpy as np

slow = True

p  = 0.4
ne = 10000  # Number of experiments
nt = 100    # Number of trials per experiment

def p_exact(x, nt, p):
  # Could also use
  # import scipy.stats
  # scipy.stats.binom.pmf(x, nt, p)
  nCk = math.factorial(nt)/(math.factorial(nt-x)*math.factorial(x))
  return nCk*(1-p)**(nt-x)*p**x


def p_gauss(x, nt, p):
  return (1/np.sqrt(2*np.pi*nt*p*(1-p)))*np.exp(-(x-nt*p)**2/(2*nt*p*(1-p)))


def p_expmt(x, nt, p, ne):
  nx = 0
  for i in range(ne):
    # Count the number of successes in this experiment
    n_success = np.sum(np.random.rand(nt) < p)
    if n_success == x:
      nx += 1

  return nx/ne


def plot(P_expmt, P_exact, P_gauss):

  from matplotlib import pyplot as plt

  plt.rcParams["font.family"] = "Times New Roman"
  plt.rcParams['savefig.dpi'] = 300

  styles = {
    'P_expmt': {
      'marker': 'o',
      'linestyle': 'none',
      'fillstyle': 'none',
      'markeredgecolor': 'green',
      'markersize': 3,
      'label': 'Experimental'
    },
    'P_exact': {
      'width': 0.5,
      'label': '$\\binom{n}{x}(1-p)^{n-x}p^x$'
      },
    'P_gauss': {
      'color': 'r',
      'marker': 'o',
      'linestyle': 'none',
      'markersize': 3,
      'label': '$e^{-(x-np)^2/2npq}/\\sqrt{2\\pi npq}$'
    }
  }

  plt.plot(np.arange(len(P_expmt)), P_expmt,**styles['P_expmt'])
  plt.bar(np.arange(len(P_exact)), P_exact, **styles['P_exact'])
  plt.plot(np.arange(len(P_gauss)), P_gauss, **styles['P_gauss'])

  plt.grid(axis='y', color=3*[0.5], ls=':')
  plt.grid(axis='x')
  plt.xlabel('$x$  (num. of $1$s in experiment)')
  plt.ylabel('$P(x)$')
  plt.title(f'num. trials per experiment = {nt}; num. experiments = {ne}')
  plt.xlim([10, 70])
  plt.ylim([0, 0.09])
  plt.legend(fontsize=10)

  plt.savefig('HW2_4.png')
  plt.savefig('HW2_4.svg', transparent=True)


if slow:
  P_exact = np.empty(nt)
  P_gauss = np.empty(nt)
  P_expmt = np.empty(nt)
  for x in range(nt):
    P_exact[x] = p_exact(x, nt, p)
    P_gauss[x] = p_gauss(x, nt, p)
    P_expmt[x] = p_expmt(x, nt, p, ne)
else:

  x = np.arange(nt) # Array of possible number of successes (0 to nt-1)

  import scipy.stats
  # SciPy has a function for this PMF.
  P_exact = scipy.stats.binom.pmf(x, nt, p)

  P_gauss = (1/np.sqrt(2*np.pi*nt*p*(1-p)))*np.exp(-(x-nt*p)**2/(2*nt*p*(1-p)))

  # np.random.binomial(nt, p) returns the number of successes an experiment
  # of size nt. If we set size=ne, we get an array of length ne
  # containing the number of successes in each of the ne experiments.
  counts = np.random.binomial(n=nt, p=p, size=ne)
  # Count the number of occurrences of counts = x for x = 0, 1, ..., nt-1
  # and divide by the number of experiments to get the experimental probability.
  P_expmt = np.bincount(counts, minlength=nt)/ne

plot(P_expmt, P_exact, P_gauss)
