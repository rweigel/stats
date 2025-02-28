import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
from scipy.stats import t

n_b = 1000

x = [1470, 1510, 1690, 1740, 1900, 2000, 2030, 2100, 2190, 2200, 2290, 2380, 2390, 2480, 2500, 2580, 2700]
x = np.array(x)
n = len(x)
x_bar = np.mean(x)
x_std = np.std(x, ddof=1)
xstar = np.random.choice(x, size=(n, n_b), replace=True)

xstar_mean = np.mean(xstar, axis=0)
xstar_mean.sort()
ci_bootstrap = [np.percentile(xstar_mean, 2.5), np.percentile(xstar_mean, 97.5)]
#d = np.abs(x_std*norm.ppf(0.025)/np.sqrt(n-1))
d = np.abs(x_std * t.ppf(0.025, df=n-1) / np.sqrt(n))
ci_exact = [x_bar-d, x_bar+d]

print(f"Sample <X>       {x_bar:.0f}")
print(f"Bootstrap <X>    {np.mean(xstar_mean):.0f}")
print(f"Exact CI:        [{ci_exact[0]:.0f}, {ci_exact[1]:.0f}]")
print(f"Bootstrap CI:    [{ci_bootstrap[0]:.0f}, {ci_bootstrap[1]:.0f}]")

bins = np.arange(1700, 2600, 50)
counts, bins = np.histogram(xstar_mean, bins=bins)
plt.hist(bins[:-1], bins, weights=counts/sum(counts), color='black')
plt.axvline(x_bar, color='green', linestyle='-', label=f'Sample $\\overline{{X}}$ = {x_bar:.0f}')
plt.axvline(np.mean(xstar_mean), color='green', linestyle='-.', label=f'Bootstrap $<\\overline{{X}}>$ = {np.mean(xstar_mean):.0f}')
plt.axvline(ci_exact[0], color='red', label=f'Exact 95% CI = [{ci_exact[0]:.0f}, {ci_exact[1]:.0f}]')
plt.axvline(ci_exact[1], color='red')
plt.axvline(ci_bootstrap[0], color='blue', label=f'Bootstrap 95% CI = [{ci_bootstrap[0]:.0f}, {ci_bootstrap[1]:.0f}]')
plt.axvline(ci_bootstrap[1], color='blue')
plt.grid(axis='y')
plt.legend(loc='upper left')
#plt.xlim(*xlim)
plt.ylim([0, 0.4])
plt.xlabel('$\\overline{X}$')
plt.ylabel('Probability')
plt.title("Devore Example 7.15 data", fontsize=11)
plt.savefig('HW5_2a.png', dpi=300)
plt.close()

