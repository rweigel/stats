import numpy as np
from numpy import real, imag, arange
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt

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

    a = 2*a[0:q+1]/N
    b = 2*b[0:q+1]/N

    I = (a**2 + b**2)

    return f, a, b, I[0:q+1]

def plot(t, y, f, a, b, I, title):

    plt.figure()
    plt.plot(t, y)
    plt.title(title)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.grid()

    plt.figure()
    plt.plot(f, a, '.')
    plt.title(title)
    plt.xlabel('f')
    plt.ylabel('a')
    plt.grid()

    plt.figure()
    plt.plot(f, b, '.')
    plt.title(title)
    plt.xlabel('f')
    plt.ylabel('b')
    plt.grid()

    plt.figure()
    plt.plot(f, I, '.')
    plt.title(title)
    plt.xlabel('f')
    plt.ylabel('I')
    plt.grid()


Nt = 1000
T1  = 10
title = f'$y=\sin(2\pi t/T); T = {T1}, t = [0,...,{Nt-1}]$'
t1 = np.arange(5, Nt+5)
y1 = np.sin(2*np.pi*t1/T1)

f, a1, b1, I1 = dft1(y1)

if True:
    plot(t1, y1, f, a1, b1, I1, title)
    plt.figure()
    plt.plot(t1[0:20], y1[0:20],'k')
    plt.plot(t1[0:20], y1[0:20],'k.')
    plt.title(title)

T2  = 20
title = f'$y=\sin(2\pi t/T); T = {T1}, t = [0,...,{Nt-1}]$'
title += f'\n$y=\sin(2\pi t/T); T = {T2}, t = [{Nt},...,{2*Nt-1}]$'
t2 = np.arange(Nt, 2*Nt)
y2 = np.sin(2*np.pi*t2/T2)
y = np.append(y1,y2)
t = np.append(t1,t2)

if False:
    f, a, b, I = dft1(y)
    plot(t, y, f, a, b, I, title)

y = [0, 1, 0, -1]
yr = np.repmat(y, (2,))
#y.shape = (200, int(len(y)/200))