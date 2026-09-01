
from math import log, exp, factorial, pi

for n in [1, 10, 100]:
  print(f"{n}! = {factorial(n):.2e}")
  approx1 = exp(n*log(n) - n)
  approx2 = exp(n*log(n) - n + 0.5*log(2*pi*n))
  pct1 = (approx1 - factorial(n)) / factorial(n)
  pct2 = (approx2 - factorial(n)) / factorial(n)
  print(f"  exp(Nln(N) - N) = {approx1:.2e} (pct error = {pct1:.2%})")
  print(f"  exp(Nln(N) - N + 0.5ln(2piN)) = {approx2:.2e} (pct error = {pct2:.2%})")
