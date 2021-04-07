import numpy as np
from matplotlib import pyplot as plt

D = [0.125, 0.880]

plt.figure(1)

theta = 0

x = np.random.normal(theta, 1, size=(1000, 2))

plt.scatter(x[:,0],x[:,1])

dx = 1
binsx = -dx/2 + np.arange(-5, 5 + dx, dx)

bins = [binsx, binsx]

plt.figure(2)
from matplotlib import cm
viridis = cm.get_cmap('viridis', 20)

cnts, _, _, _ = plt.hist2d(x[:,0], x[:,1], bins=bins, cmap=viridis, vmax=0, vmin=200)

print(cnts.sum)

plt.plot(D[0], D[1], 'k.')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.colorbar(ticks=np.arange(0,210,10))
n_D = cnts[6,6]

print(n_D)


xo = 0.0

dtheta = 0.01
thetas = np.arange(-1, 1 + dtheta, dtheta)

dx = 0.01
binsx = np.arange(-7, 7 + dx, dx)

p_D_mu = np.full(thetas.size, np.nan)
p_D_mu_exact = np.full(thetas.size, np.nan)
for i in range(thetas.size):
    x = np.random.normal(thetas[i], 1, size=100000)
    n, _ = np.histogram(x, bins=binsx)
    
    print(np.sum(n))
    idx = np.where(np.abs(binsx - xo) <= dx/2)[0]

    p_D_mu[i] = n[idx]/10000

    p_D_mu_exact[i] = np.exp( -(xo-thetas[i])**2/2.0 )/np.sqrt(2*np.pi)

import math
E = (math.erf(np.abs(xo)+1) + math.erf(1-np.abs(xo)))/2
print("Evidence integral: {0:.4f}".format(E))

E = 0.68
p_mu_D_exact = p_D_mu_exact/E

p_mu_D = p_D_mu/np.sum(p_D_mu)
print(np.sum(p_mu_D))
plt.figure()
plt.bar(thetas, p_mu_D/dtheta, width=dtheta/2)
plt.plot(thetas, p_mu_D_exact, 'k.')
plt.xlabel('$\\theta$')
plt.ylabel('$p(\\theta|\mathcal{D})$')