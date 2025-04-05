import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import chi2

def periodogramraw(x, method='slow'):
  """
  Compute raw periodogram.

  Parameters:
  x : array-like
      Input signal.
  method : str, optional
      Method to compute coefficients ('slow' or 'fast'). Default is 'slow'.

  Returns:
  I : array-like
      Periodogram values.
  f : array-like
      Frequencies.
  a : array-like, optional
      Coefficients a (only for 'slow' method).
  b : array-like, optional
      Coefficients b (only for 'slow' method).
  a0 : float, optional
      Coefficient a0 (only for 'slow' method).

  # See https://rweigel.github.io/stats/hw.html#dft-and-the-raw-periodogram
  # for notation.
  """

  if method == 'fast':
    N = len(x)
    xfft = np.fft.fft(x)
    n = len(x)
    b = (2 / n ) * np.real(xfft)
    a = (2 / n) * np.imag(xfft)
    if N % 2 == 0:  # N is even
      a[N // 2] = (1 / 2) * a[N // 2]
      b[N // 2] = (1 / 2) * b[N // 2]
      I = (N / 2) * (a**2 + b**2)
      I = I[1:N // 2+1]
  f = np.arange(0, N // 2) / n
  a0 = np.mean(x)
  return I, f, a, b, a0

y = np.array([0, 1, 0, -1])
I, f, a, b, a0 = periodogramraw(y, 'fast')
print(f'f  = {f}')
print(f'a0 = {a0}')
print(f'a  = {a}')
print(f'b  = {b}')
print(f'I  = {I}')
y = np.array([0, 1, 0, -1])
Y = np.fft.fft(y)
print(Y)

N = 1000
f0 = 1/100
A = 0.2
title = f'A = {A}, $f_o$ = {f0}'
y = np.random.normal(size=N, loc=0, scale=1)
y = y + A * np.sin(2 * np.pi * f0 * np.arange(N))
plt.plot(y)
plt.title(title)
plt.ylabel('$y$')
plt.xlabel('$t$')
plt.grid()
plt.savefig('HW7_2a.png', dpi=300, bbox_inches='tight')
plt.savefig('HW7_2a.svg', bbox_inches='tight', transparent=True)
plt.close()

I, f, a, b, a0 = periodogramraw(y, 'fast')
Ix = np.random.chisquare(df=2, size=len(f))
# Note that for f = 0, I is chi_1^2 distributed
plt.title(title)
plt.plot(f, I, 'k', label='$I$ for 1000 values from $\mathcal{N}$(0,1)')
plt.plot(f, Ix, color=3*[0.5], linewidth=1, label='Values from $\chi_2^2$')
plt.plot(f0, (N/2)*A**2, 'rx', label='$(N/2)A^2$')
plt.grid()
plt.legend()
plt.savefig('HW7_2b.png', dpi=300, bbox_inches='tight')
plt.savefig('HW7_2b.svg', bbox_inches='tight', transparent=True)

x_value = (A**2)*N/2
cdf_value = chi2.cdf(x_value, df=2)
print(f'The CDF value at x = {x_value} is {cdf_value}')
