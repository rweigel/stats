"""
Motivation: Use of Matplotlib's plt.hist() rarely produces a plot that is good
representation of data (however, it is useful for a first visualization).
In this script, several methods for computing the empirical probability
density function (PDF) of a dataset are implemented and visualized.
"""

def pdf(x, dx, a=None):
  """Given a list x or 1-D NumPy array containing numerical values, a bin width
  dx, and the range [a, b], return the bin centers and their empirical PDF."""
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
  e_pdf = counts / np.sum(counts) / dx
  bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

  return e_pdf, bin_centers, bin_edges


def annotate(xlabel, ylabel):
  import matplotlib.pyplot as plt
  # Make axis limits symmetric around mean.
  plt.xlim(460, 540)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.grid(True)


def save(filename):
  import matplotlib.pyplot as plt
  plt.savefig(f"{filename}.svg", transparent=True)
  plt.savefig(f"{filename}.png", dpi=300)
  plt.close()


def pdf_plot():
  import numpy as np
  import matplotlib.pyplot as plt

  np.random.seed(0)
  x = np.random.normal(loc=500, scale=10, size=1000)
  dx = 10

  # Not ideal because the bins are not centered on "nice" values.
  e_pdf, bin_centers, bin_edges = pdf(x, dx)
  plt.bar(bin_centers, e_pdf, width=dx, align='center')
  annotate("Height [mm]", "PDF [1/mm]")
  save("pdf/pdf_bad_1")


  # Compute the starting bin center as a multiple of dx
  a = np.floor(np.min(x)/dx) * dx
  e_pdf, bin_centers, bin_edges = pdf(x, dx, a=a)
  plt.bar(bin_centers, e_pdf, width=dx, align='center')
  annotate("Height [mm]", "PDF [1/mm]")
  save("pdf/pdf_good_1a")


  # Same as previous, but showing probability in bin (relative frequency in bin)
  plt.stairs(e_pdf, bin_edges)
  annotate("Height [mm]", "PDF [1/mm]")
  save("pdf/pdf_good_1b")


  # Same as previous, but showing probability in bin (relative frequency in bin)
  plt.bar(bin_centers, e_pdf*dx, width=dx, align='center')
  annotate("Height [mm]", "Probability in bin")
  save("pdf/pdf_good_1c")


  # Same as previous, but as histogram (some label as "frequency", but this
  # terms has other meanings and I find "counts" to be more precise).
  plt.bar(bin_centers, e_pdf*len(x), width=dx, align='center')
  annotate("Height [mm]", "Count")
  save("pdf/pdf_good_1d")


if __name__ == "__main__":
  pdf_plot()