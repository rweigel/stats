import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'

N = 21
Ao = 2   # Area of dartboard
x = np.random.uniform(low=-1, high=1, size=N)
y = np.random.uniform(low=0, high=1, size=N)

dx = 0.1
xg = np.arange(-1, 1+dx, dx)

I = np.where(y < 1 - x**2)[0]

exact = 4/3

print('Numerical integration ({0:d} rectangles): {1:.5f}'.format(xg.shape[0],np.sum((1-xg**2)*dx)))
print('Exact: {0:.5f}'.format(exact))
print('Monte Carlo {0:d} points: {1:.5f}'.format(N, Ao*I.shape[0]/N))


plt.plot(x, y, 'b.',ms=2)
plt.plot(xg, 1 - xg**2,'k-')
plt.plot(x[I], y[I], 'r.',ms=2)
plt.title('N = {0:d}; Fraction red = {1:.2f}'.format(N, I.shape[0]/N))

# Notice that in 1-D, MC is less accurate that simple numerical integration.

for n in range(1, 6):
    N = 10**n
    x = np.random.uniform(low=-1, high=1, size=N)
    y = np.random.uniform(low=0, high=1, size=N)
    I = np.where(y < 1 - x**2)[0]
    A = Ao*I.shape[0]/N
    print('N = 10^{0:d}; Area = {1:.8f}'.format(n, A))

plt.savefig('HW10_3_notes.svg', transparent=True, bbox_inches='tight')
plt.savefig('HW10_3_notes.png', bbox_inches='tight', dpi=300)
