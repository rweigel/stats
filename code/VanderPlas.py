import numpy as np

true_B = 100
sigma_x = 10

#np.random.seed(1)
D = np.random.normal(true_B, sigma_x, size=3)
print(D)

# first define some quantities that we need
Nsamples = np.int(2e7)
N = len(D)
sigma_x = 10

# if someone changes N, this could easily cause a memory error
#if N * Nsamples > 1E8:
#    raise ValueError("Are you sure you want this many samples?")

# eps tells us how close to D we need to be to consider
# it a matching sample. The value encodes the tradeoff
# between bias and variance of our simulation
eps = 0.5

# Generate some mean values from the (flat) prior in a reasonable range
#np.random.seed(0)
mu = 80 + 40 * np.random.random(Nsamples)

# Generate data for each of these mean values
x = np.random.normal(mu, sigma_x, (N, Nsamples)).T

# find data which matches matches our "observed" data
x.sort(1)
D.sort()
from scipy.special import erfinv
def bayes_CR_mu(D, sigma, frac=0.95):
    """Compute the credible region on the mean"""
    Nsigma = np.sqrt(2) * erfinv(frac)
    mu = D.mean()
    sigma_mu = sigma * D.size ** -0.5
    return mu - Nsigma * sigma_mu, mu + Nsigma * sigma_mu


i1 = np.all(abs(x - D) < eps, 1)
print("number of suitable samples: {0}".format(i1.sum()))
# Now we ask how many of these mu values fall in our credible region
mu_good = mu[i1]
CR = bayes_CR_mu(D, 10)
within_CR = (CR[0] < mu_good) & (mu_good < CR[1])
print("Fraction of means in Credible Region: {0:.3f}".format(within_CR.sum() * 1. / within_CR.size))

i2 = np.sqrt(np.sum((x - D)**2,axis=1)) < 2*np.sqrt(sigma_x)
print("number of suitable samples: {0}".format(i2.sum()))
print("fraction of suitable samples: {0:.5f}".format(i2.sum()/Nsamples))