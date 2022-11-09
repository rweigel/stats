import numpy as np
from matplotlib import pyplot as plt
import emcee


np.random.seed(42)

a = 2
b = 3

N = 40
x = np.arange(0,N)/N
y = a*x + b + np.random.normal(0,0.3, size=N)

print('  x    y')
for i in range(len(x)):
    print(' {0:.2f} {1:.2f}'.format(x[i],y[i]))

def log_LxP_normal(theta):
    """Return Log( Likelihood * Posterior) given data D."""

    #print(theta)
    LxP = np.prod(np.exp( -(y-theta[0]*x-theta[1])**2 /2 ))
    if LxP == 0:
        return -np.inf
    return np.log(LxP)

log_LxP = log_LxP_normal

nstep = 1e3     # Number of steps each walker takes
nwalk = 10      # Number of initial values for theta
ndims = 2       # Number of unknown parameters in theta vector

# Create a set of 10 inital values for theta. Values are drawn from
# a distribution that is unform in range [-1, 1] and zero outside.
thetas_initial =  np.random.uniform(-1, 1, (nwalk, ndims))

# Initialize the sampler object
sampler = emcee.EnsembleSampler(nwalk, ndims, log_LxP)

# Run the MCMC algorithm for each initial theta for nsteps
sampler.run_mcmc(thetas_initial, nstep, progress=False);

# Get the values of theta at each step
samples = sampler.get_chain()

# print(samples.shape) # (nstep, nawlk, ndims)

plt.figure()
plt.plot(x,y,'.')
plt.xlabel('x')
plt.ylabel('y')


plt.figure()
plt.plot(samples[:,0,0])
plt.title('First Walker')
plt.xlabel('Step')
plt.ylabel('$a$')
plt.grid()

plt.figure()
plt.plot(samples[:,0,1])
plt.title('First Walker')
plt.xlabel('Step')
plt.ylabel('$b$')
plt.grid()
