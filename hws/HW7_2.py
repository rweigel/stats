import numpy as np
from matplotlib import pyplot as plt

n = 9
mu_act = 132
mu_o   = 130.0 # Hypothesized
sigma  = 1.5
N = 10000

zt = 2.58 # z_0.005 (two-tailed)
#zt = 2.33 # z_0.01

# Ho: Data are drawn from Gaussian with mu_o = 130.
# Reject if |z| > zt
# Don't reject if |z| < zt

# Test of type I (Ho rejected when it is true b/c mu = 132)
zI = np.empty(N)
xbarI = np.empty(N)
for i in range(N):
    x = np.random.normal(mu_o, sigma, size=n)
    xbarI[i] = np.mean(x)
    zI[i] = (np.mean(x) - mu_o)/(sigma/np.sqrt(n))

xbar_tl = -zt*sigma/np.sqrt(n) + mu_o
xbar_tu = +zt*sigma/np.sqrt(n) + mu_o

I = np.where(np.abs(zI) > zt)[0]
print('P(type I)  = 0.0100 (exact)')
print('P(type I)  = %.4f (simulation)' % (I.size/N))

z = np.linspace(-4, 4, 100)
std_normal = (1/np.sqrt(2*np.pi))*np.exp( -z**2/2. )

fig, ax = plt.subplots()
plt.plot(z, std_normal, 'k', label='Null hypothesis distribution (exact)')
plt.hist(zI, bins=z, density=True, alpha=0.5, label='Null distribution (bootstrapped)')
plt.plot((-zt, zt), (0.01, 0.01), color='r', lw=2, label='Do not reject null if $\overline{T}$ in this range')
plt.xlabel('$z$')
plt.ylabel('pdf')
plt.xlim([-3, 3])
plt.ylim([0,0.6])


T = np.linspace(128, 134, 100)
normal = (1/(sigma/np.sqrt(n))/np.sqrt(2*np.pi))*np.exp( -(T-mu_o)**2/(2*(sigma/np.sqrt(n))**2) )

if True:
    from matplotlib.patches import Rectangle, FancyArrowPatch
    fig, ax = plt.subplots()
    plt.plot(T, normal, 'k', label='Null hypothesis distribution (exact)')
    plt.hist(xbarI, bins=T, density=True, alpha=0.5, label='Null distribution (bootstrapped)')
    #rp = Rectangle((xbar_tl,0),xbar_tu-xbar_tl,0.03, color='k', alpha=0.4, hatch='//', label='Do not reject if $\overline{T}$ in this range')
    #ax.add_patch(rp)
    plt.plot((xbar_tl, xbar_tu), (0.01, 0.01), color='r', lw=2, label='Do not reject null if $\overline{T}$ in this range')
    #ax.add_patch(p1)
    plt.xlabel('$\overline{T}$ [degrees]')
    plt.ylabel('pdf')
    plt.xlim([128, 134])
    plt.ylim([0,1])
    handles, labels = plt.gca().get_legend_handles_labels()
    # https://stackoverflow.com/questions/22263807/how-is-order-of-items-in-matplotlib-legend-determined
    order = [0,2,1]
    plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])

# Test of type II (Ho not rejected when it is false b/c mu = 132)
zII = np.empty(N)
xbarII = np.empty(N)
for i in range(N):
    x = np.random.normal(mu_act, sigma, size=n)
    xbarII[i] = np.mean(x)
    zII[i] = (np.mean(x) - mu_o)/(sigma/np.sqrt(n))

if True:
    from matplotlib.patches import Rectangle
    fig, ax = plt.subplots()
    plt.plot(T, normal, 'k')
    #ax.add_patch(Rectangle((xbar_tl,0),xbar_tu-xbar_tl,0.03, color='k', alpha=0.4, hatch='//'))
    plt.plot((xbar_tl, xbar_tu), (0.005, 0.005), color='r', lw=2, label='Do not reject null if $\overline{T}$ in this range')
    nII, binsII, patches = plt.hist(xbarII, bins=T, density=True, alpha=0.5,color='b')
    plt.xlabel('$\overline{T}$ [degrees]')
    #plt.hist(xbarII[np.where(xbarII < xbar_tu)[0]], bins=T, density=True, alpha=0.5,color='b')
    plt.ylabel('pdf')
    plt.xlim([128, 134])
    #plt.ylim([0,400])
    ax.add_patch(Rectangle((xbar_tl,0),xbar_tu-xbar_tl,0.00, color=(0,1,0,0.5)))
    ax.legend(['Null hypothesis distribution (exact)',
               'Do not reject null if $\overline{T}$ in this range',
               'Simulated data - non-rejected',
               'Simulated data - rejected'],
              loc='upper right')

for patch in patches:
    xy = patch.get_xy()
    w = patch.get_width()
    if xy[0] + w/2 <= xbar_tu:
        patch.set_facecolor((0,1,0,0.5))




# Test of type II (Don't reject Ho when we should have)

# Number of cases where simulation's mean gave a z value in the null
# hypothes' "do not reject" region. When we get such a z value, we say
# this is a reasonable value under the assumption of the null hypothesis.
I = np.where(np.abs(zII) < zt)[0]

from scipy.stats import norm
za = zt + (mu_o-mu_act)/(sigma/np.sqrt(n))
zb = -zt + (mu_o-mu_act)/(sigma/np.sqrt(n))
#print(za)
#print(zb)
#print(norm.cdf(za))
#print(norm.cdf(zb))
print('P(type II) = %.4f (exact)' % (norm.cdf(za) - norm.cdf(zb)))

print('P(type II) = %.4f (simulation)' % (I.size/N))


if False:
#    plt.plot([xbar_tl, xbar_tl], [0, 400],'k')
#    plt.plot([xbar_tu, xbar_tu], [0, 400],'k')
    plt.hist(xbarII)
    plt.plot([xbar_tl, xbar_tl], [0, 400],'k')
    plt.plot([xbar_tu, xbar_tu], [0, 400],'k')
    I = np.where(np.abs(zII) < zt)[0]



if False:
    xbar.append(np.mean(x**2))
    S = np.std(x, ddof=1)
    z.append( (np.mean(x) - mu)/(S/np.sqrt(n)) )

    bins = np.linspace(-5,10,50)
    normal = (1/np.sqrt(2*np.pi))*np.exp( -bins**2/2 )
    plt.hist(xbar, bins=bins, density=True)
    #plt.hist(xbar, density=True)
    #plt.plot(bins, normal)
    plt.xlabel('\overline{x}')
    plt.ylabel('pdf(\overline{x})')
    plt.legend(['Parametric Bootstrap pdf','Standard Normal'])