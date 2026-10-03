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
Answer 1: [9.52, 10.48]
Answer 2: [9.55, 10.45]
Answer 3:
   n=  5:  2.56,  1.81
   n= 10:  1.47,  1.28
   n= 15:  1.14,  1.04
   n= 20:  0.96,  0.90
   n= 25:  0.85,  0.81
   n= 30:  0.77,  0.74
   n= 35:  0.71,  0.68
   n= 40:  0.66,  0.64
   n= 45:  0.62,  0.60
   n= 50:  0.59,  0.57
   n= 55:  0.56,  0.54
   n= 60:  0.53,  0.52
   n= 65:  0.51,  0.50
   n= 70:  0.49,  0.48
   n= 75:  0.47,  0.47
   n= 80:  0.46,  0.45
   n= 85:  0.44,  0.44
   n= 90:  0.43,  0.43
   n= 95:  0.42,  0.41
   n=100:  0.41,  0.40
"""