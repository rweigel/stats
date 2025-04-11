import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'

# P_k = (N choose k) * θ^k * (1-θ)^(N-k)

# 1.
# If 𝒟 = [H], then N = 1 and k = 1 and P(𝒟|θ) = θ.

# 2.
# p(θ|𝒟) = P(𝒟|θ)p(θ)/P(𝒟), where
# P(𝒟) = ∫ P(𝒟|θ)p(θ)dθ with limits of θ = 0 to 1.
# when p(θ) = 1 and P(𝒟|θ) = θ, P(𝒟) = 1/2

# 3.
# p(θ|𝒟=[H]) = P(𝒟|θ)p(θ)/P(𝒟) = 2θ.
θ = np.linspace(0, 1, 100)
y = 2 * θ
plt.plot(θ, y, 'k-')
plt.xlabel('θ')
plt.ylabel('p(θ|$\\mathcal{D}$=[H])')
plt.title('p(θ) = 1')
plt.grid()
plt.savefig('HW8_3a.png', dpi=300, bbox_inches='tight')
plt.savefig('HW8_3a.svg', transparent=True, bbox_inches='tight')
plt.close()

# 4.
# If 𝒟 = [H, T], then N = 2 and k = 1 and P(𝒟|θ) = 2θ(1-θ) and
# if p(θ) = 1, then P(𝒟) = ∫ P(𝒟|θ)p(θ)dθ with limits of θ = 0 to 1
# and P(𝒟) = 1 - 2/3 = 1/3, giving
# p(θ|𝒟=[H,T]) = 6θ(1-θ).
θ = np.linspace(0, 1, 100)
y = 6*θ*(1-θ)
plt.plot(θ, y, 'k-')
plt.xlabel('θ')
plt.ylabel('p(θ|$\\mathcal{D}$=[H,T])')
plt.title('p(θ) = 1')
plt.grid()
plt.savefig('HW8_3b.png', dpi=300, bbox_inches='tight')
plt.savefig('HW8_3b.svg', transparent=True, bbox_inches='tight')
plt.close()

# 6.
# P(𝒟) = ∫ P(𝒟|θ)p(θ)dθ
# p(θ) = A e^(-(θ-0.5)^2/0.1), where A is a constant
# P(𝒟|θ) = 2θ(1-θ)
# P(𝒟) = ∫ P(𝒟|θ)p(θ)dθ = 2A ∫ θ(1-θ)e^(-(θ-0.5)^2/0.1)dθ
# Using Wolfram Alpha with limits of 0 to 1, we get
# P(𝒟) = 0.113363*2A
# Thus
# p(θ|𝒟) = P(𝒟|θ)p(θ)/P(𝒟) = 2θ(1-θ)Ae^(-(θ-0.5)^2/0.1)/0.113363*2A
# p(θ|𝒟) = P(𝒟|θ)p(θ)/P(𝒟) = θ(1-θ)e^(-(θ-0.5)^2/0.1)/0.113363

θ = np.linspace(0, 1, 100)
y = θ*(1-θ)*np.exp((-(θ-0.5)**2/0.1))/0.113363
plt.plot(θ, y, 'k-')
plt.xlabel('θ')
plt.ylabel('p(θ|$\\mathcal{D}$=[H,T])')
plt.title(r'p(θ)$\propto$exp(-(θ-0.5)$^2$/0.1)', fontname='Times New Roman')
plt.grid()
plt.savefig('HW8_3c.png', dpi=300, bbox_inches='tight')
plt.savefig('HW8_3c.svg', transparent=True, bbox_inches='tight')
plt.close()

# Demonstration of the effect of prior on posterior
# In general, we expect prior to dominate when we have little data and
# have less influence as we get more data.

# Suppose 100 tosses and 40 heads, 60 tails
# P(𝒟|θ) ∝ θ^40 (1-θ)^60
# If diffuse prior,
# P(θ|𝒟) ∝ P(𝒟|θ)
# If gaussian prior,
# P(θ|𝒟) ∝ P(𝒟|θ) e^(-(θ-0.5)^2/0.1)

θ = np.linspace(0, 1, 1000)
dθ = θ[1] - θ[0]

P_D_given_θ = θ**40 * (1-θ)**60

# Diffuse prior
P_θ_d = 1
P_θ_given_D_d = P_D_given_θ*P_θ_d
P_θ_given_D_d = P_θ_given_D_d / (dθ*np.sum(P_θ_given_D_d))
# Note that this is approximate - could compute denominator analytically

# Gaussian prior
P_θ_g = np.exp((-(θ-0.5)**2/0.1))
P_θ_g = P_θ_g / (dθ*np.sum(P_θ_g))
P_θ_given_D_g = P_D_given_θ*P_θ_g
P_θ_given_D_g = P_θ_given_D_g / (dθ*np.sum(P_θ_given_D_g))
# Note that this is approximate - could compute denominator analytically

plt.title(r'$\mathcal{D}$ = 40 heads, 60 tails')
plt.plot(θ, P_θ_given_D_d, 'k--', label='p(θ|$\\mathcal{D}$) for Diffuse prior')
plt.plot(θ, P_θ_given_D_g, 'k-', label='p(θ|$\\mathcal{D}$) for Gaussian prior')
plt.plot(θ, P_θ_g, 'k:', label='Gaussian prior p(θ)')
plt.grid()
plt.xlabel('θ')
plt.legend()
plt.savefig('HW8_3d.png', dpi=300, bbox_inches='tight')
plt.savefig('HW8_3d.svg', transparent=True, bbox_inches='tight')
