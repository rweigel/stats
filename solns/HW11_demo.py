import numpy as np
import emcee

from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'

D = np.array([0.5])
#D = np.array([0.5, 0.5, 1.0])

def log_LxP(theta, D):
  """Return Log( Likelihood * Prior) given data D."""
  theta = theta[0] # Only one parameter in this example
  p = np.full(D.shape, np.nan)
  for i in range(D.shape[0]):
    p[i] = np.exp( -((theta-D[i])**2)/2 )
  if np.abs(theta) <= 1:
    LxP = np.prod(p)
    return np.log(LxP)
  else:
    # Prior is zero outside of range [-1, 1], so want LxP = 0.
    # So log(LxP) = -np.inf
    return -np.inf

def posterior_exactish(theta_centers, D):
  P_theta_D = np.full(theta_centers.shape, np.nan) # Empty array
  for i, theta in enumerate(theta_centers):
    P_theta_D[i] = np.exp(log_LxP([theta], D))
  # This is exactish because I am not computing P(D).
  P_theta_D = P_theta_D/np.sum(P_theta_D)
  return P_theta_D

def posterior_mcmc(theta_edges, samples):
  counts, _ = np.histogram(samples, bins=theta_edges)
  return counts/np.sum(counts)

nstep = int(1e4) # Number of steps each walker takes
nwalk = 10       # Number of initial values for theta
ndims = 1        # Number of unknown parameters in theta vector

# Create a set of 10 initial values for theta (initial values for walkers).
# Values are drawn from a distribution that is uniform in range [-1, 1]
# and zero outside.
thetas_initial = np.random.uniform(-1, 1, (nwalk, ndims))

# Initialize the sampler object
sampler = emcee.EnsembleSampler(nwalk, ndims, log_LxP, args=(D, ))

# Run the MCMC algorithm for each initial theta for 5000 steps
sampler.run_mcmc(thetas_initial, nstep)#, progress=True)

# Get the values of theta at each step in the chain (a chain is all steps of a
# walker). samples.shape = (nstep, nwalk, ndims).
samples = sampler.get_chain()

w = 1 # Walker to plot

plt.figure()
plt.plot(samples[:,w,0])
plt.title('First Walker')
plt.xlabel('Step')
plt.ylabel('$\\theta$')
plt.grid()
plt.savefig('HW11_demo_a.png', dpi=300, bbox_inches='tight')
plt.savefig('HW11_demo_a.svg', bbox_inches='tight', transparent=True)

dtheta = 0.1 # Bin size
theta_edges = np.arange(-1, 1+dtheta, dtheta)
theta_centers = theta_edges[:-1] + dtheta/2

P_theta_D_exactish = posterior_exactish(theta_centers, D)
P_theta_D_mcmc = posterior_mcmc(theta_edges, samples[:,w,0])

plt.figure()
plt.bar(theta_centers, P_theta_D_mcmc, width=dtheta, color='b', alpha=0.5, label='MCMC')
plt.plot(theta_centers, P_theta_D_exactish, 'k.', lw=2, label='Exactish')
plt.ylabel('$P(\\theta|\\mathcal{D})$')
plt.xlabel('$\\theta$')
plt.xticks(theta_edges[0:-1:2])
plt.legend()
plt.grid()
plt.savefig('HW11_demo_b.png', dpi=300, bbox_inches='tight')
plt.savefig('HW11_demo_b.svg', bbox_inches='tight', transparent=True)
