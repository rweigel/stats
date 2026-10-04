import numpy as np
import scipy.stats

# Checks:
# 1. t CI should be wider
# 2. As n increases, the z and t CIs should converge
# 3. As n increases, each CI should decrease in length
# 4. Could do a simulation to verify the theoretical CIs (how often they trap)
# 5. Use code with numbers from a textbook example to verify logic correct.

# Use the percent point function (inverse of the CDF) to find critical z-values
n = 20
xbar = 10
s = 1.03

def compute_cis(n):
  tc = scipy.stats.t.ppf(0.995, df=n-1)
  ci1 = [xbar-tc*s/np.sqrt(n), xbar+tc*s/np.sqrt(n)]

  zc = scipy.stats.norm.ppf(0.995)
  ci2 = [xbar-zc*s/np.sqrt(n), xbar+zc*s/np.sqrt(n)]

  return ci1, ci2

ci1, ci2 = compute_cis(n)
print(f"Answer 1: [{ci1[0]:.2f}, {ci1[1]:.2f}]")
print(f"Answer 2: [{ci2[0]:.2f}, {ci2[1]:.2f}]")

print("Answer 3:")
for n in range(5, 105, 5):
  ci1, ci2 = compute_cis(n)
  print(f"   n={n:3d}: {ci1[1]-ci1[0]:5.2f}, {ci2[1]-ci2[0]:5.2f}")

"""
Answer 1: [9.34, 10.66]
Answer 2: [9.41, 10.59]
Answer 3:
   n=  5:  4.24,  2.37
   n= 10:  2.12,  1.68
   n= 15:  1.58,  1.37
   n= 20:  1.32,  1.19
   n= 25:  1.15,  1.06
   n= 30:  1.04,  0.97
   n= 35:  0.95,  0.90
   n= 40:  0.88,  0.84
   n= 45:  0.83,  0.79
   n= 50:  0.78,  0.75
   n= 55:  0.74,  0.72
   n= 60:  0.71,  0.69
   n= 65:  0.68,  0.66
   n= 70:  0.65,  0.63
   n= 75:  0.63,  0.61
   n= 80:  0.61,  0.59
   n= 85:  0.59,  0.58
   n= 90:  0.57,  0.56
   n= 95:  0.56,  0.54
   n=100:  0.54,  0.53
"""