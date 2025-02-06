


# Distributions

Discrete distributions used thus far

- The Binomial Distribution, which follows from Bernoulii Trials.
- The Poisson Distribution, which is limiting case of Binomial Distribution (requires $n\gg 1$ and valid for $kp\ll 1$ and $k/n\ll 1$) (did derivation in class).
- The Exponential Distribution (aka "Waiting Time Distribution)", which is the distribution of the time between successes (aka "events") in a Poisson-distributed variable (derivation is not trivial).
- The Normal or Gaussian distribution (note Normal and Gaussian are used interchangeably), which is a limiting case of Binomial Distribution (and Poisson Distribution, but not Exponential distribution).

Three key distributions are

- The "Standard Normal" is the **sampling distribution** of the quantity

   $$z = \frac{\overline{X}-\mu}{\sigma/\sqrt{n}}$$

   **Constraint**: $X$ is a random variable with mean $\mu$ and standard deviation $\sigma$ **and $\boldsymbol{n}$ is large** (unless the random variable is normally distributed, which case any $n$)

   A standardized variable will have a histogram that is centered on the origin and a standard deviation of unity.

   If $X$ is a random variable from _almost any_ probability distribution with mean $\mu$ and standard deviation $\sigma$, the sampling distribution of $z$ is the Standard Normal.

- The "Student $t$" distribution is the **sampling distribution** of the quantity

   $$t = \frac{\overline{X}-\mu}{S/\sqrt{n}}$$

   where

   $$S = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (X-\overline{X})^2}$$

   **Constraint**: $X$ is a Gaussian--distributed random variable. Both the numerator and denominator of $t$ will vary from sample to sample and so we expect that the histogram of 

   $$t=\frac{\overline{X}-\mu}{S/\sqrt{n}}$$

   to be "fatter" or have "fatter tails" than

   $$z=\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}$$

   The $t$ distribution is actually a family of distributions that depend on $n$ and so "$t$ distribution" is ambiguous. We usually discuss "a $t$ distribution with $\nu$" degrees of freedom, where $\nu \equiv n-1$.

   <img src="hws/figures/compare_gaussian_and_t.svg"/>

    ```Python
    import numpy as np
    from matplotlib import pyplot as plt
        
    n     = 5
    mu    = 10
    sigma = 20

    # n x 10,000 matrix
    X = mu + sigma*np.random.randn(n, 10000)

    # Compute 10,000 averages of n values
    Xbar = np.mean(X, axis=0)

    V = np.var(X, axis=0, ddof=1)
    S = np.sqrt(V)

    z = (Xbar - mu)/(sigma/np.sqrt(n))
    t = (Xbar - mu)/(S/np.sqrt(n))
    plt.figure()
    plt.grid()
    plt.hist(t, bins=np.linspace(-5,5,50), edgecolor='k', facecolor='k')
    plt.hist(z, bins=np.linspace(-5,5,50), edgecolor='b', facecolor='b')
    plt.xlabel('$t$ or $z$')
    plt.ylabel('# in bin')
    plt.title('$10^4$ t and z values using $n=4$')
    plt.legend(['$t$','$z$'])

    plt.savefig("figures/compare_gaussian_and_t.png", format="png", transparent=True)
    plt.savefig("figures/compare_gaussian_and_t.svg", format="svg", transparent=True)
    ```

- The Chi-square ($\chi^2$) distribution is the **sampling distribution** of the quantity $e$ (think "error") 

   $e^2_1 = X_1^2 + ... + X_n^2$

   $...$

   $e^2_{\infty} = X_1^2 + ... + X_n^2$

   **Constraint**: $X$ is a Gaussian--distributed random variable.

   Similar to the $t$ distribution, the $\chi^2$ distribution is actually a family of distributions that depends on $n$.

   We use the $\chi^2$ distribution deriving error bars and confidence intervals for mean-square errors and power spectra.

- Often we do not know the **sampling distribution**; in the examples given above, there was a severe constraint on the distribution of $X$. In general, given an arbitrary distribution of $X$ and an arbitrary statistic derived from it, we don't know the sampling distribution of the statistic.

   We can use the **boostrap** method to derive a **sampling distribution** using data from a single sample.

   Suppose we don't know that $X$ is Gaussian--distributed. Then we don't know how

   Suppose that we have a quantity $Y$

   $$Y_1 = X_1^2 + ... + X_n^2$$

   that we compute from a set of measurements $X_1, ..., X_n$ and we can assume the measurements are independently distributed random variables, but we don't know if their distribution is Gaussian. As a result, we don't know how $Y$ will be distributed -- it does not fit the constraint of the $\chi^2$ distribution and nobody has worked out the expected distribution of $e$ for this calculation.

   We can "bootrap" a sampling distribution by drawing $n$ values from the list $[X_1,...X_n]$ with replacement and computing $Y^{\*}_1$. We repeat $10,000$ times. The distribution of 10,000 $Y^{\*}$ values is a good approximation to the unknown sampling distribution of $Y$. See also page 251 of Devore.


