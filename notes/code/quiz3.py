
import numpy as np

#np.random.seed(42)
n = 10 # Number of samples
mu = 0
sigma = 1
sample = np.random.normal(loc=mu, scale=sigma, size=n)
xbar = np.mean(sample)

ne = 1000 # Number of experiments
xbars = np.zeros(ne)
delta = 1.96*sigma/np.sqrt(n)

cnt = 0
xcnt = 0
for i in range(ne):
  sample = np.random.normal(loc=mu, scale=sigma, size=n)
  xbar = np.mean(sample)
  if xbar - delta > mu or xbar + delta < mu:
    xcnt = xcnt + 1

  if xbar - delta < mu and xbar + delta > mu:
    cnt = cnt + 1

print(1-xcnt/ne)
print(cnt/ne)

exps = np.random.normal(loc=mu, scale=sigma, size=(n, ne))
print(exps.shape) # (10, 10000)
# size=(n_rows, n_cols)
# 10x1000
xbars = np.mean(exps, axis=0)
#print(xbars[(xbars - delta < mu) & (xbars + delta > mu)])
# trapped is 0 if not trapped
trapped = np.where((xbars - delta < mu) & (xbars + delta > mu), 1, 0)
cnt = np.sum(trapped)
print(cnt/ne)