import numpy as np
import scipy.stats

np.random.seed(99)
x = np.random.normal(5, 2, size=50) # Generates given values
np.set_printoptions(precision=2)
print("x = ")
print(x)

# 1.1 Options: 
#   a. Equation 7.15 of Devore (pg 288) 
#   b. Non-parametric bootstrap

n = len(x)
xbar = np.mean(x)
xstd = np.std(x, ddof=1)

t = scipy.stats.t.ppf(0.975, n-1) # 
cil = xbar - t*xstd/np.sqrt(n)
ciu = xbar + t*xstd/np.sqrt(n)
print('μ = {0:.2f}; 95% CI = [{1:.2f}, {2:.2f}]'.format(xbar, cil, ciu))

# 1.2 Options: 
#   a. page 295 of Devore
#   b. Non-parametric bootstrap

# Lower limit 
chi2l = scipy.stats.chi2.ppf(0.975, n-1) 
cil = np.sqrt((n-1)*xstd**2/chi2l)

# Upper limit 
chi2u = scipy.stats.chi2.ppf(0.0250, n-1) 
ciu = np.sqrt((n-1)*xstd**2/chi2u)

print('σ = {0:.2f}; 95% CI = [{1:.2f}, {2:.2f}]'.format(xstd, cil, ciu))

# 2.1 Options: Extend exact soln in solns of 9.1.1 or use emcee

import emcee

def log_LxP(theta, D):

    LxP = np.prod(scipy.stats.norm(theta[0], theta[1]).pdf(D))
    if LxP == 0.0 or theta[1] <= 0.0:
        return -np.inf
    else:
        return np.log(LxP)

nstep = 1e4
nwalk = 4
ndims = 2
mu_initial = np.random.uniform(3, 5, nwalk)
sigma_initial = np.random.uniform(0.1, 5, nwalk)
thetas_initial = np.array([mu_initial, sigma_initial]).transpose()

sampler = emcee.EnsembleSampler(nwalk, ndims, log_LxP, args=(x,))
sampler.run_mcmc(thetas_initial, nstep, progress=True)
samples = sampler.get_chain()

from matplotlib import pyplot as plt

plt.figure()
plt.hist(samples[:,0,0],density=True, bins=20)
plt.title('pdf of $\\mu$ for first walker')
plt.ylabel('$p(\\mu|\\mathcal{D})$')
plt.xlabel('$\\mu$')
plt.grid()

plt.figure()
plt.hist(samples[:,0,1],density=True, bins=20)
plt.title('pdf of $\\sigma$ for first walker')
plt.ylabel('$p(\\sigma|\\mathcal{D})$')
plt.xlabel('$\\sigma$')
plt.grid()

# Bootstrap
sdata = np.random.choice(x,size=(1000,len(x)))
sigs = np.std(sdata,axis=1,ddof=1)
plt.hist(sigs,density=True, bins=20)


# 2.2 Use code I provided in previous HW.

