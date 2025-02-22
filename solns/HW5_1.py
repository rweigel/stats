import numpy as np
from scipy.stats import expon, chi2
from matplotlib import pyplot as plt

lambda_pop = 1
dx = 0.1
x = np.arange(0, 10+dx, dx)
# Exponential distribution PDF
pdf = expon.pdf(x, scale=lambda_pop)

n = 100
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


# Part 1
# Test claim of Devore Example 7.5 on page 274 that
# P(chi^2(dof=2*n, 0.025) < q < chi^2(dof=2*n, 0.975)) = 0.95
# where q = 2*lambda*sum(x_i) and x_i ~ Exponential(lambda)
# I have defined q for convenience as 2*lambda*sum(x_i)

n_in = 0
for i in range(0, 500):
  n_b = 1000

  # Array of bootstrapped q values
  qb = np.zeros(n_b)

  for i in range(n_b):
    # Non--parametric bootstrap on q. Resample the original sample with replacement
    xb = np.random.choice(sample, n, replace=True)
    qb[i] = 2*lambda_pop*np.sum(xb)

    # Parametric bootstrap on q. Resample from the exponential distribution using
    # the sample lambda. (Note that in class, I was using lambda_pop instead of
    # lambda_sample, which does not make sense because presumably we don't know
    # lambda_pop.)
    #xb = expon.rvs(size=n, scale=1/lambda_sample)
    #qb[i] = 2*lambda_pop*np.sum(xb)

  qb.sort()

  # Bootstrap confidence interval for q.
  q_sample = 2*lambda_pop*np.sum(sample)
  q_pop = 2*lambda_pop*n
  print(f"q = {q_sample:.2f} with parametric bootstrap derived 95% CI = [{qb[25]:.2f}, {qb[975]:.2f}]")
  if qb[25] < q_pop < qb[975]:
    n_in = n_in + 1
  print(f"Is q_pop = {q_pop} in the 95% CI?", qb[25] < q_pop < qb[975])

print(f"n_in = {n_in}")

#print(qb)
dx = 100/n
x = np.arange(0, 4*n+dx, dx)
pdf = chi2.pdf(x, df=2*n)
plt.plot(x, pdf, 'k.', markersize=3, label='Exact sampling dist of $q$')
plt.hist(qb, bins=x, density=True, label='Bootstrap sampling dist of $q$')
plt.axvline(x=q_sample, color='r', linestyle='--', label='$q_s$ (sample $q$)')
plt.axvline(x=2*n, color='k', linestyle='--', label='Population $q$')
plt.title(f'$q_s=2\\lambda\\sum_{{i=1}}^{{{n}}} x_i$ with $\\lambda = {lambda_pop}$')
plt.legend()
plt.savefig('HW5_1_2.png', dpi=300)
plt.close()
