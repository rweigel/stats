import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

n = 100
# Sample from a normal distribution with mean 0 and standard deviation 1
μ = 2
σ = np.sqrt(2)
x_bar = 2.4

alpha_limits = [μ-1.96*σ/np.sqrt(n), μ+1.96*σ/np.sqrt(n)]

x_bar_grid = np.linspace(μ-4*σ/np.sqrt(n), μ+4*σ/np.sqrt(n), 1000)
d = np.sqrt(2*np.pi)*(σ/np.sqrt(n))
x_bar_sampling_dist = (1/d)*np.exp(-(x_bar_grid-μ)**2/(2*(σ/np.sqrt(n))**2))
label = 'Sampling distribution of $\\overline{x}$'
plt.plot(x_bar_grid, x_bar_sampling_dist, color='black', label=label)
plt.savefig('hypothesis.png', dpi=300, bbox_inches='tight')
plt.ylim(bottom=0)
plt.axvline(μ, color='k', linewidth=3, label=r'$\mu$')
plt.axvline(x_bar, linestyle=':', color='k', linewidth=3, label=r'$\overline{x}_{sample}$')
plt.fill_between(x_bar_grid, x_bar_sampling_dist,
                 where=(x_bar_grid < alpha_limits[0]), color='red', alpha=0.5, label='rejection region')
plt.fill_between(x_bar_grid, x_bar_sampling_dist, where=(x_bar_grid > alpha_limits[1]), color='red', alpha=0.5)
plt.fill_between(x_bar_grid, x_bar_sampling_dist, where=(x_bar_grid >= alpha_limits[0]) & (x_bar_grid <= alpha_limits[1]), color='green', alpha=0.5, label='non-rejection region')
plt.text(alpha_limits[0], -0.02, f'{alpha_limits[0]:.2f}', horizontalalignment='center', verticalalignment='top', color='red')
plt.text(alpha_limits[1], -0.02, f'{alpha_limits[1]:.2f}', horizontalalignment='center', verticalalignment='top', color='red')
plt.legend(loc='upper left')
plt.xlabel('$\\overline{x}$')
plt.ylabel('Probability density')
plt.grid()
#plt.close()
# Compute the exact area under the curve for x_bar_grid > 2.4

# Compute the area under the curve for x_bar_grid > 2.4 using the trapezoidal rule
area_trapz = np.trapz(x_bar_sampling_dist[x_bar_grid > x_bar], x_bar_grid[x_bar_grid > x_bar])
print(f'Area under the curve for x_bar > 2.4 using trapezoidal rule: {2*area_trapz:.4f}')

# Calculate the z-score for x_bar
z_score = (x_bar - μ) / (σ / np.sqrt(n))

# Compute the area using the survival function (1 - CDF)
area = norm.sf(z_score)
print(f'Exact area under the curve for |x_bar| > 2.4: {2*area:.4f}')