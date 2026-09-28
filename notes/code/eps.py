
import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(loc=0, scale=1/10, size=100)

def findeps(x, f):
  epsi = np.linspace(0, 1, 100)

  for eps in epsi:
    nin = len(x[(x < eps) & (x > -eps)])
    plt.title(f"eps={eps}, nin={nin} fin={nin/len(x)}")
    plt.hist(x, bins=10)
    plt.vlines([-eps, eps], ymin=0, ymax=plt.gca().get_ylim()[1], colors='r', linestyles='dashed')  
    plt.show()

    if nin/len(x) >= f:
      return eps
  return None

f = 0.99
eps = findeps(x, f)
print(f"Found eps: {eps}")