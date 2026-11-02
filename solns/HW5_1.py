import numpy as np
from lib.savefig import savefig

def ols(x, y, method='manual'):
  if method == 'scipy':
    from scipy import stats
    slope, intercept, r_value, p_value, slope_std_err = stats.linregress(x, y)
    return intercept, slope, slope_std_err

  if method == 'manual':
    b1 = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x))**2)
    b0 = np.mean(y) - np.mean(x) * b1

    # Compute standard error of the slope
    # Page 494
    s = np.std(y - (b0 + b1 * x), ddof=2) # Page 491
    Sxx = np.sum((x - np.mean(x))**2)     # Page 493
    s_beta_1 = s / np.sqrt(Sxx)  # Page 493
    # t_{alpha/2, n-2}, 100(1-alpha) = X% confidence interval => alpha = 0.05
    return b0, b1, s_beta_1


def scatter(x, y, b0, b1, ci_delta=None):
  import matplotlib.pyplot as plt
  plt.scatter(x, y, color='k')
  plt.xlabel('x')
  plt.ylabel('y')
  label = f'y = {b0:.2f} + {b1:.2f}x'
  plt.plot(x, b0 + b1 * x, color='black', label=label)
  plt.title(f'b1 = {b1:.2f}; 95% CI: [{b1-ci_delta:.2f}, {b1+ci_delta:.2f}]')
  plt.legend()
  plt.grid(True)
  savefig('HW5_1')

n = 20
x = np.arange(n)/n
beta_0 = 1.0
beta_1 = 1.0
sigma = 0.2

np.random.seed(0)
y = beta_0 + beta_1 * x + np.random.normal(size=n, loc=0.0, scale=sigma)

b0, b1, b1_stderr = ols(x, y, method='manual')
print(f"True coefficients:               b0 = {beta_0:10.2f}  b1 = {beta_1:10.2f}")
print(f"Estimated coefficients (manual): b0 = {b0:10.2f}  b1 = {b1:10.2f}")

b0_scipy, b1_scipy, b1_scipy_stderr = ols(x, y, method='scipy')
print(f"Estimated coefficients (scipy):  b0 = {b0_scipy:10.2f}  b1 = {b1_scipy:10.2f}")
print(f"Difference (scipy - manual):     b0 = {b0_scipy - b0:10.2e}  b1 = {b1_scipy - b1:10.2e}")

import scipy.stats
t = scipy.stats.t.ppf(0.975, df=len(x)-2)
ci_manual = f"[{b1 - b1_stderr*t:5.2f}, {b1 + b1_stderr*t:5.2f}]"
print(f"95% confidence interval for b1 (manual):  {ci_manual}")
ci_scipy = f"[{b1_scipy - b1_scipy_stderr*t:5.2f}, {b1_scipy + b1_scipy_stderr*t:5.2f}]"
print(f"95% confidence interval for b1 (scipy):   {ci_scipy}")

ci_delta = t * b1_stderr


scatter(x, y, b0, b1, ci_delta)

# Part 5
nt = 0
ne = 1000
for exp in range(ne):
  y = beta_0 + beta_1 * x + np.random.normal(size=n, loc=0.0, scale=sigma)
  b0, b1, b1_stderr = ols(x, y, method='manual')
  ci_delta = t * b1_stderr
  if b1 - ci_delta <= beta_1 <= b1 + ci_delta:
    nt += 1
print(f"Fraction of CIs that trap beta_1: {nt/ne:.4f}")

"""
True coefficients:               b0 =       1.00  b1 =       1.00
Estimated coefficients (manual): b0 =       1.23  b1 =       0.76
Estimated coefficients (scipy):  b0 =       1.23  b1 =       0.76
Difference (scipy - manual):     b0 =  -2.22e-16  b1 =   3.33e-16
95% confidence interval for b1 (manual):  [ 0.49,  1.03]
95% confidence interval for b1 (scipy):   [ 0.49,  1.03]
Fraction of CIs that trap beta_1: 0.9500
"""