import numpy as np
from matplotlib import pyplot as plt

def count(condition):
    return np.sum(condition)

# 1.

N_T = 3  # Number of tosses/experiment
N_H = 2  # Number of heads in an experiment

N_E = 10000 # Number of experiments to run for each p_H.

dtheta = 0.01 

thetas = np.arange(0, 1 + dtheta, dtheta)
n_B = np.full(thetas.size, np.nan) # prior
p_theta = np.full(thetas.size, np.nan)
for i in range(thetas.size):
    x = np.random.binomial(N_T, thetas[i], size=N_E)
    n_B[i] = count(x == N_H)

P_D_given_theta = n_B/N_E # a probability, but not a pmf b/c sum(P_B) != 0
print('sum(P_D_given_theta) = {0:.2f}'.format(np.sum(P_D_given_theta)))

plt.figure(1)
plt.bar(thetas, P_D_given_theta, width=dtheta/2, color='k', alpha=0.5, align='center')
plt.xlabel('$\\theta$ of coin')
plt.ylabel('$P(\mathcal{{D}}|\\theta)$'.format(N_H))
plt.title('Experiment: Toss coins with different $\\theta$ {0:d}x; Each bin is\n' \
          ' result from 10k reps of experiment for given $\\theta$' \
          .format(N_T))
plt.xticks(np.arange(0,11,1)/10)


# Exact pdf
p_theta_given_D_exact = 12*(1-thetas)*thetas**2

# Experimental pdf
p_theta_given_D = P_D_given_theta/np.sum(P_D_given_theta*dtheta)
print('sum(p_theta_given_D)*dtheta = {0:.2f}'.format(dtheta*np.sum(p_theta_given_D)))

plt.figure(2)
plt.bar(thetas, p_theta_given_D, width=dtheta/2, color='k', alpha=0.5, align='center', label='Experiment')
plt.plot(thetas, p_theta_given_D_exact, 'k.', ms=2, label='Exact')
plt.xlabel('$\\theta$ of coin')
plt.ylabel('$p(\mathcal{{D}}|\\theta)$'.format(N_H))
plt.title('Experiment: Toss coins with different $\\theta$ {0:d}x; Each bin is\n' \
          ' result from 10k reps of experiment for given $\\theta$' \
          .format(N_T))
plt.xticks(np.arange(0,11,1)/10)
plt.legend()

plt.savefig('figures/HW8_1.svg', transparent=True)
plt.savefig('figures/HW8_1.png', transparent=True)

# 2.

# The exact area under the curve 12*(1-theta)*theta**2 is
# A = ((a + l)**3 - a**3)/3 - ((a+l)**4 - a**4)/4
# where a is left boundary and a + l is right boundary.

A = np.full((thetas.size, thetas.size - 1), np.nan)
A95 = np.full((thetas.size, thetas.size - 1), np.nan)
for i in range(thetas.size):          # a = dtheta, 2*dtheta, ..., 1
    a = thetas[i]
    for j in range(1, thetas.size-1): # l = dtheta, 2*dtheta, ..., 1
        l = thetas[j]
        if a + l >= 1.:
            continue
        A[i,j] = 12*(((a + l)**3 - a**3)/3 - ((a + l)**4 - a**4)/4)
        #print("a = {0:.3f}, l = {1:.3f}, A = {2:.3f}".format(a, l, A[i,j]))
        if np.abs(A[i,j] - 0.95) < 0.001:
            print("a = {0:.3f}, l = {1:.3f}, A = {2:.5f}, |A - 0.95| = {3:.5f}"\
                  .format(a, l, A[i,j], np.abs(A[i,j]-0.95)))

plt.figure(3)
plt.pcolor(thetas, thetas[1:], A.T)
cb = plt.colorbar()
plt.ylabel('l')
plt.xlabel('a')
cb.ax.set_title('Area')

# Final plot with credible interval
# TODO: Extract credible interval boundarys from A.
a = 0.19
b = a + 0.74

plt.figure(4)
plt.bar(thetas, p_theta_given_D, width=dtheta/2, color='k', alpha=0.5, align='center', label='Experiment')
plt.plot(thetas, p_theta_given_D_exact, 'k.', ms=2, label='Exact')
plt.plot([a,b], [0, 0], 'k-', linewidth=3, label='95% credible int. [{0:.2f},{1:.2f}]'.format(a, b))
plt.xlabel('$\\theta$ of coin')
plt.grid()
plt.ylim([0, 2.25])
plt.ylabel('$p(\mathcal{{D}}|\\theta)$'.format(N_H))
plt.title('Experiment: Toss coins with different $\\theta$ {0:d}x; Each experiment\n' \
          ' bin is result from 10k reps of experiment for given $\\theta$.\n' \
          '$\mathcal{{D}}=[H,H,T]$'
          .format(N_T))
plt.xticks(np.arange(0,11,1)/10)
plt.legend()

plt.savefig('figures/HW8_1.svg', transparent=True)
plt.savefig('figures/HW8_1.png', transparent=True)
