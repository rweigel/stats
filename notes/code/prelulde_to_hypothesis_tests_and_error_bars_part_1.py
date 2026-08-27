"""
The following program draws draws 10 random numbers to form list x and 10
random number to form list y and plots the results. Ordinary least squares
regression is used to find the line of best fit. 
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate random data on interval [0, 1]
x = np.random.rand(10)
print(x)
y = np.random.rand(10)
print(y)

# Perform ordinary least squares regression
# We'll cover this later in the semester.
# Solve y = Ax + b for the best fit line parameters m and c
A = np.vstack([x, np.ones(len(x))]).T
print(A)

fit = np.linalg.lstsq(A, y, rcond=None)
print(fit)

m, c = fit[0]

plt.scatter(x, y, label='Data points')
plt.plot(x, m*x + c, 'r', label='Best fit line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
