import numpy as np

n_experiments = 10000
results = np.full(n_experiments, np.nan)
for i in range(1, n_experiments + 1):
  result = np.random.choice([-1, 1], 3)
  results[i-1] = sum(result)

P_1 = np.sum(results == 1)/n_experiments

print(f"From {n_experiments} experiments:")
for s in range(-3, 4):
  print(f"  P(sum = {s:2d}) = {np.sum(results == s)/n_experiments}")
