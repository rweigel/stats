import numpy as np

n = 9
mu = 130
sigma = 1.5

# This choice happens to give a small p value. Comment out and run multiple
# times to see how p varies from experiement to experiment.
np.random.seed(623)

# Draw 9 values from normal with mean = 130.0 and std = 1.5.
x = np.random.normal(130.0, 1.5, size=9)
print('Xbar = {0:.3f}'.format(np.mean(x))) # 131.081
Xbar = np.mean(x)
# Sample std
S = np.std(x, ddof=1)
print('S    = {0:.3f}'.format(S)) # 1.451

T = (Xbar - mu)/(S/np.sqrt(n))
print('T    = {0:.3f}'.format(T)) # 2.236

Z = (Xbar - mu)/(sigma/np.sqrt(n))
print('Z    = {0:.3f}'.format(Z)) # 2.236

# Compute T using SciPy
from scipy import stats
T, p = stats.ttest_1samp(x, mu)
print('SciPy: t = {0:.3f}'.format(T)) # 2.236
print('SciPy: p = {0:.3f}'.format(p)) # 0.056
