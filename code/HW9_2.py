import numpy as np
import scipy

x = np.array([-1.22, -1.17, 0.93, -0.58, -1.14])
y = np.array([1.03, -1.59, -0.41, 0.71, 2.10])

print(np.mean(y)-np.mean(x))

sigma_x = np.std(x,ddof=1)
sigma_y = np.std(y,ddof=1)
sigma_xy_pooled = np.sqrt(sigma_x**2 + sigma_y**2)/np.sqrt(2)
print(sigma_xy_pooled)

t = (np.mean(y)-np.mean(x))/(sigma_xy_pooled*np.sqrt(2/5))
print(t)

a = sigma_x**2/5
b = sigma_y**2/5
nu = 4*(a + b)**2/(a**2 + b**2)
print(np.floor(nu))

f = scipy.stats.t.cdf(-t, 6)
print(f)


t, p = scipy.stats.ttest_ind(x, y, equal_var=False)

print(t)
print(p)

print(t*np.sqrt(a + b))