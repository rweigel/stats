
slow_method = False

if slow_method:
  import random

  print("Slow method")
  n_max = 1000
  rel_freqs = []
  N = []
  for n in range(1, n_max + 1):
  #for n in [1, 10, 100, 1000, 10000]:
    results = []
    for exp in range(1, n+1):
      result = random.choice([0, 1])
      results.append(result)

    N.append(n)
    rel_freqs.append(sum(results) / n)

    if n < 10:
      print(f"n = {n} experiments. P_H = {results.count(1) / n}")
    if n == 10:
      print("...")

if not slow_method:
  import numpy as np

  print("Fast method")
  n_max = 1000000
  rel_freqs = np.full(n_max, np.nan) # Create an array of n_max elements, all NaN
  N = np.arange(1, n_max + 1)
  for n in N:
    result = np.random.choice([0, 1], n)
    rel_freqs[n-1] = sum(result) / n

    if n < 10:
      print(f"n = {n} experiments. P_H = {sum(result) / n}")
    if n == 10:
      print("...")

from matplotlib import pyplot as plt
if n < 1000:
  plt.plot(N, rel_freqs, marker='.', linestyle='None', color='black')
else:
  plt.semilogx(N, rel_freqs, marker='.', linestyle='None', color='black')
plt.grid()
plt.axhline(0.5, color='red', linestyle='--')
plt.title("Experiment: Select from $[0, 1]$ with relacement")
plt.xlabel('Number Experiments')
plt.ylabel('Relative Frequency of $1$')
#plt.show()
print("Writing HW1_1.png")
plt.savefig('HW1_1.png', dpi=300, transparent=True)
