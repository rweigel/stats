import numpy as np
from math import erf
from matplotlib import pyplot as plt

xo = 0.5

N = 100000
dtheta = 0.2
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

for i in range(theta1s.size):
    for j in range(theta2s.size):
        x = np.random.normal(theta1s[i], theta2s[j], size=N)
        n, _ = np.histogram(x, bins=binsx)

        idx = np.where(np.abs(binsxc - xo) <= dx/2)[0]
        if (idx.size > 1):
            print('xo is on boundary of two bins.')
            idx = idx[0]

        P_D_theta[i,j] = n[idx]/N
        
        print('P = {0:.2f}; theta1 = {1:.2f}; theta2 = {2:.2f}'.format(P_D_theta[i,j],theta1s[i],theta2s[j]))

        P_D_theta_exactish[i,j] = dx*np.exp( -(xo-theta1s[i])**2/(2.0*theta2s[j]**2) )/np.sqrt(2*np.pi*theta2s[j]**2)

print("sum(P_D_theta_exactish) on grid: {0:.4f}".format(np.sum(P_D_theta_exactish)))

P_theta_D_exactish = P_D_theta_exactish/np.sum(P_D_theta_exactish)
P_theta_D = P_D_theta/np.sum(P_D_theta)

theta1se = np.append(theta1s, theta1s[-1] + dtheta)
theta1se = theta1se - dtheta/2

theta2se = np.append(theta2s, theta2s[-1] + dtheta)
theta2se = theta2se - dtheta/2

plt.figure(1)
m = plt.pcolor(theta1se, theta2se, P_theta_D.T, cmap=plt.get_cmap('viridis', 20))
m.set_clim(0,0.1)
cb = plt.colorbar(m)
plt.ylabel('$\\theta_2$')
plt.xlabel('$\\theta_1$')
cb.ax.set_title('$P([\\theta_1,\\theta_2]|\mathcal{D})$')
plt.title('Simulation')

# Set ticks to match centers
plt.xticks(theta1s)
plt.yticks(theta2s)

plt.figure(2)
m = plt.pcolor(theta1se, theta2se, P_theta_D_exactish.T, cmap=plt.get_cmap('viridis', 20))
m.set_clim(0,0.1)
cb = plt.colorbar(m)
plt.ylabel('$\\theta_2$')
plt.xlabel('$\\theta_1$')
cb.ax.set_title('$P([\\theta_1,\\theta_2]|\mathcal{D})$')
plt.title('Exactish')

# Set ticks to match centers
plt.xticks(theta1s)
plt.yticks(theta2s)

P_delta = P_theta_D -P_theta_D_exactish
plt.figure(3)
m = plt.pcolor(theta1se, theta2se, P_delta.T, cmap=plt.get_cmap('viridis', 20))
m.set_clim(-0.1,0.1)
cb = plt.colorbar(m)
plt.ylabel('$\\theta_2$')
plt.xlabel('$\\theta_1$')
plt.title('Simulation-Exactish using same color scale')

# Set ticks to match centers
plt.xticks(theta1s)
plt.yticks(theta2s)