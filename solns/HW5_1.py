import numpy as np
from scipy.stats import chi2, norm
from matplotlib import pyplot as plt

def _ci_bootstrap(xstar, s):
  # Compute bootstrap S^2 values
  xstar_s2 = np.var(xstar, axis=0, ddof=1)

  # Sort values for percentile calculation
  xstar_s2.sort()
  ci_bootstrap = [np.percentile(xstar_s2, 2.5), np.percentile(xstar_s2, 97.5)]

  # Alternative method to compute CI using bootstrap SE
  # https://bookdown.org/compfinezbook/introcompfinr/The-Nonparametric-Bootstrap.html
  # This is a form of what
  # https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#Methods_for_bootstrap_confidence_intervals
  # calls the studentized bootstrap execept large n is assumed.
  # See Devore p 252 for definition of se_boot
  #se_boot = np.std(xstar_s2, ddof=1)
  #ci_bootstrap = [s^2 - 2*se_boot, s^2 + 2*se_boot]

  return ci_bootstrap, xstar_s2

def _ci_devore(s, n):
  return [(n-1)*s**2/chi2.ppf(0.975, n-1), (n-1)*s**2/chi2.ppf(0.025, n-1)]

def plot(xstar, bins, xlim, ylim, title):

  n = xstar.shape[0]
  x_std = np.std(xstar, ddof=1)

  ci_bootstrap, xstar_s2 = _ci_bootstrap(xstar, x_std)
  ci_devore = _ci_devore(x_std, n)
  counts, bins = np.histogram(xstar_s2, bins=bins)
  xstar_mean = np.mean(xstar, axis=0)

  print(f"  Sample <X>       {x_bar:.0f} [V]")
  print(f"  Bootstrap <X>    {np.mean(xstar_mean):.0f} [V]")
  print(f"  Sample S^2       {x_std**2:.0f} [V^2]")
  print(f"  Bootstrap <S^2>  {np.mean(xstar_s2):.0f} [V^2]")
  print(f"  Exact CI:        [{ci_devore[0]:.0f}, {ci_devore[1]:.0f}] [V^2]")
  print(f"  Bootstrap CI:    [{ci_bootstrap[0]:.0f}, {ci_bootstrap[1]:.0f}] [V^2]")

  units = '$[\\mathtt{V}^2]$'
  counts, bins = np.histogram(xstar_s2, bins=bins)
  plt.hist(bins[:-1], bins, weights=counts/sum(counts), color='black')
  plt.axvline(x_std**2, color='green', linestyle='-', label=f'Sample $S^2$ = {x_std**2:.0f} {units}')
  plt.axvline(np.mean(xstar_s2), color='green', linestyle='-.', label=f'Bootstrap $<S^2>$ = {np.mean(xstar_s2):.0f} {units}')
  plt.axvline(ci_devore[0], color='red', label=f'Devore 95% CI = [{ci_devore[0]:.0f}, {ci_devore[1]:.0f}] {units}')
  plt.axvline(ci_devore[1], color='red')
  plt.axvline(ci_bootstrap[0], color='blue', label=f'Bootstrap 95% CI = [{ci_bootstrap[0]:.0f}, {ci_bootstrap[1]:.0f}] {units}')
  plt.axvline(ci_bootstrap[1], color='blue')
  plt.grid(axis='y')
  plt.legend()
  plt.xlim(*xlim)
  plt.ylim(*ylim)
  plt.xlabel(f'$S^2$ {units}')
  plt.ylabel('Probability')
  plt.title(title, fontsize=11)

n_b = 1000
xlim = [3000, 350000]
ylim = [0, 0.25]

# Devore pg 295 data
x = [1470, 1510, 1690, 1740, 1900, 2000, 2030, 2100, 2190, 2200, 2290, 2380, 2390, 2480, 2500, 2580, 2700]
x = np.array(x)

# Devore's CI. Note that I calculate it using the chi2.ppf function. Results
# are similar, but not same, because Devore uses table values with 3 decimals.
ci_devore = np.array([76172.3, 318064.4])
bins = np.arange(40000, 250000, 10000)

x_std = np.std(x, ddof=1)
x_bar = np.mean(x)

# Part 1.
n = len(x)
title = 'Parametric Bootstrap 95% CI for $S^2$\nSample mean and variance used to generate bootstrap samples'
xstar = np.random.choice(x, size=(n, n_b), replace=True)
print(f"Part 1. Nonparametric Bootstrap; n_b = {n_b}")
plot(xstar, bins, xlim, ylim, title)
plt.savefig('HW5_1a.png', dpi=300)
plt.savefig('HW5_1a.svg', transparent=True)
plt.close()

# Part 2.
n = 100
x = np.random.normal(loc=x_bar, scale=x_std, size=n)
xstar = np.random.choice(x, size=(n, n_b), replace=True)

print("\nPart 2")
ci_bootstrap, _ = _ci_bootstrap(xstar, x_std)
ci_devore = _ci_devore(x_std, n)

plot(xstar, bins, xlim, ylim, title)
plt.savefig('HW5_1b.png', dpi=300)
plt.savefig('HW5_1b.svg', transparent=True)
plt.close()

# Part 3.
nr = 100
print(f"\nPart 3. Repeat part 2 {nr} times and report mean bootstrap CI width")
ci_bootstrap_widths = []
for i in range(0, 100):
  x = np.random.normal(loc=x_bar, scale=x_std, size=n)
  xstar = np.random.choice(x, size=(n, n_b), replace=True)
  ci_bootstrap, xstar_s2 = _ci_bootstrap(xstar, x_std)
  ci_bootstrap_width = ci_bootstrap[1] - ci_bootstrap[0]
  ci_bootstrap_widths.append(ci_bootstrap_width)
  #print(f"CI width: {ci_bootstrap_width:.0f}")

ci_devore = _ci_devore(x_std, n)
ci_devore_width = ci_devore[1] - ci_devore[0]
print(f"  Mean bootstrap CI width: {np.mean(ci_bootstrap_widths):.0f} [V^2]")
print(f"  Devore CI width:         {np.mean(ci_devore_width):.0f} [V^2]")
