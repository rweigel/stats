import numpy as np
from matplotlib import pyplot as plt

m = 2
N = 10000
n = 10
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
xo = [-0.546, -0.406, -0.115, -1.262, -1.386, -0.448,  0.829,  0.799, -1.100, 0.385]
print(np.mean(xo)) # -0.325 (much different than mu)

# The measurements I should have given ...
xo = [ 3.03399726, -0.41833714, -0.34603477,  0.84167495,  1.46829221,
       0.79846543,  1.11989497,  1.55009339,  1.54485525,  1.26485924]
print(np.mean(xo))

# Alternative set of n measurements
#xo = np.random.normal(loc=mu, scale=sigma, size=(n))
#print(np.mean(xo)) # will vary

# Create n x N matrix where each column contains
# n random samples from xo with replacement
xstar = np.empty((n,N))
for b in range(N):
    xstar[:,b] = np.random.choice(xo, size=n, replace=True)

# Square each element of xstar
Xstar = np.power(xstar, m)

# Sum over rows.
Ystar = np.sum(Xstar, axis=0)

plt.figure()
bin_edges = np.linspace(np.min([np.min(Y),np.min(Ystar)]),np.max([np.max(Y),np.max(Ystar)]),100)
plt.hist(Y,density=True, bins=bin_edges)
plt.hist(Ystar,density=True, bins=bin_edges, alpha=0.5)
plt.title('N=%d; n=%d; $\overline{Y} = $ = %.1f; $\overline{Y^*}$ = %.1f' % (N,n,np.mean(Y), np.mean(Ystar)))
plt.legend(['$Y$','$Y^*$'])
plt.ylabel('PDF')
plt.xlabel('$Y$ or $Y^*$')

# Will discuss this mess of a plot in class.
plt.figure()
pdf, _ = np.histogram(Y, bins=bin_edges, density=True)
pdf_star, _ = np.histogram(Ystar, bins=bin_edges, density=True)
plt.plot(pdf, pdf_star, '.')