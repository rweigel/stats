import numpy as np
from matplotlib import pyplot as plt

N = 1000
n = 20

alpha = 1
beta  = 1
sigma = 0.2

I = np.arange(0, N)
x = I/N

y = beta*x + alpha + np.random.normal(loc=0.0, scale=sigma, size=(N))

plt.plot(x, y, '.')
plt.title('$y=x + 1 + \\epsilon$; $\\epsilon \sim \\mathcal{N}(0,0.2)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
#plt.gca().set_aspect(1)
plt.xlim([0,1])

# Select 20 values from [0, 1, ..., N-1] with replacement.
I20 = np.random.choice(I, size=n, replace=True)

plt.plot(x[I20], y[I20], 'r.', ms=4)
plt.legend(['Population (N={0:d})'.format(N), 'Sample (n={0:d})'.format(n)])

from scipy import stats

def linear_regression(x,y,method='scipy'):

    #np.polyfit(x,y,1)
    if method == 'scipy':
      b, a, _, _, _ = stats.linregress(x,y)
      return a, b
    else:
      # At some point in your academic career, you used the following
      # formulas, most likely in at least a physics lab.
      # https://www4.stat.ncsu.edu/~dickey/summer_institute/formulas
      xbar = np.mean(x)
      ybar = np.mean(y)
      b = np.sum( (x-xbar)*(y-ybar) )/np.sum( (x-xbar)**2 )
      a = ybar-b*xbar

      return a, b

print(len(np.unique(I20)))
a, b = linear_regression(x[I20], y[I20])
print(a, b)
a, b = linear_regression(x[I20], y[I20], method='manual')
print(a, b)

B = 10000
a = np.full(B, np.nan)
b = np.full(B, np.nan)
for i in range(B):
    # Select 20 values from [0, 1, ..., N-1] with replacement.
    I20 = np.random.choice(I, size=n, replace=True)
    a[i], b[i] = linear_regression(x[I20], y[I20])

abar = np.mean(a)
bbar = np.mean(b)
s_a = np.std(a, ddof=1)
s_b = np.std(b, ddof=1)

bins = np.linspace(0.4, 1.6, 50)

plt.figure()
plt.grid()
plt.hist(a, density=True, bins=bins)
#plt.hist(a, density=True)
plt.title('$\overline{{a}}={0:.2f}; s_{{\overline{{a}}}}={1:.2f}$'.format(abar,s_a))
plt.xlabel('a')
plt.ylabel('pdf(a)')
plt.legend(['Parametric bootstrap samp. dist.'])

plt.figure()
plt.grid()
plt.title('$\overline{{b}}={0:.2f}; s_{{\overline{{b}}}}={1:.2f}$'.format(bbar,s_b))
plt.hist(b, density=True, bins=bins)
#plt.hist(b, density=True)
plt.xlabel('b')
plt.ylabel('pdf(b)')

# Confidence intervals are given in many books and online resources. For
# example, https://en.wikipedia.org/wiki/Simple_linear_regression#Normality_assumption
# https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_Linear_Regression_Slope.pdf

x = x[I20]
y = y[I20]
xbar = np.mean(x)
ybar = np.mean(y)
yhat = alpha + beta*x
s_betahat = np.sqrt( (1/(n-2))*np.sum( (y - yhat)**2 )/np.sum( (x-xbar)**2 ) )
print(s_betahat)

t = stats.t.ppf(0.975, n-2)
print(t)
b_ci = [bbar-t*s_betahat, bbar+t*s_betahat]
print('CI using t distribution')
print(b_ci)

plt.figure()
plt.plot(a-1, b-1, '.')

print(stats.pearsonr(a-alpha, b-beta))

idx = a-alpha > 0
print(np.mean(b[idx]-beta))
plt.figure()
plt.hist(b[idx]-beta)

b.sort()
b_ci_boot = [b[250-1], b[10000-250-1]]
print('CI using non-parametric bootstrap')
print(b_ci_boot)
