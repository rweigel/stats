import numpy as np

x = np.nan*np.ones(1000)
x = np.nan*np.empty(1000)


x = np.full((1000, 2), np.nan)

#x = np.nan*np.empty(10)
x = np.zeros(10)

x[0:9] = 1

s = 0
for i in range(len(x)):
    s = x[i] + s

print(s)