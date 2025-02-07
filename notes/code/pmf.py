import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

# Set font to match that used in document.
rc('font', **{'family': 'serif', 'serif': ['Times'], 'size': 12})

# As a matter of style choice, I also set the bar color to black because no
# other colors are used.

'''
When plotting histograms, matplotlib's defaults are rarely appropriate.
In this example, we plot a discrete probability distribution function
(probability mass function, pmf) using NumPy and Matplotlib's pyplot.bar() and
using only Matplotlib's pyplot.hist().
'''

# Simulate experiment of tossing a fair coin 4x
# Repeat experiment N_E times
N_E = 100

np.random.seed(1)

# n_h = number of heads in each experiment.
n_h = np.random.binomial(4, 0.5, size=N_E)
print('Results from {0:d} experiments (number heads in 4 tosses):\n'.format(N_E))
print(n_h)

bin_c = np.arange(0, 6) # 0, 1, ..., 5
bin_e = bin_c - 0.5     # Bin edges = -0.5, 0.5, ..., 4.5
bin_c = bin_c[0:-1]     # Bin centers = 0, 1, ..., 4

methods = ['numpy_bar', 'matplotlib_alternative', 'matplotlib_default']

for method in methods:
  pmf = None

  if method == 'numpy_bar':
    # Use np.histogram to compute counts in bins
    n_e, _ = np.histogram(n_h, bins=bin_e)

    # Compute Probability Mass Function
    pmf = n_e/N_E

    plt.bar(bin_c, pmf, width=0.5, color='k')

  if method == 'matplotlib_alternative':
    # With density=True and bins with unit width, Matplotlib can be used to
    # plot and compute the pmf. Internally, plt.hist uses np.histogram.
    pmf, bins, patches = \
      plt.hist(n_h, bins=bin_e, align='mid', density=True, rwidth=0.5, color='k')

  if method == 'matplotlib_default':
    plt.hist(n_h)

  if pmf is not None:
    # Check that sum(pmf) ~= 1.
    print('sum(pmf) = {0:.16f}'.format(np.sum(pmf)))

  plt.xlabel('# of heads in experiment')
  plt.ylabel('P or pmf (= fraction of {0:d} experiments)'.format(N_E))
  plt.title('Example of a pmf (probability mass function)\nExperiment is tossing fair coin 4x')

  # Show grid only for y because a grid guide is not needed for x values in plot.
  plt.grid(axis='y', color=[0.5, 0.5, 0.5], ls=':')

  # Force ticks to match bin center values; fractional tick labels don't
  # make sense for plotted data.
  plt.xticks(bin_c)

  plt.savefig(f'pmf.{method}.svg', transparent=True)
  plt.savefig(f'pmf.{method}.png', dpi=300)
