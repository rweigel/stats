import random

N = 100001
a = [0, 1]

#import numpy as np
#print(np.random.choice([0, 1], 5))

#a = np.random.choice([0, 1], 5)
#rf = np.sum(a)/5
#print(a)
#print(rf)
#exit()
# Experiment: Randomly select an element from the list 'a'
result = random.choice(a)

# Repeat the experiment n times
rfs = []
ns = []
for n in range(1, N):
  results = []
  for exp in range(1, n+1):
    result = random.choice(a)
    results.append(result)
  rf = sum(results) / n
  rfs.append(rf)
  ns.append(n)
  if n < 10:
    print(n)
    print(results)

# Plot relative frequency vs. n
from matplotlib import pyplot as plt
plt.plot(ns, rfs, marker='.', linestyle='-', color='blue')
plt.grid()
plt.xlabel('n')
plt.ylabel('Relative Frequency')
plt.show()
