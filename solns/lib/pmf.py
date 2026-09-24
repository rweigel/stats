"""
Motivation: Use of Matplotlib's plt.hist() rarely produces a plot that is good
representation of data. In this script, several methods for computing the
empirical probability mass function (PMF) of a dataset are implemented and
visualized.
"""

def pmf(x, method='numpy'):
  """Given a list x or 1-D NumPy array containing integers, return the unique values and their relative frequencies."""
  import numpy as np

  return_list = isinstance(x, list)
  if not return_list and not isinstance(x, np.ndarray):
    raise TypeError("x must be a list or NumPy array.")

  if not all(isinstance(val, (int, np.integer)) for val in x):
    raise TypeError("All values of x must be integers.")

  x_array = np.asarray(x)
  if x_array.ndim != 1:
    raise ValueError("Input array x must be 1-D.")

  if method is None or method == 'numpy':
    unique_vals, counts = np.unique(x_array, return_counts=True)
    frequencies = counts / len(x_array)

  elif method == 'manual':
    unique_vals = []
    counts = []
    for val in x:
      if val not in unique_vals:
        unique_vals.append(val)
        counts.append(1)
      else:
        counts[unique_vals.index(val)] += 1
    unique_vals = np.array(unique_vals)
    frequencies = np.array(counts) / len(x_array)

  elif method == 'set':
    unique_vals = list(set(x))
    counts = [sum(item == val for item in x) for val in unique_vals]
    unique_vals = np.array(unique_vals)
    frequencies = np.array(counts) / len(x_array)

  elif method == 'counter':
    from collections import Counter

    counts = Counter(x)
    unique_vals = np.array(list(counts.keys()))
    frequencies = np.array([counts[val] for val in unique_vals]) / len(x_array)

  else:
    raise ValueError(f"Unknown method: {method}")

  if return_list:
    return unique_vals.tolist(), frequencies.tolist()

  return unique_vals, frequencies


def pmf_test():

  def print_pmfs(x):
    print()
    print(f"Input ({type(x).__name__}): {x}")
    print("PMF using set:", pmf(x, method='set'))
    print("PMF using numpy:", pmf(x, method='numpy'))
    print("PMF using manual:", pmf(x, method='manual'))
    print("PMF using counter:", pmf(x, method='counter'))

  import numpy as np
  x = [1, 2, 2, 3, 3, 3]
  print_pmfs(x)

  x = np.array(x)
  print_pmfs(x)


def annotate(xlabel, ylabel):
  import matplotlib.pyplot as plt
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.grid(True)


def save(filename):
  import matplotlib.pyplot as plt
  plt.savefig(f"{filename}.svg", transparent=True)
  plt.savefig(f"{filename}.png", dpi=300)
  plt.close()

def pmf_plot():
  import numpy as np
  import matplotlib.pyplot as plt

  x = np.array([1, 2, 2, 3, 3, 3])
  unique_vals, frequencies = pmf(x)

  # Bins make it look like values other than integers are present."
  plt.bar(unique_vals, frequencies)
  annotate("Value", "Frequency")
  plt.title("Bin width makes it seem values other than integers are present.")
  save("pmf/pmf_bad_1")

  plt.hist(x)
  annotate("Value", "Frequency")
  # Note that the centering issue can be resolved using align='mid', but
  # few people find this.
  plt.title("Bins are not centered on integer values!")
  save("pmf/pmf_bad_2")

  plt.stem(unique_vals, frequencies, basefmt=" ")
  annotate("Value", "Frequency")
  # Important: Fractional x-values should not be labeled because they do not exist.
  # If there are too many unique values, the x-axis labels may overlap. In
  # this case, set only every other tick label.
  # plt.xticks(unique_vals[::2])
  plt.xticks(unique_vals) # Set x-axis ticks to the unique values

  save("pmf/pmf_good_1a")

  # Acceptable alternative: bar plot with thin bars.
  plt.bar(unique_vals, frequencies, width=0.1)
  annotate("Value", "Frequency")
  plt.xticks(unique_vals) # Set x-axis ticks to the unique values
  save("pmf/pmf_good_1b")

  # To plot as a histogram, use
  plt.stem(unique_vals, len(x)*frequencies, basefmt=" ")
  annotate("Value", "count")
  plt.xticks(unique_vals) # Set x-axis ticks to the unique values
  # Make y-ticks integer values
  plt.yticks(range(int(len(x)*max(frequencies))+1))
  # Manual:
  #plt.yticks([0, 1, 2, 3])
  save("pmf/pmf_good_1c")

  # Plotting two PMFs
  # If three PMFs, plot circles for all.
  unique_vals2, frequencies2 = pmf([1, 1, 2, 3, 3, 4])
  plt.bar(unique_vals2, frequencies2, width=0.1)
  plt.plot(unique_vals, frequencies, 'r.', markersize=10)
  unique_vals_union = list(set(unique_vals) | set(unique_vals2))
  plt.xticks(unique_vals_union) # Set x-axis ticks to union of unique values
  plt.legend(["pmf 1", "pmf 2"])
  annotate("Value", "Frequency")
  save("pmf/pmf_good_1d")


if __name__ == "__main__":
  pmf_test()
  pmf_plot()
