import numpy as np

def dft(y, method='slow'):

  n = len(y)
  if n % 2 == 0:
    q = n // 2
  else:
    q = (n - 1) // 2

  i = np.arange(1, q+1)
  f = i / n

  if method == 'slow':
    a = np.full(q, np.nan)
    b = np.full(q, np.nan)
    a0 = np.mean(y)
    for k in range(q):
      a[k] = 0
      b[k] = 0
      for t in range(n):
        a[k] = a[k] + y[t] * np.cos(2 * np.pi * (k+1) * t / n)
        b[k] = b[k] + y[t] * np.sin(2 * np.pi * (k+1) * t / n)

      a[k] = 2 * a[k] / n
      b[k] = 2 * b[k] / n

  if method == 'fast':
    yfft = np.fft.fft(y)
    a0 = np.real(yfft[0]) / n
    a = (2 / n) * np.real(yfft[1:q+1])
    b = -(2 / n) * np.imag(yfft[1:q+1])

  if n % 2 == 0:
    a[-1] = a[-1] / 2

  return a0, a, b, i, f


def plot(i, a, b, y, sigma=None, title=None, i_max=None, p=None):
  import matplotlib.pyplot as plt
  from matplotlib.ticker import MaxNLocator

  _, axes = plt.subplots(3, 1, figsize=(8.5, 11), layout='constrained')
  if title is not None:
    axes[0].set_title(title)
  axes[0].plot(np.arange(len(y)), y, marker='o', ls='none', color='k')
  axes[0].set(xlabel='Sample index ($t$)\n', ylabel='$y_t$')
  axes[0].grid(True)

  axes[1].plot(i, a, label='$a_i$', marker='o', ls='none', ms=8)
  axes[1].plot(i, b, label='$b_i$', marker='o', ls='none', ms=6)
  axes[1].tick_params(labelbottom=False)
  axes[1].legend()
  axes[1].grid(True)

  power = np.asarray(a)**2 + np.asarray(b)**2
  regular = np.asarray(i) != i_max
  axes[2].plot(np.asarray(i)[regular], power[regular], marker='o', ls='none', color='k')
  axes[2].set(xlabel='DFT index ($i$)', ylabel='$a_i^2 + b_i^2$')
  axes[2].grid(True)
  axes[2].sharex(axes[1])
  axes[2].grid(True)
  if sigma is not None:
    axes[2].axhline((4/len(y))*sigma**2, color='gray', lw=1, ls='--')


  # Modify all x labels so fractions are never shown (x values are always integer)
  axes[0].xaxis.set_major_locator(MaxNLocator(integer=True))
  axes[1].xaxis.set_major_locator(MaxNLocator(integer=True))
  axes[2].xaxis.set_major_locator(MaxNLocator(integer=True))

  if i_max is not None:
    max_position = np.flatnonzero(np.asarray(i) == i_max)[0]
    axes[2].plot(i_max, power[max_position], marker='o', ls='none', color='r')
    if p is not None:
      kwargs = {
        'xy': (i_max, power[max_position]),
        'xytext': (0, 6),
        'textcoords': 'offset points',
        'color': 'r',
        'ha': 'center',
        'va': 'bottom',
        'bbox': {
          'facecolor': 'white',
          'edgecolor': 'gray',
          'alpha': 0.9,
          'pad': 3
        }
      }
      axes[2].annotate(f'p={p:.2e}', **kwargs)


_print = print
def print(a0, a, b, i, f, i_max=None, p=None):
  _print(f'  {"i":>4} {"a_i":>12} {"b_i":>12} {"f_i":>12}')
  _print(f'  {0:4d} {a0:12.4f} {" ":12s} {0:12.4f}')
  for idx in range(len(a)):
    suffix = f' p={p:.2e}' if i[idx] == i_max and p is not None else ''
    _print(f'  {i[idx]:4d} {a[idx]:12.4f} {b[idx]:12.4f} {f[idx]:12.4f}{suffix}')


def test(y):
  # Verify that the slow and fast methods of computing the DFT give the same results
  a0_s, a_s, b_s, i_s, f_s = dft(y, method='slow')
  a0_f, a_f, b_f, i_f, f_f = dft(y, method='fast')
  assert np.allclose(a0_s, a0_f, rtol=1e-10, atol=1e-12)
  assert np.allclose(a_s, a_f, rtol=1e-10, atol=1e-12)
  assert np.allclose(b_s, b_f, rtol=1e-10, atol=1e-12)
  assert np.all(i_s == i_f)
  assert np.all(f_s == f_f)

if __name__ == "__main__":
  for n in [1, 2, 3, 4, 5, 10, 11, 100, 101]:
    y = np.random.randn(n)
    test(y)
