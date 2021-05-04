import numpy as np
from math import erf
from matplotlib import pyplot as plt

xo = 0.5

N = 100000
dtheta = 0.1
dx = 0.1

# Theta values to test. Theta corresponds to pop. mean.
theta1s = np.arange(-1, 1 + dtheta, dtheta)
theta2s = np.arange(dtheta, 1 + dtheta, dtheta)

# bin edges
binsx = np.arange(-5, 5 + dx, dx)
# bin centers
binsxc = binsx[0:-1] + dx/2

d = (theta1s.size, theta2s.size)
P_D_theta = np.full(d, np.nan)
P_D_theta_exactish = np.full(d, np.nan)
P_D_theta_exactish2 = np.full(d, np.nan)

for i in range(theta1s.size):
    for j in range(theta2s.size):
        x = np.random.normal(theta1s[i], theta2s[j], size=N)
        n, _ = np.histogram(x, bins=binsx)

        # Find cases where samples are near xo.
        idx = np.where(np.abs(binsxc - xo) <= dx/2)[0]
        if (idx.size > 1):
            print('xo is on boundary of two bins.')
            idx = idx[0]

        # Probability of data given theta is # of times
        # draw from Normal(theta1, theta2**2) was near xo.
        P_D_theta[i,j] = n[idx]/N
        
        print('P = {0:.2f}; theta1 = {1:.2f}; theta2 = {2:.2f}'.format(P_D_theta[i,j],theta1s[i],theta2s[j]))

        # Exact-"ish" because to be exact we would need to integrate over
        # area around xo.
        P_D_theta_exactish[i,j] = dx*np.exp( -(xo-theta1s[i])**2/(2.0*theta2s[j]**2) )/np.sqrt(2*np.pi*theta2s[j]**2)

        # Using Jeffrey's prior
        P_D_theta_exactish2[i,j] = (1/theta2s[j])*dx*np.exp( -(xo-theta1s[i])**2/(2.0*theta2s[j]**2) )/np.sqrt(2*np.pi*theta2s[j]**2)


print("sum(P_D_theta_exactish) on grid: {0:.4f}".format(np.sum(P_D_theta_exactish)))

P_theta_D_exactish = P_D_theta_exactish/np.sum(P_D_theta_exactish)
P_theta_D_exactish2 = P_D_theta_exactish2/np.sum(P_D_theta_exactish2)

P_theta_D = P_D_theta/np.sum(P_D_theta)

theta1se = np.append(theta1s, theta1s[-1] + dtheta)
theta1se = theta1se - dtheta/2

theta2se = np.append(theta2s, theta2s[-1] + dtheta)
theta2se = theta2se - dtheta/2

plt.figure(1)
m = plt.pcolor(theta1se, theta2se, P_theta_D.T, cmap=plt.get_cmap('viridis', 20))
#m.set_clim(0,0.1)
cb = plt.colorbar(m)
plt.ylabel('$\\theta_2$ ($\sigma$)')
plt.xlabel('$\\theta_1$ ($\mu$)')
cb.ax.set_title('$P([\\theta_1,\\theta_2]|\mathcal{D})$')
plt.title('Simulation')

# Set ticks to match centers
if theta1s.size < 11:
    plt.xticks(theta1s)
if theta2s.size < 11:
    plt.yticks(theta2s)
plt.savefig('figures/HW9_1_1a.svg', transparent=True)
plt.savefig('figures/HW9_1_1a.png', transparent=True)


plt.figure(2)
m = plt.pcolor(theta1se, theta2se, P_theta_D_exactish.T, cmap=plt.get_cmap('viridis', 20))
#m.set_clim(0,0.1)
cb = plt.colorbar(m)
plt.ylabel('$\\theta_2$ ($\sigma$)')
plt.xlabel('$\\theta_1$ ($\mu$)')
cb.ax.set_title('$P([\\theta_1,\\theta_2]|\mathcal{D})$')
plt.title('Exactish')

# Set ticks to match centers
if theta1s.size < 11:
    plt.xticks(theta1s)
if theta2s.size < 11:
    plt.yticks(theta2s)

plt.savefig('figures/HW9_1_1b.svg', transparent=True)
plt.savefig('figures/HW9_1_1b.png', transparent=True)

plt.figure(3)
m = plt.pcolor(theta1se, theta2se, P_theta_D_exactish2.T, cmap=plt.get_cmap('viridis', 20))
#m.set_clim(0,0.1)
cb = plt.colorbar(m)
plt.ylabel('$\\theta_2$ ($\sigma$)')
plt.xlabel('$\\theta_1$ ($\mu$)')
cb.ax.set_title('$P([\\theta_1,\\theta_2]|\mathcal{D})$')
plt.title('Exactish w/ $1/\\theta_2$ prior')

# Set ticks to match centers
if theta1s.size < 11:
    plt.xticks(theta1s)
if theta2s.size < 11:
    plt.yticks(theta2s)


P_delta = P_theta_D - P_theta_D_exactish
plt.figure(4)
m = plt.pcolor(theta1se, theta2se, P_delta.T, cmap=plt.get_cmap('viridis', 20))
#m.set_clim(-0.1,0.1)
cb = plt.colorbar(m)
plt.ylabel('$\\theta_2$ ($\sigma$)')
plt.xlabel('$\\theta_1$ ($\mu$)')
plt.title('Simulation-Exactish')

# Set ticks to match centers
if theta1s.size < 11:
    plt.xticks(theta1s)
if theta2s.size < 11:
    plt.yticks(theta2s)

plt.savefig('figures/HW9_1_1c.svg', transparent=True)
plt.savefig('figures/HW9_1_1c.png', transparent=True)
