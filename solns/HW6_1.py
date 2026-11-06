import numpy as np
from lib import dft
from lib.savefig import savefig


def part1():
  y = [0, 1, 0, -1]
  a0, a, b, i, f = dft.dft(y, method='slow')

  print("--Part 1--")
  print(f"  y = {y}")
  print("DFT")
  dft.print(a0, a, b, i, f)

  dft.plot(i, a, b, y)
  savefig('HW6_1_1')


def part2():
  #y = [0, -1, 0, 1]
  y = [1, 0, -1, 0]
  a0, a, b, i, f = dft.dft(y, method='slow')

  print("--Part 2--")
  print(f"  y = {y}")
  print("DFT")
  dft.print(a0, a, b, i, f)

  dft.plot(i, a, b, y)
  savefig('HW6_1_2')


def part3():
  n = 40 # When n = 4, gives same result as part 1
  y = np.full(n, np.nan)
  i = 1 # The frequency index for the sine wave. i = 1 means the sine wave
        # will have a frequency of i/n cycles per sample and a period of n/i samples.
  for t in range(n):
    y[t] = np.sin(2 * np.pi * (i/n) * t )

  a0, a, b, i, f = dft.dft(y, method='slow')

  print("--Part 3--")
  dft.plot(i, a, b, y)

  dft.print(a0, a, b, i, f)
  savefig('HW6_1_3')


def part4():
  """
  Modify the values in y so that the DFT has the following values:
  DFT
     i          a_i          b_i          f_i
     0       0.0000                    0.0000
     1       1.0000      -0.0000       0.2500
     2       0.0000       0.0000       0.5000
  """

  y = [1, 0, -1, 0]
  a0, a, b, i, f = dft.dft(y, method='slow')

  print("--Part 4-")
  print(f"  y = {y}")
  print("DFT")
  dft.print(a0, a, b, i, f)

  dft.plot(i, a, b, y)
  savefig('HW6_1_4')


def part5():
  """
  Keep n the same, but modify the equation for y[t] so that 
  a_3 = b_3 = 1; otherwise, all a_i and b_i are 0.
  """

  n = 40
  y = np.full(n, np.nan)
  i = 3
  for t in range(n):
    y[t] = np.sin(2 * np.pi * (i/n) * t ) + np.cos(2 * np.pi * (i/n) * t )

  a0, a, b, i, f = dft.dft(y, method='slow')

  print("--Part 5--")
  dft.plot(i, a, b, y)

  dft.print(a0, a, b, i, f)
  savefig('HW6_1_5')


def part6():
  """
  Keep n the same, but modify the equation for y[t] so that 
  a_3 = b_3 = 1 and a_6 = 1; otherwise, all a_i and b_i are 0.
  """

  n = 40
  y = np.full(n, np.nan)
  for t in range(n):
    y[t] = np.sin(2 * np.pi * (3/n) * t ) + np.cos(2 * np.pi * (3/n) * t ) + np.cos(2 * np.pi * (6/n) * t )


  a0, a, b, i, f = dft.dft(y, method='slow')

  print("--Part 6--")
  dft.plot(i, a, b, y)

  dft.print(a0, a, b, i, f)
  savefig('HW6_1_6')


def part7():
  """
  Here we want to determine from the plot of a^2 + b^2 when you can "see"
  evidence of the sine wave at DFT index i (frequency i/40). For small sigma,
  you should see a clear spike in the bottom plot (for the magnitude squared
  of the DFT coefficients).

  Increase sigma until it is your opinion that, visually, you can not see the
  spike in the bottom plot.

  Later we will compare your visual assessment with a more quantitative measure.
  """

  n = 40

  y = np.full(n, np.nan)
  i5 = 5 # The frequency index for the sine wave. i = 1 means the sine wave
         # will have a frequency of i/n cycles per sample and a period of n/i samples.
  sigma = 1 # Standard deviation of the noise
  A = 1 # Amplitude of the sine wave
  # At and below this sigma, every time I run this, the plot shows a spike in
  # a_i^2 + b_i^2 at i=5 that seems clearly higher than that for the other indices.
  for exp in range(100):
    for t in range(n):
      epsilon = np.random.normal(loc=0, scale=sigma)
      y[t] = epsilon + A*np.sin(2 * np.pi * (i5/n) * t )

    a0, a, b, i, f = dft.dft(y, method='fast')

  print("--Part 7--")
  title = f"$y_t=\\sin(2\\pi ({i5}/{n})t ) + \\epsilon_t;   \\epsilon \\sim \\mathcal{{N}}(0, \\sigma = {sigma:.1f})$"
  dft.plot(i, a, b, y, title=title, sigma=sigma)
  dft.print(a0, a, b, i, f)
  savefig('HW6_1_7')

if False:
  part1()
  part2()
  part3()
  part4()
  part5()
  part6()
part7()
