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
