from scipy.stats import linregress
import numpy as np

x1 = np.array([1, 2.1, 3.0, 4.1])  # time
x2 = np.array([1, 2, 3, 4])        # image number
y = np.array([0.0, 0.1, 0.2, 0.3]) # position

def fit(x1, x2, y):

  res = linregress(x1, y)
  print(f"  y = b0 + b1*x1\n    b0 = {res.intercept:>10.4f}\n    b1 = {res.slope:>10.4f}")

  res = linregress(x2, y)
  print(f"  y = b0 + b1*x2\n    b0 = {res.intercept:>10.4f}\n    b1 = {res.slope:>10.4f}")

  # Now do 2-D regression
  design = np.column_stack((np.ones(len(y)), x1, x2))
  coefficients, residuals, rank, singular_values = np.linalg.lstsq(design, y, rcond=None)
  intercept, slope1, slope2 = coefficients
  print(f"  y = b0 + b1*x1 + b2*x2\n    b0 = {intercept:>10.4f}\n    b1 = {slope1:>10.4f}\n    b2 = {slope2:>10.4f}")

# First example
print("First example:")
fit(x1, x2, y)  # First example

print("Second example:")
y = y + 0.1*np.random.normal(size=len(y))
fit(x1, x2, y)  # Second example
