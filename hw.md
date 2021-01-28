# HW 1

This homework involves the Law of Large Numbers, confidence intervals, and the Central Limit Theorem. You do not need to fully understand the statistical theory behind these problems. 

These problems are intended to primarily be a review of the programming techniques that you will need for this class.

----

The Law of Large Numbers tells us that as $n\rightarrow \infty$ the sample average defined by

$$\overline{X}=\frac{1}{n}\sum_{i=1}^n X_i$$

will be near the population average $\mu$ with a given probability. Given $n$ samples from a population, we don't expect $\overline{X}$ to exactly match $\mu$. The Law of Large Numbers allows us to make a statement about the difference $\overline{X}-\mu$.

If you are interested, for a more formal definition of the Law of Large Numbers and proofs, see
* [Orloff and Bloom, Reading 6b](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading6b.pdf)
* Bulmer, Chapter 6 (see Piazza)
* DeGroot, Chapter 6 (see Piazza)

## Law of Large Numbers I

### a

1. Draw $n=100$ values from a population of numbers drawn from a gaussian distribution with mean $\mu=0$ and standard deviation $\sigma=1$.
2. Compute $\overline{X}$.
3. Repeat 1. and 2. $10,000$ times and plot a histogram of $\overline{X}$.

Save your program as `HW1_1a.py`. When I execute your program, I should see a histogram with $\overline{X}$ displayed in the title.

### b

1. For $n=100$, what fraction of the $10,000$ $\overline{X}$s were in the range $[-0.01, 0.01]$?
2. How does the fraction depend on $n$? <sup>+</sup>
3. For $n=100$, what is the range $[-\epsilon,\epsilon]$ for which $99$% of the $10,000$ $\overline{X}$s fall in?
4. How does $\epsilon$ depend on $n$? <sup>+</sup>
5. How does your answer change if the distribution changes?

<sup>+</sup> You may explain this using one or more of words, tables, and a plots.

Save your program as `HW1_1b.py`. Save your answers in a file named `HW1_1b.txt` or `HW1_1b.pdf`.

## Prelude to Hypothesis Testing

This problem is a prelude to the frequentist interpretation of probability and hypothesis testing.

I select $n=100$ men at random from the U.S. population and compute the average of their heights. Using only the techniques used in the previous problem, make a statement about the liklihood that the actual U.S. population average is more than 1 inch larger or smaller than the mean of the $n$ heights.

Describe the program that you would write to determine the liklihood. If you have done hypothesis testing before, don't use any of it's terminology or techniques.

Save your answer in a file named `HW1_2.txt` or `HW1_2.pdf`.

## Histograms

## Central Limit Theorem (590 only)

According to the Central Limit Theorem, the histogram of $\overline{X}$ in Problem 1.1.1a will still be gaussian even if the values in the population are not gaussian distributed.

1. Repeat 1.1.1a using a different distribution for the population.
2. I have claimed that the histogram of the 10,000 $\overline{X}$ values should be gaussian. Research Q-Q plots and plot a line  on a Q-Q plot for the 10,000 $\overline{X}$ values and a line for a gaussian distribution.

Save your answer in a file named `HW1_4.txt` or `HW1_4.pdf`.



