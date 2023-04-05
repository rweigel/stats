import numpy as np
from matplotlib import pyplot as plt
try:
    %config InlineBackend.figure_formats = ['svg']
except:
    pass

n = 9
mu_act = 132
mu_o   = 130.0 # Hypothesized
sigma  = 1.5
N = 10000

zt = 2.58 # P(|z| > zt) = 0.01
#zt = 2.33  # P(|z| > zt) = 0.05

# Ho: Data are drawn from Gaussian with mu_o = 130.
# Reject if |z| > zt
# Don't reject if |z| < zt

# Compute type I error probability (Ho rejected when true).
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
'''
P(type I)  = 0.0100 (exact)
P(type I)  = 0.0120 (simulation)
'''

# Compute type II error probability (Don't reject Ho when we should have).

zII = np.empty(N)
xbarII = np.empty(N)
for i in range(N):
    x = np.random.normal(mu_act, sigma, size=n)
    xbarII[i] = np.mean(x)
    zII[i] = (np.mean(x) - mu_o)/(sigma/np.sqrt(n))

# Number of cases where simulation's mean gave a z value in the null
# hypothes' "do not reject" region. When we get such a z value, we say
# this is a reasonable value under the assumption of the null hypothesis.
I = np.where(np.abs(zII) < zt)[0]

from scipy.stats import norm
za =  zt + (mu_o-mu_act)/(sigma/np.sqrt(n))
zb = -zt + (mu_o-mu_act)/(sigma/np.sqrt(n))
#print(za)
#print(zb)
#print(norm.cdf(za))
#print(norm.cdf(zb))
print("P(type II) = %.4f (exact) μ' = %.1f" % ((norm.cdf(za) - norm.cdf(zb)), mu_act))
print("P(type II) = %.4f (simulation) μ' = %.1f" % (I.size/N, mu_act))
'''
P(type II) = 0.0778 (exact)
P(type II) = 0.0731 (simulation)
'''

z = np.linspace(-4, 4, 100)
std_normal = (1/np.sqrt(2*np.pi))*np.exp( -z**2/2. )
T = np.linspace(128, 134, 100)

# Normal with mean of mu_o and standard deviation of sigma
normal = (1/(sigma/np.sqrt(n))/np.sqrt(2*np.pi)) \
         *np.exp( -(T-mu_o)**2/(2*(sigma/np.sqrt(n))**2) )

# pdf of temperature
fig, ax = plt.subplots()
plt.plot(T, normal, 'k', 
         label='Sampling distribution (exact)')
plt.hist(xbarI, bins=T, density=True, alpha=0.5, 
         label='Sampling distribution (bootstrapped)')
plt.plot((xbar_tl, xbar_tu), (0.005, 0.005), color='r', lw=2, 
         label='Do not reject null if $\overline{T}$ in this range')
plt.xlabel('$\overline{T}$ [degrees]')
plt.ylabel('pdf($\overline{T}$) [1/degrees]')
plt.xlim([128, 132])
plt.ylim([0,1.1])
handles, labels = plt.gca().get_legend_handles_labels()
# https://stackoverflow.com/questions/22263807/how-is-order-of-items-in-matplotlib-legend-determined
order = [0,2,1]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.savefig('figures/HW7_2a.svg', transparent=True)
plt.savefig('figures/HW7_2a.png', transparent=True)

# pdf of z (tranformed temperature variable)
fig, ax = plt.subplots()
plt.plot(z, std_normal, 'k', 
         label='Sampling distribution (exact)')
plt.hist(zI, bins=z, density=True, alpha=0.5, 
         label='Sampling distribution (bootstrapped)')
plt.plot((-zt, zt), (0.005, 0.005), color='r', lw=2,
         label='Do not reject null if $\overline{T}$ in this range')

plt.xlabel('$z=(\mu-\overline{T})/(\sigma\sqrt{n})$')
plt.ylabel('pdf(z)')
plt.xlim([-5, 5])
plt.ylim([0,0.6])
plt.legend()
plt.savefig('figures/HW7_2b.svg', transparent=True)
plt.savefig('figures/HW7_2b.png', transparent=True)

from matplotlib.patches import Rectangle
fig, ax = plt.subplots()
plt.plot(T, normal, 'k')
plt.plot((xbar_tl, xbar_tu), (0.005, 0.005), color='r', lw=2, 
         label='Do not reject null if $\overline{T}$ in this range')
nII, binsII, patches = plt.hist(xbarII, bins=T, density=True, alpha=0.5,color='b')
plt.xlabel('$\overline{T}$ [degrees]')
plt.ylabel('pdf($\overline{T}$) [1/degrees]')
plt.xlim([128, 134])
plt.ylim([0,1.2])
plt.title("$\mu'=132$")
ax.add_patch(Rectangle((xbar_tl,0),xbar_tu-xbar_tl,0.00, color=(0,1,0,0.5)))
ax.legend([
            'Sampling distribution for null (exact)',
            'Do not reject null if $\overline{T}$ in this range',
            'Simulated data - non-rejected',
            'Simulated data - rejected'
          ],
          loc='upper right')

# Modify bar colors for non-rejected part of pdf.
for patch in patches:
    xy = patch.get_xy()
    w = patch.get_width()
    if xy[0] + w/2 <= xbar_tu:
        patch.set_facecolor((0,1,0,0.5))

plt.savefig('figures/HW7_2c.svg', transparent=True)
plt.savefig('figures/HW7_2c.png', transparent=True)
