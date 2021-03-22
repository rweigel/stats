import numpy as np

n = 9
mu = 130
sigma = 1.5

#np.random.seed(623)

z = np.empty(10000)
for i in range(10000):
    x = np.random.normal(mu, sigma, size=n)
    xbar = np.mean(x)
    z[i] = (xbar - mu)/(sigma/np.sqrt(n))

plt.hist(z)
I = np.where(np.abs(z) > 3)[0]
print(10000/len(I))

#from scipy.stats import norm
#print(1/(2*(1-norm.cdf(3))))
