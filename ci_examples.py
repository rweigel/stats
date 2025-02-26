import numpy as np
import scipy
from matplotlib import pyplot as plt

n = 10
# Sample from a normal distribution with mean 0 and standard deviation 1
μ = 0
σ = 1

def _annotate(title=''):
  plt.xlabel('$\\overline{x}$')
  plt.ylabel('Probability density')
  plt.title(title, fontsize=11)
  plt.axvline(x_bar, color='black', linestyle='--', linewidth=3, label='$\\overline{x}_{sample}$')
  plt.axvline(μ, color='magenta', linewidth=3, label='$\\mu$')
  plt.grid()
  plt.legend(loc='upper left')
  plt.ylim([0, 1.8])

# Part 1.
x = np.random.normal(loc=μ, scale=σ, size=n)

# Compute the sample mean and standard deviation
x_bar = np.mean(x)

# Sampling distribution of x_bar when x drawn from a normal distribution with
# mean μ and standard deviation σ is a normal distribution with mean μ and
# standard deviation σ/sqrt(n)
x_bars = np.linspace(-4*σ/np.sqrt(n), 4*σ/np.sqrt(n), 1000)
d = np.sqrt(2*np.pi)*(σ/np.sqrt(n))
x_bar_sampling_dist = (1/d)*np.exp(-(x_bars-μ)**2/(2*(σ/np.sqrt(n))**2))
# Or
#x_bar_sampling_dist = scipy.stats.norm(loc=μ, scale=σ/np.sqrt(n)).pdf(x_bar)

# If we re-run this code many times, green line will move around. Most often
# it will be near zero.
plt.plot(x_bars, x_bar_sampling_dist, color='black', label='Sampling distribution of $\\overline{x}$')
title = f'$\\overline{{x}}_{{sample}}$ is mean of n=${{{n}}}$ values drawn from N(μ, σ)'
_annotate(title=title)
plt.savefig('ci_examples_1.png', dpi=300)
plt.close()


# Part 2.

# A confidence interval is an interval around the point estimate x_bar.
# Clearly it should be related to the sampling distribution of x_bar.
# Plot sampling distribution with center at x_bar.
x_bar_sampling_dist_shifted = (1/d)*np.exp(-(x_bars-x_bar)**2/(2*(σ/np.sqrt(n))**2))
ci_limits = scipy.stats.norm.ppf([0.025, 0.975], loc=x_bar, scale=σ/np.sqrt(n))
print(ci_limits)
ci_limits = [x_bar-1.96*σ/np.sqrt(n), x_bar+1.96*σ/np.sqrt(n)]
print(ci_limits)

# Plot the confidence interval as a shaded region
plt.plot(x_bars, x_bar_sampling_dist_shifted, linestyle='--', color='black', label='Shifted sampling distribution of $\\overline{x}$')

title = 'If we regenerate plot many times, 95% of time μ should be in shaded region'
title += '\nShaded region is 95% of area under shifted sampling distribution'
_annotate(title=title)
plt.fill_betweenx([*plt.ylim()], ci_limits[0], ci_limits[1], color='gray', alpha=0.5, label='95% CI for $\\mu$')
plt.savefig('ci_examples_2.png', dpi=300)
plt.close()
