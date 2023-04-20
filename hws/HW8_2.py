import numpy as np
import matplotlib.pyplot as plt
try:
    %config InlineBackend.figure_formats = ['svg']
except:
    pass

N = 1000
a1 =  0.7
a2 = -0.2

z = np.zeros(N)
eps = np.random.normal(0.0, 1.0, size=N)
for i in range(2,N):
    z[i] = a1*z[i-1] + a2*z[i-2] + eps[i]

# 8.2.1

## 8.2.1.1
zbar = np.mean(z)
c = np.full(N, np.nan)
for k in range(0, N):
    c[k] = 0
    for t in range(0, N-k):
        c[k]= c[k] + (z[t] - zbar)*(z[t+k] - zbar)

r = c/c[0]

if True:
    plt.figure()
    plt.plot(z)
    plt.xlabel('$t$')
    plt.ylabel('$z$')
    plt.ylim([-7,7])
    plt.grid()

## 8.2.1.2
rho1 = a1/(1-a2)
rho2 = a2 + a1**2/(1-a2)

print('r1 = {0:4.1f}; ρ1 = {1:4.2f}'.format(r[1], rho1))
print('r2 = {0:4.1f}; ρ2 = {1:4.2f}'.format(r[2], rho2))
rho = np.full(N, np.nan)
rho[0] = 1
rho[1] = rho1
rho[2] = rho2

for m in range(3,N):
    rho[m] = a1*rho[m-1] + a2*rho[m-2]

title = '$z_t={0:.1f}z_{{t-1}}{1:+.1f}z_{{t-2}}+ε_t$; $ε_t$ ~ $\mathcal{{N}}(0,1)$'
title = title.format(a1,a2)

if True:
    plt.figure()
    plt.plot(r)
    plt.plot(rho)
    plt.xlabel('$t$')
    plt.legend(['$r$','ρ'])
    plt.title('Full $t$ scale\n'+title)
    plt.ylim([-1,1])
    #plt.xlim([0,10])
    plt.grid()
    plt.savefig('figures/HW8_2_1a.svg', transparent=True)
    plt.savefig('figures/HW8_2_1a.png', transparent=True, dpi=300)

    plt.figure()
    plt.plot(r)
    plt.plot(rho)
    plt.xlabel('$t$')
    plt.legend(['$r$','ρ'])
    plt.title('Reduced $t$ scale\n'+title)
    plt.ylim([-1,1])
    plt.xlim([0,10])
    plt.grid()
    plt.savefig('figures/HW8_2_1b.svg', transparent=True)
    plt.savefig('figures/HW8_2_1b.png', transparent=True, dpi=300)

## 8.2.1.3

Nb = 1000
r1 = np.zeros(Nb)
z = np.zeros(N)

for b in range(0, Nb):
    eps = np.random.normal(0.0, 1.0, size=N)
    for i in range(2,N):
        z[i] = a1*z[i-1] + a2*z[i-2] + eps[i]

    zbar = np.mean(z)
    c = np.full(2, np.nan)
    for k in range(0, len(c)):
        c[k] = 0
        for t in range(0, N-k):
            c[k]= c[k] + (z[t] - zbar)*(z[t+k] - zbar)

    r1[b] = c[1]/c[0]

bins = np.linspace(0.5, 0.66, 9)
plt.figure()
plt.grid()
plt.hist(r1, color='k', bins=bins)
plt.title('Parametric bootstrap sampling dist of $r_1$')
plt.xlabel('$r_1$')
plt.xticks(bins)
plt.axvline(x=r[1])
plt.legend(['Sample $r_1$','# in bin'])
plt.savefig('figures/HW8_2_1c.svg', transparent=True)
plt.savefig('figures/HW8_2_1c.png', transparent=True, dpi=300)

r1.sort()
lb = int(Nb*0.05)
ub = Nb - lb
print('99% CI for r1 = [{0:.2f}, {1:.2f}]'.format(r1[lb], r1[ub]))

# 8.2.2
ahat1 = r[1]*(1-r[2])/(1-r[1]**2)
ahat2 = (r[2]-r[1]**2)/(1-r[1]**2)

print('a1 = {0:4.1f}; ahat1 = {1:4.2f}'.format(a1, ahat1))
print('a2 = {0:4.1f}; ahat2 = {1:4.2f}'.format(a2, ahat2))

# Sampling distribution and CI can be computed following procedure used for r1.
