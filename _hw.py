
S = set(range(1, 101))
V = set(range(1, 51))
M = set(range(26, 66))
X = set(range(67, 101))

notV = S - V
notM = S - M

print(len(V.union(M))/100)
print(len(notV & notM)/100)
notM = S - M
print(len(V & notM)/100)
exit()

import random

a = [0, 1]

# Experiment: Randomly select an element from the list a
result = random.choice(a)

# Repeat the experiment n times
n = 2
results = []
for exp in range(1, n+1):
  result = random.choice(a)
  results.append(result)

print(f"n = {n} experiments:")
print(f"  Results: {results}")
print(f"  rf(0) = {results.count(0) / n}")
print(f"  rf(1) = {results.count(1) / n}")

import numpy as np
P_H = np.full(1000, np.nan)
for n in range(1, 1001):
  result = np.random.choice([0, 1], n)
  print(f"n = {n} experiments. P_H = {sum(result) / n}")
  P_H[n-1] = sum(result) / n

# Generalize to compute relative frequency as a function of n
rel_freqs = []
N = []
for n in range(1, 1001):
#for n in [1, 10, 100, 1000, 10000]:
  results = []
  for exp in range(1, n+1):
    result = random.choice(a)
    results.append(result)

  if n < 10:
    print(f"n = {n} experiments:")
    print(f"  Results: {results}")
    print(f"  rf(0) = {results.count(0) / n}")
    print(f"  rf(1) = {results.count(1) / n}")

  p_H = sum(results) / n
  N.append(n)
  rel_freqs.append(p_H)

from matplotlib import pyplot as plt
#plt.plot(N, rel_freqs, marker='.', linestyle='-', color='blue')
plt.plot(N, P_H, marker='.', linestyle='-', color='black')
#plt.plot(N, rel_freqs, linestyle='-', color='blue')
plt.axhline(0.5, color='red', linestyle='--')
plt.grid()
plt.xlabel('Number of Experiments')
plt.ylabel('Relative Frequency of Heads')
plt.show()
