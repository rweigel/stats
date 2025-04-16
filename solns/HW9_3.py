import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import chi2
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['mathtext.rm'] = 'serif'

# 1. copied from HW7_2.py.
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

# Copied from HW7_2.py.
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

# Copied from HW7_2.py.
N = 1000
y = np.random.normal(size=N, loc=0, scale=1)
plt.plot(y, 'k')
plt.ylabel('$y$')
plt.xlabel('$t$')
plt.title(r'$N =1000$ values from $\mathcal{N}$(0,1)')
plt.grid()
plt.savefig('HW9_3a.png', dpi=300, bbox_inches='tight')
plt.savefig('HW9_3a.svg', bbox_inches='tight', transparent=True)
plt.close()

# 2. and 3.
I, f, a, b, a0 = periodogramraw(y, 'fast')
dx = 0.5
bin_c = dx/2 + dx*np.arange(0, 15/dx) # Bin centers
bin_e = bin_c - dx/2 # Bin edges

ppf_value = chi2.ppf(0.99, df=2)
print(f'The PPF value at 0.99 for chi_2^2 is {ppf_value}')

fraction_above_ppf = np.sum(I > ppf_value) / len(I)
title = f'Fraction of $I$ observed above $I_o={ppf_value:.2f}$: {fraction_above_ppf:.3f}'
text = fr'$I_o = {ppf_value:.2f}$: $\int_0^{{I_o}} \chi^2_2(I) dI = 0.99$'

x = np.linspace(0, 15, 1000)
pdf = chi2.pdf(x, df=2)
plt.hist(I, bins=bin_e, color='k', width=dx*0.98, density=True, label='observed')
plt.plot(x, pdf, '--', color=3*[0.5], label=r'$\chi_2^2$')
plt.annotate('', xy=(9.21, 0.1), xytext=(9.21, 0),
       arrowprops=dict(facecolor='black', shrink=0.02, width=1, headwidth=4))
plt.text(ppf_value, 0.1, text, ha='left', va='bottom', fontsize=8)
plt.title(title)
plt.xlabel('$I$')
plt.ylabel('pdf')
plt.legend()
plt.grid()
plt.savefig('HW9_3b.png', dpi=300, bbox_inches='tight')
plt.savefig('HW9_3b.svg', bbox_inches='tight', transparent=True)
plt.close()
