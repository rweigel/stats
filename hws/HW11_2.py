import numpy as np
from numpy import real, imag, arange
from numpy.fft import fft, ifft

def dft0(y):
    N = len(y)
    q = int(N/2)
    a = np.full(q+1, np.nan)
    b = np.full(q+1, np.nan)
    f = np.full(q+1, np.nan)
    t = np.arange(N)
    a[0] = np.mean(y)
    b[0] = 0
    f[0] = 0
    for i in range(1, q+1):
        f[i] = i/N
        a[i] = np.sum(y*np.cos(2*np.pi*f[i]*t))
        b[i] = np.sum(y*np.sin(2*np.pi*f[i]*t))
    return f, 2*a/N, 2*b/N

def dft1(y):
    N = len(y)
    if np.round(N/2) == N/2:
        q = int(N/2)
    else:
        q = int((N-1)/2)

    c = fft(y)
    a = real(c)
    a[0] = a[0]/N
    b = -imag(c)
    f = arange(0, q+1)/N
    return f, 2*a[0:q+1]/N, 2*b[0:q+1]/N

#y = [0, 1, 0, -1]
y = np.random.randn(100)
f0, a0, b0 = dft0(y)
f1, a1, b1 = dft1(y)

if len(f0) < 10:
    print(f0)
    print(f1)
    print(a0)
    print(a1)
    print(b0)
    print(b1)

eps = np.finfo(np.double).eps;

print(f"max(f0-f1)/eps = {(np.max(f0-f0))/eps}")
print(f"max(a0-a1)/eps = {(np.max(a0-a1))/eps}")
print(f"max(b0-b1)/eps = {(np.max(b0-b1))/eps}")
