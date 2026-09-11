"""
Motivation: Use of Matplotlib's plt.hist() rarely produces a plot that is good
representation of data (however, it is useful for a first visualization).
In this script, several methods for computing the empirical probability
density function (PDF) of a dataset are implemented and visualized. To convert
to a histogram (showing the count in each bin), multiply the PDF frequencies
by the total number of observations.
"""

def pdf(x, dx, a=None):
  """Given a list x or 1-D NumPy array containing numerical values, a bin width
  dx, and the range [a, b], return the bin centers and their relative frequencies (PDF)."""
  import numpy as np

  x_array = np.asarray(x)
  if x_array.ndim != 1:
    raise ValueError("Input array x must be 1-D.")

  if a is None:
    a = np.min(x_array) - dx
  else:
    a = a - dx/2

  b = np.max(x_array) + dx
  bin_edges = np.arange(a, b + dx, dx)
  counts, _ = np.histogram(x_array, bins=bin_edges)
  frequencies = counts / np.sum(counts)
  bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

  return frequencies, bin_centers

def pdf_plot():
  import matplotlib.pyplot as plt
  import numpy as np

  x = np.random.normal(loc=50, scale=1, size=1000)
  dx = 1

  if False:
    # Not ideal because the bins centered on values such as 48.9, so one
    # reads as "the pmf for heights in the range [48.3, 49.4] is ...".
    # It is prefered if the bins were centered on integers or common fractions
    # such as 0.1, 0.2, 0.5, etc.
    dx = 1
    frequencies, bin_centers = pdf(x, dx)

    plt.bar(bin_centers, frequencies, width=dx, align='center')
    plt.xlabel("Height [inches]")
    plt.ylabel("pdf [1/inches]")
    plt.grid(True)
    plt.show()

  if False:
    # Compute the starting bin center as the minimum value rounded down to
    # the nearest integer.
    a = np.floor(np.min(x))
    frequencies, bin_centers = pdf(x, dx, a=a)
    plt.bar(bin_centers, frequencies, width=dx, align='center')
    plt.xlabel("Height [inches]")
    plt.ylabel("pdf [1/inches]")
    plt.grid(True)
    plt.show()

  if True:
    # Same as previous, but histogram
    a = np.floor(np.min(x))
    frequencies, bin_centers = pdf(x, dx, a=a)
    plt.bar(bin_centers, frequencies*len(x), width=dx, align='center')
    plt.xlabel("Height [inches]")
    plt.ylabel("count")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
  pdf_plot()