import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

n = 100
# Sample from a normal distribution with mean 0 and standard deviation 1
μ = 2
σ2 = 2
σ = np.sqrt(σ2)
x_bar = 2.4
μ_prime = 2.2

def _norm_pdf(μ, σ, x=None):
  if x is None:
    x = μ + np.linspace(-4*σ, 4*σ, 1000)
  pdf = (1/(σ*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-μ)/σ)**2)
  return x, pdf

def _annotate():

  title = f'$\\overline{{x}}_{{sample}}$ based on $n={n}$ values of $x$ drawn from $N(\\mu={μ}, \\sigma^2={σ2})$'
  plt.title(title)
  plt.ylim([0, 3.0])
  plt.gca().spines['top'].set_visible(False)
  plt.gca().spines['right'].set_visible(False)

  plt.axvline(μ, color='k', linewidth=3)
  plt.text(μ, 2.9, f' $\\mu={μ}$', ha='left')
  plt.xlabel('$\\overline{x}$')
  plt.ylabel('Probability density')
  plt.grid()

def _plot_type_I_areas(x_bar_grid, x_bar_sampling_dist, alpha_limits, alpha='0.05'):
  plt.fill_between(x_bar_grid, x_bar_sampling_dist,
                  where=(x_bar_grid < alpha_limits[0]),
                  color='red', alpha=1.0, label=f'rejection region for $H_0$: $\\mu=2$. Area = $\\alpha$ = {alpha}')
  plt.fill_between(x_bar_grid, x_bar_sampling_dist,
                  where=(x_bar_grid > alpha_limits[1]),
                  color='red', alpha=1.0)
  plt.fill_between(x_bar_grid, x_bar_sampling_dist,
                  where=(x_bar_grid >= alpha_limits[0]) & (x_bar_grid <= alpha_limits[1]),
                  color='green', alpha=0.5, label='non-rejection region for $H_0$. Area = $1-\\alpha$')

def _plot_type_II_area(μ_prime_grid, μ_prime_sampling_dist, alpha_limits, beta):
  #print(f"Area under the $\\mu'$ curve between CI limits for μ_prime: {beta:.4f}")
  plt.fill_between(μ_prime_grid, μ_prime_sampling_dist,
                  where=(μ_prime_grid <= alpha_limits[1]) & (μ_prime_grid >= alpha_limits[0]),
                  hatch='xx', alpha=0, label=f'Type II error region; area = $\\beta$ = {beta:0.2f}')

def _plot_pdf(x_bar_grid, x_bar_sampling_dist, ls='-', label=True):
  if ls == '-':
    var = '\\mu'
  else:
    var = "\\mu'"
  plt.plot(x_bar_grid, x_bar_sampling_dist, ls=ls, linewidth=1, color='black')
  if label:
    label = f'Sampling dist. of\n$\\overline{{x}}$ = $N({var}, \\sigma^2/n)$'
    plt.annotate(label, xytext=(1.55, 2.5), xy=(1.88, 2.0),
                arrowprops=dict(arrowstyle="->"), ha='left', va='center')

def _savefig(fig):
  plt.savefig(f'HW6_1{fig}.png', dpi=300, bbox_inches='tight')
  plt.savefig(f'HW6_1{fig}.svg', transparent=True, bbox_inches='tight')

legend_kwargs = {
  'loc': 'upper center',
  'bbox_to_anchor': (0.5, -0.15),
  'fontsize': 10,
  'facecolor': 'white',
  'framealpha': 0
}
x_bar_grid, x_bar_sampling_dist = _norm_pdf(μ, σ/np.sqrt(n))

# Part 1
ci = [x_bar - 1.96*σ/np.sqrt(n), x_bar + 1.96*σ/np.sqrt(n)]
print(f'95% CI for μ given x_bar={x_bar}: [{ci[0]:.2f}, {ci[1]:.2f}]')
_plot_pdf(x_bar_grid, x_bar_sampling_dist)
_annotate()
plt.axvline(x_bar, linestyle=':', color='k', linewidth=3)
plt.text(x_bar, 2.9, r' $\overline{x}_{sample}$')
plt.plot(ci, [0, 0], 'b', linewidth=5, label=f'95% CI for $\\mu$ given $\\overline{{x}}_{{sample}}={x_bar}$: [{ci[0]:.2f}, {ci[1]:.2f}]')
plt.legend(**legend_kwargs)
_savefig("a")

# Part 2
alpha_limits = [μ-1.96*σ/np.sqrt(n), μ+1.96*σ/np.sqrt(n)]
print(f'95% alpha limits: [{alpha_limits[0]:.2f}, {alpha_limits[1]:.2f}]')
_plot_type_I_areas(x_bar_grid, x_bar_sampling_dist, alpha_limits)

plt.text(alpha_limits[0], -0.02, f'{alpha_limits[0]:.2f}',
         horizontalalignment='center', verticalalignment='top', color='red')
plt.text(alpha_limits[1], -0.02, f'{alpha_limits[1]:.2f}',
         horizontalalignment='center', verticalalignment='top', color='red')

plt.legend(**legend_kwargs)
_savefig("b")

# HW6_2
# Find p value for x=x_bar
p_value = 2 * (1 - norm.cdf(np.abs(x_bar - μ) / (σ / np.sqrt(n))))
print(f'p value for x={x_bar}: {p_value:.4f}')

# Find x_bar values associated with p=0.0047
plt.close()
_plot_pdf(x_bar_grid, x_bar_sampling_dist)
_annotate()
p_value = 0.0047
z_value = norm.ppf(p_value/2)
x_sample_value = (σ/np.sqrt(n))*z_value + μ
print(f'z value associated with p={p_value}: {z_value:.4f}')
alpha_limits_p = [x_sample_value, 2*μ - x_sample_value]
print(f'alpha = {100*p_value:0.2}% limits: [{alpha_limits_p[0]:.2f}, {alpha_limits_p[1]:.2f}]')
_plot_type_I_areas(x_bar_grid, x_bar_sampling_dist, alpha_limits_p, alpha=f'{p_value:.4f}')
plt.xlim([1.5, 2.5])
plt.ylim([0, 3])
plt.title('')
plt.legend(**legend_kwargs)
plt.savefig('HW6_2.png', dpi=300, bbox_inches='tight')
plt.savefig('HW6_2.svg', transparent=True)

# Part 3
plt.close()
beta = norm.cdf(ci[1], loc=μ_prime, scale=σ/np.sqrt(n)) - norm.cdf(ci[0], loc=μ_prime, scale=σ/np.sqrt(n))
_annotate()
plt.axvline(μ_prime, linestyle=':', color='k', linewidth=3)
plt.text(μ_prime, 2.9, r" $\mu'$")
_plot_pdf(x_bar_grid, x_bar_sampling_dist)
μ_prime_grid, μ_prime_sampling_dist = _norm_pdf(μ_prime, σ/np.sqrt(n))
_plot_pdf(μ_prime_grid, μ_prime_sampling_dist, ls=':', label=False)
_plot_type_I_areas(x_bar_grid, x_bar_sampling_dist, alpha_limits)
_plot_type_II_area(μ_prime_grid, μ_prime_sampling_dist, alpha_limits, beta)
plt.legend(**legend_kwargs)
plt.title('')
_savefig("c")

# Part 4
betas = []
ds = []
μ_primes = np.arange(2.01, 3, 0.01)
for val in μ_primes:
  betas.append(norm.cdf(alpha_limits[1], loc=val, scale=σ/np.sqrt(n)) - norm.cdf(alpha_limits[0], loc=val, scale=σ/np.sqrt(n)))
  ds.append(np.abs(val - μ))

plt.close()
plt.ylabel('$\\beta$  ', rotation=0, horizontalalignment='right')
plt.xlabel("$|\\mu'-\\mu|$")
plt.ylim([0, 1])
plt.xlim([0, 0.8])
#plt.axhline(0.95, color='r', linestyle='--')
plt.plot(ds, betas, 'k-')
plt.plot([0.2, 0.2], [0, beta], color='k', linestyle=':')
plt.plot([0, 0.2], [beta, beta], color='k', linestyle=':')
plt.plot([0.2, 0.2], [beta, beta], 'k.', label="$\\mu'=2.2$")

plt.text(-0.1, 0.95, '0.95',
         horizontalalignment='left', verticalalignment='center', color='red')
plt.annotate("", xytext=(-0.05, 0.95), xy=(0.005, 0.95),
            arrowprops=dict(arrowstyle="->"))

plt.text(-0.1, beta, f'{beta:.2f}',
         horizontalalignment='left', verticalalignment='center', color='black')
plt.annotate("", xytext=(-0.05, beta), xy=(0.005, beta),
            arrowprops=dict(arrowstyle="->"))

plt.text(0.2, 0.1, "  $\\mu'=2.2$",
         horizontalalignment='left', verticalalignment='center', color='black')
plt.title("Type II error probability")
plt.grid()
_savefig("d")

