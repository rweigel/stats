import numpy as np
from math import erf
from matplotlib import pyplot as plt

run = 1

xo = 0.5
sigma = 1

if run == 1:
    N = 10
    sigma = 1
    dtheta = 0.2
    dx = 1
else:
    N = 100000
    dtheta = 0.2
    dx = 0.1

# Theta values to test. Theta corresponds to pop. mean.
thetas = np.arange(-1, 1 + dtheta, dtheta)

# bin edges
binsx = np.arange(-5, 5 + dx, dx)
# bin centers
binsxc = binsx[0:-1] + dx/2


P_D_theta = np.full(thetas.size, np.nan)
P_D_theta_exactish = np.full(thetas.size, np.nan)
data = np.full((N, thetas.size), np.nan)
for i in range(thetas.size):
    x = np.random.normal(thetas[i], 1, size=N)
    data[:,i] = x
    n, _ = np.histogram(x, bins=binsx)

    idx = np.where(np.abs(binsxc - xo) <= dx/2)[0]
    if (idx.size > 1):
        print('xo is on boundary of two bins.')
        idx = idx[0]

    P_D_theta[i] = n[idx]/N

    # The following is called exactish because to be exact the integral of 
    # exp((x-thetas[i])**2/(2*sigma**2))/np.sqrt(2*np.pi*sigma**2) from
    # x=thetas[i] - dtheta/2 to x=thetas[i] + dtheta/2 should be computed.
    # This is simply the "rectangle rule" approximation of the area.
    P_D_theta_exactish[i] = dx*np.exp( -(xo-thetas[i])**2/(2.0*sigma**2) )/np.sqrt(2*np.pi*sigma**2)

print("sum(P_D_theta_exactish) on grid: {0:.4f}".format(np.sum(P_D_theta_exactish)))

P_theta_D_exactish = P_D_theta_exactish/np.sum(P_D_theta_exactish)
P_theta_D = P_D_theta/np.sum(P_D_theta)

if run == 1:
    # TODO: Switch to heatmap if N > 100, dx < 0.5 or dtheta < 0.1.
    Ns = np.min([N, 100])
    plt.figure()
    for i in range(thetas.size):
        thetas_rep = np.full(Ns, thetas[i])
        plt.plot(thetas_rep, data[0:Ns,i], 'k.', ms=1)
        plt.axvline(thetas[i]-dtheta/2, linewidth=1, color=[0,0,0,0.1])
    for i in range(binsx.size):
        plt.axhline(binsx[i], linewidth=1, color=[0,0,0,0.1])
    xmin = thetas[0] - 1.05*dtheta/2
    xlims = plt.xlim([xmin, thetas[-1] + 1.05*dtheta/2])
    plt.plot([xmin,xmin],[xo,xo], 'b.', label='$x_o$ = {0:.1f}'.format(xo))
    plt.legend()
    plt.yticks(binsxc)
    plt.xlabel('$\\theta$ (population mean)')
    plt.ylabel('$x$ bin centers')
    plt.title('Grid and values used for computing experiment-derived posterior\nEach $\\theta$ value has 10 points.')
    plt.xticks(thetas)
    plt.savefig('figures/HW8_2a_run-{0:d}.svg'.format(run), transparent=True)
    plt.savefig('figures/HW8_2a_run-{0:d}.png'.format(run), transparent=True)


title = '$\mathcal{{D}}=[{0:.1f}]$; $p(\\theta)=0$ if $|\\theta|>1$ and 0.5 if $|\\theta| ≤ 1$\nEach bin based on {1:d} experiments (draws from $\mathcal{{N}}(\\theta,1)$)'.format(xo,N)
plt.figure()
plt.bar(thetas, P_D_theta, width=dtheta/2, label='Experiment')
plt.plot(thetas, P_D_theta_exactish, 'k.', label='Exactish')
plt.xlabel('$\\theta$')
plt.ylabel('$P(\mathcal{D}|\\theta)$')
plt.title(title)
plt.legend()
plt.savefig('figures/HW8_2b_run-{0:d}.svg'.format(run), transparent=True)
plt.savefig('figures/HW8_2b_run-{0:d}.png'.format(run), transparent=True)


print('sum(P_theta_D) = {0:.4f}'.format(np.sum(P_theta_D)))
plt.figure()
plt.bar(thetas, P_theta_D, width=dtheta/2, label='Experiment')
plt.plot(thetas, P_theta_D_exactish, 'k.', label='Exactish')
plt.xlabel('$\\theta$')
plt.ylabel('$P(\\theta|\mathcal{D})$')
plt.title(title)
plt.legend()
plt.savefig('figures/HW8_2c_run-{0:d}.svg'.format(run), transparent=True)
plt.savefig('figures/HW8_2c_run-{0:d}.png'.format(run), transparent=True)

# Gaussian integral in terms of erf is given at
# https://en.wikipedia.org/wiki/Error_function#Name
# where c = 1/(2*sigma**2)
P_D = erf((xo + 1)/(np.sqrt(2)*sigma))/2 - erf((xo - 1)/(np.sqrt(2)*sigma))/2
print("P(D) = {0:.4f}".format(P_D))

P_D_theta_exact = np.exp( -(xo-thetas)**2/(2.0*sigma**2) )/np.sqrt(2*np.pi*sigma**2)
plt.figure()
plt.bar(thetas, P_theta_D/dtheta, width=dtheta/2, label='Experiment')
plt.plot(thetas, P_theta_D_exactish/dtheta, 'k.', label='Exactish')
plt.plot(thetas, P_D_theta_exact/P_D, 'bx', label='Exact')
plt.xlabel('$\\theta$')
plt.ylabel('$p(\\theta|\mathcal{D})$')
plt.title(title)
plt.legend()
plt.savefig('figures/HW8_2d_run-{0:d}.svg'.format(run), transparent=True)
plt.savefig('figures/HW8_2d_run-{0:d}.png'.format(run), transparent=True)
