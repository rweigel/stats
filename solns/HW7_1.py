import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

N = 1000
n = 20

alpha = 1
beta  = 1
sigma = 0.2

idx_N = np.arange(0, N)
x = idx_N/N

def _savefig(letter):
  plt.savefig(f'HW7_1{letter}.png', dpi=300, bbox_inches='tight')
  plt.savefig(f'HW7_1{letter}.svg', transparent=True, bbox_inches='tight')

# 1
y = beta*x + alpha + np.random.normal(loc=0.0, scale=sigma, size=(N))

plt.plot(x, y, '.')
plt.title('$y=x + 1 + \\epsilon$; $\\epsilon \\sim \\mathcal{N}(0,0.2^2)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.xlim([0,1])

# Select 20 values from [0, 1, ..., N-1] with replacement.
idx_n = np.random.choice(idx_N, size=n, replace=True)

plt.plot(x[idx_n], y[idx_n], 'ko', ms=4)
plt.legend(['Population (N={0:d})'.format(N), 'Sample (n={0:d})'.format(n)])
_savefig('a')

def linear_regression(x, y, method='scipy'):

    if method == 'scipy':
      b, a, _, _, _ = stats.linregress(x,y)
      return a, b
    else:
      xbar = np.mean(x)
      ybar = np.mean(y)
      b = np.sum( (x-xbar)*(y-ybar) )/np.sum( (x-xbar)**2 )
      a = ybar-b*xbar

      return a, b

# 3. and 4.
print(len(np.unique(idx_n)))
a1, b1 = linear_regression(x[idx_n], y[idx_n])
print("Manual    : a = {0:.3f};   b = {1:.3f}".format(a1, b1))
a2, b2 = linear_regression(x[idx_n], y[idx_n], method='manual')
print("SciPy     : a = {0:.3f};   b = {1:.3f}".format(a2, b2))

print("Difference: a = {0:.1e}; b = {1:.1e}".format(a1-a2, b1-b2))

# 5.

B = 1000
a = np.full(B, np.nan)
b = np.full(B, np.nan)
a_boot = np.full(B, np.nan)
b_boot = np.full(B, np.nan)
for i in range(B):
    # Select 20 values from [0, 1, ..., n-1] with replacement.
    idx_n_boot = np.random.choice(idx_n, size=n, replace=True)
    a_boot[i], b_boot[i] = linear_regression(x[idx_n_boot], y[idx_n_boot])

    # Select 20 values from [0, 1, ..., N-1] with replacement.
    idx_n  = np.random.choice(idx_N, size=n, replace=True)
    a[i], b[i] = linear_regression(x[idx_n], y[idx_n])

abar = np.mean(a)
bbar = np.mean(b)
abar_boot = np.mean(a_boot)
bbar_boot = np.mean(b_boot)

s_a = np.std(a, ddof=1)
s_b = np.std(b, ddof=1)

s_a_boot = np.std(a_boot, ddof=1)
s_b_boot = np.std(b_boot, ddof=1)

a_ci_boot = np.percentile(a, [2.5, 97.5])
print('95% CI for a using non-parametric bootstrap: [{0:.2f}, {1:.2f}]'.format(a_ci_boot[0], a_ci_boot[1]))

b_ci_boot = np.percentile(b, [2.5, 97.5])
print('95% CI for b using non-parametric bootstrap: [{0:.2f}, {1:.2f}]'.format(b_ci_boot[0], b_ci_boot[1]))

bins = np.linspace(0.4, 1.6, 50)

# 6.
# Confidence intervals are given in many books and online resources. For
# example, https://en.wikipedia.org/wiki/Simple_linear_regression#Normality_assumption
# https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_Linear_Regression_Slope.pdf

xbar = np.mean(x[idx_n])
ybar = np.mean(y[idx_n])
yhat = a1 + b1*x[idx_n]
s_betahat = np.sqrt( (1/(n-2))*np.sum( (y[idx_n] - yhat)**2 )/np.sum( (x[idx_n]-xbar)**2 ) )
t = stats.t.ppf(0.975, n-2)
b_ci = [b1-t*s_betahat, b1+t*s_betahat]
print('95% CI for b using t distribution:           [{0:.2f}, {1:.2f}]'.format(b_ci[0], b_ci[1]))

plt.figure()
plt.grid()
plt.hist(a, density=True, bins=bins, color='k')
title = '$\\overline{{a}}$={0:.2f}; Bootstrap 95% CI: [{1:.2f}, {2:.2f}]'.format(abar,a_ci_boot[0], a_ci_boot[1])
plt.title(title)
plt.xlabel('$a$')
plt.ylabel('pdf($a$)')
_savefig('b')

plt.figure()
plt.grid()
title = f'$\\overline{{b}}$={bbar:.2f}\nBootstrap 95% CI: [{b_ci_boot[0]:.2f}, {b_ci_boot[1]:.2f}]'
title = title +  f'\nt-dist 95% CI: [{b_ci[0]:.2f}, {b_ci[1]:.2f}]'
plt.title(title)
plt.hist(b, density=True, bins=bins, color='k')
plt.xlabel('$b$')
plt.ylabel('pdf($b$)')
_savefig('c')

# Check of 6. Compute B CIs and see how often they trap beta.
cnt = 0
for i in range(B):
    idx_n  = np.random.choice(idx_N, size=n, replace=True)
    ao, bo = linear_regression(x[idx_n], y[idx_n])
    xbar = np.mean(x[idx_n])
    ybar = np.mean(y[idx_n])
    yhat = ao + bo*x[idx_n]
    s_betahat = np.sqrt( (1/(n-2))*np.sum( (y[idx_n] - yhat)**2 )/np.sum( (x[idx_n]-xbar)**2 ) )
    t = stats.t.ppf(0.975, n-2)

    b_ci = [bo-t*s_betahat, bo+t*s_betahat]
    if b_ci[0] < beta and b_ci[1] > beta:
        cnt = cnt + 1
print("Fraction of t-distribution CIs for b that trap beta: {0:.3f}".format(cnt/B))

# Check of 8.
cc, p = stats.pearsonr(a-1, b-1)
plt.figure()
plt.plot(a-1, b-1, 'k.')
plt.grid()
plt.xlabel('$a-\\alpha$')
plt.ylabel('$b-\\beta$')
#plt.gca().set_aspect('equal')
plt.title('cc = {0:.2f}; Reject hyp. that cc = 0\n with significance level of p = {1:.1g}'.format(cc,p))
_savefig('d')

bins = np.arange(-0.7, 0.75, 0.05)
idx_p = a-alpha > 0
idx_n = a-alpha < 0

plt.figure()
plt.hist(b[idx_p]-beta, bins=bins, alpha=0.5, density=True)
plt.hist(b[idx_n]-beta, bins=bins, alpha=0.5, density=True)
plt.legend(['pdf($b-\\beta$) for $a>0$', 'pdf($b-\\beta$) for $a<0$'])
plt.grid()

t, p = stats.ttest_ind(b[idx_p]-beta, b[idx_n]-beta)

plt.title('Reject hyp. that means are same\nwith significance level p = {0:.1e}'.format(p))

_savefig('e')

