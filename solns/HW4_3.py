import math
import numpy as np
import matplotlib.pyplot as plt
import datetime as datetime
import scipy.stats as stats

test = True

def pmf(bin_edges, data, **kwargs):
  import warnings
  if np.min(data) < bin_edges[0]:
    warnings.warn(f'Minimum data value {np.min(data)} is less than minimum bin edge {bin_edges[0]}.', stacklevel=2)
  if np.max(data) > bin_edges[-1]:
    warnings.warn(f'Maximum data value {np.max(data)} is greater than maximum bin edge {bin_edges[-1]}.', stacklevel=2)

  db = bin_edges[1:] - bin_edges[0:-1]
  bin_centers = bin_edges[0:-1] + db/2

  n, _ = np.histogram(data, bins=bin_edges)
  pmf = n/len(data)
  #print(np.sum(pmf))
  plt.grid(axis='y', color=[0.5, 0.5, 0.5], ls=':')
  width = np.min(db)
  if np.all(data.astype(int) == data):
    width = width/5
  kwargs = {
            "edgecolor": "w",
            "linewidth": 0.5,
            **kwargs,
            "width": width
          }
  plt.bar(bin_centers, pmf, **kwargs)

def read_and_prep(data_file):
  data = np.loadtxt(data_file)

  data = data.astype(int)
  to = datetime.datetime(*data[0, :5])
  tf = datetime.datetime(*data[-1, :5])
  dt = tf - to
  # m_g = "minute grid" of with the number of minutes
  # between to and tf (inclusive)
  m_g = np.zeros(1+int(dt.total_seconds() / 60))
  for i in range(1, len(data)):
    print(f"Flare at {data[i, :5]}")
    # Time in minutes since first minute
    dt = datetime.datetime(*data[i, :5]) - to
    idx = int(dt.total_seconds() / 60)
    m_g[idx] = 1

  n_m = 24*60
  print("Total number of minutes: %d" % len(m_g))
  print("Total number of days: %f" % (len(m_g)/(24*60)))
  n = 24*60*np.floor(len(m_g)/n_m)
  if n != len(m_g):
    print("Truncating to integer number of days since first flare")
  m_g = m_g[0:int(n)] # Truncate to integer number of days
  # Each row in m_g_r is a day, each column is a minute in day
  m_g_r = np.reshape(m_g, (int(n/n_m), n_m))
  fpd = np.sum(m_g_r, axis=1)

  return to, fpd, m_g

def conditional_probabilities(m_g, test):

  p   = np.sum(m_g)/m_g.size

  #For testing
  #p = 0.3
  #m_g = np.random.binomial(m_g.size, p, m_g.size)

  n11 = np.logical_and(m_g[1:] == 1, m_g[0:-1] == 1).nonzero()[0].size
  n10 = np.logical_and(m_g[1:] == 1, m_g[0:-1] == 0).nonzero()[0].size
  n00 = np.logical_and(m_g[1:] == 0, m_g[0:-1] == 0).nonzero()[0].size
  n01 = np.logical_and(m_g[1:] == 0, m_g[0:-1] == 1).nonzero()[0].size

  nF = np.sum(m_g)
  nxF = m_g.size - nF
  if test:
    assert(nF == 5)

  p11 = n11/nF
  p10 = n10/nxF
  p00 = n00/nxF
  p01 = n01/nF

  print("P(F)             = %.8f" % p)
  print("P(F_t|F_{t-1})   = %.8f" % p11)
  print("P(F_t|xF_{t-1})  = %.8f" % p10)
  print("xP(F)            = %.8f" % (1-p))
  print("P(xF_t|xF_{t-1}) = %.8f" % p00)
  print("P(xF_t|F_{t-1})  = %.8f" % p01)

if not test:
  to, fpd, m_g = read_and_prep("HW4_3.xray.txt")
else:
  to, fpd, m_g = read_and_prep("HW4_3.xray.fake.txt")
  assert(np.all(fpd == np.array([0., 2., 3., 0.])))
  non_zero_indices = np.nonzero(m_g)[0]
  print("Indices of non-zero values in m_g:", non_zero_indices)
  assert(np.all(non_zero_indices == np.array([1441,2160,2881,3362,3600])))
  assert(m_g.size == 24*60*4)

conditional_probabilities(m_g, test)
tof = to.strftime('%Y-%m-%dT%H:%M')
plt.plot(fpd, 'k')
plt.xlabel(f"Days since {tof}")
plt.ylabel("# of flares")
plt.grid()
plt.savefig("HW4_3a.png", dpi=300)
plt.savefig("HW4_3a.svg", transparent=True)
plt.close()

# Exact solutions

# P(k) = mu^k/k! * e^(-mu)
mu = np.mean(fpd)
P_P = np.zeros(int(np.max(fpd))+1)
P_B = np.empty(len(P_P))
ks = np.arange(0, len(P_P))
p_o = np.sum(fpd)/len(fpd)
for k in ks:
  P_P[k] = mu**k/math.factorial(k) * np.exp(-mu)

P_B = stats.binom.pmf(ks, 24*60, p_o/(24*60))

n, _ = np.histogram(fpd, bins=range(0, int(np.max(fpd))+1))
bin_edges = np.arange(-0.5, int(np.max(fpd))+1)
pmf(bin_edges, fpd, color='black', label='Observed')
plt.plot(ks, P_P, 'ko', label=f'Poisson $\\lambda={p_o:.2f}$/day', markerfacecolor='none')
plt.plot(ks, P_B, 'k.', label='Binomial')
plt.ylabel('Probability')
plt.xlabel('# of flares/day')
plt.xlim([0, 20])
plt.xticks(np.arange(0, 21, 2))
plt.legend()
plt.savefig("HW4_3b.png", dpi=300)
plt.savefig("HW4_3b.svg", transparent=True)
plt.close()
