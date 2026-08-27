"""
The following program draws draws 10 random numbers to form list x and 10
random number to form list y and plots the results. Ordinary least squares
regression is used to find the line of best fit.
"""

import numpy as np
import matplotlib.pyplot as plt

n = 0
m_thresh = 0.5
n_e = 1000
for experiment in range(n_e):
  # Generate random data on interval [0, 1]
  x = np.random.rand(10)
  y = np.random.rand(10)

  # Perform ordinary least squares regression
  # We'll cover this later in the semester.
  # Solve y = Ax + b for the best fit line parameters m and c
  A = np.vstack([x, np.ones(len(x))]).T
  fit = np.linalg.lstsq(A, y, rcond=None)
  m, c = fit[0]
  print(f'm = {m: 4.2f}, c = {c: 4.2f}')
  if m > m_thresh:
    n = n+1
  # Compute Pearson correlation coefficient
  r = np.corrcoef(x, y)[0, 1]
  print(f'Pearson correlation coefficient squared: {r**2: 4.2f}')

print(f'Number of experiments with m > {m_thresh}: {n} of {n_e}')
print(f'Fraction of experiments with m > {m_thresh}: {n/n_e: 4.2f}')

if False:
  plt.scatter(x, y, label='Data points')
  plt.plot(x, m*x + c, 'r', label='Best fit line')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.show()
