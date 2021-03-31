import numpy as np
A = np.array([11,12,13])
x = A[[0,1]] # x is new array
y = A[0:2]   # y is reference to elements 0 and 1 of x

x[0] = 99
print(A)
y[0] = 99
print(A)
