# HW 1

The first two problems of this homework are intended to primarily be a review of the programming techniques that you will need for this class. The problems mention the Law of Large Numbers, confidence intervals, and hypothesis testing. You do not need to know anything about the statistical theory behind them in order to solve these problems.

----

The Law of Large Numbers tells us that as $n\rightarrow \infty$ the sample average defined by

$$\overline{X}=\frac{1}{n}\sum_{i=1}^n X_i$$

will be near the population average $\mu$ with a given probability. Given $n$ samples from a population, we don't expect $\overline{X}$ to exactly match $\mu$. The Law of Large Numbers allows us to make a statement about the difference $\overline{X}-\mu$. Specifically, the statement involves the probability that $|\overline{X}-\mu|$ is smaller that a certain value.

If you are interested, for a more formal definition of the Law of Large Numbers and proofs, see
* [Orloff and Bloom, Reading 6b](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading6b.pdf)
* Bulmer, Chapter 6 ([Piazza](https://piazza.com/gmu/spring2021/ce0c/resources))
* DeGroot, Chapter 6 ([Piazza](https://piazza.com/gmu/spring2021/ce0c/resources))

## Law of Large Numbers I

### a

1. Draw $n=100$ values from a population of numbers drawn from a gaussian distribution with mean $\mu=0$ and standard deviation $\sigma=1$.
2. Compute $\overline{X}$.
3. Repeat 1. and 2. $10,000$ times and plot a histogram of $\overline{X}$.

Save your program as `HW1_1a.py`. When I execute your program, I should see a histogram with _**the average of**_ $\overline{X}$ displayed in the title.

**Answer**

See [HW1_1a.py](hws/HW1_1a.py). Several students turned in plots without axis labels 🤷. I should not have to ask and I should really give a zero to make the point that it is never acceptable to create a plot with missing or incorrect labels.

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

See [HW1_1b.py](hws/HW1_1b.py)

1.  7.6%
2.  The following plot shows the dependence. As $n$ increases, the standard deviation of the histogram of $\overline{X}$ decreases so that more of the distribution is in the range $[-0.01, 0.01]$.
    <img src="hws/figures/HW1_1b2.svg"/>
3.  25.8%
4.  The following plot shows the dependence.
    <img src="hws/figures/HW1_1b4.svg"/>
5.  I accepted any answer to this question as it was not interpreted correctly. By "distribution", I mean the type of distribution, e.g., Gaussian, uniform, lognormal, etc. If you choose parameters for these distributions such that their mean is zero, the results are unchanged. This is a consequence of the Central Limit Theorem. It does not matter how the $n$ $X$s are distributed, the distribution of $\overline{X}$ is still Gaussian. In [HW1_1a.py](hws/HW1_1a.py), there is a line with `np.random.uniform` commented out. Try running the code with it uncommented and notice that the histogram is still Gaussian even though a uniform distribution was used for the $n$ $\overline{X}$s.

## Prelude to Hypothesis Testing

This problem is a prelude to the frequentist interpretation of probability and hypothesis testing.

I select $n=100$ men at random from the U.S. population and compute the average of their heights. Using only the techniques used in the previous problem, make a statement about the likelihood that the actual U.S. population average is more than 1 inch larger or smaller than the average of the $n$ heights.

Briefly describe a program that you would write to determine the likelihood. If you have done hypothesis testing before, don't use any of its terminology or techniques. I am only interested in hearing ideas that you have about how the approach used in the previous problem could be used to give an answer.

Save your answer in a file named `HW1_2.md` or `HW1_2.pdf`.

**Answer**

In this problem, a single sample of $n=100$ was used to compute an average, $\overline{X}_o$ and standard deviation $s_o$. We do not know the population average $\mu$ but want to make a statement (or "inference") about it.

Now do many (say 10,000) experiments of drawing a sample of $100$ values from a gaussian distribution with mean $\overline{X}_o$ and sample standard deviation $s_o$. That is, assume that the actual unknown population distribution has a mean and standard deviation that is equal to that from the sample.

The percentage of $10,000$ experiments that had an $\overline{X}$ that was one inch larger or smaller than $\overline{X}_o$ is our estimate of the likelihood.

The above is the basic process of inferential statistics. However, instead of doing a simulation of 10,000 experiments, one can use a table to look up the expected percentage when an infinite number of experiments are performed.

## Basic Concepts in Probability

Read Chapter 2.1-2.2 of Devore, 2012 ([PDF available on Piazza](https://piazza.com/gmu/spring2021/ce0c/resources)). 

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

# HW 2

## Counting

1. By hand, solve problem 38. in Chapter 2. of Devore. See Piazza for a copy of this chapter. (Save as `HW2_1_1.pdf` or `HW2_1_1.md`)
2. Use Python to check your answer by simulating many experiments in which 3 bulbs are randomly selected and then computing the ratios requested in parts a.--d. of the problem statement. This will not be an exact answer, but as you increase the number of experiments, this approximate answer should become closer to your answers found by hand. (Save as `HW2_1_2.py`)

_Update_: Technically parts a.-c. ask for drawing three bulbs, so the inclusion of part d in the above does not make sense. So just use the simulation to check your answers to parts a.-c., but you are encouraged to use a simulation to check your answer to part d.

**Answer**

1.  &nbsp;&nbsp;&nbsp;$\displaystyle \frac{3(6\cdot 5\cdot 4 + 6\cdot 5\cdot 5)}{15!14!13!}$

2. See [HW2_1_2.py](hws/HW2_1_2.py)

## Bayes' Theorem

2% of people age 50--60 who participate in routine screening have colon cancer. 80% of people with colon cancer will test positive. 9.6% of of those without colon cancer will also test positive. A person in this age group had a positive test in a routine screening. What is the probability that they actually have colon cancer?

Draw diagrams and be prepared to explain your answer to the class. If you do not know how to solve this analytically, come up with a simulation to give an approximate answer.

(Save as `HW2_2.pdf` or `HW2_2.md`)

**Answer**

*   $P(N) = 0.98$ (probability of **N**o cancer)
*   $P(C) = 0.02$ (probability of **C**ancer)
*   $P(T^+|\overline{C}) = 0.096$ (probability of false positive)
*   $P(T^+|C) = 0.80$ (probability of +**T**est given Cancer)
*   $P(C|T^+) = ?$ (probability of cancer given +Test)
  
We can't apply Bayes' rule                                                            
$$P(C) = P(T^+)\frac{P(C|T^+)}{P(T^+|C)}$$

rewritten as

$$P(C|T^+)=\frac{P(C)\cdot P(T^+|C)}{P(T^+)}$$

immediately, because we need $P(T^+)$.  To get this, first compute the number of patients that get a positive colon cancer test                                                     
$$n_{T^+}=n_{C}P(T^+|C)+n_{N}P(T^+|N)$$

where $n_{X}$ is the number of patients in category $X$.  Divide through by the total number of patients to get                                                                
$$P(T^+)=P(C)P(T^+|C)+P(N)P(T^+|N)$$

then

$$P(C|T^+)\frac{}{}=\frac{P(C)\cdot P(T^+|C)}{P(C)P(T^+|C)+P(N)P(T^+|N)}$$

inserting numbers gives

$$P(C|T^+) = \frac{0.02\cdot 0.8}{0.02\cdot 0.8+0.98 \cdot 0.096} = 0.145$$

So the probability of actually having colon cancer given a postive test is about $14.5\\%$. 

(Often students report their answer to many more than 2 significant digits.  How would you calculate the appropriate number of significant digits and the uncertainty in your reported answer, based on the numbers given?)

**Alternative Answer**

To explain this calculation to someone, I would say:

Out of $1000$ people, $20$ will have cancer $(2\\%)$.  Sixteen of the $20$ $(80\\%)$ will have a positive test, the other four will have a negative test.

This leaves 980 without cancer.  However, $980\cdot 0.096 = 94$ of these cancer--free people will still have a positive test. This is a large number of false positives!

If you received a positive test, you are one of the checked boxes. The number of checked boxes is $94+16=110$ and $16$ of them have cancer. So given a positive test, your chances are $16/110$, or about a $1$ in $14$ 
chance.

<img src="hws/figures/HW2_2.png" style="width:100%"/>

See also [How to Improve Bayesian Reasoning Without Instruction:
Frequency Formats](http://library.mpib-berlin.mpg.de/ft/gg/GG_How_1995.pdf) for a discussion on how to explain problems involving Bayesian reasoning.

# HW 3

## Exact answer for coin flips

In HW 1.3, you considered the question of the probability of getting two heads when flipping a fair coin 3x. This question was easily answered by explicitly writing out the sample space (the set of all possible outcomes) using a tree diagram and counting the number of outcomes with two heads.

Write out the sample space for four flips of a fair coin using a tree diagram and then by inspection of the diagram determine the probability of getting two heads.

Next, inspect the sample space and provide an argument for why, if the probability of heads is $\theta$, then the probability of $k$ heads in $N$ tosses is

$$P(k)={N \choose k}(1-\theta)^{N-k}\theta^k$$

Do this using counting techniques with an explanation at the level that I used to explain the number of possible license plates of length three using only numbers. I used this example to give answers to the number of 3-digit license plates that could be formed using stickers with a digit (0-9) on them under three different constraints:

1. An infinite supply of stickers: $10^3$;
2. A supply of 10 stickers, one for each digit: $10\cdot 9\cdot 8 = 10!/7!$;
3. Same as 2., but also a license plate with the same three numbers as another license plate (but in a different order) being counted as the same license plate: $10!/(7!3!) = {10 \choose 3}$. 

You do not need to use a license plate/sticker analogy -- use whatever you need to in order to explain the equation at a fundamental level. Save your answer as <code>HW3_1.pdf</code> or <code>HW3_1.md</code> and be prepared to explain your answer to the class.

## Bayes' Rule Derivation and Terminology

You only need the law of multiplication to derive Bayes' theorem. The law of multiplication is

$$P(A\text{ and }B)=P(A)P(B|A)$$

The labels $A$ and $B$ are arbitrary. Swapping them gives:

$$P(B\text{ and }A)=P(B)P(A|B)$$

$P(B\text{ and }A)$ means the same thing as $P(A\text{ and }B)$ (mathematically, the set intersection $A\text{ and }B$ is commutative). Equating the above two equations gives

$$P(B)P(A|B)=P(A)P(B|A)$$

Bayes' theorem ("theorem", rule", and "law" are all used, seemingly arbitrarily) is

$$P(A|B)=P(B|A)\frac{P(A)}{P(B)}$$

In this form,

- $P(A|B)$ is called the posterior. It is a probability that we compute after (**post**) consideration of the other probabilities.
- $P(B|A)$ is called the likelihood (this is poor choice of name)
- $P(A)$ is called the prior. If $B$ and $A$ are independent, then $P(A|B)=P(A)$, so $P(A)$ is the probability **prior** to knowing any relationship between $A$ and $B$.
- $P(B)$ is called a normalizing factor [Wall and Jenkins, p26] or, when $B$ is evidence and $A$ is a hypothesis, then $P(B)$ is also referred to the evidence.

Another form of Bayes' theorem, valid when the events $A_j$ are mutually exclusive and exhaustive, has the denominator re-written using the law of total probability, which is

$$P(B) = \sum_{j=1}^kP(A_j)P(B|A_j)\.$$

In this case, Bayes' theorem is

$$P(A_j|B)=P(B|A_j)\frac{P(A_j)}{\sum_{j=1}^kP(A_j)P(B|A_j)}\.$$

In class, a student noted that the equation $P(A\text{ and }B)=P(A)P(B|A)$ was not intuitively obvious and I gave an example to justify the equation that involved throwing darts at two overlapping circles labeled $A$ and $B$; then I drew 10 dots corresponding to dart tosses and computed each term in the equation $P(A\text{ and }B)=P(A)P(B|A)$ by inspection.

Come up with your own basic explanation/justification for the Law of Total Probability in a spirit similar to my dart-tossing example. Save your answer as <code>HW3_2.pdf</code> or <code>HW3_2.md</code> and be prepared to explain your answer to the class.

## Bayes' Rule for Statistical Inference

**References**

All of the following references describe the problem covered in this HW problem (see Piazza for PDFs). I've attempted to write this problem in a way that you won't need to study these reference and I recommend attempting to solve this problem before reading them.

* Silva 2006, Chapter 2.1. In this problem, I am walking you through the steps needed to create Figures 1. and 2. This book uses a somewhat unconventional notation by explicitly including the variable $I$. You can safely ignore it in the equations written.
* The coin tossing experiment is covered at a basic level in Chapters 1 and 4 of Stone.
* A much more mathematically advanced description of this problem is given in Liu and Wasserman 2014.

----

**I don't expect you to be able to solve these problems without questions! Please be active on Piazza and Discord.**

----

Let $\theta$ be a parameter, such as a length, or, as considered in this problem, a probability. For example, suppose a computer program is created that prints an $H$ with probability $\theta$ and a $T$ with probability $1-\theta$ or a coin is manufactured so that the probability of heads is exactly $\theta$. 

Let $\mathcal{D}$ be data from an experiment, for example the results of coin flips, e.g., $\mathcal{D}=[H,T,H,T]$. 
With these variables, Bayes' theorem is

$$P(\theta|\mathcal{D})=P(\mathcal{D}|\theta)\frac{P(\theta)}{P(\mathcal{D})}$$

Suppose that we don't know what $\theta$ is -- we are given a coin from a machine and we don't know if the machine produces a fair coin or not.

A typical Bayesian inference problem seeks to assign a probability of $\theta$ given a set of measurements (data). That is, to assign a value to $P(\theta|\mathcal{D})$. In class, I discussed the case where we only had one or two measurements from coin tosses, that is, $\mathcal{D}=[H]$, and $\mathcal{D}=[H,T]$, respectively. In this problem, you will consider these two cases in detail.

For $\mathcal{D}=[H]$,

1.  Use the equation in problem 3.1 to compute the probability of $\mathcal{D}$ given a probability of heads. That is, find an expression for the liklihood term $P(\mathcal{D}|\theta)$, which will be a function that depends on $\theta$.

The $P(\theta)$ term in Bayes theorem above is the so-called prior. Assume you are an alien and know nothing about coin manufacturing machines and have never seen a coin tossed. In this case, based on your lack of subjective prior knowledge, you would say all values of $\theta$ are equally likely and thus $P(\theta)=c$, where $c$ is a constant.

2.  In class, I mentioned that we often don't need to worry about the term $P(\mathcal{D})$ because it is a constant that will "cancel". To elaborate, we are often interested in a ratio of probabilities such as $P(\theta_1|\mathcal{D})/P(\theta_2|\mathcal{D})$. For example, given a sequence of coin tosses from a coin manufactured by a new machine, we would want to know the ratio of the probability that a coin has a probability of heads of $\theta_1$ to the ratio that the probability of heads is $\theta_2$. However, it is sometimes useful to compute this term expliclity. In this case, the law of total probability can be used:
    $$P(\mathcal{D})=\int_0^1P(\theta)P(\mathcal{D}|\theta)d\theta$$
    Compute $P(\mathcal{D})$ in terms of $c$.

3.  Plot of $P(\theta|\mathcal{D})$ vs $\theta$.

4.  Repeat parts 1.-3. for $\mathcal{D}=[H,T]$.

5.  You are not an alien. Suppose your subjective judgement is that it is difficult to manufacture a coin with a probability of heads that differs much from 0.5. In equation form, you decide to use a sharply peaked Gaussian to represent this experience. That is, $P(\theta) \propto e^{(\theta-0.5)^2/0.1}$. Using this, plot $P(\theta|\mathcal{D})$ vs. $\theta$ for $\mathcal{D}=[H,T]$.

Save your answers in a file named `HW3_3.pdf` or `HW3_3.md`.








