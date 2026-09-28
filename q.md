For each problem, I will give students a few minutes to think of an answer without referring to notes or looking anything up.

Then we will reach a consensus as a group.

# Point Estimate Definition

Define "point estimate".

# Sampling Distribution

Give an example of a sampling distribution.

# Sampling Distribution Bias

The population mean of the random variable with a set of possible values $D$ is defined as

$$\mu = \sum_{x\in D} xp(x).$$

where $p(x)$ is the probability of the value $x$ and $x\in D$ means "for all $x$ in $D$".

A point estimate of $\mu$ based on a random sample of $n$ values from this population is

$$\overline{X} = \frac{1}{n}\sum_{i=1}^n x_i$$

The expectation operator is defined as

$$E[h(X)] = \sum_D h(x) p(x)$$

where $D$ is the set of all possible values of $X$.

To show that $\overline{X}$ is unbiased, we use

$$E[\overline{X}] = E\left[\frac{1}{n}\sum_{i=1}^n x_i\right] = \frac{1}{n}E\left[x_1 + ... + x_n\right]$$

Justify this step. Next, we use

$$\frac{1}{n}\big( E[x_1] + ... + E[x_n] \big)= \frac{1}{n}\big(nE[X]\big) =\frac{1}{n}(n\mu)=\mu$$

1. This step used the fact that $E[x_1]=E[x_2]=...=E[X]$. Justify this.
2. In a previous homework, you approximated the expectation value of $\overline{X}$. What problem was this?

# Sampling Distribution Variance

1. How does the variance of the sampling distribution of $S^2$, the point estimate of $\sigma^2$, depend on $n$?

2. Given two point estimates that have no bias, should the one with a lower sampling distribution variance be used?

# Point Estimate Choice

Recall that $\overline{X}_e = (\text{max}+\text{min})/2$. Propose a numerical experiment that compares the sampling distribution of $\overline{X}_e$ with that of $\overline{X}$.

On p. 249 of Devore, it is noted that the best estimator for $\mu$ depends crucially on which distribution is being sampled from and that "If the underlying distribution is uniform, the best estimator is $\overline{X}_e$; this estimator is greatly influenced by outlying observations, but the lack of tails makes such observations impossible."

# Interval Estimate

1. Define an interval estimate.
2. How is an interval estimate related to a sampling distribution?
3. What are some types of interval estimates?

# Deriving a Confidence Interval

If $Z\sim\mathcal{N}(0,1)$ ($Z$ is a random variable that is normally distributed with a mean of zero and variance of 1), then

$P(-1.96 < Z < 1.96) = 0.95$

Where do the numbers $1.96$ and $0.95$ come from?

Devore computes a confidence interval for $\overline{X}$ by starting with

$$P\left(-1.96 < \frac{\overline{X}-\mu}{\sigma/\sqrt{n}} < 1.96\right) = 0.95$$

Why was this form used for $Z$?

# Computing a Confidence Interval

##

A $95$% confidence interval for the mean $\mu$ of a normal population when the value of $\sigma$ is known is given by

$$\left(\overline{x}-1.96\frac{\sigma}{\sqrt{n}}, \quad \overline{x}+1.96\frac{\sigma}{\sqrt{n}}\right)$$

How is this equation related to

$$P\left(-1.96 < \frac{\overline{X}-\mu}{\sigma/\sqrt{n}} < 1.96\right) = 0.95?$$

##

More generally, a $100(1-\alpha)$% confidence interval for the mean $\mu$ of a normal population when the value of $\sigma$ is known is given by

$$\left(\overline{x}-z_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \quad \overline{x}+z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right)$$

(Devore Equation 7.5)

Suppose a sample of $100$ values had $\overline{x}=10.1$. We happen to know that the values were drawn from a population with $\sigma=1$.

What is a

* 95% CI?
* 99% CI?

Why is the statement "this is a 95\% CI for $\overline{x}$" wrong?

[Tables](https://www.craftonhills.edu/current-students/tutoring-center/mathematics-tutoring/distribution_tables_normal_studentt_chisquared.pdf)

# Interpreting a Confidence Interval

What is the correct interpretation of a confidence interval?

What is a common incorrect interpretation of a confidence interval?

# Other CIs

A random variable $T$ that is $t$ distributed with $n-1$ degrees of freedom has

$$P\left(-t_{\alpha/2,n-1} < T < t_{\alpha/2,n-1}\right) = 1-\alpha$$

It can be shown that the "standardized variable"

$$T=\frac{\overline{X}-\mu}{S/\sqrt{n}}$$

is $t$ distributed with $n-1$ degrees of freedom.

Devore Equation 7.15, p. 288 gives

Let $\overline{x}$ and $s$ be the sample mean and the sample deviation computed from the results of a random sample from a normal population with a mean $\mu$. Then a $100(1-\alpha)$% confidence interval for the mean $\mu$ is

$$\left(\overline{x}-t_{\alpha/2, n-1}\frac{s}{\sqrt{n}}, \quad \overline{x}+t_{\alpha/2, n-1}\frac{s}{\sqrt{n}}\right)$$

Suppose a sample of $100$ values had $\overline{x}=10$ and $S=1.03$. We happen to know that the values were drawn from a population with $\sigma=1$.

What is a

* 95% CI?
* 99% CI?

[Tables](https://www.craftonhills.edu/current-students/tutoring-center/mathematics-tutoring/distribution_tables_normal_studentt_chisquared.pdf)

# Experiments

The CI calculations are based on a single sample from a population, and their interpretation requires imagining a large number of experiments.

Propose a numerical experiment to explore the CI calculations.

# Bootstrapping a Confidence Interval Preliminaries

We don't always know the sampling distribution of a given statistic (a quantity computed from a sample such as $\overline{X}$ or $S$).

On a previous homework, you simulated the sampling distributions of $\overline{X}$ and $\overline{S_b^2}$ by taking samples from a known population distribution $10,000$ times.

Often, we have only one sample of size $n$ and don't have enough information about the population distribution to determine the sampling distribution analytically or numerically.

Idea: Create $10,000$ "bootstrap" experiments by sampling from the $n$ values with replacement and compute the statistic each time. Then the PDF of the statistic approximates the sampling distribution.

Suppose you are given the following code.

```python

n = 50
x_sample = np.random.normal(10, np.sqrt(10), n)
x_bar = np.mean(x_sample)
# Draw n values from x_sample with replacement
x_sample_b = np.random.choice(x_sample, size=n, replace=True)
x_bar_b = np.mean(x_sample_b)
```

1. How would you verify that `x_sample_b` is a draw of $n$ values from `x_sample` with replacement? (What is a "sanity" check?)

2. How would you modify this program to create 10,000 `x_bar_b` values?

\newpage
# Prelude to Hypothesis Testing

Figure 1. Visualization of a confidence interval showing relationship to sampling distribution.

<img src="HW6_1a.svg" width="300px"/>

Figure 2. If instead of quoting a confidence interval, we want to make a claim about the probability that $\overline{x}_\text{sample}$ had the observed value assuming the sampling distribution is correct. We reject the claim about the sampling distribution if the observed value is in the red region.

<img src="HW6_1b.svg" width="300px"/>

Questions:

1. What is the statistical interpretation of "rejection" (in the same spirit as the "trapping" explanation).
2. Could we determine if the claim can be rejected if the CI does not overlap $\mu=2$?
3. How is the probability that we mistakenly rejected the claim depend on $\alpha$?
