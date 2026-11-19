from lib import dft, pdf
import numpy as np
from scipy.stats import chi2

n = 40
A = 0
σ = 1
i0 = 5
ne = 10000

def signal(n, A, σ, i0):
  t = np.arange(n)
  epsilon = np.random.normal(loc=0, scale=σ, size=n)
  y = epsilon + A*np.sin(2 * np.pi * (i0/n) * t )
  return y


def periodograms(n, A, σ, i0, ne):
  I = np.zeros((n//2, ne))
  for exp in range(ne):
    y = signal(n, A, σ, i0=i0)
    I[:, exp], f = dft.periodogram(y)
  return I, f


def plot_pdfs(I_column):
  from matplotlib import pyplot as plt
  dx = 1
  e_pdf, bin_centers, _ = pdf.pdf(I_column, dx, a=0.5)
  plt.bar(bin_centers, e_pdf*dx, width=dx, align='center', label='Numerical (estimate)')

  # Add chi^2_2
  plt.plot(bin_centers, chi2.pdf(bin_centers, df=2), 'k.', label=r'$\chi^2_2$ (exact)')

  plt.legend()
  plt.ylabel('PDF')
  plt.xlabel(f'$I_{{{i0}}} = \\frac{{n}}{{2}} (a_{{{i0}}}^2 + b_{{{i0}}}^2)$')

# Plot the numerically estimated sampling distribution of I_5 and compare
# with the exact sampling distribution of I_5, which is chi^2_2
I, f = periodograms(n, A, σ, i0, ne)
I5 = I[i0-1, :]
plot_pdfs(I5)

# Compute the periodogram of the given y and print I(f_{i0})
y = [0.9286277042696437, 1.7045034622025108, 1.2050233168496631, 1.3845192085275169, 0.7431622214379727, -0.5679286290463883, -0.48302490734666614, -1.5114589444139053, -1.764577341185066, -1.418292052669948, 0.5691222893590951, 1.5289585406721782, -0.460701510623547, 1.2776882948506474, -2.6770015657394532, -0.08993270340891461, -1.3686260170604216, 0.41212214197362895, -1.8219485330400222, -0.9514020560144467, -0.2935061113992405, -1.248384532410733, 0.3339742830685172, 0.39336906362403434, -0.025834598877514714, -0.811666785526905, 0.6705521440034906, 0.2112093102712752, 0.6226097153544842, 0.1183604974191117, -0.05356324386643412, -0.6882896771055533, -0.48979126500005604, -0.09310013954981483, 0.28948660168776613, 2.162314587980623, 1.9419564408387695, 1.046727620184002, -1.03476056281878, -0.12472014892027071]
I_y, f_y = dft.periodogram(y)

# Find fraction of area under chi^2_2 curve above I(f_{i0})
# This corresponds to the probability of observing a periodogram value greater
# than I(f_{i0})
fraction_above = 1 - chi2.cdf(I_y[i0-1], df=2)
print(f"I(f_{i0}) = {I_y[i0-1]}")
print(f"Fraction of area above I(f_{i0}): {fraction_above}")

# I(f_5) = 9.176689137753517
# Fraction of area above I(f_5): 0.010169679650502306

# Add an annotation for I(f_{i0}) on the plot
from matplotlib import pyplot as plt
statement = f"If case B., prob. of observing I(f_{i0}) or larger is {fraction_above:.3f}"
plt.title(f'Sampling Distribution of $I_{{{i0}}}$\n{statement}')
plt.axvline(I_y[i0-1], color='r', linestyle='--', label=f'I(f_{{{i0}}})')
text = f' Area under $\\chi^2_2$\n above $I(f_{{{i0}}})={I_y[i0-1]:.1f}$: {fraction_above:.3f}'
plt.text(I_y[i0-1], plt.ylim()[1]*0.4, text, color='r', ha='left')

plt.savefig("HW8_1.png")

# Statistical statement:
# The I_5 value for the given y is such that there is a ~1.02% chance of observing
# this value or larger.
#
# Statistical statement as a hypothesis test:
#   H0: no periodic component at frequency f_5
#   Ha: periodic component at frequency f_5
#   with a rejection region corresponding to a 5% significance level,
#   we will reject H0 if I_5 falls in the top 5% of the chi^2_2 distribution.
#
#   In this case, the observed I_5 is in the top 1.02% of the chi^2_2 distribution,
#   which is more extreme than the 5% significance level. Therefore, we reject H0
#   with P = 0.01.
#
#   This conclusion corresponds to a type I error because I generated y using
#   y_t = epsilon_t (no periodic component)!

# Part 5.

# The sampling distribution of I_5 is approximately chi^2_2, so we can construct a 95% confidence interval using the chi^2 distribution.
# https://www.stat.berkeley.edu/~bartlett/courses/153-fall2010/lectures/20.pdf
chi_upper = chi2.ppf(0.025, df=2)
chi_lower = chi2.ppf(0.975, df=2)
I5 = I_y[i0-1]
# Because we used sigma^2 = 1, the factor of 2/f(v) = 1.
ci_lower = I5/chi_lower
ci_upper = I5/chi_upper
CI = [I_y[i0-1] - ci_lower, I_y[i0-1] + ci_upper]  # Use the upper bound of the chi^2 interval for the margin
print(f"95% confidence interval for I_5: {CI}")

# To test that this CI is correct, we could simulate 10,000 y's using case B.
# and compute the 10,0000 corresponding I_5 values. Then, we could compute the
# fraction of the 10,0000 CIs that overlapped the expected I_5 value of 2
# (when sigma^2= 1, I_5 is chi^2_2 distributed and the mean of chi^2_v is v).
