import numpy as np
import scipy.stats

x = np.array([-1.22, -1.17, 0.93, -0.58, -1.14])
y = np.array([1.03, -1.59, -0.41, 0.71, 2.10])

xbar = np.mean(x)
ybar = np.mean(y)

print('mean(x): {0:.4f}'.format(xbar))
print('mean(y): {0:.4f}'.format(ybar))
print('mean(y)-mean(x): {0:.4f}'.format(np.mean(y)-np.mean(x)))

S_x = np.std(x, ddof=1)
S_y = np.std(y, ddof=1)
# https://en.wikipedia.org/wiki/Student%27s_t-test#Independent_two-sample_t-test
S_xy = np.sqrt( (S_x**2)/5 + (S_y**2/5) )

S_p = np.sqrt( (S_x**2)/2 + (S_y**2)/2 )

S_xy_pooled = np.sqrt( (S_p**2)/5 + (S_p**2/5) )

print('S_x:         {0:.8f}'.format(S_x))
print('S_y:         {0:.8f}'.format(S_y))
print('S_xy:        {0:.8f}'.format(S_xy))
print('S_p:         {0:.8f}'.format(S_p))
print('S_xy pooled: {0:.8f}'.format(S_xy_pooled))


T = (ybar-xbar)/(S_xy)

print('T:           {0:.4f}'.format(T))

T_pooled = (ybar-xbar)/(S_xy_pooled)
print('T pooled:    {0:.4f}'.format(T_pooled))

print('')

a = S_x**2/5
b = S_y**2/5
nu = 4*(a + b)**2/(a**2 + b**2)
print('nu = {0:.2f}'.format(nu))
nu = np.floor(nu)
print('floor(nu) = {0:.2f}'.format(nu))

# The t-distribution is approximate, so this is not expected to match
# the output of SciPy, which uses the exact distribution.
f = scipy.stats.t.cdf(-T, 6)
print('2*(Integral of t_6 from -infty to -T):        {0:.4f}'.format(2*f))

# The t-distribution is exact, so this should match 2*p from SciPy.
f_pooled = scipy.stats.t.cdf(-T_pooled, 8)
print('2*(Integral of t_8 from -infty to -T_pooled): {0:.4f}'.format(2*f_pooled))

t, p = scipy.stats.ttest_ind(x, y, equal_var=False)

print('t:         {0:.4f}'.format(t))
print('p:         {0:.4f}'.format(p))

t_pooled, p_pooled = scipy.stats.ttest_ind(x, y, equal_var=True)
print('t pooled:  {0:.4f}'.format(t_pooled))
print('p pooled:  {0:.4f}'.format(p_pooled))
