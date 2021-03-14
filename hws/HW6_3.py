import numpy as np
from matplotlib import pyplot as plt

alpha = 0.05

xo = np.asarray([-0.54603241, -0.40652794, -0.11570264, -1.26244673, -1.38616981,
                -0.44812319,  0.82880132,  0.79937713, -1.098357,  0.38530288])
xo_mean = np.mean(xo)

B = 10000

# Create bootstrap sampling distribution
X_star = np.nan*np.empty(B)
for i in range(B):
    x_star = np.random.choice(xo, size=xo.size, replace=True)
    X_star[i] = np.mean(x_star)

bins = np.linspace(-1.5, 1.5, 30)
N_star, bins = np.histogram(X_star, bins=bins)

# Find CI values
X_star_sorted = np.sort(X_star)
idx_lower = - 1 + np.int(np.round(B*alpha/2))    # location nearest 2.5 percentile
idx_upper = -1 + np.int(B - np.round(B*alpha/2)) # location nearest 97.5 percentile
ci = [X_star_sorted[idx_lower], X_star_sorted[idx_upper]]

plt.plot([ci[0],ci[0]], [0, 0.2], 'k:')
plt.plot([xo_mean,xo_mean], [0, 0.2], 'k')
plt.fill_between(bins[0:-1], N_star/B, color='k', alpha=0.5, step='mid')

l1 = '95%% CI = [%.2f, %.2f]' % (ci[0], ci[1])
l2 = '$\hat{\mu} = %.2f$' % xo_mean
plt.legend([l1, l2, 'Bootstrap sampling dist.'])
plt.plot([ci[1],ci[1]], [0, 0.2], 'k:')

plt.ylabel('$P(\overline{X}^*)$')
plt.xlabel('$\overline{X}^*$')
plt.grid()
plt.xlim([-1.5, 1.5])
plt.ylim([0, 0.2])
