```mdextension
Title: Spring 2025 PHYS/ASTR 390/590 Midterm Exam Part II
```

Provide a revision of your mid-term by April 3rd at 4:30 pm. Turn in both your mid--term and new answers. Your mid--term grade will be based on your original and revised answers.

You may not discuss these problems with any other students. You are welcome to ask me questions. If you use Discord, use a direct message.

# 

1. Provide a visual derivation of $P(B|A)=P(A|B)P(B)/P(A)$

> Some students gave an example of the use of this formula but did not provide either a mathematical or visual derivation. I covered several derivations in class, and they also appear in many textbooks.

2. One bag contains only white balls, while another bag contains 30 white balls and 10 black balls. A bag is selected at random, and a ball from that bag is selected at random. The selected ball is white. What is the probability that the selected ball was from the bag with only white balls?

# 

Derive the Gaussian distribution from the Binomial distribution.

> In class, I mentioned key steps used in statistical mechanics to arrive at the Gaussian distribution in the random walk problem: Defining $m=N_{\text{right}}-N_\text{left}$, using Stirling's approximation, using $m/N\ll 1$ for $N$ large, and $\ln(1+\epsilon)\simeq \epsilon$ for $\epsilon \ll 1$.

#

Explain the interpretation of 

1. a confidence interval,
2. not rejecting a null hypothesis, and
3. a $P$ value.

Provide examples to support your explanation, if needed.

> Most students gave a definition and not an interpretation for 2. and 3. I spend much time discussing the interpretation of a confidence interval in terms of repeated experiments. The same reasoning applies to 2. and 3.

#

1. You are given a list of $100$ numbers and asked to compute a 95% confidence interval on their average. Describe how you would calculate the confidence interval using the non--parametric bootstrap. Provide enough details so that your description can be implemented in code without ambiguity.

2. Describe how you would use a parametric simulation to determine if a sample statistic is biased.

> The wording of part 2. could have been better, or I should have put part 2. as a separate problem. Stated a different way that is perhaps to revealing, I am asking: suppose you have a sample statistic that is meant to be a proxy for a population statistic. You know the population distribution and its parameters. Instead of doing this analytically as was done for $\overline{x}$, $S^2_b$, and the slope parameter in regression in class, how would you use a simulation to determine if the sample statistic is biased?