import numpy as np
import emcee

from matplotlib import pyplot as plt

D = [0.5, 1.5]

def log_LxP(theta, D):
    """Return Log( Likelihood * Posterior) given data D."""
    p1 = np.exp( -((theta-D[0])**2)/2 )
    p2 = np.exp( -((theta-D[1])**2)/2 )
    if np.abs(theta) <= 1:
        LxP = p1*p2
    else:
        LxP = 0.0
    return np.log(LxP)

nstep = 1e3     # Number of steps each walker takes
nwalk = 10      # Number of initial values for theta
ndims = 1       # Number of unknown parameters in theta vector

# Create a set of 10 inital values for theta. Values are drawn from
# a distribution that is unform in range [-1, 1] and zero outside.
thetas_initial =  np.random.uniform(-1, 1, (nwalk, ndims))

# Initialize the sampler object
sampler = emcee.EnsembleSampler(nwalk, ndims, log_LxP, args=(D, ))

# Run the MCMC algorithm for each initial theta for 5000 steps
sampler.run_mcmc(thetas_initial, nstep, progress=True);

# Get the values of theta at each step
samples = sampler.get_chain()

# print(samples.shape) # (nstep, nawlk, ndims)

plt.figure()
plt.plot(samples[:,0,0])
plt.title('First Walker')
plt.xlabel('Step')
plt.ylabel('$\\theta$')
plt.grid()

plt.figure()
plt.hist(samples[:,0,0])
plt.title('Histogram of $\\theta$ values for first walker')
plt.ylabel('# in bin')
plt.xlabel('$\\theta$')
plt.grid()

plt.figure()
plt.hist(samples[:,0,0],density=True)
plt.title('pdf of $\\theta$ values for first walker')
plt.ylabel('p($\\theta|\\mathcal{D})$')
plt.xlabel('$\\theta$')
plt.grid()
