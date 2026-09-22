# Point Estimate Definition

Define "point estimate".

# Sampling Distribution

Give an example of a sampling distribution.

# Sampling Distribution Bias

The population mean of the random variable with set of possible values $D$ is defined as

$$\mu = \sum_{x\in D} xp(x).$$

where $p(x)$ is the probability of the value $x$.

A point estimate of $\mu$ based on a random sample of $n$ values from this population is

$$\overline{X} = \frac{1}{n}\sum_{i=1}^n x_i$$

The expectation operator is defined as

$$E[h(X)] = \sum_D h(x) p(x)$$

where $D$ is the set of all possible values of $X$.

To show that $\overline{X}$ is unbiased, we use

$$E[\overline{X}] = E\left[\frac{1}{n}\sum_{i=1}^n x_i\right] = \frac{1}{n}E\left[x_1 + ... + x_n\right]$$

Justify this step. Next, we use

$$\frac{1}{n}\big( E[x_1] + ... + E[x_n] \big)= \frac{1}{n}\big(nE[X]\big) =\frac{1}{n}(n\mu)=\mu$$

This step used the fact that $E[x_1]=E[x_2]=...=E[X]$. Justify this.

# Sampling Distribution Variance

1. How does the variance of of the point estimate of $\sigma^2$, $S^2$, depend on $n$?

2. Given two point estimates that have no bias, should the one with a lower sampling distribution variance be used?

# Point Estimate Choice

Recall that $\overline{X}_e = (\text{max}+\text{min})/2$. Propose a numerical experiment that compares the sampling distribution of $\overline{X}_e$ with that of $\overline{X}$.

On p 249 of Devore, it is noted that the best estimator for $\mu$ depends crucially on which distribution is being sampled from and that "If the underlying distribution is uniform, the best estimator is $\overline{X}_e$; this estimator is greatly influcence by outlying observations, but the lack of tails makes such observations impossible."

# Interval Estimate

1. Define an interval estimate.
2. How is an interval estimate relate to a sampling distribution?

