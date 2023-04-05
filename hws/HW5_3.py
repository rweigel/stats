import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

n = 10
mu = 10
sigma = 1
B = 10000
alpha = 0.05

xo = np.random.normal(loc=mu, scale=sigma, size=(n))

xo_mean = np.mean(xo)

n = np.size(xo)
s = np.std(xo, ddof=1)

# Part 1.

# Devore 7.4
w1 = 1.96*sigma/np.sqrt(n) # width of error bar for part 1.

print('95% CI: Eqn 7.4: [{0:.2f}, {1:.2f}]'.format(xo_mean - w1, xo_mean + w1))

# Part 2.

# Devore 7.15
# From the n = 9 row and 0.975 column at
# https://stats.stackexchange.com/questions/122768/statistic-t-test-t-table
# t = 2.262. (In this table, "n" is used for degrees of freedom instead of
# the more conventional "\nu".)
t = 2.262 # Note larger than 1.96, as expected.

# Alternative approach, more accurate t value:
t = stats.t.ppf(0.975, n-1) # 2.2621571627409915

w2 = t*s/np.sqrt(n) # width of error bar for part 2.

print('95% CI: Eqn 7.15: [{0:.2f}, {1:.2f}]'.format(xo_mean - w2, xo_mean + w2))

# Part 3

x = np.random.normal(loc=mu, scale=sigma, size=(B, n))
xbars = np.mean(x, axis=1)
w1s = 1.96*sigma/np.sqrt(n) # widths of error bar for part 1.
ci1s_lower = xbars - w1s
ci1s_upper = xbars + w1s


idx1 = np.where(np.logical_and(mu > ci1s_lower, mu < ci1s_upper), 1, 0)
f1 = np.sum(idx1)/B

bins = np.linspace(8.5,11.5,50)

plt.figure()
plt.hist(xbars, color='k', alpha=0.5, bins=bins, density=True)
plt.xlabel('$\overline{X}$')
plt.ylabel('$pdf(\overline{X})$')
title = '{0:.1f}% of time $\mu$ in CI range given by eqn. 7.4:\n'
title += '$[\overline{{X}}-z_{{.025}}\sigma/\sqrt{{n}},\overline{{X}}+z_{{.025}}\sigma/\sqrt{{n}}]$'
title = title.format(100*f1)
plt.title(title)
plt.legend(['Parametric bootstrap pdf'])

plt.savefig('figures/HW5_3_3.svg', transparent=True)
plt.savefig('figures/HW5_3_3.png', transparent=True)

# Part 4

ss = np.std(x, axis=1, ddof=1)
w2s = t*ss/np.sqrt(n) # width of error bar for part 1.
ci2s_lower = xbars - w2s
ci2s_upper = xbars + w2s

idx2 = np.where(np.logical_and(mu > ci2s_lower, mu < ci2s_upper), 1, 0)
f2 = np.sum(idx2)/B
title = '{0:.1f}% of time $\mu$ in CI range given by eqn. 7.15:\n'
title += '$[\overline{{X}}-t_{{.025, 9}}s/\sqrt{{n}},\overline{{X}}+t_{{.025, 9}}s/\sqrt{{n}}]$'
title = title.format(100*f2)

plt.figure()
plt.hist(xbars, color='k', alpha=0.5, bins=bins, density=True)
plt.xlabel('$\overline{X}$')
plt.ylabel('$pdf(\overline{X})$')
plt.title(title)
plt.legend(['Parametric bootstrap pdf'])
plt.savefig('figures/HW5_3_4.svg', transparent=True)
plt.savefig('figures/HW5_3_4.png', transparent=True)

# Extra plots to explain results

plt.figure()
plt.plot([w1s,w1s], [0, 2.5], 'k', label='Equation 7.4')
plt.plot([np.median(w2s),np.median(w2s)], [0, 2.5], 'r', label='Equation 7.15 median')
plt.hist(w2s, bins=np.linspace(0,1.5,50), color='k', alpha=0.5, density=True, label='Equation 7.15')
plt.ylim([0, 2.5])
plt.ylabel('pdf')
plt.xlabel('CI width')
plt.legend()
plt.savefig('figures/HW5_3_x.svg', transparent=True)
plt.savefig('figures/HW5_3_x.png', transparent=True)


plt.figure()
idx2x = np.where(np.logical_or(mu < ci2s_lower, mu > ci2s_upper), 1, 0)
idx2x = np.asarray(np.logical_or(mu < ci2s_lower, mu > ci2s_upper)).nonzero()[0]
idx1x = np.asarray(np.logical_or(mu < ci1s_lower, mu > ci1s_upper)).nonzero()[0]
w1s = np.ones(B)*1.96*sigma/np.sqrt(n)
plt.plot(xbars-mu, w1s,'m.',label='Equation 7.4', zorder=3)
plt.plot(xbars[idx1x]-mu, w1s[idx1x],'y.',ms=2,  zorder=4, label='Equation 7.4 gives $\mu$ outside CI')
plt.plot(xbars-mu, w2s, '.', color=[1,0,0,0.5], label='Equation 7.15', zorder=1)
plt.plot(xbars[idx2x]-mu, w2s[idx2x], 'k.',ms=2, zorder=1, label='Equation 7.15 gives $\mu$ outside CI')
plt.xlabel('$\overline{X}-\mu$')
plt.ylabel('CI width')
plt.legend(loc='upper left')
plt.savefig('figures/HW5_3_y.svg', transparent=True)
plt.savefig('figures/HW5_3_y.png', transparent=True)

#print(stats.pearsonr(w2s, xbars-mu))
