import math

# Average probability of event in each hour
p = 900/(1000*24)
lambda_ = 900/(1000*24)
print(lambda_)
# Part 1.

# Poisson solution
t = 24
x = 2
Px = ((lambda_*t)**x)*math.exp(-lambda_*t)/math.factorial(x)
print(Px)

# Binomial solution
Px = math.factorial(24)/(math.factorial(x)*math.factorial(24-x)) * p**x * (1-p)**(24-x)
print(Px)