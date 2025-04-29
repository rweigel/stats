import numpy as np
from math import erf
from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'

run = 2

xo = 0.5
sigma = 1

if run == 1:
    N = 10
    sigma = 1
    dtheta = 0.2
    dx = 1
else:
    N = 500000
    dtheta = 0.1
    dx = 0.01

# Theta values to test. Theta corresponds to pop. mean.
thetas = np.arange(-4, 4 + dtheta, dtheta)

# bin edges
binsx = np.arange(-4, 4 + dx, dx)
# bin centers
binsxc = binsx[0:-1] + dx/2

#print("bin edges:   {0}".format(binsx))
#print("bin centers: {0}".format(binsxc))
# Find the index of of the bin that contains the point xo by looking for when
# the difference between a bin center and xo is less than or equal to dx/2.
idx = np.where(np.abs(binsxc - xo) <= dx/2)[0]
if (idx.size > 1):
    print('xo is on boundary of two bins. Using the bin to the left.')
idx = idx[0]
print(f"x_o = {xo:.1f} is in bin #{idx:d}")
print(f"x_o is in bin with range [{binsx[idx]:.1f}, {binsx[idx+1]:.1f}] and center {binsxc[idx]:.1f}")

P_D_theta = np.full(thetas.size, np.nan)
P_D_theta_exactish = np.full(thetas.size, np.nan)
data = np.full((N, thetas.size), np.nan)
for i in range(thetas.size):

    x = np.random.normal(thetas[i], 1, size=N)
    data[:,i] = x
    # Count the number of points in each bin
    n, _ = np.histogram(x, bins=binsx)

    # Compute the probability of the data given theta by finding
    # the number of points in the bin that contains x_o divided by N.
    P_D_theta[i] = n[idx]/N

    # The following is called exactish because to be exact the integral of 
    # exp((x-thetas[i])**2/(2*sigma**2))/np.sqrt(2*np.pi*sigma**2) from
    # x=thetas[i] - dtheta/2 to x=thetas[i] + dtheta/2 should be computed.
    # This is simply the "rectangle rule" approximation of the area.
    P_D_theta_exactish[i] = dx*np.exp( -(xo-thetas[i])**2/(2.0*sigma**2) )/np.sqrt(2*np.pi*sigma**2)

print("sum(P_D_theta_exactish) on grid: {0:.4f}".format(np.sum(P_D_theta_exactish)))

# p(θ) ∝ exp(-θ^2), and we know p(θ) is a probability density function,
# so it must be normalized to integrate to 1.
prior = np.exp(-thetas**2)/np.sqrt(np.pi)

P_theta_D_exactish = P_D_theta_exactish*prior/np.sum(P_D_theta_exactish*prior)
P_theta_D = P_D_theta*prior/np.sum(P_D_theta*prior)
print('sum(P_theta_D) = {0:.4f}'.format(np.sum(P_theta_D)))
print('sum(P_theta_D_exactish) = {0:.4f}'.format(np.sum(P_theta_D_exactish)))

title = '$\\mathcal{{D}}=[{0:.1f}]$; $p(\\theta)\\propto e^{{-\\theta^2}}$\nEach bin based on {1:d} experiments (draws from $\\mathcal{{N}}(\\theta,1)$)'.format(xo,N)
plt.figure()
plt.bar(thetas, P_D_theta, width=dtheta/2, label='Experiment')
plt.plot(thetas, P_D_theta_exactish, 'k.', label='Exactish')
plt.xlabel('$\\theta$')
plt.ylabel('$P(\\mathcal{D}|\\theta)$')
plt.title(title)
plt.legend()
if thetas.size < 12:
    plt.xticks(thetas)
plt.savefig('HW10_2b.svg', bbox_inches='tight', transparent=True)
plt.savefig('HW10_2b.png', bbox_inches='tight', dpi=300)


plt.figure()
plt.bar(thetas, P_theta_D, width=dtheta/2, label='Experiment')
plt.plot(thetas, P_theta_D_exactish, 'k.', label='Exactish')
plt.xlabel('$\\theta$')
plt.ylabel('$P(\\theta|\\mathcal{D})$')
plt.title(title)
plt.legend()
if thetas.size < 12:
    plt.xticks(thetas)

plt.savefig('HW10_2c.svg', bbox_inches='tight', transparent=True)
plt.savefig('HW10_2c.png', bbox_inches='tight', dpi=300)

p_D_theta_exact = np.exp( -(xo-thetas)**2/(2.0*sigma**2) )/np.sqrt(2*np.pi*sigma**2)
# where c = 1/(2*sigma**2)
# P(𝒟) = ∫ p(𝒟|θ) p(θ) dθ
# p(𝒟|θ) = exp(-(xo-θ)^2/(2σ^2)) / sqrt(2πσ^2)
# p(θ) = exp(-θ^2)/sqrt(π)
# Using σ = 1 and simplifying
# P_D = (1/π) 1/sqrt(2) ∫ exp(-(xo-θ)^2/2) exp(-θ^2) dθ
# Where limits of integration are -∞ to ∞
# Third term below is from
#   https://www.wolframalpha.com/input?i=%E2%88%AB+e%5E%28-%28a-x%29%5E2%2F2%29+e%5E%28-x%5E2%2F2%29+dx+from+-infinty+to+infinity
P_D = 0.299691
print("P(D) = {0:.4f}".format(P_D))

plt.figure()
plt.bar(thetas, P_theta_D/dtheta, width=dtheta/2, label='Experiment')
plt.plot(thetas, P_theta_D_exactish/dtheta, 'k.', label='Exactish')
plt.plot(thetas, p_D_theta_exact*prior/P_D, 'bx', label='Exact')
plt.xlabel('$\\theta$')
plt.ylabel('$p(\\theta|\\mathcal{D})$')
plt.title(title)
plt.legend()
if thetas.size < 12:
    plt.xticks(thetas)
plt.savefig('HW10_2d.svg', bbox_inches='tight', transparent=True)
plt.savefig('HW10_2d.png', bbox_inches='tight', dpi=300)