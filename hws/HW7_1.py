import numpy as np

n = 9
mu = 130
sigma = 1.5

np.random.seed(623)
x = np.random.normal(130.0, 1.5, size=9)
print(np.mean(x)) #131.0812930740811
Xbar = np.mean(x)
S = np.std(x, ddof=1)

T = (Xbar - mu)/(S/np.sqrt(n))
print(T) # 2.236

Z = (Xbar - mu)/(sigma/np.sqrt(n))
print(Z) # 2.16

from scipy import stats
mu = 130
sigma = 1.5
np.random.seed(623)
x = np.random.normal(mu, sigma, size=9)
T, p = stats.ttest_1samp(x, mu)
print('Scipy: t = {0:.3f}'.format(T)) # 2.236
print('Scipy: p = {0:.3f}'.format(p)) # 0.056

#from scipy.stats import norm
#print(1/(2*(1-norm.cdf(3))))

from scipy.stats import norm
-norm.ppf(0.005)

