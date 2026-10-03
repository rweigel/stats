import math
import numpy as np
from matplotlib import pyplot as plt
from lib.savefig import savefig
from lib.pdf import pdf

ns = 10
ne = 10000
sigma = 1

# Each column is an experiment
exps = np.random.normal(0, 1, size=(ns, ne))

# Sample variances, s2, for each experiment
s2s = np.var(exps, axis=0, ddof=1)

s2s_scaled = (ns-1)*s2s/sigma**2

e_pdf, bin_centers, bin_edges = pdf(s2s_scaled, 1)

n = ns - 1
ch2_pdf = (bin_centers**(n/2-1) * np.exp(-bin_centers/2)) / (2**(n/2) * math.gamma(n/2))

width = (bin_edges[1]-bin_edges[0])*0.94
plt.bar(bin_centers, e_pdf, color='black', width=width, zorder=1)
plt.plot(bin_centers, ch2_pdf, '.', zorder=10)
plt.xlabel(r"$(n-1)S^2/\sigma^2$")
plt.ylabel("Probability Density")
plt.legend([r"$\chi^2$ Exact", r"Simulated"])
plt.gca().set_axisbelow(True)
plt.grid(True)

savefig("HW4_2_2")