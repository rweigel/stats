import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import chi2
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['mathtext.rm'] = 'serif'

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

# 1.
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

#2.
N = 1000
y = np.random.normal(size=N, loc=0, scale=1)
plt.plot(y)
plt.ylabel('$y$')
plt.xlabel('$t$')
plt.grid()
plt.savefig('HW7_2a.png', dpi=300, bbox_inches='tight')
plt.savefig('HW7_2a.svg', bbox_inches='tight', transparent=True)
plt.close()

I, f, a, b, a0 = periodogramraw(y, 'fast')
Ix = np.random.chisquare(df=2, size=len(f))
# Note that for f = 0, I is chi_1^2 distributed
#plt.title(title)
plt.plot(f, I, 'k', label=r'$I$ for 1000 values from $\mathcal{N}$(0,1)')
plt.plot(f, Ix, color=3*[0.5], linewidth=1, label=r'Values from $\chi_2^2$')
plt.grid()
plt.legend()
plt.savefig('HW7_2b.png', dpi=300, bbox_inches='tight')
plt.savefig('HW7_2b.svg', bbox_inches='tight', transparent=True)
plt.close()

# 3.
dx = 0.5
bin_c = dx/2 + dx*np.arange(0, 15/dx)
print("Bin centers:")
print(bin_c)

bin_e = bin_c - dx/2 # Bin edges
print("Bin edges:")
print(bin_e)

nXbar, _ = np.histogram(I, bins=bin_e)
bin_c = bin_c[0:-1]

plt.bar(bin_c, nXbar, width=dx*0.98, color='k')
plt.xlabel('$I$')
plt.ylabel('# in bin')
plt.grid()
plt.savefig('HW7_2c.png', dpi=300, bbox_inches='tight')
plt.savefig('HW7_2c.svg', bbox_inches='tight', transparent=True)
plt.close()

# 4.
x = np.linspace(0, 15, 1000)
pdf = chi2.pdf(x, df=2)
plt.hist(I, bins=bin_e, color='k', width=dx*0.98, density=True,  label='data')
plt.plot(x, pdf, '--', color=3*[0.5], label=r'$\chi_2^2$')
plt.xlabel('$I$')
plt.ylabel('pdf')
plt.legend()
plt.grid()
plt.savefig('HW7_2d.png', dpi=300, bbox_inches='tight')
plt.savefig('HW7_2d.svg', bbox_inches='tight', transparent=True)
plt.close()

# 5.
A = 0.2
f0 = 1/100
y = y + A * np.sin(2 * np.pi * f0 * np.arange(N))
I, f, a, b, a0 = periodogramraw(y, 'fast')
Ix = np.random.chisquare(df=2, size=len(f))
# Note that for f = 0, I is chi_1^2 distributed
plt.title(f'$A$ = {A}, $f_o$ = {f0}')
plt.plot(f, I, 'k', label=r'$I$ of 1000 values from $\mathcal{N}$(0,1)')
plt.plot(f, Ix, color=3*[0.5], linewidth=1, label=r'1000 values from $\chi_2^2$')
plt.plot(f0, (N/2)*A**2, 'rx', label='$(N/2)A^2$')
plt.xlabel('$f$')
plt.grid()
plt.legend()
plt.savefig('HW7_2e.png', dpi=300, bbox_inches='tight')
plt.savefig('HW7_2e.svg', bbox_inches='tight', transparent=True)
plt.close()
