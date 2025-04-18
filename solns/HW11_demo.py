import numpy as np
import emcee

from matplotlib import pyplot as plt

D = np.array([0.5])

def log_LxP(theta, D):
    """Return Log( Likelihood * Prior) given data D."""
    theta = theta[0] # Only one parameter in this example
    p = np.full(D.shape, np.nan)
    for i in range(D.shape[0]):
      p[i] = np.exp( -((theta-D[i])**2)/2 )
    if np.abs(theta) <= 1:
      LxP = np.prod(p)
    else:
      # Prior is zero outside of range [-1, 1], so want LxP = 0.
      # Assign machine epsilon to avoid log(0)
      LxP = np.finfo(float).eps

    return np.log(LxP)

nstep = int(1e4) # Number of steps each walker takes
nwalk = 10       # Number of initial values for theta
ndims = 1        # Number of unknown parameters in theta vector

# Create a set of 10 initial values for theta. Values are drawn from
# a distribution that is uniform in range [-1, 1] and zero outside.
thetas_initial =  np.random.uniform(-1, 1, (nwalk, ndims))

# Initialize the sampler object
sampler = emcee.EnsembleSampler(nwalk, ndims, log_LxP, args=(D, ))

# Run the MCMC algorithm for each initial theta for 5000 steps
sampler.run_mcmc(thetas_initial, nstep)#, progress=True)

# Get the values of theta at each step
samples = sampler.get_chain()

# print(samples.shape) # (nstep, nwalk, ndims)
w = 1
plt.figure()
plt.plot(samples[:,w,0])
plt.title('First Walker')
plt.xlabel('Step')
plt.ylabel('$\\theta$')
plt.grid()
plt.savefig('HW11_demo_a.png', dpi=300, bbox_inches='tight')
plt.savefig('HW11_demo_a.svg', bbox_inches='tight', transparent=True)

dtheta = 0.1
theta_edges = np.arange(-1, 1+dtheta, dtheta)
theta_centers = theta_edges[:-1] + dtheta/2
P_theta_D = np.full(theta_centers.shape, np.nan)
for i, theta in enumerate(theta_centers):
  P_theta_D[i] = np.exp(log_LxP([theta], D))
P_theta_D = P_theta_D/np.sum(P_theta_D)

print(theta_edges)
counts, bins = np.histogram(samples[:,w,0], bins=theta_edges)
print(np.sum(counts/np.sum(counts)))
print(np.sum(P_theta_D))
plt.figure()

#plt.plot(theta_centers, counts/np.sum(counts), 'b.', label='Metropolis')
plt.hist(samples[:,w,0], bins=theta_edges, density=True, label='Metropolis')
plt.plot(theta_centers, P_theta_D/dtheta, 'k.', lw=2, label='Exact')
plt.title('pdf of $\\theta$ values for first walker')
plt.ylabel('p($\\theta|\\mathcal{D})$')
plt.xlabel('$\\theta$')
plt.xticks(theta_edges[0:-1:2])
plt.legend()
plt.grid()
plt.savefig('HW11_demo_b.png', dpi=300, bbox_inches='tight')
plt.savefig('HW11_demo_b.svg', bbox_inches='tight', transparent=True)
