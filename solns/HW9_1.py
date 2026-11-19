from math import sqrt
from scipy.stats import norm

n = 10
α = 0.01
z = norm.ppf(1 - α/2)
p̂ = 0.4
q̂ = 1 - p̂
p̃ = (p̂ + z**2/(2*n))/(1 + z**2/n)
print(f'p̃ = {p̃:5.2f}')

Δ = sqrt( p̂*q̂/n + z**2/(4*n**2) ) / (1 + z**2/n)
print(f'Δ = {Δ:5.2f}')

CI_score = [p̃ - Δ, p̃ + Δ]
CI_large = [p̂ - z*sqrt(p̂*q̂/n), p̂ + z*sqrt(p̂*q̂/n)]
print(f'"Score" CI:      {CI_score[0]:5.2f} - {CI_score[1]:5.2f}')
print(f'Large sample CI: {CI_large[0]:5.2f} - {CI_large[1]:5.2f}')
# "Score" CI:       0.32 -  0.56
# Large sample CI:  0.00 -  0.80