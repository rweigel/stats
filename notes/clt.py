from matplotlib import pyplot as plt
import numpy as np

m = 1e3-1
m1 = m + 1
m2 = 1
values = [m1, m2] # Particle masses
p1 = 1/m
p2 = 1 - p1
pmf = [p1, p2]

exp = 4
n = 10**exp
ne = 1000

# Generate sampling distribution of 
x = np.random.choice(values, size=(n, ne), p=pmf)

x_bar = np.mean(x, axis=0) # Sample mean for each experiment

plt.hist(x_bar, bins=20, color='black', edgecolor='w', linewidth=0.5, density=True)
title = f'$m_1$ = {m1}, $m_2$ = {m2}'
title += '; $p_1 = 1/(m_1 + m_2)$, $p_2 = 1 - p_1$'
title += f'\nExperient: Draw $n=10^{exp}$ values from pmf = [p1, p2] and compute $\\overline{{x}}$'
plt.title(title, fontsize=11)
plt.grid()
plt.xlabel('$\\overline{x}$')
plt.ylabel(f'PDF from $n_e={ne}$ experiments')
plt.savefig(f'clt.{exp}.png', dpi=300, bbox_inches='tight')
