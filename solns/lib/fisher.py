# https://www.mathworks.com/help/signal/ug/significance-testing-for-periodic-component.html

def fisher_g(y):
  # For later HW
  _, a, b, i, f = dft(y, method='fast')
  power = (a**2 + b**2)[f < 0.5]
  total_power = np.sum(power)
  i_max = i[f < 0.5][np.argmax(power)]
  return i_max, np.max(power) / total_power


def fisher_g_ppf(n, alpha=0.05):
  # Given the number of time series values n and significance level alpha,
  # return the threshold value for the Fisher's g statistic.

  if not isinstance(n, (int, np.integer)) or n < 2:
    raise ValueError("n must be an integer of at least 2.")
  if not 0 < alpha < 1:
    raise ValueError("alpha must be between 0 and 1, exclusively.")

  if n % 2 == 0:
    # Shimshoni 1971 p. 377 defines n = 2m + 2
    m = (n - 2) // 2
  else:
    # Shimshoni 1971 p. 373 defined n = 2m + 1
    m = (n - 1) // 2

  def tail_difference(g):
    from math import comb, floor, fsum
    from scipy.optimize import brentq
    if g <= 1 / m:
      return 1 - alpha
    terms = []
    for index in range(1, min(m, floor(1 / g)) + 1):
      term = (-1)**(index - 1) * comb(m, index) * max(0.0, 1 - index * g)**(m - 1)
      terms.append(term)
    return fsum(terms) - alpha

  return brentq(tail_difference, 1 / m, 1.0)


def fisher_g_test(y):
  # For later HW
  """Return Fisher's upper-tail p-value for equally spaced Gaussian white noise.
  Returns the DFT index corresponding to the maximum power and the p-value.
  """
  from math import comb, floor

  i_max, g = fisher_g(y)
  m = (len(y) - 1) // 2
  if g <= 1 / m:
    return i_max, 1.0, np.nan

  p = 0.0
  for index in range(1, floor(1 / g) + 1):
    term = (-1)**(index - 1) * comb(m, index) * (1 - index * g)**(m - 1)
    p += term

  return i_max, float(np.clip(p, 0, 1)), g
  
y = np.full(n, np.nan)
i = 5 # The frequency index for the sine wave. i = 1 means the sine wave
        # will have a frequency of i/n cycles per sample and a period of n/i samples.
sigma = 1.0 # Standard deviation of the noise

nc = 0
ne = 1000
g_thresh = fisher_g_ppf(n=n, alpha=0.1)
for exp in range(ne):
  for t in range(n):
    epsilon = np.random.normal(loc=0, scale=sigma)
    y[t] = epsilon #+ np.sin(2 * np.pi * (i/n) * t )

  a0, a, b, _, f = dft(y, method='fast')
  i_max, p, g = fisher_g_test(y)


  #if i_max == 5 and g > g_thresh:
  #  nc += 1

  star = ""
  if g > g_thresh:
    star = "*"
    nc += 1
  print(f"Experiment {exp}: g_t = {g_thresh:.2f}, i_max = {i_max:2d}, p = {p:.2e}, g: {g:.2f} {star}")

print(f"Number of times i_max = 5: {nc} out of {ne}")
