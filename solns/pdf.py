import numpy as np
from scipy.stats import chi2, norm
from matplotlib import pyplot as plt

n = 10
x = np.linspace(0, 20, 1000)
chi2 = chi2.pdf(x*(n-1), df=n-1)
plt.plot(x, chi2, label=f'$\chi^2_{{{n-1}}}$')
plt.legend()
plt.grid()
plt.savefig('pdf.png', dpi=300)