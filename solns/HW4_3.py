import numpy as np
import matplotlib.pyplot as plt
import datetime as datetime
import scipy.stats as stats

def pmf(bin_edges, data, color='k'):
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
  width = db
  if np.all(data.astype(int) == data):
    width = db/5
  plt.bar(bin_centers, pmf, width=width, color=color, edgecolor='w', linewidth=0.5)

def read_and_prep():
  data = np.loadtxt("xray.txt")

  data = data.astype(int)
  to = datetime.datetime(*data[0, :5])
  tf = datetime.datetime(*data[-1, :5])
  dt = tf - to
  m_g = np.zeros(1+int(dt.total_seconds() / 60))
  m_o = np.zeros(len(data))
  t = np.zeros(len(data))
  for i in range(1, len(data)):
    dt = datetime.datetime(*data[i, :5]) - to
    idx = int(dt.total_seconds() / 60)
    t[i] = idx
    m_o[i] = 1
    m_g[idx] = 1

  n_m =24*60
  n = 24*60*np.floor(len(m_g)/n_m)
  m_g = m_g[0:int(n)]
  m_g = np.reshape(m_g, (int(n/n_m), n_m))
  fpd = np.sum(m_g, axis=1)

  return to, fpd

to, fpd = read_and_prep()
tof = to.strftime('%Y-%m-%dT%H:%M')
plt.plot(fpd, 'k')
plt.xlabel(f"Days since {tof}")
plt.ylabel("# of flares")
plt.grid()
plt.savefig("HW4_3a.png", dpi=300)
plt.savefig("HW4_3a.svg", transparent=True)
plt.close()

# Exact solution
import math
def nCk(n,k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

# P(k) = mu^k/k! * e^(-mu)
mu = np.mean(fpd)
P_P = np.zeros(int(np.max(fpd))+1)
P_B = np.empty(len(P_P))
ks = np.arange(0, len(P_P))
p_o = np.sum(fpd)/len(fpd)
for k in ks:
  P_P[k] = mu**k/np.math.factorial(k) * np.exp(-mu)

print(p_o)
po = np.sum(fpd)/
P_B = stats.binom.pmf(ks, 24, p_o)
print(P_B)
n, _ = np.histogram(fpd, bins=range(0, int(np.max(fpd))+1))
bin_edges = np.arange(-0.5, int(np.max(fpd))+1)
plt.grid()
pmf(bin_edges, fpd)
plt.plot(ks, P_P, 'r.')
plt.plot(ks, P_B, 'g.')
print(P_B)
plt.ylabel('Probability')
plt.xlabel('# of flares/day')
plt.legend(['Observed', 'Poisson'])
plt.savefig("HW4_3b.png", dpi=300)
plt.savefig("HW4_3b.svg", transparent=True)
plt.close()
