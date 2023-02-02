# HW 1

The first two problems of this homework are intended to primarily be a review of the programming techniques that you will need for this class. The problems mention the Law of Large Numbers, confidence intervals, and hypothesis testing. You do not need to know anything about the statistical theory behind them in order to solve these problems.

----

The Law of Large Numbers tells us that as $n\rightarrow \infty$ the sample average defined by

$$\overline{X}\equiv\frac{1}{n}\sum_{i=1}^n X_i$$

will be near the population average $\mu$ with a given probability. Given $n$ samples from a population, we don't expect $\overline{X}$ to exactly match $\mu$. The Law of Large Numbers allows us to make a statement about the difference $\overline{X}-\mu$. Specifically, the statement involves the probability that $|\overline{X}-\mu|$ is smaller that a certain value.

If you are interested, for a more formal definition of the Law of Large Numbers and proofs, see
* [Orloff and Bloom, Reading 6b](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading6b.pdf)
* Bulmer, Chapter 6 ([Piazza](https://piazza.com/gmu/spring2021/ce0c/resources))
* DeGroot, Chapter 6 ([Piazza](https://piazza.com/gmu/spring2021/ce0c/resources))

## Law of Large Numbers I

### a

1. Draw $n=100$ values from a population of Gaussian-distributed numbers drawn with mean $\mu=0$ and standard deviation $\sigma=1$.
2. Compute $\overline{X}$.
3. Repeat 1. and 2. $10,000$ times and plot a histogram of $\overline{X}$.

Save your program as `HW1_1a.py`. When I execute your program, I should see a histogram with _**the average of**_ $\overline{X}$ displayed in the title.

**Answer**

See [HW1_1a.py](https://github.com/rweigel/astrostats/blob/main/hws/HW1_1a.py). Several students turned in plots without axis labels 🤷. I should not have to ask and I should really give a zero to make the point that it is never acceptable to create a plot with missing or incorrect labels.

From the following plot, it should be clear that when we draw $100$ values from a population with a mean of zero, the average of the $100$ values will not always be zero.

<img src="hws/figures/HW1_1a.svg"/>

### b

1. For $n=100$, what fraction of the $10,000$ $\overline{X}$s were in the range $[-0.01, 0.01]$?
2. How does the fraction depend on $n$? <sup>+</sup>
3. For $n=100$, what is the range $[-\epsilon,\epsilon]$ for which $99$% of the $10,000$ $\overline{X}$s fall in?
4. How does $\epsilon$ depend on $n$? <sup>+</sup>
5. How does your answer change if the distribution changes?

<sup>+</sup> You may explain this using one or more of words, tables, and plots.

Save your program as `HW1_1b.py`. Save your answers in a file named `HW1_1b.md` or `HW1_1b.pdf`.

**Answer**

See [HW1_1b.py](https://github.com/rweigel/astrostats/blob/main/hws/HW1_1b.py)

1.  7.6%
2.  The following plot shows the dependence. As $n$ increases, the standard deviation of the histogram of $\overline{X}$ decreases so that more of the distribution is in the range $[-0.01, 0.01]$.

    <img src="hws/figures/HW1_1b2.svg"/>
3.  25.8%
4.  The following plot shows the dependence.
  
    <img src="hws/figures/HW1_1b4.svg"/>
5.  I accepted any answer to this question if it was not interpreted correctly. By "distribution", I mean the type of distribution, e.g., Gaussian, uniform, lognormal, etc. If you choose parameters for these distributions such that their mean is zero, the results are unchanged. This is a consequence of the Central Limit Theorem. It does not matter how the $n$ $X$s are distributed, the distribution of $\overline{X}$ is still Gaussian. In [HW1_1a.py](https://github.com/rweigel/astrostats/blob/main/hws/HW1_1a.py), there is a line with `np.random.uniform` commented out. Try running the code with it uncommented and notice that the histogram is still Gaussian even though a uniform distribution was used for the $n$ $\overline{X}$s.

## Prelude to Hypothesis Testing

This problem is a prelude to the frequentist interpretation of probability and hypothesis testing.

I select $n=100$ men at random from the U.S. population and compute the average and standard deviation of their heights. Assume that the distribution of the population is gaussian with a standard deviation that happens to equal the standard deviation of the sample. 

Using only the techniques used in the previous problem and these assumptions, make a statement about the likelihood that the actual U.S. population average is more than 1 inch larger or smaller than the average of the $n$ heights.

1. Briefly describe how you could do a calculation to estimate the likelihood. If you have done hypothesis testing before, don't use any of its terminology or techniques.
2. Implement the calculation. Assume the mean of the $100$ men was 72 inches and the standard deviation was 3 inches.

Save your answer to part 1. in a file named `HW1_2.md` or `HW1_2.pdf`. Save your answer to part 2. in a file named `HW1_2.py`.

## Basic Concepts in Probability

Read Chapter 2.1-2.2 of Devore, 2012. 

1. An experiment involves tossing a coin 3x. What is the sample space of this experiment?
2. How many of the outcomes in the sample space had two heads? 
3. Define event $A$ to be that the experiment yields two heads. Define event $B$ to be that the experiment yields two tails. What is $A \cup B$ and $A \cap B$?

Save your answers in a file named `HW1_3a.md` or `HW1_3a.pdf`.

**Answer**

1. The sample space has 8 elements ($2^3$). This list can be found using a tree diagram as shown below.

    ```
            H   => HHH
        H -
            T   => HHT
    H -        
            H   => HTH
        T -
            T   => HTT

            H   => THH
        H -
            T   => THT
    T -        
            H   => TTH
        T -
            T   => TTT

    ```
2. $3$ by inspection of the table above. Also, suppose that we have three unique coins $T$, $H_1$, and $H_2$. There are $3!$ unique permutations. If we drop the subscripts, then the number of unique permutations is divided by 2. So $3!/2=3$.
3. By inspection of the list from 1., $A \cup B = 6$ and  $A \cap B = \emptyset$.

In the above, I assumed "experiement yields two heads" to mean "the experiment yielded exactly two heads" and not "the experiement yielded two or more heads".

