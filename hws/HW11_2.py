import numpy as np
import emcee

from matplotlib import pyplot as plt
import scipy

if True:
    # Here theta can only take on a set of discrete values because it is
    # the number of degrees of freedom. This is addressed by rounding theta to
    # the nearest integer values. See also the discussion at
    # https://github.com/dfm/emcee/issues/150
    # and also related discussions linked to from that thread.
    nD = 30
    D = np.random.chisquare(3, size=nD)
    variable_str = '$\\nu$'
    def log_LxP_chi2(theta, D):
        """Return Log( Likelihood * Posterior) given data D."""

        #print("theta = {0:.1f}".format(theta[0]))
        if theta > 1:
            LxP = np.prod(scipy.stats.chi2(np.round(theta[0])).pdf(D))
        else:
            LxP = 0.0
        #print("LxP = {0:.1f}".format(LxP))

        return np.log(LxP)

    log_LxP = log_LxP_chi2

    D = np.random.chisquare(3, size=nD)
    dnu = 1
    nu = np.arange(0, 6 + dnu, dnu)
    P = np.full(nu.shape, np.nan)
    for i in range(nu.size):
        P[i] = np.prod(scipy.stats.chi2(i).pdf(D))
    P[0] = 0
    P = P/np.sum(P)


if False:
    variable_str = '$\nu'
    D = np.random.uniform(-1, 1, size=10)
    D = np.array([-0.5, 0.5])
    def log_LxP_uniform(theta, D):
        """Return Log( Likelihood * Posterior) given data D."""
    
        if np.abs(theta) <= 1:
            LxP = 1.0/D.size
        else:
            LxP = 0.0
        return np.log(LxP)

    log_LxP = log_LxP_uniform


if False:
    variable_str = '$\mu'
    D = np.random.normal(0, 1, size=10)
    def log_LxP_normal(theta, D):
        """Return Log( Likelihood * Posterior) given data D."""
    
        if np.abs(theta) <= 5:
            LxP = np.prod(np.exp( -((theta-D)**2)/2 ))
        else:
            LxP = 0.0
        return np.log(LxP)

    log_LxP = log_LxP_normal

nstep = 1e3     # Number of steps each walker takes
nwalk = 10      # Number of initial values for theta
ndims = 1       # Number of unknown parameters in theta vector

# Create a set of 10 inital values for theta. Values are drawn from
# a distribution that is unform in range [-1, 1] and zero outside.
thetas_initial =  np.random.uniform(2, 10, (nwalk, ndims))

# Initialize the sampler object
sampler = emcee.EnsembleSampler(nwalk, ndims, log_LxP, args=(D, ))

# Run the MCMC algorithm for each initial theta for nsteps
sampler.run_mcmc(thetas_initial, nstep, progress=False);

# Get the values of theta at each step
samples = sampler.get_chain()

# print(samples.shape) # (nstep, nawlk, ndims)

plt.figure()
plt.plot(samples[:,0,0])
plt.title('First Walker')
plt.xlabel('Step')
plt.ylabel('$\\theta$')
plt.grid()


if False:
    plt.figure()
    #plt.hist(samples[:,0,0],bins=20)
    plt.hist(np.round(samples[:,0,0]),bins=20)
    plt.title('Histogram of $\\theta$ values for first walker')
    plt.ylabel('# in bin')
    plt.xlabel('$\\theta$')
    plt.grid()

plt.figure()
#plt.hist(samples[:,0,0],density=True)
plt.hist(np.round(samples[:,0,0]),density=True, bins=np.arange(1,10)-0.5, label='emcee')
plt.plot(nu, P, 'k.', label='Exact')
#plt.title('pdf of ' + variable_str + ' values for first walker')
plt.ylabel('p(' + variable_str + '|$\\mathcal{D})$')
plt.xlabel(variable_str)
plt.xticks(nu)
plt.title('$\mathcal{{D}}$=np.random.chisquare(3, size={0:d})'.format(nD))
plt.legend()
plt.grid()
