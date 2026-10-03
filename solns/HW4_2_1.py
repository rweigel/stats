import numpy as np
import scipy.stats

n = 17
s2 = 137324.3

sample = [1470, 1510, 1690, 1740, 1900, 2000, 2030, 2100, 2190,
          2200, 2290, 2380, 2390, 2480, 2500, 2580, 2700]
s2 = np.var(sample, ddof=1)
print(f"Sample variance: {s2:.2f}")

chi2_lower = scipy.stats.chi2.ppf(0.025, df=n-1)
chi2_upper = scipy.stats.chi2.ppf(0.975, df=n-1)

print(f"Chi2 lower: {chi2_lower:.2f}, Chi2 upper: {chi2_upper:.2f}")
ci_lower = (n-1)*s2/chi2_upper
ci_upper = (n-1)*s2/chi2_lower

print(f"95% CI for the variance: [{ci_lower:.2f}, {ci_upper:.2f}]")

"""
Sample variance: 137324.26
Chi2 lower: 6.91, Chi2 upper: 28.85
95% CI for the variance: [76171.31, 318079.76]
"""