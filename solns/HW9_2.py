import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'

from scipy.special import comb

#case = '8.3.5'
case = '10.2'

θ = np.linspace(0, 1, 1000)
dθ = θ[1] - θ[0]

# pdf = p(θ|𝒟) for problem 8.3.5:
if case == '8.3.5':
  pdf = θ*(1-θ)*np.exp((-(θ-0.5)**2/0.1))/0.113363
if case == '10.2':
  # Not normalized. Will use numerical integration to find
  # normalization constant.
  pdf = θ**4 * (1-θ)**4
cdf = dθ*np.cumsum(pdf)
print(f"Integral of pdf: {cdf[-1]:.16f}")
# Integral of pdf: 0.9999967412650484
# (not 1. b/c using numerical integration and the 0.113363 is not exact)
# We can fix this by normalizing the pdf
pdf = pdf/cdf[-1]
cdf = dθ*np.cumsum(pdf)
print(f"Integral of pdf after normalization: {cdf[-1]:.16f}")
# Integral of pdf after normalization: 1.0000000000000013

results = []
for lb_idx in range(len(θ)-1):
  for ub_idx in range(lb_idx, len(θ)-1):
    # Numerically integrate pdf from lb to ub by summing values of pdf from
    # lb_idx to ub_idx and multiplying by dθ
    integral = dθ*np.sum(pdf[lb_idx:ub_idx])

    if integral > 0.95:
      lb = θ[lb_idx] # Lower bound (lb) value
      ub = θ[ub_idx] # Upper bound (ub) value
      print(f"lb = {lb:.3f}, ub = {ub:.3f}, ub-lb = {ub - lb:.3f}")
      results.append((lb, ub))
      break

results = np.array(results)
lengths = results[:, 1] - results[:, 0] # Lengths of intervals
idx = np.argmin(lengths) # Find index of minimum interval length
print(f"95% Credible interval: [{results[idx, 0]:.3f}, {results[idx, 1]:.3f}]")
# 95% Credible interval: [0.160, 0.825]

plt.plot(θ, pdf, 'k-', label='p(θ|$\\mathcal{D}$)')
label = f'95% Credible Interval: [{results[idx, 0]:.3f}, {results[idx, 1]:.3f}]'
plt.plot([results[idx, 0], results[idx, 1]], [0, 0], 'r', lw=5, label=label)
plt.xlabel(r'$\theta$')
plt.ylim([0, 2.9])
plt.grid()
if case == '8.3.5':
  plt.title(r'$\mathcal{D}$ = [H, T]; $p(\theta)\propto e^{-(\theta-0.5)^2/0.1}$')
  plt.legend(loc='upper left')
  plt.savefig('HW9_2a.png', dpi=300, bbox_inches='tight')
  plt.savefig('HW9_2a.svg', transparent=True, bbox_inches='tight')
if case == '10.2':
  plt.title(r'$\mathcal{D}$ = [H, H, T, T, H, T, T, H]; $p(\theta) = 1$')
  plt.savefig('HW9_2b.png', dpi=300, bbox_inches='tight')
  plt.savefig('HW9_2b.svg', transparent=True, bbox_inches='tight')
  plt.close()

  n = 8
  P_exact = np.full(n+1, np.nan)
  ks = np.array(range(0, n+1))
  for k in ks:
    result = comb(n, k, exact=True)
    print(f"{n} choose {k} * 0.5^8 = {result*0.5**n:.3f}")
    P_exact[k] = result*0.5**n

  plt.grid()
  plt.stem(ks/8, P_exact, linefmt='k-', markerfmt='ko', basefmt=' ')
  #plt.legend(loc='upper left')
  plt.xlabel(r'$k/n$')
  plt.ylabel(r'$p(k|n)$')
  plt.ylim([0, 0.3])
  plt.xticks(ks/8)
  plt.savefig('HW9_2c.png', dpi=300, bbox_inches='tight')
  plt.savefig('HW9_2c.svg', transparent=True, bbox_inches='tight')
