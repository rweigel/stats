import numpy as np
import scipy
from matplotlib import pyplot as plt

n = 10
# Sample from a normal distribution with mean 0 and standard deviation 1
μ = 0
σ = 1

dbin = 0.1 # Bin width
# dbin/2 shift so a bin centered on 0.0, a symmetry point.
bins = np.arange(-2-dbin/2, 2+dbin/2, 0.1)

hist_kwargs = {
  'color': 'black',
  'edgecolor': 'w',
  'linewidth': 0.5,
  'density': True
}

def _savefig(fig):
  plt.savefig(f'figures/sampling_dists_{fig}.png', dpi=300, bbox_inches='tight')
  plt.close()

def _annotate(title=''):
  plt.xlabel('$\\overline{x}$')
  plt.ylabel('Probability density')
  plt.title(title, fontsize=11)
  plt.axvline(x_bar, color='black', linestyle='--', linewidth=3, label='$\\overline{x}_{sample}$')
  plt.axvline(μ, color='magenta', linewidth=3, label='$\\mu$')
  plt.grid()
  plt.legend(loc='upper left', facecolor='white', framealpha=1)
  plt.xlim([-2, 2])
  plt.ylim([0, 1.8])

##############################################################################
# Part 1a.
# Plot the sampling distribution of x_bar when x is drawn from a normal
# distribution with mean μ and standard deviation σ.
##############################################################################

x = np.random.normal(loc=μ, scale=σ, size=n)
x = tuple(x) # Make sure we don't modify

# Compute the sample mean and standard deviation
x_bar = np.mean(x)
s = np.std(x, ddof=1)

# Sampling distribution of x_bar when x drawn from a normal distribution with
# mean μ and standard deviation σ is a normal distribution with mean μ and
# standard deviation σ/sqrt(n)
x_bar_grid = np.linspace(-4*σ/np.sqrt(n), 4*σ/np.sqrt(n), 1000)
d = np.sqrt(2*np.pi)*(σ/np.sqrt(n))
x_bar_sampling_dist = (1/d)*np.exp(-(x_bar_grid-μ)**2/(2*(σ/np.sqrt(n))**2))
# Or
#x_bar_sampling_dist = scipy.stats.norm(loc=μ, scale=σ/np.sqrt(n)).pdf(x_bar_grid)

# If we re-run this code many times, green line will move around. Most often
# it will be near zero.
label = 'Sampling distribution of $\\overline{x}$'
plt.plot(x_bar_grid, x_bar_sampling_dist, color='black', label=label)
title = f'$\\overline{{x}}_{{sample}}$ is mean of n=${{{n}}}$ values drawn from N(μ={μ}, σ={σ})'
title += '\nNote that sampling distribution is centered on μ, not $\\overline{x}_{sample}$'
title += '\nEach time simulation is run, $\\overline{x}_{sample}$ will be different'
_annotate(title=title)
_savefig('1a')

##############################################################################
# Part 2a.
# Use a non-bootstrap simulation to generate the sampling distribution of x_bar.
##############################################################################

ns = 10000 # subscript "s" => simulated
xs = np.random.normal(loc=μ, scale=σ, size=(n, ns))

# x has n rows and ns columns. Each column is a simulated sample.
# Compute the sample mean for each column
xs_bars = np.mean(xs, axis=0) 

title = 'Non-bootstrap simulation of sampling distribution of $\\overline{x}$'
plt.hist(xs_bars, bins=bins, **hist_kwargs)
_annotate(title=title)
_savefig('2a')

##############################################################################
# Part 3a.
# Use a parametric bootstrap simulation to generate the sampling distribution
# of x_bar.
##############################################################################

nb = 10000 # subscript "b" => bootstrap
# Here we assume that we don't know the true mean and standard deviation of the
# population, but know the population pdf is normal.
# Next line is same as part 2. except μ -> x_bar and σ -> s.
xb = np.random.normal(loc=x_bar, scale=s, size=(n, nb))
xb_star_bars = np.mean(xb, axis=0)

title = 'Parametric bootstrap simulation of sampling distribution of $\\overline{x}$'
_annotate(title=title)
plt.hist(xb_star_bars, bins=bins, **hist_kwargs)
_savefig('3a')

##############################################################################
# Part 4a.
# Use a nonparametric bootstrap simulation to generate the sampling distribution of x_bar.
# Here we don't know μ, σ, or the population pdf.
##############################################################################

nb = 1000
xb_star_bars = np.full(nb, np.nan)
for i in range(nb):
  xb_star = np.random.choice(x, size=n, replace=True)
  xb_star_bars[i] = np.mean(xb_star)

title = 'Nonparametric bootstrap simulation of sampling distribution of $\\overline{x}$'
plt.hist(xb_star_bars, bins=bins, **hist_kwargs)
_annotate(title=title)
_savefig('4a')

##############################################################################
# Part 1b.
# Compute the exact 95% confidence interval for μ using results of part 1a.
##############################################################################

# A confidence interval is an interval around the point estimate x_bar.
# Clearly it should be related to the sampling distribution of x_bar.
# Plot sampling distribution with center at x_bar.
x_bar_sampling_dist_shifted = (1/d)*np.exp(-(x_bar_grid-x_bar)**2/(2*(σ/np.sqrt(n))**2))
print("1b. 95% CI for μ:")
ci_limits = scipy.stats.norm.ppf([0.025, 0.975], loc=x_bar, scale=σ/np.sqrt(n))
print(f"  Using scipy.stats.norm.ppf: {ci_limits}")
ci_limits = [x_bar-1.96*σ/np.sqrt(n), x_bar+1.96*σ/np.sqrt(n)]
print(f"  Using formula for pdf: {ci_limits}")

label = 'Sampling distribution of $\\overline{x}$ shifted by $(\\overline{{x}}_{{sample}}-\\mu$)'
plt.plot(x_bar_grid, x_bar_sampling_dist_shifted, linestyle='--', color='black', label=label)

# Plot the confidence interval as a shaded region
plt.fill_betweenx([*plt.ylim()], ci_limits[0], ci_limits[1],
                  color='gray', alpha=0.5, label='95% CI for $\\mu$')

title = 'If we regenerate plot many times, 95% of time μ should be in shaded region'
title += '\nShaded region is 95% of area under shifted sampling distribution'
_annotate(title=title)
_savefig('1b')

##############################################################################
# Part 2b.
# Compute the 95% confidence interval for μ using results of part 2a.
##############################################################################

##############################################################################
# Part 3b.
# Compute the 95% confidence interval for μ using results of part 3a.
##############################################################################

##############################################################################
# Part 4b.
# Compute the 95% confidence interval for μ using results of part 4a.
##############################################################################

# Part 1c.
# Test the hypothesis that μ = 0 using results of part 1a.