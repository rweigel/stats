import numpy as np
from scipy.stats import expon, chi2
from matplotlib import pyplot as plt

lambda_pop = 1
dx = 0.1
x = np.arange(0, 10+dx, dx)
# Exponential distribution PDF
pdf = expon.pdf(x, scale=lambda_pop)

n = 200
# Draw n samples from the exponential distribution
sample = expon.rvs(size=n, scale=1/lambda_pop)
lambda_sample = n/np.sum(sample)

if n < 11:
  print(f"Sample values: {sample}")
  print(f"Sample lambda: {lambda_sample}")

label = fr"$\lambda e^{{-\lambda x}}$; $\lambda = {lambda_pop}$"
plt.plot(x, pdf, 'k-', markersize=3, label=label)
plt.xlabel('$x$')
plt.ylabel('PDF')
plt.grid()

n_per_bin, bins, _ = plt.hist(sample, bins=x, density=True, label=f'Sample ($n={n}$)')
if n < 11:
  # Plot actual sample values on x-axis as a sanity check of histogram
  # Shift by 0.01 to avoid overlap with x-axis line.
  plt.plot(sample, 0*sample+0.01,'r.', markersize=2, label='Sample values')

# Recall that ~ means "distributed as"
plt.title(fr"$\lambda_s = n/(\sum_{{i=1}}^{{{n}}} x_i) = {lambda_sample:.2f}$;   $x_i \sim $ Exponential($\lambda$)")
plt.legend()
plt.savefig('HW5_1_1.png', dpi=300)
plt.close()


# Test claim of Devore Example 7.5 on page 274 that
# P(chi^2(dof=2*n, 0.025) < q < chi^2(dof=2*n, 0.975)) = 0.95
# where q = 2*lambda*sum(x_i) and x_i ~ Exponential(lambda)
# I have defined q for convenience as 2*lambda*sum(x_i)

# Test using three simulations methods:
# 1. Generate a sampling distribution via simulation. Assume lambda known.
#    based on above statement, we expect the equality to be satisfied
#    for 95% of simulated samples.
# 2. Bootstrap the sampling distribution. Assume the population
#    distribution is exponential with lambda the value from our sample.

q_lower = chi2.ppf(0.025, 2*n)
q_upper = chi2.ppf(0.975, 2*n)
n_in_1 = 0
n_in_2 = 0
n_in_3 = 0

n_s = 1000

# Array of simulated q values
q1 = np.zeros(n_s)
q2 = np.zeros(n_s)
q3 = np.zeros(n_s)

for i in range(n_s):

  # Simulate the sampling distribution of q
  # Draw n samples from the exponential distribution
  x1 = expon.rvs(size=n, scale=1/lambda_pop)
  q1[i] = 2*lambda_pop*np.sum(x1)

  if q_lower < q1[i] < q_upper:
    n_in_1 = n_in_1 + 1
  print(f"1. Is 2n = {2*n} in the 95% CI [{q_lower:.2f},{q_upper:.2f}]?", q_lower < q1[i] < q_upper)

  # Parametric bootstrap on q. Resample the original sample with replacement
  x2 = np.random.choice(sample, n, replace=True)
  q2[i] = 2*lambda_pop*np.sum(x2)
  if q_lower < q2[i] < q_upper:
    n_in_2 = n_in_2 + 1
  print(f"2. Is 2n = {2*n} in the 95% CI [{q_lower:.2f},{q_upper:.2f}]?", q_lower < q2[i] < q_upper)

  # Non--parametric bootstrap on q. Resample the original sample with replacement and
  # use the sample to estimate lambda
  x3 = np.random.choice(sample, n, replace=True)
  lambda_sample = n/np.sum(x3)
  q3[i] = 2*lambda_sample*np.sum(x3)
  if q_lower < q3[i] < q_upper:
    n_in_3 = n_in_3 + 1
  print(f"3. Is 2n = {2*n} in the 95% CI [{q_lower:.2f},{q_upper:.2f}]?", q_lower < q3[i] < q_upper)


print(f"n_in_1 = {n_in_1}")
print(f"n_in_2 = {n_in_2}")
print(f"n_in_3 = {n_in_3}")

#qb.sort()


if False:
  # Bootstrap confidence interval for q.
  q_sample = 2*lambda_pop*np.sum(sample)
  q_pop = 2*lambda_pop*n
  print(f"q = {q_sample:.2f} with parametric bootstrap derived 95% CI = [{qb[25]:.2f}, {qb[975]:.2f}]")
  if qb[25] < q_pop < qb[975]:
    n_in = n_in + 1
  print(f"Is q_pop = {q_pop} in the 95% CI?", qb[25] < q_pop < qb[975])


  #print(qb)
  dx = 100/n
  x = np.arange(0, 4*n+dx, dx)
  pdf = chi2.pdf(x, df=2*n)
  plt.plot(x, pdf, 'k.', markersize=3, label='Exact sampling dist of $q$')
  plt.hist(qb, bins=x, density=True, label='Bootstrap sampling dist of $q$')
  #plt.axvline(x=q_sample, color='r', linestyle='--', label='$q_s$ (sample $q$)')
  plt.axvline(x=2*n, color='k', linestyle='--', label='Population $q$')
  plt.title(f'$q_s=2\\lambda\\sum_{{i=1}}^{{{n}}} x_i$ with $\\lambda = {lambda_pop}$')
  plt.legend()
  plt.savefig('HW5_1_2.png', dpi=300)
  plt.close()
