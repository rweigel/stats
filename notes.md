# Probability Definitions

[Devore Chapter 2](https://drive.google.com/file/d/1-n9-6OK9r6DSqrUyK77fVUo-yNUK8Zc9/view?usp=sharing★★★★★remove★★★★★)

* Probability
  > The term probability refers to the study of randomness and uncertainty. In any situation in which one of a number of possible outcomes may occur, the discipline of probability provides methods for quantifying the chances, or likeli- hoods, associated with the various outcomes. (p 50)

  > Given an experiment and a sample space $\mathcal{S}$, the objective of probability is to assign to each event $A$ a number $P(A)$, called the probability of the event $A$, which will give a precise measure of the chance that $A$ will occur. (p 55)

* Experiment

* Event

  > An event is any collection (subset) of outcomes contained in the sample space S. An event is simple if it consists of exactly one outcome and compound if it consists of more than one outcome. (p 52)

  > An event is just a set. (p 53)

* Sample Space, $\mathcal{S}$ (or Event Space)

  > the set of all possible outcomes of an experiement.
  
  Can we also say a sample space is the set of all possible simple events?

  The outcomes in a sample space are noted using the shorthand
  
  $\mathcal S = ${outcome 1, outcome 2, ...}
  
  For example, if the experiment is tossing a coin twice and counting the number of heads and tails, the three simple events are ${1H1T, 2T, 2H}$, and the sample space is

  $\mathcal S = $ {$1H1T$, $2T$, $2H$}

  If the experiment is tossing a coin twice and writing down the result of the first toss if box 1 and the result of the second toss in box 2,

  $\mathcal S = $ {$HH$, $HT$, $TH$, $TT$}

  We can define a compound event: $A$ is outcome of the experiment yielding one tail.

* Compliment -- "Not $A$" is represented by four symbols: `$A^\prime$` $\quad$ `$\overline{A}$` $\quad$ `~$A$` $\quad$ $\neg A$

  > The complement of an event $A$, denoted by $A'$, is the set of all outcomes in $\mathcal{S}$ that are not contained in $A$. (p 53)

* Difference (not defined by Devore. See Rozanov p 14) -- $A-B$ means the event in which $A$ occurs but not $B$.

* Subset (Rozanov, p15) -- $A\subset B$ means the set $A$ is a subset of $B$.

* Union -- "Or" (union) is typically represented by `$\cup$`

  > The union of two events $A$ and $B$, denoted by $A \cup B$ "$A$ or $B$" is the event consisting of all outcomes that are _either in_ $A$ _or in_ $B$ _or in both events_ (so that the union includes outcomes for which both $A$ and $B$ occur as well as outcomes for which exactly one occurs) -- that is, all outcomes in at least one of the events. (p 53)

* Intersection - "And" (intersect) is represented by four symbols: `$\cap$` $\quad$ `&` $\quad$ `,` $\quad$ `+`

  > The intersection of two events $A$ and $B$, denoted by $A \cap B$ and read "$A$ and $B$," is the event consisting of all outcomes that are in _both_ $A$ _and_ $B$. (p 53)

* Null event

  > Let $\varnothing$ denote the null event (the event consisting of no outcomes whatsoever). When $A\cap B = \varnothing$, $A$ and $B$ are said to be mutually exclusive or disjoint events.

* Mutually exclusive -- Defined in Null Event definition. Also referred to as "pairwise disjoint".

* Axioms of Probability (p 56)

  1. For any event $A$, $P(A) \ge 0$.
  2. $P(\mathcal{S})=1$
  3. If $A_1$, $A_2$, ... is an infinite collection of disjoint events, then
     
     $$P(A_1 \cup A_2 ....) = P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i)$$

     Corallary

     $$P(A_1 \cup A_2 .... \cup A_k) = \sum_{i=1}^k P(A_i)$$

  > Axioms do not completely determine an assignment of probabilities to events. The axioms serve only to rule out assignments inconsisten with our intuitve notions of probability. (p 57)

* Geometric Series

  $$a + ar + ar^2 + ... = \frac{a}{1-r}$$

  In an experiment where the event is either true (with probability $1-p$) or false (with probability $p$) and we run experiments until we get a false, the sample space of all experiments is
  $E_1=F$, $E_2=TF$, $E_3=TTF$, ... and by Axiom 3.
  
  $1 = P(E_1) + P(E_2) + P(E_3) + ....$
  
  and we will learn later why $P(E_1)=p$, $P(E_2)=(1-p)p$, $P(E_3)=(1-p)^2p$, ...
  
  This is a geometric series with $a=p$ and $r=1-p$ and thus
  
  $1 = P(E_1) + P(E_2) + P(E_3) + ....$

*  Relative Frequency and Interpretation of Proability

  > ... most frequently used an most easily understood is based on the notation of relative frequencies. (p 57)

  Repeat experiment $n$ times (each repetition is called a "replication"). If event $A$ occurs $n(A)$ times in $n$ replications, then relative frequency is $n(A)/n$.
  
  > The _objective interpretation of probability_ identifies this limiting relative frequency to $P(A)$.
  
  If exeriment is not repeatable, prior information must be used to determine $P(A)$ and not everyone may conclude the same $P(A)$; in this case $P(A)$ has a subjective interpretation.

* Law of Compliments (Devore does not use this, however)

  > For any event $A$, $P(A)+P(A')=1$, from which $P(A)=1-P(A')$. (p 59)

* Corallary to Axiom 3 (Devore only calls this a proposition) 

  > For any event $A$, $P(A)\le 1$.

* Law of Addition (Devore does not use this, however)

  For any two events $A$ and $B$ that are mutually exclusive,
  
  $P(A\cup B) = P(A) + P(B)$

* General Law of Addition (Devore does not use this, however)

  > For any two events $A$ and $B$,
  >
  > $P(A\cup B) = P(A) + P(B) - P(A\cap B)$

  > For any three events $A$, $B$, and $C$,
  >
  > $P(A\cup B\cup C) = P(A) + P(B) + P(C) - P(A\cap B) - P(A\cap C) - P(B\cap C) + P(A\cap B\cap C)$

  **Visual proof**

  [[Image:Image2.png|left|thumb|Image of two targets]]

  Number of ways $A$ or $B$ could occur: $n(A \cup B) = n(A) + n(B) - n(A \cap B)$
  
  Divide by the total number of dots, $n$ and use the relative frequency interpretation of probability

  $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

  Note that the two dots in the overlapping segment were double counted; the last term removes the extra count.

  Probability of events A or B to occur: P(A or B) = P(A) + P(B) - P(A and B)

  **Example**

  If you are in a firing line and two people have guns that shoot a real bullet instead of a blank with probability of 1/3, what is the probability that you get shot (assuming the marksmen never miss?)  Draw a tree diagram and a Venn diagram to explain the answer.

  *Answer*

  $P(A \text{ or } B) = 1/3 + 1/3 - 1/9 = 5/9$

  or, $P(\overline{A\text{ or } B}) = (2/3)(2/3) = 4/9$

  Check: $P(\overline{A\text{ or } B}) = 1 - P(A \text{ or } B)$

* Product Rule (or Law of Multiplication)

  > If the first element or object of an ordered pair can be selected in $n_1$ ways, and for each of these $n_1$ ways the second element of the pair can be selected in $n_2$ ways, then the number of pairs is $n_1n_2$.

* Tree Diagram -- Use for visually justifying product rule and counting permutations (defined later)

* Tuple -- A "$k$--tuple" is an ordered collection of $k$ objects. (p 66)

* General Product Rule (or Product Rule for $k$-Tuples)

  > Suppose a set consists of ordered collections of $k$ elements ($k$-tuples) and that there are $n_1$ possible choices for the first element; for each choice of the first element, there are $n_2$ possible choices of the second element; ...; for each possible choice of the first $k-1$ elements, there are $n_k$ choices of the $k$th element. Then there are $n_1n_2...n_k$ possible $k$-tuples. (p 66).

  Note that "elements" is used here, but in definition of tuple, objects is used.
  
  **Example**: Roll a die five times. How many $5$-tuples? Create a five boxes. There are six possible "choices" for first box, six possible choices for second box, ..... So there are $6^5$ possible $k$--tuples.

  **Example**: Flip a coin 2 times. There number of $2$--tuples is $2\cdot 2$. (Think of two boxes and you put either a $H$ or $T$ in the first box and a $H$ or $T$ in the secon box.)
  
  **Example**: Given three circles of different diameter and four squares of different side length, put a circle in the first box and a square in the second. The number of $2$--tuples is $3\cdot 4$.

  **Example**: Each clinic has two $O$ doctors and three $P$ doctors and you must select two doctors from the same clinic. How many possible pairs of $O$s and $P$s are there?
  
  In the first box, put one of the four $O$s. For each $O$, there are $3$ $P$s to choose from and put in the second box. So $n=4\cdot 3$.
  
  If each clinic also has three $I$s and two $G$s, how many possible choices for four doctors?
  
  In the third box, put one of the three $I$s; in the fourth box, put one of the three $G$s. Then $n=4\cdot 3\cdot 3\cdot 2$.

  **Example**: Suppose you want to pick a team of two tennis players from $3$ players, $A$, $B$, and $C$. The number of ways you can pick the team is $3\cdot 2$: $AB$, $AC$, $BA$, $BC$, $CA$, and $CB$.

  This is not the list possible teams because $AB$ is the same as $BA$ (That is, order is not important.). The list of possible teams is $3$, by inspection.

* Permutation -- An ordered arrangement of distinct objects, where each arrangement has no duplicate objects. Usually relevant in problems that involve "without replacement".

  Suppose you have $n$ distinct objects and you want to put them in boxes labeled $1$, $2$, ..., $k$. You select one object and put it in the first box. You select a second object from the remaining $n-1$ objects and put it in box $2$, ....
  
  The number of ways to do this is denoted $P_{k,n}$ (or $_nP_k$) and is
  
  $$P_{k,n}=\frac{n!}{(n-k)!} = n\cdot (n-1) ... \cdot (n-k)=\frac{n\cdot (n-1) \cdot (n-2) ... \cdot (n-k) \cdot (n-k-1) ... 1}{\phantom{n\cdot (n-1) \cdot (n-2) ... \cdot}(n-k)\cdot(n-k-1) ... 1}$$

  Do see this, consider
  
  $$6\cdot 5\cdot 4=\frac{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}{\phantom{6\cdot 5\cdot 4\cdot}3\cdot 2\cdot 1}$$

* Combination (un-ordered subset) -- The number of unique $k$--tuples if $k$--tuples with the same elements (but in a different order) are treated as the same. In the team picking example, there are $3$ team combinations. 

# Set operations in Python



# Statistics

In the experiments done in the homework, the $X_i$ values are **random samples** from a **probability distribution** with **expectation values** for the mean and variance defined by $E[X]\equiv\mu$ and $E[(X-\mu)^2]\equiv\sigma^2$.

The probability distribution of the $\overline{X}$s, each computed using $n$ samples, is called the **sampling distribution**.

* **Population** - "All" of the data is called the population. A population can be finite or infinite. An example of a finite population is all US citizens. An example of an infinite population are values from a continuous probability density function. (Technically, when you draw a value from a continuous probability distribution, you are actually drawing from a discrete distribution, because there are finite number of values that can be represented as 64--bit floating point numbers.)

* **Sample statistic** - a computation based on a sample from a population that gives an estimate of the equivalent value that would be obtained if the same computation was performed on the population (see also Devore p214).

* **Population statistic** - a computation based on all values in a population.

* **Probability distribution** -- There are two types: discrete and continuous.

   **1\. Discrete**

   Devore (p97) calls the discrete case a "probability mass function" and I've been using the variable $P$. If $x$ is a discrete variable, then

   $$1 = \sum_{\text{all x}}P(x)$$

   and

   $$P(x)\ge 0$$

   An example probability mass function that we've used is $P(0)=0.5$, $P(1)=0.5$, which can be used to simulate the outcome of a fair coin toss, where $x=0$ represents tails and $x=1$ represents heads. The Binomial Distribution is another discrete probability distribution.

   To compute a probability mass function from a histogram, scale the histogram heights by the total number of observations.

   ```Python
   # src=code/pmf.py
   ```

   <img src="code/figures/pmf.svg"/>

   **2\. Continuous**

   See also the [lecture notes by Orloff and Bloom](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading5b.pdf)

   The discrete case is called the "probability density function", and I've been using the variable $p$. The requirements are

   $$1 = \int_{-\infty}^\infty p(x)dx$$

   and

   $$p(x)\ge 0$$

   In the continuous case, the probability that $x$ is a given value is $p(x)dx$, which is a differential. As a result, it only makes sense to talk about the probability that $x$ is in a range, e.g.,

   $$P(a\le x\le b) = \int_a^bp(x)dx$$

   An example of a continuous distribution is the Gaussian or Normal:
    
   $$p(x)=\frac{1}{\sigma\sqrt{2\pi}} e^{{-(x-\mu)^2}/{2\sigma^2}}$$
    
   which satisfies $p(x)\ge 1$ and

   $$\int_{-\infty}^\infty p(x)dx=1$$

   You are already familiar with statements such as "95% of the time a value of $x$ drawn a Gaussian will be in the range $[\mu-1.96\sigma,\mu+1.96\sigma]$, or

   $$P(\mu-1.96\sigma\le x\le \mu+1.96\sigma) = 0.95 = \int_{\mu-1.96\sigma}^{\mu+1.96\sigma}p(x)dx$$

   To compute a probability density from a histogram, divide the height of each histogram bar by the total number of obervations and the width of each bar. The sum of the resulting bar heights will be unity.

* **Sampling distribution** - When we take a sample from a population and compute a statistc, for example a mean, we want to know the uncertainty in the statistic. That is, we want to know what the probability distribution of the means would be if we took many samples and computed many means. The probability histogram of the test statistic is the sampling distribution. If the sampling distribution is known, we can easily put error bars on our test statistic.

   In [HW #1](hw.html#hw-1), we derived a sampling distribution numerically. It was found that when $n$ values of $X$ were drawn from a Gaussian distribution with mean $\mu$ and standard deviation $\sigma$ and the statistic 

   $$\overline{X} = \frac{1}{n}\sum_{i=1}^nX_i$$

   was computed $10,000$ times, 95% of the time the range

   $$\left[\overline{X}-1.96\frac{\sigma}{\sqrt{n}}\text{ },\text{ } \overline{X}+1.96\frac{\sigma}{\sqrt{n}}\right]$$

   included $\mu$. (We say that this range "traps" $\mu$ 95% of the time.) We actually did not need to do the numerical experiement when $n$ is large. We know the expected result from the Central Limit Theorem.

* **Expectation values**

   The general definition of the expectation operator $E[\cdot]$ is, for discrete $x$,

   $$E \left[X\right] = \sum_{\text{all }x}xP(x)$$

   or, for continuous $x,$

   $$E\left[X\right] = \int_{x}xp(x)dx$$

   By definition, $\mu=E\left[X\right]$. That is $\mu$ is the average of $X$ over the population. The variance of a population is defined as

   $$\sigma^2=E\left[(X-\mu)^2\right]$$

   When we invent a statistic (a quantity computed from a sample) that is intended to be used as an estimate of a similar quantity from a population, we want the statistic to be unbiased. That is, the expectation value of the statistic should equal the population value. Two statistics that were considered are the mean and variance.

* **Random samples** By random samples, we mean a value drawn from a population with a certain probability distribution. In general **random samples** implies "independent and identically distributed random variables" (often abbreviated iid). 

* **Law of Large Numbers**

   The _weak law of large numbers_ [Rozanov, p69]: given an arbitrarily small $\delta > 0$ and $\epsilon > 0$, there is an integer $n$ for which the quantity $\overline{X}\equiv (1/n)(X_1+...+X_n)$ (with $X$ iid) will be in a small window centered on $\mu$ with a probability near 1, that is,

   $$\mu-\epsilon\le \overline{X} \le \mu + \epsilon$$

   with a probability greater than $1-\delta$. This means we can choose very small $\epsilon$ and $\delta$ values and there will always be a value of $n$ for which the constraints are satisfied.

   It follows from _The Strong Law of Large Numbers_ that $\lim_{n\rightarrow\infty}\overline{X}$ exists and is equal to $\mu$ with a probability of 1 [Rosanov, p 70]. (The Strong Law may seem equivalent to the Weak Law, but their statements are not quite equivalent.)

* **Central Limit Theorem**

   The Law of Large Numbers tells use that if we require $\overline{X}$ to fall in range that we specify around $\mu$ with a probability that we specify, we can find an $n$ value to satisfy our requirement. The central limit theorem says that for large $n$, $\overline{X}$ is Gaussian-distributed with mean $\mu$ and standard deviation $\sigma$. With the Central Limit theorem, we can make statements such as "I took a sample of $n$ values and computed $\overline{X}$. If I took many samples and computed many $\overline{X}s$, 95\% of the time the range $[\overline{X}-1.96\sigma/\sqrt{n},\overline{X}+1.96\sigma/\sqrt{n}]$ would include ("trap") $\mu$.

* **Parametric bootstrap sample statistic distribution** -- A pmf or pdf created by simulating many experiments and the calculation of a sample statistic for each experiment. For example, suppose that we wanted to know the distribution of the sample statistic $Y=X_1^2 + X_2^2 + ... + X_n^2$, where an experiment consists of drawing $n$ values, $X$, which are Gaussian distribution with a known mean and standard deviation. We could use a random number generator so simulate many experiements and for each experiment compute $Y$. If a theoretical distribution for $Y$ is not known, this method can be used.

* **Non-parametric bootstrap sample statistic distribution**

   [The definition](https://www.oxfordlearnersdictionaries.com/us/definition/english/bootstrap_2?q=bootstrapping) of the idiom "bootstrapping" is "get (oneself or something) into or out of a situation using existing resources." If we don't know the sampling distribution of $X$, we can't use a random number generator to simulate many experiments. In this case, we use the only available resource: the measurments from one experiment. This done by drawing a sample of $n$ with replacement from the $n$ measurements. Each such draw is called a bootstrap sample (or experiment) and the test statistic computed from it is indicated by $Y^*$. The bootstrap pmf or pdf is computed from the histogram of the $Y^*$s.

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

# Counting

## Distinct ordered pairs (2-tuples)

Given $a_1$, $a_2$, ... $a_{n_a}$ and $b_1$, $b_2$, ... $b_{n_b}$, one can form $N=n_an_b$ distinct ordered pairs with one element from each list. Said another way, if slot $1$ is filled with a choice from $a$ and slot $2$ is filled with a choice from $b$, there are $n_an_b$ unique ways to fill the slots.

If there are n<sub>1</sub> ways of doing operation 1 and  n<sub>2</sub> ways of doing operation 2, then both operations can be performed in n<sub>1</sub>·n<sub>2</sub> ways.  For example, if operation 1 is moving north, south, east, or west and operation 2 is moving up or down, then there are 8 possible combinations of a horizontal step followed by a vertical step.

One can use a tree diagram, table, or $x$--$y$ plot to prove.

**Typical Example**:

Two teams of twelve players each. How many unique handshakes between members of opposing teams?

*Answer*: $n_a=12$, $n_b=12$, $N=12\cdot 12=144$.

Brute force calculation: [code/probability_brute_force_ordered_2_tuples.m](code/probability_brute_force_ordered_2_tuples.m)

## Distinct ordered $k$-tuples (Uniquely ordered groups of $k$)

Given $k$ lists

$L_1$: $a_1$, $a_2$, ... $a_{n_a}$

$L_2$: $b_1$, $b_2$, ... $b_{n_b}$ 

...

$L_k$: $x_1$, $x_2$, ... $x_{n_k}$ (where $x$ represents the $k$th letter of the alphabet)

one can form $N=n_an_b...n_k$ distinct ordered $k$--tuples containing one element from each list. Can use a tree diagram to prove. Said another way, ...

**Typical Example**:

What is the probability of getting three sixes in an experiment when three dice are thrown? 

*Answer*: $6\cdot 6\cdot 6=216$ is the number of unique experiment results. Of these experiments, only one will have three sixes, so $P=1/216$.

## Sampling with replacement to form distinct ordered $k$-tuples

Choose $k$ objects in succession from a population of $n$ distinct objects. The number, $N$ of distinct and ordered $k$-tuples is $N=n^k$. Each $k$-tuple is equiprobable.

Equivalent to given $k$ lists

$L_1$: $a_1$, $a_2$, ... $a_{n}$

$L_2$: $b_1$, $b_2$, ... $b_{n}$

...

$L_k$: $x_1$, $x_2$, ... $x_{n_k}$ (where $x$ represents the $k$th letter of the alphabet)

one can form $N=n^k$ distinct ordered $k$--tuples containing one element from each list.

## Permutations

Given a population of $a_1, a_2, ..., a_n$, sample without replacement to form distinct orderings of size $k$. The number of possible distinct $k$--tuples is

$N=n\cdot (n-1)\cdot ... (n-k+1)$

This can be rewritten as

$$N=\frac{n!}{(n-k)!}$$

This number is typically written as $P_n^k$, $_nP_k$, or $P_{n,k}$, where the $P$ means "number of permuations" and not "probability".

**Typical Example**:

You have stickers labled $1$, ..., $6$ that are used to form a license plate. How many unique license plates can you form?

*Answer*: $6!$

## Combinations (shuffled permutations)

Each permutation can be regarded as group of $k$. If we regard a group as equivalent if they have the same elements, then there are fewer groups than permuations. For example, if the two permutations

$(1,2)$

$(2,1)$

are regarded as equivalent, then there is only one group containing the numbers $1$ and $2$. To determine the number of possible orderings of each permutation, ask how many ways a set of $k$ elements can be arranged. The answer is $k!$.

So, to find the number of combinations, divide the number of permutations by $k!$.

$$C_{n,k}=\frac{P_{n,k}}{k!}=\frac{\ds\frac{n!}{(n-k)!}}{k!}=\frac{n!}{k!(n-k)!}$$

$C_{n,k}$ is often called a binomial coefficient and the denoted by $\ds{N\choose k}$ and referred to as "$n$ choose $k$".

**Typical Example**:
* How many unique ordered hands of size $5$ can be formed using a $52$-card deck?

   *Answer*: $52\cdot 51\cdot 50\cdot 49\cdot 48$.
* How many hands of size $5$ can be formed using a $52$-card deck?

   *Answer*: Each permutation can be rearranged in $5!$ ways. So the number of hands is $52\cdot 51\cdot 50\cdot 49\cdot 48/(5\cdot 4\cdot 3\cdot 2\cdot 1)$

# Bayes

You only need to know these two laws in order to derive Bayes' theorem.

Sum law

Product law

## Review

----

[[Image:Image1.png|thumb|left|Image 1]]

**Question:* What is $n(A \text{ and } B)$ in Image 1? That is, how many dots have labels of $A$ or $B$? (Give a number)

**Answer**: All of them; $n(A) + n(B) = 11$

**Question:** What is $n(A \text{ and } B)$ in Image 1?  That is, how many dots have labels of both $A$ and $B$?  (Give a number)

**Answer**: zero

----

[[Image:Image2.png|left|thumb|Image 2]]

**Question:** What is $n(A \text{ and } B)$ in Image 2?  That is, how many dots have labels of both $A$ and $B$?  (Give a number)

**Answer**: 2

**Question:** What is $n(B \text{ and } A)$ in Image 2?  That is, how many dots have labels of both $A$ and $B$?  (Give a number)

**Answer**: 2

----

'''Question:''' In terms of n(A), n(B), n(A and B), what is n(A '''or''' B) in Image 2?  That is, how many dots have labels of A or B?

{| class="wikitable collapsible collapsed"
! Answer
|-
|
n(A '''or''' B) = n(A) + n(B) - n(A and B)
|}

'''Question:''' In terms of n(B), P(A|B), what is n(A and B) in Image 2?

{| class="wikitable collapsible collapsed"
! align="left" | Answer
|-
|
<math>n(A \mbox{ and } B) = n(B)\cdot P(A|B)</math>
|}

'''Question:''' In terms of n(A), P(B|A), what is n(B and A) in Image 2?

{| class="wikitable collapsible collapsed"
! align="left" | Answer
|-
|
<math>n(B \mbox{ and } A) = n(A)\cdot P(B|A)</math>
|}
|}

==== ====

{| border="0" cellpadding="2" width="100%" align="left"
|-
|style="vertical-align:top"|
[[Image:Image3.png|thumb|left|Image 3 (X Y Z, A B grid)]]
|style="vertical-align:top"|
'''Question:''' In terms of n(A), n(B), n(X), P(X|A), and P(A|X), what is n(A and X) in Image 3?

{| class="wikitable collapsible collapsed"
! align="left" | Answer
|-
|
<math>n(A \mbox{ and } X) = n(A)\cdot P(X|A)</math>
|}

'''Question:''' In terms of n(A), n(B), n(X), P(X|A), and P(A|X), what is n(X and A) in Image 3?

{| class="wikitable collapsible collapsed"
! align="left" | Answer
|-
|
<math>n(X \mbox{ and } A) = n(X)\cdot P(A|X)</math>
|}
|}
<br style="clear:both"/>
== Bayes' Theorem ==

=== Derivation ===


{| border="0" cellpadding="2" width="100%" align="left"
|-
|style="vertical-align:top" width="50%" |
'''Question''': In reference to Image 2, what is P(A|B) in terms of n(A), n(B), n(A and B), and n(B and A)?
|style="vertical-align:top"|
{| class="wikitable collapsible collapsed"
! Answer
|-
|
<math>P(A|B) = \frac{n(A \mbox{ and } B)}{n(B)}</math>
|}
|}

{| border="0" cellpadding="2" width="100%" align="left"
|-
|style="vertical-align:top" width="50%" |
'''Question''': In reference to Image 2, what is 

<math>\frac{n(A \mbox{ and } B)}{n(B \mbox{ and } A)}</math>

in terms of n(A), n(B), P(A|B), and P(B|A)? 
|style="vertical-align:top"|
{| class="wikitable collapsible collapsed"
! Answer
|-
|
<math>\frac{n(A \mbox{ and } B)}{n(B \mbox{ and } A)} = 1 = \frac{n(A)\cdot P(B|A)}{n(B)\cdot P(A|B)}
</math>

or

<math>
n(B) = n(A)\cdot\frac{P(B|A)}{P(A|B)}
</math>

or

<math>
P(B) = P(A)\cdot\frac{P(B|A)}{P(A|B)}
</math>

|}
|}

{| border="0" cellpadding="2" width="100%" align="left"
|-
|style="vertical-align:top" width="50%" |
'''Question''': In reference to Image 3, what is 

<math>\frac{n(A \mbox{ and } X)}{n(X \mbox{ and } A)}</math>

in terms of n(A), n(X), P(A|X), and P(X|A)? 
|style="vertical-align:top"|
{| class="wikitable collapsible collapsed"
! Answer
|-
|
<math>\frac{n(A \mbox{ and } X)}{n(X \mbox{ and } A)} = 1 = \frac{n(A)\cdot P(X|A)}{n(X)\cdot P(A|X)}
</math>

or

<math>
n(X) = n(A)\cdot\frac{P(X|A)}{P(A|X)}
</math>

or

<math>
P(X) = P(A)\cdot\frac{P(X|A)}{P(A|X)}
</math>

check

<math>
\frac{5}{13} = \frac{7}{13}\cdot\frac{\frac{2}{7}}{\frac{2}{5}}
</math>
|}
|}

