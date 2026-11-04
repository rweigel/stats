import numpy as np
import scipy.stats


def scatter(x, y, r, P):
  from lib.savefig import savefig
  import matplotlib.pyplot as plt
  plt.scatter(x, y)
  plt.title(f"r = {r:.2f} | For $H_0$: $\\rho = 0.5$; $H_a$: $\\rho > 0.5$, P={P:.3f}")
  plt.grid(True)
  plt.xlabel("cube strength (MPa)")
  plt.ylabel("cylinder strength (MPa)")
  savefig("HW6_2")

x = [55.10, 44.83, 46.32, 51.10, 49.89, 45.20, 48.18, 46.70, 54.31, 41.50, 47.50, 52.00, 52.25, 50.86, 51.66, 54.77, 57.06, 57.84, 55.22]
y = [49.10, 31.20, 32.80, 42.60, 42.50, 32.70, 36.21, 40.40, 37.42, 30.80, 35.34, 44.80, 41.75, 39.35, 
44.07, 43.40, 45.30, 39.08, 41.89]

n = len(x)
xbar = np.mean(x)
ybar = np.mean(y) 
Sxx = np.sum((x - xbar)**2)
Syy = np.sum((y - ybar)**2)
Syx = np.sum((y - ybar) * (x - xbar))
r = Syx / np.sqrt(Sxx * Syy)
v = 0.5*np.log((1 + r) / (1 - r))
vo = 0.5*np.log((1 + 0.5) / (1 - 0.5))

z = (v - vo) / np.sqrt(1/(n - 3))
P = (1 - scipy.stats.norm.cdf(np.abs(z)))

print(f"Sxx = {Sxx:.3f}")
print(f"Syy = {Syy:.3f}")
print(f"Syx = {Syx:.3f}")
print(f"r = {r:.3f}")
print(f"z = {z:.3f}")
print(f"P = {P:.3f}")
scatter(x, y, r, P)

"""
Sxx = 367.740
Syy = 488.542
Syx = 322.368
r = 0.761
z = 1.793
P = 0.036
"""