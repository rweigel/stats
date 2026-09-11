
# For a trial of size n = 3, number of outcomes is 2^3 = 8

slow_method = False

if slow_method:
  import random

  print("Slow method")
  n_max = 1000
  # Generate list of 0s and 1, each element of list equally probable
  n_1 = 0
  r_f = []
  for n in range(1, n_max + 1):
    results = []
    result = random.choice([0, 1])

    if result == 1:
      n_1 += 1

    # Relative frequency is (number of 1s) / (total number of experiments)
    r_f.append(n_1 / n)


    if n < 10:
      print(f"n = {n} experiments. P_H = {n_1 / n}")
    if n in [10, 100, 1000]:
      print(f"n = {n} experiments. P_H = {n_1 / n}")

else:
  import numpy as np

  n_max = 100000
  print(f"Fast method. N = {n_max}")
  N = np.arange(1, n_max + 1)
  r_f = np.cumsum(np.random.choice([0, 1], n_max)) / N

from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"

if n_max < 1000:
  plt.plot(r_f, marker='.', linestyle='None', color='black')
else:
  plt.semilogx(r_f, marker='.', linestyle='None', color='black')
plt.grid()
plt.axhline(0.5, color='red', linestyle='--')
plt.title("Experiment: Select from $[0, 1]$ with replacement")
plt.xlabel('Number Experiments')
plt.ylabel('Relative Frequency of $1$')
print("Writing HW1_1.png")
plt.savefig('HW1_1.png', dpi=300, transparent=True)
