import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'

from scipy.special import comb

def legend_order(ax, order, **kwargs):
  # Get the handles and labels
  handles, labels = ax.get_legend_handles_labels()
  handles = [handles[i] for i in order]
  labels = [labels[i] for i in order]
  ax.legend(handles, labels, **kwargs)

case = '8.3.5'
case = '10.2'
case = 'large_n'

# TODO:
# Technically, we should only use possible value of θ: 0, 1/n, ..., 1
θ = np.linspace(0, 1, 1000)
dθ = θ[1] - θ[0]

if case == '8.3.5':
  prior = np.exp((-(θ-0.5)**2/0.1))/0.113363
  n_H = 1
  n_T = 1
if case == '10.2':
  prior = 1
  n_H = 4
  n_T = 4
if case == 'large_n':
  prior = 1
  n_H = 20
  n_T = 20

n = n_H + n_T
# P(𝒟|θ) ∝ θ^n_H (1 - θ)^n_T
# Not normalized. Will use numerical integration to find
# normalization constant.
# P(θ|𝒟) ∝ P(𝒟|θ)*prior
posterior = θ**n_H * (1-θ)**n_T * prior

cdf = dθ*np.cumsum(posterior)
print(f"Integral of posterior: {cdf[-1]:.16f}")
# Integral of posterior: 0.9999967412650484
# (not 1. b/c using numerical integration and the 0.113363 is not exact)
# We can fix this by normalizing the pdf
posterior = posterior/cdf[-1]
cdf = dθ*np.cumsum(posterior)
print(f"Integral of pdf after normalization: {cdf[-1]:.16f}")
# Integral of pdf after normalization: 1.0000000000000013

results = []
for lb_idx in range(len(θ)-1):
  for ub_idx in range(lb_idx, len(θ)-1):
    # Numerically integrate pdf from lb to ub by summing values of pdf from
    # lb_idx to ub_idx and multiplying by dθ
    integral = dθ*np.sum(posterior[lb_idx:ub_idx])

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

plt.plot(θ, posterior, 'k-', label='$p(θ|\\mathcal{D}$)')
label = f'95% Credible Interval: [{results[idx, 0]:.3f}, {results[idx, 1]:.3f}]'
plt.plot([results[idx, 0], results[idx, 1]], [0, 0], 'r', lw=5, label=label)
plt.grid()
plt.xlabel(r'$\theta$')
plt.ylim([0, 2.9])

title = rf'$\mathcal{{D}}$ = {n_H} H, {n_T} T'
if case == '8.3.5':
  plt.title(title + r'; $p(\theta)\propto e^{-(\theta-0.5)^2/0.1}$')
  plt.legend(loc='upper left')
  plt.savefig('HW9_2a.png', dpi=300, bbox_inches='tight')
  plt.savefig('HW9_2a.svg', transparent=True, bbox_inches='tight')

if case == '10.2':
  plt.title(title + r'; $p(\theta) = 1$')
  plt.legend(loc='upper left')
  plt.savefig('HW9_2b.png', dpi=300, bbox_inches='tight')
  plt.savefig('HW9_2b.svg', transparent=True, bbox_inches='tight')
  plt.close()

if case == 'large_n':
  plt.title(title + r'; $p(\theta) = 1$')
  plt.ylim([0, 10])
  plt.legend(loc='upper left')
  plt.savefig('HW9_2c.png', dpi=300, bbox_inches='tight')
  plt.savefig('HW9_2c.svg', transparent=True, bbox_inches='tight')
  plt.close()

  P_exact = np.full(n+1, np.nan)
  ks = np.array(range(0, n+1))
  for k in ks:
    result = comb(n, k, exact=True)
    #print(f"{n} choose {k} * 0.5^8 = {result*0.5**n:.3f}")
    P_exact[k] = result*0.5**n

  plt.title(title)
  plt.grid()
  plt.plot(ks/n, P_exact, 'k.', label=r'$P(\mathcal{D}|\theta)$')
  # Devore 8th Edition equation 7.11
  ci = [0.5 - 1.96*np.sqrt(0.5*0.5/n), 0.5 + 1.96*np.sqrt(0.5*0.5/n)]
  label = f'95% Confidence Interval: [{ci[0]:.3f}, {ci[1]:.3f}]'
  plt.plot([ci[0], ci[1]], [0, 0], 'r', lw=5, label=label)
  legend_order(plt.gca(), [0, 1], loc='upper left')
  plt.xlabel(r'$\theta$')
  plt.ylim([0, 0.2])
  #plt.xticks(ks/n)
  plt.savefig('HW9_2d.png', dpi=300, bbox_inches='tight')
  plt.savefig('HW9_2d.svg', transparent=True, bbox_inches='tight')
