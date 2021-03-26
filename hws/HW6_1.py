import numpy as np
from matplotlib import pyplot as plt

m = 2
N = 10000 # Number of bootstrap samples
n = 10    # Number of measurements per sample
mu = 1
sigma = 1

x = np.random.normal(loc=mu, scale=sigma, size=(n,N))
# x is an n row by N column matrix

# Square each element of x
X = np.power(x, m)

# Sum over rows. Resulting array has N elements,
# each of which is the sum of the square of 10 values.
Y = np.sum(X, axis=0)

# Given measurements
xo = [-0.546, -0.406, -0.115, -1.262, -1.386, -0.448,
       0.829,  0.799, -1.100,  0.385]
#print(np.mean(xo)) # -0.325 (much different than mu)

# The measurements I should have given in problem statement
xo = [ 3.03399726, -0.41833714, -0.34603477,  0.84167495,  1.46829221,
       0.79846543,  1.11989497,  1.55009339,  1.54485525,  1.26485924]
#print(np.mean(xo)) # 1.09
Y_o = np.sum(np.power(xo, m))

# Alternative set of n measurements for experimentation.
if False:
    xo = np.random.normal(loc=mu, scale=sigma, size=(n))
    print(np.mean(xo))  # will vary
    Y_o = np.sum(np.power(xo, m))
    print(np.mean(Y_o)) # will vary

# Create n x N matrix where each column contains
# n random samples from xo with replacement
xstar = np.empty((n,N))
for b in range(N):
    xstar[:,b] = np.random.choice(xo, size=n, replace=True)

# Square each element of xstar
Xstar = np.power(xstar, m)

# Sum over rows.
Ystar = np.sum(Xstar, axis=0)

bin_edges = np.linspace(np.min([np.min(Y), np.min(Ystar)]),
                        np.max([np.max(Y), np.max(Ystar)]), 100)

pdf, _ = np.histogram(Y, bins=bin_edges, density=True)
pdf_star, _ = np.histogram(Ystar, bins=bin_edges, density=True)

plt.figure()
plt.plot([Y_o, Y_o], [0.0, 0.07],'-')
plt.step(bin_edges[0:-1], pdf, where='pre')
plt.step(bin_edges[0:-1], pdf_star, where='pre')
plt.title('N=%d; n=%d; $Y_o$ = %.1f; $\overline{Y} = $ = %.1f; $\overline{Y^*}$ = %.1f' % (N, n, Y_o, np.mean(Y), np.mean(Ystar)))
plt.legend(['$Y_o$ ($Y$ from $n$ measurements)','$Y$ (parametric bootstrap)','$Y^*$ (non-parametric bootstrap)'])
plt.ylabel('pdf')
plt.xlabel('$Y_o$, $Y$, or $Y^*$')
plt.ylim([0, 0.07])
plt.savefig('figures/HW6_1a.svg', transparent=True)
plt.savefig('figures/HW6_1a.png', transparent=True)

# Will discuss this plot in class.
plt.figure()
plt.plot(pdf, pdf_star, '.')
plt.grid()
plt.xlabel('pdf$(Y)$')
plt.ylabel('pdf$(Y^*)$')
plt.title('non-parametric bootstrap vs parametric bootstrap pdf')
plt.savefig('figures/HW6_1b.svg', transparent=True)
plt.savefig('figures/HW6_1b.png', transparent=True)
