import math
import numpy as np
from lib.savefig import savefig
from lib.pmf import pmf

# Given parameters
t = 24
p = 900/(1000*24)

# Exact solution
def exact_prob(x, n, p):
  def nCk(n,k):
      return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

  P_B = np.empty(len(x))
  for k in range(len(x)):
    P_B[k] = nCk(n, x[k])*(1-p)**(n-x[k])*p**x[k]

  if False:
    # Faster and shorter alternative using scipy binomial pmf
    from scipy.stats import binom
    P_B = binom.pmf(x, n, p)

  return P_B

def poisson_prob(x, t, p):

  # Poisson solution
  P_P = np.empty(len(x))
  for k in range(len(x)):
      P_P[k] = ((p*t)**x[k])*np.exp(-p*t)/math.factorial(x[k])

  # Faster and shorter alternative using scipy poisson pmf could be used
  # here instead of the loop.
  if False:
    from scipy.stats import poisson
    P_P = poisson.pmf(x, p*t)

  return P_P

def simulated_poisson(x, t, p, ne=1000):
  # Simulated solution

  # Create an 1-D array of ne*24 hours.
  e_S = np.random.binomial(n=1, p=p, size=ne*t)

  # Reshape a 24x1000 matrix, each column representing one day
  e_Sr = e_S.reshape((t, ne))

  # Count the number of events in each day by summing columns
  n_S = np.sum(e_Sr, axis=0)

  # Compute the histogram of the number of events per day.
  P_S, _ = np.histogram(n_S, bins=-0.5+np.arange(len(x)+1), density=True)

  if False:
    # Alternative approach using PMF code
    # Compute unique values, frequencies
    x_S, P_S_tmp = pmf(n_S)

    # We want output to be probabilities at each x, but x may not match x_S.
    # Create an array P_S of the same length as x, and fill in the probabilities
    # from P_S_tmp at the corresponding indices given by x_S. Any x values not present
    # in x_S will have a probability of 0.
    P_S = np.zeros(len(x))
    P_S[x_S] = P_S_tmp

  return P_S, e_S

def plot_probabilities(x, P_B, P_P, P_S, semilogy=True):
  from matplotlib import pyplot as plt
  plt.rcParams["font.family"] = "Times New Roman"
  plt.rcParams['savefig.dpi'] = 300

  # TODO: When no blue dot, P_S = 0. Add an annotation to make this more obvious.
  plt.figure()
  if not semilogy:
    plt.plot(x, P_B, 'ro', markersize=12, markerfacecolor='none')
    plt.plot(x, P_P, 'k.', markersize=12)
    plt.plot(x, P_S, 'm.', markersize=8)
  else:
    plt.semilogy(x, P_B, 'ro', markersize=12, markerfacecolor='none')
    plt.semilogy(x, P_P, 'k.', markersize=12)
    plt.semilogy(x, P_S, 'm.', markersize=8)

  plt.xticks(x)
  plt.xlabel('Events per day (x)')
  plt.ylabel('Probability')
  plt.grid()
  plt.legend(legend)
  plt.title(title)

def plot_dte(x, P_dte, semilogy=True):
  from matplotlib import pyplot as plt

  plt.figure()
  plt.plot(x, P_dte, 'k.')

  # We want to show ticks at 24 hour intervals
  xticks = plt.gca().get_xticks()
  xticks = np.arange(24, np.max(x)+1, 24)
  plt.gca().set_xticks([1, *xticks])
  plt.ylabel('Probability')
  plt.xlabel('hours between flares')

  plt.grid()
  if semilogy:
    plt.grid(which='minor', axis='y')
    plt.yscale('log')
    plt.ylim([1e-3, 1e-1])


# Part 1.
x = np.arange(6)
P_B = exact_prob(x, t, p)
P_P = poisson_prob(x, t, p)
P_S, e_S = simulated_poisson(x, t, p, ne=1000)

title = f'$t={t:d}$ hrs; $\\lambda$={p:.3f}/hr'
legend = [
  r'Binomial',
  r'Poisson: ($\lambda t)^xe^{\lambda t}/x!$',
  'Simulated (1000 days)'
]

plot_probabilities(x, P_B, P_P, P_S, semilogy=False)
savefig('HW3_2a')

plot_probabilities(x, P_B, P_P, P_S, semilogy=True)
savefig('HW3_2a_semilogy')

# Time indices when there was an event
# e_S is an array of 1000*24 days. Here we find the indices of the events.
# The indices correspond to hour number.
te = np.where(e_S == 1)[0]
# Compute the differences between consecutive event times (hours) to get
# the time between events.
dte = np.diff(te)
x, P_dte = pmf(dte)

plot_dte(x, P_dte, semilogy=False)
savefig('HW3_2b')

plot_dte(x, P_dte, semilogy=True)
savefig('HW3_2b_semilogy')
