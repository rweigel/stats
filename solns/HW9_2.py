from numpy import linspace
from lib.savefig import savefig

# 4.
b = 0.95
a = 0.1

A = 1/2310 # Integral of θ^4*(1-θ)^6 from 0 to 1
def posterior_area(a, b):
  # Integrate θ**4*(1 - θ)**6) numerically over [a, b] and normalize by A
  from scipy.integrate import quad
  integral, _ = quad(lambda θ: θ**4*(1 - θ)**6, a, b)
  return integral/A

# Find exact integral of 
# Plot the posterior
def plot_posterior(num_points=100):
  import matplotlib.pyplot as plt
  θ_values = linspace(0, 1, num_points)
  posterior_values = [(θ**4*(1 - θ)**6)/A for θ in θ_values]
  plt.plot(θ_values, posterior_values)
  plt.xlabel('θ')
  plt.ylabel('P(θ|𝒟)')
  savefig('HW9_2')

plot_posterior()

α = 0.01
for a in linspace(0, 1, 1000):
  area_lower = posterior_area(0, a)
  print(f'a = {a:7.4f}, sum = {area_lower:7.4f}')
  if area_lower > α/2:
    break

for b in linspace(0, 1, 1000):
  area_upper = posterior_area(b, 1)
  if area_upper < α/2:
    print(f'b = {b:7.4f}, sum = {area_upper:7.4f}')
    break

"""
a =  0.1151, sum =  0.0051
b =  0.7678, sum =  0.0049
"""