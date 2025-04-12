# HW 1

Due Thursday, January 30th at 11:59 pm.

1. Save your answers in a GitHub repository named `astrostats`. Under `Setting` in the GitHub repository, set me (`rweigel`) as a collaborator.
2. Save your answers in the following format:
   1. Save code as `HW1_X.ext`, where `X` is the problem number and `ext` is the extension (e.g., `py` or `m`).
   2. Save scanned hand-written answers as `HW1_X.pdf`. Use a scanner app to create the document (don't take a photo and convert it to PDF).
   3. Save plots as `HW1_X.png`. If there are multiple plots for a problem, save them as `HW1_Xa.png`, `HW1_Xb.png`
3. Guess the relative frequency that instructions 1. and 2. above are followed precisely.

If you have difficulty with any of the above, we can discuss it at the end of class.

## Objective Interpretation of Probability

The _objective interpretation of probability_ is that the the probability of event $A$ is the limit of the relative frequency of $A$, $n(A)/n$ as the number of experiments, $n$, used to compute the relative frequency approaches $\infty$:

$$P(A) = \lim_{n\rightarrow \infty}\frac{n(A)}{n}$$

The following program computes the relative frequency of heads for an experiment where a zero or 1 is randomly selected.

Modify this program so that it computes the relative frequency for $n=1, 2, ..., 1000$ and plot $\text{rf}$ vs $n$. See also Figure 2.2 of Devore.

```python
import random

a = [0, 1]

# Experiment: Randomly select an element from the list a
result = random.choice(a)

# Repeat the experiment n times
n = 2
results = []
for exp in range(1, n+1):
  result = random.choice(a)
  results.append(result)

print(f"n = {n} experiments:")
print(f"  Results: {results}")
# rf = relative frequency
print(f"  rf(0) = {results.count(0) / n}")
print(f"  rf(1) = {results.count(1) / n}")
```

In class, I will raise the following questions (you don't need to answer this on what you turn in):
* Can `np.random.choice()` be used to simplify the program?
* How would you characterized the decreasing variation around $0.5$ as a function of $n$? What calculation would you do and what plot would you make?
* In class, I generated a plot by tossing a coin $n$ times and then recording the relative frequency for that $n$. I did this for $n=1, .... 1000$, so I did $1000$ independent coin tossing trials. Another student tossed a coin $1000$ times (one trial) and used the first $n$ numbers to compute the relative frequency for that $n$ (it also appears that this is how [Devore](https://drive.google.com/file/d/1szqKzodtocD8sMhvx7SzGJgqG-PNd2vb★★★★remove★★★★) generated Figure 2.2). Be prepared to discuss the difference in interpreation of the results from the two approaches.

**Solution**

See [HW1_1.py](https://github.com/rweigel/stats/tree/main/solns). Problem is solved with and without using NumPy.

<img src="solns/HW1_1.png" width="500px"/>

Comments on in--class discussion questions:

* How would you characterized the decreasing variation around $0.5$ as a function of $n$? What calculation would you do and what plot would you make?

  **Answer**: We can repeat the process used to create the figure $N$ times. Then we could compare the histogram of the values at, say, $n=100$ and $n=1000$ and characterized the difference in their variation by the histogram's standard deviation.

* In class, I generated a plot by tossing a coin $n$ times and then recording the relative frequency for that $n$. I did this for $n=1, .... 1000$, so I did $1000$ independent coin tossing trials. Another student tossed a coin $1000$ times (one trial) and used the first $n$ numbers to compute the relative frequency for that $n$ (it also appears that this is how [Devore](https://drive.google.com/file/d/1szqKzodtocD8sMhvx7SzGJgqG-PNd2vb★★★★remove★★★★) generated Figure 2.2). Be prepared to discuss the difference in interpreation of the results from the two approaches.

  **Answer**: In the second method, the result at $n+1$ depends on the result at $n$: $P_H^{n+1} = \frac{n}{n+1}P_H^n + \frac{x}{n+1}$, where $x=0$ or $1$. My opinion is that the plot associated with this method appears artifically smooth. 

**Comments on Student Submissions**

Please follow submission instructions. I am able to look at solutions in more detail if I don't have to spend time finding things or running your code to see the results.

## Sample Space

1. An experiment involves tossing a coin 3x. What is the sample space of this experiment?
2. How many of the outcomes in the sample space had two heads? 
3. Define event $A$ to be that the experiment yields two heads. Define event $B$ as the experiment yielding two tails. What is $A \cup B$ and $A \cap B$?

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

## Set Notation

The law of addition for any three events $A$, $B$, and $C$, is

$P(A\cup B\cup C) = P(A) + P(B) + P(C) - P(A\cap B) - P(A\cap C) - P(B\cap C) + P(A\cap B\cap C)$

Provide a visual way of justifying this. Be prepared to present your answer in class.

**Answer**

<img src="solns/HW1_3.svg" width="500px"/>

From the figure on the left, we can count all of the dots that are in $A$ or $B$ (or both) by counting all the dots in $A$ and adding this to the number of dots in $B$ and then subtracting the dots that were counted twice, which are shown highlighted. The result is

$n(A\cup B) = n(A) + n(B) - n(A\cap B)$

(Dividing by $N$ and taking the limit gives probability.)

The figure on the right shows a new region, $C$. To also count dots in $C$, we add all of the dots in $C$, $n(C)$ and then remove double--counted dots.

The region of the two left--most highlighted dots is $n(A\cap C)$ must be subtracted out. The region of the right--most highighted dot must be subtracted out, but $n(B\cap C)$ includes the middle highlighted dot, so $n(A\cap B)-n(A\cap B\cap C)$ must be subtracted. Thus

$n(A\cup B) = n(A) + n(B) - n(A\cap B) + \Big[n(C) - n(A\cap C) - n(B\cap C) + n(A\cap B\cap C)\Big]$

or, dividing by $N$ and re--arranging,

$P(A\cup B\cup C) = P(A) + P(B) + P(C) - P(A\cap B) - P(A\cap C) - P(B\cap C) + P(A\cap B\cap C)$

The general formula for an arbitrary number of regions is given on [p 99 of Feller](https://drive.google.com/file/d/1lJv7o3TPLyZK7r5ad1IDVtkcaMpuaf5N/view?usp=drive_link★★★★★remove★★★★★)

## Law of Addition and Set Notation

Suppose 55\% of people exercise and 45\% drink alcohol. Also, 70\% do at least one of these.

What is the probability that a randomly selected person:
1. exercises and drinks alcohol?
2. does not do at least one of the two activities?

Use a Venn diagram (or any visual method) in the way that was used in class to demonstrate your answers.

**Answer**

Given: $P(E) = 0.55$, $P(A) = 0.45$, and $P(E\cup A) = 0.7$

1. $P(E \cap A) = P(E) + P(A) - P(E \cup A) = 0.3$
2. $P\big( (E \cup A)' \big) = 1 - P(E \cup A) = 1 - 0.7 = 0.3$

## Set Operations in Python

My basic [Python notes](python.html#sets) has examples of methods that can be used for sets in Python.

In class, we solved the Visa/Mastercard problem using the Law of Addition and also a Venn Diagram. We can also solve this using Python set operations. We were given that the probability of a student having a Visa is 0.5. So we suppose there are 100 students and students 1 through 50 have a Visa: $V =$ {$1, 2, ..., 50$}. We were given that the probability of a student having a MasterCard is 0.4 and also the probability that they have both is 0.25. We can codify this by saying students 26 through 65 have a MasterCard: $M =$ {$26, 27, ..., 65$}. The remaining students we label as $X =$ {$66, 67, ..., 100$}.

Generate sets `V`, `M`, and `X` in Python. They use set operations and the `len()` function to answer the following.

1. What is the probability that the selected individual has at least one of the two types of cards.

2. What is the probability that the selected individual has neither card type?

3. Find the probability that the student has a Visa but not MasterCard.

(Hint: For 2. and 3., you will need to create a set $M'$ using the the sample space $S={1, 2, ..., 100}$, $M$, and a set operation.)

**Solution**:

See [HW1_5.py](https://github.com/rweigel/stats/tree/main/solns). Problem is solved with and without using NumPy, which prints

```
1. 0.65 = Prob. selected student has at least one of the two types of cards
2. 0.35 = Prob. selected student has neither card type
3. 0.25 = Prob. selected student has a Visa but not MasterCard
```

## Random Walk Simulation

A random walk is a process analogous to flipping a fair coin. An example in physics is a cylinder constrained to move in one dimension being struck by air particles (and the cylinder moves without friction). Each strike sends the cylinder a small step to the left or right. The probability of a step to the left is the same as that of a step to the right. See also [Chapter 1 of Kittel and Kroemer](http://www.fulviofrisone.com/attachments/article/413/Kittel%20-%20Thermodynamics.pdf) for a description in the context of statistical physics.

Suppose we want to know the probability that after three strikes, the cylinder is one step the right of its initial position using a simulation (we will cover an exact answer later).

We could do an experiment where we randomly select values of $-1$ or $1$ with equal probability using `random.choice([-1, 1])` three times (`np.random.choice()` can also be used for efficiency). A result could be `[1, 1, -1]`. The final position after these steps is `sum([1, 1, -1]) = 1`. To compute the probability that the final position is $1$, we can repeat this experiment many times and count the number of times the final position is $1$.

1. How many possible step configurations are possible? That is, what is the sample space of the experiment of taking three steps to right or left, with equal probability for each direction?
2. Write a program for a simulation that gives an estimate the probability that the cylinder is one step to the right of its initial position after three steps.

**Answer**:

1. $2^3=8$. See problem 1.2.1 and replace $H$ with $L$ (for left step) and $T$ with $R$ (for left step).

2. See [HW1_6.py](https://github.com/rweigel/stats/tree/main/solns), which has the following output.

   ```
   From 10000 experiments:
     P(sum = -3) = 0.1264
     P(sum = -2) = 0.0
     P(sum = -1) = 0.3649
     P(sum =  0) = 0.0
     P(sum =  1) = 0.3782
     P(sum =  2) = 0.0
     P(sum =  3) = 0.1305
   ```

# HW 2

Due Thursday, February 6th at 11:59 pm.

Save all files in your repository in the same directory as HW #1 (don't use subdirectories or branches).

## Permutations and Combinations

Find a problem in a textbook involving permutations and/or combinations (cite your source unless you made up the problem) and provide a solution. Be prepared to explain the problem and its solution in class.

Try to find a way to explain your solution in multiple ways (e.g., table, tree diagram, code, etc.).

If the problem is complex and difficult to explain, make up a similar but simpler problem first so that the full problem's solution is easier to understand.

Save your answer as `HW2_1.pdf`.

## Bayes' Rule

A cab was involved in a hit-and-run accident at night. Two cab companies, the Green and the Blue, operate in the city. You are given the following data:

   * 85% of the cabs in the city are Green and 15% are Blue. A witness identified the cab as Blue. The court tested the reliability of the witness under the circumstances that existed on the night of the accident and concluded that the witness correctly identified each one of the two colors 80% of the time and failed 20% of the time.

What is the probability that the cab involved in the accident was Blue rather than Green?  Use the two approaches (equation- and diagram- based) employed in the example problem related to the breast cancer problem covered in class.

Save your answer as `HW2_2.pdf`.

**590 Students**: Create a plot that answers the question: How does the answer depend on the witness's reliability (ability to correctly identify)? We will critique these plots with regard to how clearly they answer the question during class (I won't show the names of those who created the plot). Save your plot as `HW2_2.png`.

**Answer**


**Method 1**

Consider 1000 recreations of the indident in which 850 vehicles are Green and 150 vehicles are Blue. Based on a correct identification of 80\% the expected number for each possible witness claim is shown in the last column.

```
                        850*0.80 = 680 - Is Green, claims Green
       850 Are Green 
                        850*0.20 = 170 - Is Green, claims Blue
1000
                        150*0.80 = 120 - Is Blue, claims Blue
       150 Are Blue
                        150*0.20 = 30  - Is Blue, claims Green
```

We want to know the probability the cab is Blue when the witness claimed Blue. The number of times in the last column where the witness claimed Blue is $170+120$ (middle two rows). The number of times this claim is correct is $120$.

So the probability the cab is Blue given the witness claimed Blue is

$$P(B|W_B) = \frac{120}{120+170}\approx 0.41$$

**Method 2**

The following [spreadsheet](https://docs.google.com/spreadsheets/d/1a3ty9V5bsDWKugk02zNPkO8LDG5FKQ-Mzs_Cxc-_S5o/edit?usp=sharing) is an alternative visualization of the tree diagram of **Method 1**.

<img src="solns/HW2_2a.png" width="800px">

**Method 3**

To use Bayes' theorem, we start by writing the given probabilities

* $P(G) = 0.85$ (Probability a cab is Green)
* $P(B) = 0.15$ (Probability a cab is Blue)
* $P(W_B|B) = 0.80$ (Probability witness claims Blue when Blue)
* $P(W_B|G) = 0.20$ (Probability witness claims Blue when Green)

$$
P(B|W_B) = P(W_B|B)\frac{P(B)}{P(W_B)}
$$

The denominator is $P(W_B)=P(B)P(W_B|B) + P(G)P(W_B|G) = 0.15\cdot 0.80 + 0.85\cdot 0.20 = 0.12 + 0.17$. Thus,

$$
P(B|W_B) = 0.80\frac{0.15}{0.15\cdot 0.80 + 0.85\cdot 0.20} = \frac{0.12}{0.12 + 0.17}
$$

Multiplying the numerator and the denominator by $1000$ gives the same equation for **Method 1**.

$$
P(B|W_B) = \frac{120}{120 + 170} \approx 0.41
$$

A plot of $P(B|W_B)$ vs reliability is given below. If the witness is less than 50% reliably, $P(B|W_B)$ is less than the $P(B)$, meaning that the probability that they are correct is less than the fraction of cabs that are Blue; in this case, the witness testimony is not useful and a better estimate of the probability that the cab was Blue is the faction of Blue cabs in the city. What should the threshold for witness reliability be for "reasonable doubt" if the jury only had the witness testimony?

    <img src='solns/HW2_2b.svg'>

## Law of Large Numbers

The Law of Large Numbers tells us, roughly, that as $n\rightarrow \infty$ the sample average defined by

$$\overline{X}\equiv\frac{1}{n}\sum_{i=1}^n X_i$$

will be near the population average $\mu$ with a given probability. Given $n$ samples from a population, we don't expect $\overline{X}$ to exactly match $\mu$. The Law of Large Numbers allows us to make a statement about the difference $\overline{X}-\mu$. Specifically, the statement involves the probability that $|\overline{X}-\mu|$ is smaller that a certain value.

To answer the following questions, you do not need to understand the Law of Large Numbers. However, if you are interested, more formal definitions and proofs are given in [Orloff and Bloom, Reading 6b](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading6b.pdf), [Bulmer, Chapter 6](https://drive.google.com/file/d/1IuANm_ZxtuY75c9Caguv3cdG8JbmkADi/view?usp=sharing★★★★★remove★★★★★), [DeGroot, Chapter 6](https://drive.google.com/file/d/1FtvQS1303P_GA4aM3ZbQIGPbThTXmfpq/view?usp=sharing★★★★★remove★★★★★), and [Rozanov, p 69](https://drive.google.com/file/d/1ROIF0mLquDcoMGJtj5Oz93On_ATCcfmc/view?usp=drive_link★★★★★remove★★★★★). Note that there the definition of the law of large numbers is not consistent in these references.

**a**

1. Draw $n=100$ values from a population of Gaussian-distributed numbers with mean $\mu=0$ and standard deviation $\sigma=1$.
2. Compute $\overline{X}$.
3. Repeat 1. and 2. $10,000$ times and plot a histogram of $\overline{X}$.

Save your program as `HW2_3a.py` and the associated plot as `HW2_3a.png`. When I execute your program, I should see a histogram with _**the average of**_ $\overline{X}$ displayed in the title and it should write the file `HW2_3a.png`.

**Answer**

See [HW2_3a.py](https://github.com/rweigel/astrostats/blob/main/hws/HW2_3a.py).

From the following plot, it should be clear that when we draw $100$ values from a population with a mean of zero, the average of the $100$ values will not always be zero. The standard deviation appears to be approximately $0.1$, which is smaller than $\sigma$ by a factor of $10$.

<img src="solns/HW2_3a.svg"/>

**b**

1. For $n=100$, what fraction of the $10,000$ $\overline{X}$s were in the range $[-0.01, 0.01]$?
2. How does the fraction depend on $n$? <sup>+</sup>
3. For $n=100$, what is the range $[-\epsilon,\epsilon]$ for which $99$% of the $10,000$ $\overline{X}$s fall in?
4. How does $\epsilon$ depend on $n$? <sup>+</sup>
5. How does your answer change if the distribution changes (that is, if you draw values from a distribution other than Gaussian)?

<sup>+</sup> You may explain this using one or more of words, tables, and plots.

Save your program as `HW2_3b.py`. Save your answers in a file named `HW2_3b.pdf`.

**590 students**: Be prepared to discuss in class how this experiement is related to the Weak Law of Large Numbers.

**Answer**

See [HW2_3b.py](https://github.com/rweigel/astrostats/blob/main/hws/HW2_3b.py)

1. 7.6%
2. The following plot shows the dependence (four $n$ values were used). As $n$ increases, the standard deviation of the histogram of $\overline{X}$ decreases so that more of the distribution is in the range $[-0.01, 0.01]$. A fit was given because the scaling seemed to be a power law (for larger $n$, it won't be).

   <img src="solns/HW2_3b2.svg"/>
3. `[-0.258, 0.258]`
4. The following plot shows the dependence (four $n$ values were used).

   <img src="solns/HW2_3b4.svg"/>
5. In [HW2_3a.py](https://github.com/rweigel/astrostats/blob/main/solns/HW2_3a.py), there is a line with `np.random.uniform` commented out. Try running the code with it uncommented and notice that the histogram is still Gaussian--ish even though a uniform distribution was used for the $n$ $X$s.

## Central Limit Theorem

The Central Limit Theorem (very roughly) says that as $n\rightarrow\infty$, the sampling distribution of $\overline{X}\equiv\frac{1}{n}\sum_{i=1}^n X_i$ approaches a Gaussian with mean $\mu$ and standard deviation $\sigma/\sqrt{n}$. 

(The statement also requires $\sigma$ to be finite and non--zero and $X$ iid; see DeGroot Chapter 6 and Rozanov p 78 for a formal definition. A key limitation of this statement is that the limiting distribution is a delta function and the CLT does not tell us what $n$ is required to give use a sampling distribution that is Gaussian within some tolerance; the answer depends on the distribution of $X$. )

Important: this theorem applies even if the distribution of the values used in computing $\overline{X}$ are not Gaussian--distributed.

With the Central Limit theorem, and if the sampling distribution of $X$ is not Gaussian, but $n$ is large enough so that the sampling distribution of $\overline{X}$ is "close enough" to Gaussian (this would need to be justified analytically or via simulation), or if the sampling distribution of $X$ is Gaussian (in which case the sampling distribution of $\overline{X}$ is Gaussain for any $n$, which can be shown without the CLT) we can make statements such as "I took a sample of $n$ values and computed $\overline{X}$. If I took many samples and computed many $\overline{X}s$, approximately 95\% of the time the range $[\overline{X}-1.96\sigma/\sqrt{n},\overline{X}+1.96\sigma/\sqrt{n}]$ would include ("trap") $\mu$.

In the previous problem, you computed a histogram of $10,000$ $\overline{X}$. Based on the Central Limit Theorem

1. This histogram should be approximately Gaussian;
2. The mean of $\overline{X}$ should be approximately $\mu$, which is the population mean; and
3. This standard deviation of $\overline{X}$ should be approximately $\sigma/\sqrt{n}$, where $\sigma$ is the population standard deviation.
4. 95\% of the time the range $[\overline{X}-1.96\sigma/\sqrt{n},\overline{X}+1.96\sigma/\sqrt{n}]$ should include ("trap") $\mu$

Create one or two plots that demonstrate these points. Pay careful attention to your annotations. Save your code as `HW2_4.py` and plots as `HW2_4.png` (use subplots).

**Answer**

See [HW2_4.py](solns/HW2_4.py)

<img src="solns/HW2_4.gaussian.svg">

<img src="solns/HW2_4.uniform.svg">

## Reading

Background reading on Discrete Probability Distributions: [Devore Chapter 3]((https://drive.google.com/file/d/1bN68ELL0DBrgVwbE0m74LPuTwoHqXw2M/view?usp=sharing★★★★★remove★★★★★)

Alternatives: [Bulmer Chapters 1 and 2](https://drive.google.com/file/d/1IuANm_ZxtuY75c9Caguv3cdG8JbmkADi/view?usp=sharing★★★★★remove★★★★★), [Bonamente Chapter 3](https://drive.google.com/file/d/1Z4uN1ReMXAUMZck_UmavM3lIGrbE1U-C/view?usp=sharing★★★★★remove★★★★★), [Rozanov Chapter 5](https://drive.google.com/file/d/1ROIF0mLquDcoMGJtj5Oz93On_ATCcfmc/view?usp=drive_link★★★★★remove★★★★★), [Larson Chapter 4](https://drive.google.com/file/d/1Cc65FWiptQLqtXiKHpB2JJDLe-dh7WtX/view?usp=drive_link★★★★★remove★★★★★) and [DeGroot Chapter 5.1-5.6](https://drive.google.com/file/d/1FtvQS1303P_GA4aM3ZbQIGPbThTXmfpq/view?usp=sharing★★★★★remove★★★★★).

# HW 3

Due Thursday, February 13th at 11:59 pm.

Save all files in your repository in the same directory as HW #1 (don't use subdirectories or branches).

In problem 1, a part is shown in a box that is due before class starts (this part is only graded as complete or incomplete). I want you to save your answers to these in a plain text file because it is easiest for me to cut and paste all answers into a single document.

Also, do the reading given in item 4. before class starts.

See [pmf.py](https://github.com/rweigel/stats/tree/main/notes/code) for suggesting on creating a plot of a probability mass function (aka discrete probability distribution function) in Python.

## Binomial Distribution

A Bernoulli trial has 

* two possible outcomes;
* the probability of "success" is $p$ and the probability of "failure" is $1-p$;
* these probabilities don't change

For $n$ trials, the probability of $k$ successes is given by the Binomial distribution:

$$P(k)={n \choose k}p^k(1-p)^{n-k}$$

In [Devore](https://drive.google.com/file/d/1szqKzodtocD8sMhvx7SzGJgqG-PNd2vb★★★★remove★★★★) 3.4, an experiment that conforms to the Bernoulli trials constraints is referred to as a "Binomial Experiment."

(As noted in class, sometimes we write $P(k; n,p)$ to indicate that we are interested in the function $P(k)$, which has parameters $n$ and $p$ that affect its shape. Also, I am using $k$ here, but in class, I used $x$; I think $k$ is a better choice because we usually think of $k$ as an integer and $x$ as a real number.)

1. Use a random number generator to simulate 10,000 Binomial experiments with $n=100$ and $p=0.4$ and plot $P(k)$. That is, execute 10,000 experiments in which the experiment is selecting 100 values from the list `[0, 1]` with the probability of selecting a $1$ being $p$. On the same axes, plot $P(k)$ expected from the equation above using the given $n$ and $p$. 

2. In the next class, I'll show that as $n\rightarrow \infty$, and for $k \ll np$,

    $$P(k)\rightarrow \frac{1}{\sqrt{2\pi n p q}} e^{-(k-np)^2/2npq}$$

    where $q \equiv 1-p$ (the symbol $\equiv$ means "is defined to be"). Plot this on the same axes as $P(k)$ in part 1.

3. Suppose $p$ follows the rule: "If two trials in a row are a success, the probability of success on the next trial is $0.44$; otherwise, the probability of success is $p=0.4$". Modify your code for 1. to do this, and plot the resulting $P(k)$ on the same axes as $P(k)$ in part 1.

Save your code as `HW3_1.py` and the plot as `HW3_1.png`.

> In a file named `HW3.txt`, provide brief answers to the following questions (post to your GitHub repository before class):
>
> 1. How is part 1. related to problem HW #1, problem 6?
> 1. What is an interpretation of the meaning of the constraint $k \ll np$?
> 1. You are given a list of $10,000$ `0's and `1's and the claim that the values were generated by Bernoulii trials. How would you test this claim?

**Answer**

[HW3_1.py](solns/HW3_1.py)

<img src="solns/HW3_1.svg">

## Poisson Distribution

The Poisson distribution can be derived as a limit of the Binomial distribution; see [Devore 3.6](https://drive.google.com/file/d/1szqKzodtocD8sMhvx7SzGJgqG-PNd2vb★★★★remove★★★★).

If

1. in a sufficiently short amount of time, $\Delta t$, only 0 or 1 event can occur (two or more simultaneous events are impossible); and
2. the probability of exactly one event occurring in $\Delta t$ is equal to $\lambda \Delta t$, where $\lambda$ is a constant.

the probability of $k$ events occurring in the time interval $t=n\Delta t$ is

$$P(k)=\frac{(\lambda t)^k e^{-\lambda t}}{k!}$$

for sufficiently large $n$. Said another way, if you measure events with a recording device, choose the sampling rate of the recording device to be small enough that two events never occur in the same $\Delta t$, and let the device record for a time of $t=n\Delta t$, the probability of recording $k$ events in a recording time of $t$ is given by the above formula. To estimate $\lambda$, one can use $p$ using $k/n$ and $\lambda = p/\Delta t$.

In class, I derived the formula

$$P(k)=\frac{\mu^k e^{-\mu}}{k!}$$

where $\mu \equiv pn$.

The two forms for $P(k)$ are related by using $t\equiv n\Delta t$, to give

$$P(k)=\frac{\ds\left(p\frac{t}{\Delta t}\right)^k e^{-p\large\frac{t}{\Delta t}}}{k!}$$

and $\lambda \equiv p/\Delta t$, which is the average number of events per $\Delta t$ to give

$$P(k)=\frac{(\lambda t)^k e^{-\lambda t}}{k!}$$

Use a random number generator to create a dataset that simulates the following result. Every hour, the number of x-ray flares is tabulated. It is found that over $1,000$ days, $900$ flares occurred so that the average probability of a flare in a given hour is $900/(1000\cdot 24)$.

1. Plot

   a. $P_S(k)$, the probability of $k$ flare events occurring **per day** for the **S**imulated dataset,

   b. $P_P(k)$ expected from the equation above using the value of $\lambda$ computed based on the **P**oisson distribution equation above, and

   c. $P_B(k)$ expected from the **B**inomial distribution, from which the Poisson distribution was derived.

2. From your dataset, derive a new dataset, the time between flares, and plot a histogram of the time between flares.

Save your code as `HW3_2.py` and the plot as `HW3_2.png`. Spend time thinking about the label axes, title, legend, colors, and annotations. As discussed, you want to have enough detail on the plot so that a reader can start to make interpretations without having to read or hear a long description. 

Be prepared to justify any differences between the three cases in class.

**Solution**

See [HW3_2.py](https://github.com/rweigel/astrostats/blob/main/solns/HW3_2.py)

<img src="solns/HW3_2a.svg"/>

<img src="solns/HW3_2b.svg"/>

<img src="solns/HW3_2c.svg"/>

Same as above but semilogy.

<img src="solns/HW3_2d.svg"/>

**Student Solution Comments**

Many students presented their solution in the following form. For the first plot, the bin edge less than zero is potentially confusing. In my plot for HW3_1, I used bars and made them a bit thinner; this too may be misleading and very thin bar may be argued to be more appropriate. The connected lines are inappropriate because all x--values are integer. 

For the second plot, the bin width is not integer, but should be because the data are integer. One could again use thin bars. In my case, thin bars or stems made the plot look too cluttered, so I went with dots.

Note that I generally don't take points off for minor presentation issues like this. However, I do comment on them in the hopes that you make improvements in future homeworks. (Quite often I find myself revising my plots because I think something is not clear enough. It is much like revising writing -- you revise until you run out of ideas for improvement.)

<img src="solns/HW3_2a.example.png"/>

<img src="solns/HW3_2b.example.png"/>

## Expectation Values and Biased Estimator

A summary (or descriptive) statistic is a quantity that summarizes an aspect of a collection of data. Examples include the mean and standard deviation. Descriptive statistics are always based on a computation done on a **sample** (subset) of the population of data. 

Definitions

* **Population** - "All" of the data is called the population. A population can be finite or infinite. An example of a finite population is all US citizens. An example of an infinite population is values from a continuous probability density function.
* **Sample statistic estimator** - a computation based on a sample from a population that gives an estimate of the equivalent value that would be obtained if the same computation was performed on the population. ([Devore](https://drive.google.com/file/d/1szqKzodtocD8sMhvx7SzGJgqG-PNd2vb★★★★remove★★★★) p214)

   It is important that sample statistic estimators are **unbiased**. If we compute a sample statistic based on a sample from a population and repeat this process many times, we want the average of the sample statisic to be equal to the corresponding population statistic.

An example of an unbiased sample statistic estimator is the sample average defined by

$$\overline{X}=\frac{1}{n}\sum_{i=1}^n X_i\$$

We usually used this to estimate the population mean without thought. 

Suppose we have a population of $1000$ numbers with a mean $\mu$. If our experiment is drawing $n$ numbers at random with replacement, compute the average $\overline{X}_1$, and repeat this experiment $N_e\rightarrow \infty$ times, it can be shown that the average of these averages will be $\mu$, the population average. Mathematically, this is

$$
\lim_{N_e\rightarrow \infty} \frac{1}{N_e}\sum_{i=1}^{N_e}\overline{X}_i = \mu
$$

The distribution of the $\overline{X}$ values in the sum is called the **sampling distribution** ([Devore](https://drive.google.com/file/d/1szqKzodtocD8sMhvx7SzGJgqG-PNd2vb★★★★remove★★★★) p214). If the limit is satisfied, we can state that $\overline{X}$ is an unbiased estimator of $\mu$.

Given that we estimate $\mu$ from a sample of $n$ values from the population using 

$$\overline{X}=\frac{1}{n}\sum_{i=1}^n X_i$$

and the definition of the variance of a population of $N$ is

$$\sigma^2= \frac{1}{N}\sum_{i=1}^N(X_i-\mu)^2$$

It seems that we should estimate $\sigma^2$ using

$$S_{b}^2 = \frac{1}{n}\sum_{i=1}^n(X_i-\overline{X})^2$$

Demonstrate using a simulation that $S_{b}^2$ is biased by drawing $n=10$ values from at normal distribution with $\mu=0$ and $\sigma=1$, computing $S_{b}^2$, and repeating $N_e=10,000$ times. Plot the histogram of the $10,000$ $S_{b}^2$ values, and, in the title, display the average and variance of the $10,000$ $S_{b}^2$ values. Save your code as `HW3_3.py` and plot as `HW3_3.png`.

In class, I'll show how to prove that $S_b^2$ is a biased estimator mathematically.

**Solution**

See [HW3_3.py](https://github.com/rweigel/astrostats/blob/main/solns/HW3_3.py)

<img src="solns/HW3_3.png" width="600px"/>

## Reading

[Devore](https://drive.google.com/file/d/1szqKzodtocD8sMhvx7SzGJgqG-PNd2vb★★★★remove★★★★) Ch 6 and 7.1-7.2.

# HW 4

## Proof that $S_b^2$ is a Biased Estimator of $\sigma^2$

(Note that Devore p 245 has a briefer proof with many steps skipped; I'd prefer you fill in the gaps in my proof outlined below, but if you use Devore's method, justify the steps he skipped. I prefer use of this longer proof initially, because it forces one to understand the details in some of the short--cuts.)

In class, I gave part of the proof that $E\left[S^2_b\right] = \sigma^2(n-1)/n$, where $S_b^2=\frac{1}{n} \sum_{i=1}^n(X_i-\overline{X})^2$, which was

$$E\left[S^2_b\right] = E\left[ \frac{1}{n} \sum_{i=1}^n(X_i-\overline{X})^2 \right]$$

expanding the square gives

$$E\left[S^2_b\right] = E\left[ \frac{1}{n} \sum_{i=1}^n(X_i^2-2X_i\overline{X}+\overline{X}^2) \right]$$

or, equivalently,

$$I.\qquad E\left[S^2_b\right] = E\left[ \frac{1}{n} \sum_{i=1}^nX_i^2-\frac{2}{n}\sum_{i=1}^nX_i\overline{X}+\frac{1}{n}\sum_{i=1}^n\overline{X}^2 \right]$$

The second term in the square braces in Equation $I.$ can be simplified by noting that $\overline{X}$ does not depend on $i$, so it can be factored out:

$$\frac{2}{n}\sum_{i=1}^nX_i\overline{X}=2\overline{X}\left(\frac{1}{n}\sum_{i=1}^nX_i\right)$$

Using this and the definition $\overline{X}\equiv (1/n)\sum_{i=1}^nX_i$, the second term in Equation $I.$ is

$$\frac{2}{n}\sum_{i=1}^nX_i\overline{X}=2\overline{X}^2$$

The third term is 

$$\frac{1}{n}\sum_{i=1}^n\overline{X}^2=\frac{1}{n}n\overline{X}^2=\overline{X}^2$$

Therefore, the second and third terms combine to be $-2\overline{X}^2+\overline{X}^2=-\overline{X}^2$ and Equation $I.$ simplifies to

$$E\left[S^2_b\right] = E\left[ \frac{1}{n} \sum_{i=1}^nX_i^2-\overline{X}^2\right]$$

Distributing the $E$ to each of the two terms by using $E[a+b]=E[a]+E[b]$ gives

$$E\left[S^2_b\right] = E\left[ \frac{1}{n} \sum_{i=1}^nX_i^2\right]-E\left[\overline{X}^2\right]$$

or

$$E\left[S^2_b\right] = \frac{1}{n}\left( E[X_1^2] + E[X_2]^2 + ...\right)-E\left[\overline{X}^2\right]$$

Note that $E[X_1^2]$ means "the expectation of the first value of the sample". The first value drawn can take on any value in the population, so $E[X_1^2]=E[X^2]$. Using this, we have

$$II.\qquad E\left[S^2_b\right] = E\left[X^2\right]-E\left[\overline{X}^2\right]$$

Both of the terms in Equation $II.$ can be re-written using $\mu$, $\sigma$, and $n$.

The first term simplifies to

$$E\left[X^2\right]=\mu^2+\sigma^2,$$

which follows from the definition

$\sigma^2 \equiv E\left[(X-\mu)^2\right]$, expanding the square and using $E[a+b]=E[a]+E[b]$ to give

$$\sigma^2 = E\left[X^2-2\mu X+\mu^2\right] = E\left[X^2\right]-2\mu E[X]+E[\mu^2]$$

Using the definition $\mu \equiv E[X]$ and the fact that $E[\mu^2]=\mu^2$ because $\mu$ is a constant, this simplifies to

$$\sigma^2 = E[X^2]-\mu^2$$

giving $E\left[X^2\right]=\mu^2+\sigma^2$ as claimed.

Therefore, the first term in Equation $II.$ is

$$\frac{1}{n}\sum_{i=1}^n E\left[ X_i^2 \right]=\frac{1}{n}\sum_{i=1}^n (\mu^2+\sigma^2)=\frac{1}{n}n(\mu^2+\sigma^2)=\mu^2+\sigma^2$$

The second term in Equation $II.$, $E[\overline{X}^2]$, can be rewritten as

$$E\left[\overline{X}^2\right]=E\left[\left(\frac{1}{n}\sum_{i=1}^nX_i\right)^2\right]=\frac{1}{n^2}E\left[\left(\sum_{i=1}^nX_i\right)^2\right]$$

The square of the sum,

$$\left(\sum_{i=1}^nX_i\right)^2=(X_1+X_2+...)(X_1+X_2+...)$$

expands to 

$X_1^2+X_1(X_2+X_3+...+X_n)+$

$X_2^2+X_2(X_1+X_3+X_4+...+X_n)+$

$...$

$X_n^2+X_n(X_1+X_2+...+X_{n-1})$

Let $X^\prime=X-\mu$. Then, the above can be written as 

$(X^{\prime}_1+\mu)^2+(X^{\prime}_1+\mu)(X^{\prime}_2+\mu+X^{\prime}_3+\mu+...+  X^{\prime}_n+\mu)$

$(X^{\prime}_2+\mu)^2+(X^{\prime}_2+\mu)(X^{\prime}_1+\mu+X^{\prime}_3+\mu+...+X^{\prime}_n+\mu)+$

$...$

$(X^{\prime}_n+\mu)^2+(X^{\prime}_n+\mu)(X^{\prime}_1+\mu+X^{\prime}_2+\mu+...+X^{\prime}_{n-1}+\mu)$

We are given that $E\left[X^\prime_iX^{\prime}_j\right]=0$ for $i\ne j$ because the values in the sample are uncorrelated.

**Problems**

1. Show that

   $E\left[X^\prime\right]=0$, 

   $E\left[X^{\prime 2}\right]=\sigma^2$.

2. Finish the proof that $E\left[S^2_b\right] = \sigma^2(n-1)/n$.

**Answer**

1\.

$E[X'] = E[X-\mu] = E[X] - \mu = \mu - \mu = 0$

$E\left[X^{\prime 2}\right] = E\left[X^2 - 2\mu X - \mu^2\right] = E\left[X^2] - E[2\mu X] - E[\mu^2\right] = E[X^2] - 2\mu^2 - \mu^2=E[X^2] - \mu^2$
   
Earlier it was shown that $E\left[X^2\right]=\mu^2+\sigma^2$, so substitution gives

$E\left[X^{\prime 2}\right] = \sigma^2$

2\.

Consider the first row of the expansion of $\left(\sum_{i=1}^nX_i\right)^2$

$(X^{\prime}_1+\mu)^2+(X^{\prime}_1+\mu)(X^{\prime}_2+\mu+X^{\prime}_3+\mu+...+  X^{\prime}_n+\mu)$

$(X^{\prime}_2+\mu)^2+(X^{\prime}_2+\mu)(X^{\prime}_1+\mu+X^{\prime}_3+\mu+...+X^{\prime}_n+\mu)+$

$...$

$(X^{\prime}_n+\mu)^2+(X^{\prime}_n+\mu)(X^{\prime}_1+\mu+X^{\prime}_2+\mu+...+X^{\prime}_{n-1}+\mu)$

Its first term, $(X^{\prime}_1+\mu)^2$, is $X_1^2$, which has an expectation value of $E[X]$, which was shown earlier to be $\mu^2+\sigma^2$.

In the second term,

$(X^{\prime}_1+\mu)(X^{\prime}_2+\mu+X^{\prime}_3+\mu+...+  X^{\prime}_n+\mu),$

there are $n-1$ $\mu$ terms so it can be re--written as

$$X^{\prime}_1X^{\prime}_2+X_1^\prime X^{\prime}_3+...\mu(n-1)\mu$$

Becuase $E[X_i^\prime X_j^\prime] = 0$, 

$$E\big[X^{\prime}_1X^{\prime}_2+X_1^\prime X^{\prime}_3+...+\mu^2(n-1)\big]=\mu^2(n-1)$$

Thus,

$E\left[(X^{\prime}_1+\mu)^2+(X^{\prime}_1+\mu)(X^{\prime}_2+\mu+X^{\prime}_3+\mu+...+  X^{\prime}_n+\mu)\right]=\mu^2+\sigma^2 + \mu^2(n-1) = \sigma^2+n\mu$

We only considered one row. There are a total of $n$ rows, so

$$E\left[\overline{X}^2\right]=\frac{1}{n^2}E\left[\left(\sum_{i=1}^nX_i\right)^2\right]=\frac{1}{n^2}(n\sigma^2+n^2\mu)=\mu^2+\sigma^2/n$$

In summary, we have shown that $E[X^2]=\mu^2+\sigma^2$ and $E[\overline{X}^2]=\mu^2+\sigma^2/n$. As a result, Equation $II.$ simplifies to

$$E[S_{b}^2] = E\left[ X^2 \right] - E\left[ \overline{X}^2 \right] =\mu^2+\sigma^2-\left( \mu^2+\sigma^2/n\right) = \sigma^2-\sigma^2 /n$$

or,

$$E[S_{b}^2] = \frac{n-1}{n}\sigma^2$$

with the interpretation that $S_b^2$ is downward biased by a factor of $(n-1)/n$.

This equation makes sense in one limit - suppose we draw a single sample from a distribution with variance $\sigma^2$. $S_b^2$ will always be zero, which is less than $\sigma^2$ for any nonzero $\sigma$.

It follows from the calculation above that an unbiased estimate of the variance of a population is

$$S^2=\frac{1}{n-1}\sum_{i=1}^n(X_i-\overline{X})^2$$

because $E[S^2]=\sigma^2$. Note that when $n=1$, $S^2$ is $0/0$, which indeterminate; this makes sense as -- we don't expect to be able to estimate the variance of a population with only one sample.

Recall that, in contrast, an unbiased estimate of $\mu$ is

$$\overline{X}=\frac{1}{n}\sum_{i=1}^n X_i$$

which has $n$ and not $n-1$.

----

Devore on pg 245 starts with the observation that for the variance of random variable $Y$, $V(Y)$, can be written 

$$V(Y)=E[Y^2]-(E[Y])^2$$

or, rearranging,

$$A.\qquad E[Y^2]=V(Y)+(E[Y])^2,$$

which is stated without proof. The formula is also given on page 112, but a proof is not given.

Next, he states that it follows from the definition

$$S^2 = \frac{1}{n-1}\sum_{i=1}^n(X_i-\overline{X})^2$$

that

$$S^2 = \frac{1}{n-1}\left[\sum_{i=1}^nX_i^2-\frac{1}{n}\left(\sum_{i=1}^nX_i\right)^2\right].$$

Taking the expectation and moving it inside of the sum in the first term gives

$$E[S^2] = \frac{1}{n-1}\left(\sum_{i=1}^nE[X_i^2]-\frac{1}{n}E\left[\left(\sum_{i=1}^nX_i\right)^2\right]\right)$$

Using equation $A.$, which is $E[Y^2]=V(Y)+(E[Y])^2$, with $Y=X$ is $E[X^2]=V(X)+(E[X])^2=\sigma^2+\mu^2$ using the definitions of $\sigma$ and $\mu$. Using this, the above equation can be re-written as

$$E[S^2] = \frac{1}{n-1}\left(\sum_{i=1}^n(\sigma^2+\mu^2)-\frac{1}{n}E\left[\left(\sum_{i=1}^nX_i\right)^2\right]\right)$$

Using equation $A.$ again, which is $E[Y^2]=V(Y)+(E[Y])^2$, this time with $Y=\sum_{i=1}^n X_i$ gives

$$E\left[\left(\sum_{i=1}^n X_i\right)^2\right]=V\left(\sum_{i=1}^n X_i\right)+\left(E\left[\sum_{i=1}^n X_i\right]\right)^2=n\sigma^2+(n\mu)^2$$

so now

$$E[S^2] = \frac{1}{n-1}\left(\sum_{i=1}^n(\sigma^2+\mu^2)-\frac{1}{n}\left[n\sigma^2+(n\mu)^2\right]\right)$$

or

$$E[S^2] = \frac{1}{n-1}\left(n(\sigma^2+\mu^2)-\frac{1}{n}(n\sigma^2+n^2\mu^2)\right)=\sigma^2$$

----

Alternative proof (from J.G.). Start with

$$E\left[S^2_b\right] = E\left[ \frac{1}{n} \sum_{i=1}^n(X_i-\overline{X})^2 \right]$$

and replace $X_i$ with $X_i-\mu$ and $\overline{X}$ with $\overline{X}-\mu$, then expanding the square and using the definition of $\sigma^2$ gives

$$E\left[S^2_b\right] = E\left[ \sigma^2 - (\overline{X}-\mu)^2\right]$$

or

$$E\left[S^2_b\right] = \sigma^2 - E\left[(\overline{X}-\mu)^2\right]$$

Using the definition of variance, this is

$$E\left[S^2_b\right] = \sigma^2 - \text{Var}\left[\overline{X}\right]$$

Next, use

$$\text{Var}\left[\overline{X}\right]=\text{Var}\left[\frac{1}{n}\sum X_i\right] = \frac{1}{n^2}\text{Var}\left[\sum X_i\right]=\frac{1}{n^2}\text{Var}\left[\sum X_i\right]=\frac{1}{n^2}n\text{Var}\left[X\right]=\frac{1}{n}\sigma^2$$

giving

$$E\left[S^2_b\right] = \sigma^2 - \frac{1}{n}\sigma^2=\frac{n-1}{n}\sigma^2$$

## Bootstraping Sampling Distribution of $S^2$

By definition, $S^2$, the point estimate of the population variance, $\sigma^2$, is defined by

$$S^2 \equiv \frac{1}{n-1}\sum_{i=1}^n (X_i-\overline{X})^2$$

Suppose an experiment is drawing a sample of $n$ values from a Gaussian distribution with $\mu=0$ and $\sigma^2=1$.

You want to assess the uncertainty by using $S^2$ as an approximation of $\sigma^2$. If you were able to do many experiments, you could compute many $S^2$ values and plot its histogram (as done in HW 3.3) to numerically generate the sampling distribution of $S^2$; this approach is called the "parametric bootstrap" and is only possible when you know (or have high confidence that you know) the population distribution's functional form and any parameter in the function.

As an alternative to resampling the population to create many $S^2$ values, you can resample the experimental data (this is referred to as non--parametric bootstrap resampling).

1. Draw a sample of $10$ values from a Gaussian distribution with $\mu=0$ and $\sigma^2=1$ and compute $S^2$.
2. Create a bootstrap sample by drawing $10$ values, with replacement, from the sample from part 1. and compute this sample's $S^2$.
3. Repeat 2. $10,000$ times and plot the probability distribution function of the $10,000$ $S^2$ values. Display the mean and variance of the $10,000$ $S^2$ values in the title.
4. Suppose someone handed you a sample of $10$ values (instead of you generating it) and said, "I used a Gaussian distribution with mean of $0$, but I don't know the value of $\sigma^2$ I used except that it was greater than $2$". How would you use your results to assess their claim about the $\sigma^2$ used?

5. **590 only**: Find an equation (derivation not needed, but cite source) for the exact sampling distribution of $S^2$ and add it to the plot. Add to the title the mean and variance of this exact sampling distribution.

**Solution**

See [HW4_2.py](https://github.com/rweigel/astrostats/blob/main/solns/HW4_2.py)

I've plotted the solution for $n=10$ and $n=100$.

For part 5., we can state that the the bootstrap sampling distribution was such that $S^2 > 2$ occured in a small fraction of the bootstrap resamples. As a result, if the bootstrap sampling distribution is a good representation of the actual sampling distribution of $S^2$, we can say that the liklihood that your sample was from a population with $\sigma^2>2$ is small. That is, it is possible for your claim to be true, but when we simulate many experiments, we find that only $n_{>}$ in $1000$ experiments yielded $S^2 > 2$. The value of $n_{>}$ is determined by counting the number $S^{*2}$ that are greater than $2$.

<img src="solns/HW4_2.n_10.png" width="600px"/>

<img src="solns/HW4_2.n_100.png" width="600px"/>

## Solar Flare Data

The file [xray.txt](http://mag.gmu.edu/git-data/astrostats/SOLAR_FLARES/xray.txt), contains rows that correspond to the year, month, day, hour, and min of a solar flare.

1. Plot the probability distribution function for the number of solar flares per day.
2. Use the data to determine the $\lambda$ parameter in the Poisson distribution and plot the distribution on the same axes used in part 1.
3. Do the data conform to the assumptions of the Poisson distribution?
4. **590 Only**: The Poisson distribution follows from the Binomial distribution. Add to the plot the values expected using the Binomial distribution

**Answer**

See [HW4_3.py](https://github.com/rweigel/astrostats/blob/main/solns/HW4_3.py)

**Comments on Student Solutions**

Many had a slightly different PMF for the data. I believe this is due to not accounting for days with no flares. This is the type of calculation for which I would create a simulated data file where I have zero flares on day 1, one on day 2, etc. and confirm that my code gives the correct result.

In my case, I have a close match between Binomial and Poisson because I used as $p$ the probability of a flare in a given minute. The Poisson follows from the Binomial when the probability is small, and so using a time scale of one minute to compute $\lambda$ gives a better match between the two.

3\.

I accepted most answers. What I was looking for was some insight or ideas on how to answer this question. Students who use flare data for their project will consider analysis to explain why there are differences (as does Wheatland, 2000).

Based on PMF, it seems not. Would should do a test on the different between the distributions, however. I also looked to see there were any trends in the number of flares per days. These data were considered in [Wheatland, 2000](https://iopscience.iop.org/article/10.1086/312739). The fit to both a binomial and Poisson distribution is poor. This is somewhat expected given that the probability that a flare occured in a given minute depends on whether a flare occured in the previous minute. From the data, I find

$P(F_t)=0.004973$

$P(F_t|F_{t-1})=0.0001912$

$P(F_t|\overline{F}_{t-1})=0.004998$

$P(\overline{F}_t)=0.99502568$

$P(\overline{F}\_t|\overline{F}_{t-1})=0.99500130$

$P(\overline{F}\_t|F_{t-1})=0.99980876$

where $F_t$ indicates a flare in minute $t$ and $\overline{F}_t$ indicates no flare. One assumption of the binomial distribution is that the probability of an event does not depend on whether an event occured in the previous "trial" (here a trial is the measurement of a flare or no flare in a given minute).

Recall that events $A$ and $B$ are independent if $P(A|B) = P(A)$.

To be consistent with this independence, we should have

$P(F_t) = P(F_t|F_{t-1})=P(F_t|\overline{F}_{t-1})$

$P(\overline{F}_t)=P(\overline{F}\_t|\overline{F}_{t-1})=P(\overline{F}\_t|F_{t-1})$

Visually, $P(F_t|F_{t-1})$ too small. However we would need to confirm that it is smaller than expected in a statistical sense using a hypothesis test. In the homework solution, I created time series with the same probability of a flare and assumed a binomial distribution to get a sense of the variability of the above probabilities.

There are many other checks that once can make. For example, does the rate of flares depend on time (it does, see Wheatland Figure 2.)

<img src="solns/HW4_3a.svg"/>

<img src="solns/HW4_3b.svg"/>

## Reading

Read Chapter 7 of [Devore](https://drive.google.com/file/d/1szqKzodtocD8sMhvx7SzGJgqG-PNd2vb★★★★remove★★★★). In class, I will ask how we could use the bootstrap method (both non--parametric or parametric) to check the claims in the chapter such as Equations 7.5, 7.10, 7.15, and 7.17.

# HW 5

(Note -- I decided not to give a problem on the exponential distribution that I started in class. I decided that it was better to build on a previous HW problem.)

## Confidence Interval on $S^2$

On page 295 of Devore, the $100(1-\alpha)$% confidence interval for the variance $\sigma^2$ of $n$ values drawn from a normal population with mean $\mu$ and variance $\sigma^2$ is

$$\left(\frac{(n-1)S^2}{\chi^2_{\alpha/2, n-1}},
\quad\frac{(n-1)S^2}{\chi^2_{1-\alpha/2, n-1}}\right)$$

where

$$S^2 \equiv \frac{1}{n-1}\sum_{i=1}^n (X_i-\overline{X})^2$$

and the $\chi^2$ values are described in Figure 7.11 on page 295. What this means is if you have $n$ values drawn from a Gaussian distribution with unknown $\mu$ and $\sigma^2$, you can estimate $\sigma^2$ using $S^2$ and associate with $S^2$ a confidence interval as given above.

Suppose that you did not know the sampling distribution of $S^2$. In this case, you would not know the equation for the confidence interval. All you have is a list of $n$ values from a single sample from a population.

In problem 3.3, you simulated the sampling distribution of $S_b^2$ (and could do so equivalently for $S^2$). You did this by drawing $n$ values from a known population distribution many times and plotting the distribution of the $S^2$ values. In this case, you knew $\mu$, $\sigma^2$, and the population distribution. As a result, this method is not useful for this problem.

In problem 4.3, you simulated the sampling distribution of $S^2$ using the bootstrap method. Instead of drawing $n$ values from a population many times and computing $S^2$ for each draw, you drew $n$ values from a single population sample (with replacement) many times and plotted the corresponding "resampled" $S^2$ values.

To compute the 95% confidence interval for the bootstrap case, and if you computed $n_b$ resamples, sort the list of $n_b$ $S^2$ values, and the lower confidence limit is the $0.025n_b$ element's value, and the upper confidence limit is the $0.975n_b$ element's value.

1. Using the values on page 296 in Devore, compute a 95% confidence interval for $\sigma^2$ using the bootstrap method.
2. In part 1., you should have found a confidence interval with an upper limit of $\sim 200,000$. This is much less than the value he quoted of $318, 064.4$. The number of samples is only $ 17 $, which is small for the bootstrap. To test the claim that the large difference in the confidence intervals is due to a small number of samples, generate $n=100$ values from a Gaussian distribution with the same mean and variance as data used in part 1. Then, compute a confidence interval using the method of example 7.15 of Devore and the bootstrap method.

**Answer**

[HW5_1.py](solns/HW5_1.py)

<img src="solns/HW5_1a.svg"/>

<img src="solns/HW5_1b.svg"/>

Note that the width of the boostrap confidence interval is similar to the "textbook" confidence interval, but the centers differ. The bootstrap $\langle S^2\rangle$ is biased downwards from the sample $S^2$. This is a known problem with bootstrap confidence intervals, and there are [alternatives](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#Methods_for_bootstrap_confidence_intervals). In general, one should try several confidence intervals and also attempt to understand bootstrap confidence intervals using simulations with data having known sampling distributions, as was done here.

## Textbook Confidence Interval

In problem 5.2, you compared a "textbook" confidence interval with that using the bootstrap. Find a problem in a textbook (or online resource) where the data is given an a confidence interval is computed using a formula. Then compute a confidence interval using the bootstrap.

**Answer**

[HW5_2.py](solns/HW5_2.py)

<img src="solns/HW5_2.svg"/>

## Reading

Read Chapter 8.1, 8.2, and 8.4 of [Devore](https://drive.google.com/file/d/1szqKzodtocD8sMhvx7SzGJgqG-PNd2vb★★★★remove★★★★).

# HW 6

## Confidence Intervals and Hypothesis Tests

Consider the following experiment: you are given a sample of $n=100$ values. You are told that they were generated by a gaussian random number generator with mean $\mu=2$ and variance $\sigma^2=2$. You are certain about the gaussian and $\sigma^2$ claim (this seems unrealistic, but simplifies the analysis), but suspect the $\mu=2$ claim is wrong because you find $\overline{x}$ of the sample is 2.4.

1. Compute a 95% confidence interval for $\mu$.

2. Use a hypothesis test to assess the claim about $\mu$. Use a significance level of 5% and let $H_0$ be $\mu=2$ and $H_a$ be $\mu \ne 2$.

3. Make an assessment about the chances that your hypothesis test conclusion (which will be reject or don't reject) is wrong. There two ways you can be wrong (only one will apply):
   * You rejected $H_0$ and $H_0$ is true (Type I error)
   * You didn't reject $H_0$ and $H_0$ is false (Type II error). Note that $H_0$ can be false because for an infinite number of reasons because there are an infinite number of $\mu$ values that could have been used to generate the $n$ values. As a result, assess only the chances that your hypothesis test conclusion is wrong assuming $\mu=2.2$.

4. Suppose you found $\overline{x}=2.1$. In this case you should not reject $H_0$, but it could be that $\mu=2.2$ was used to generate the $n$ values. Given this, what are the chances that your non--rejection is a Type II error?

5. Explain how the confidence interval and the results of parts 2. and 3. are related.

In class, I used visual representations of [confidence intervals](http://localhost:2025/notes/code/sampling_dists.py) and a hypothesis test problem such as [Devore 8.6](http://localhost:2025/index.md!#hypothesis-testing-notes&l=128&c=1) to explain their interpretation and meaning. To support and explain your answers, use plots and annotations.

Save your hand--written answers as `HW6_1.pdf`, plots as `HW6_1{a,b,etc}.png`, and code as `HW6_1.py`.

**Answer**

[HW6_1.py](solns/HW6_1.py)

1. 95% CI is [2.12, 2.68]. See Figure 1.
2. 2.4 is in the rejection region (see Figure 2) for $H_0\Rightarrow$ Reject claim.
3. Here we rejected, so probability this was incorrect is 5%. See Figure 2.
4. If $\overline{x}_{\text{sample}}=2.1$, we do not reject $H_0$. This non--rejection could be wrong if true population mean is $\mu'=2.2$. Figure 3. shows how this probability is computed. 
5. If the confidence interval does not include $\mu=2.0$, we reject the hypothesis that $\mu = 2.0$. When $\overline{x}_{\text{sample}}$ is in the range $[1.72, 2.28]$ (values shown on Figure 2), the blue confidence interval includes $\mu=2$ and we do not reject the hypothesis that $\mu=2.0$. So the confidence interval conveys the same information as the hypothesis test and when seeing only a confidence interval, you should recognize the implied hypothesis test. (The CI provides more information because it is the 95% "trapping" interval for $\mu$; also, if we test a null hypothesis with any $\mu$ outside the CI, we will reject.)

Figure 1.

<img src="solns/HW6_1a.svg"/>

Figure 2.

<img src="solns/HW6_1b.svg"/>

Figure 3.

<img src="solns/HW6_1c.svg"/>

Figure 4: $\beta$ for a range of $\mu'$ values. ($\mu'$ is used for values of the population mean that are not equal to the one considered in $H_0$.) Note that the $\mu'=2$ case is not plotted ($d=0$) because $\beta$ is associated with the probability of not rejecting $H_0$ when it is false so it only makes sense to check $\mu'$ values that are false with respect to $H_0$; if $\mu'=\mu$, $H_0$ is true.

<img src="solns/HW6_1d.svg"/>

## $P$--value

Instead of performing a hypothesis test on a claim such as $H_0$: $\mu=2$ and $H_a$: $\mu \ne 2$ with a significance level of $\alpha$, some researchers will simply state "$\mu \ne 2$ with $P=0.0047$". What does this mean? Provide a visual explanation.

Save your hand--written answers as `HW6_2.pdf`, plots as `HW6_2.png`, and code as `HW6_2.py`. (If your annotations are sufficient to answer the question, the pdf may be omitted.)

**Answer**

Code for figure is in [HW6_1.py](solns/HW6_1.py).

The figure below is Figure 2. from the previous problem modified so the total rejection area is $p/2$. When one states "$\mu \ne 2$ with $P=0.0047$", it means $\overline{x}_{\text{sample}}$ was such that the rejection area for $H_0$: $\mu=2$ is $P$. Usually the researcher will state what $\overline{x}_{\text{sample}}$ is. Based on the statement and the fact that the non--rejection region limits are $[1.6, 2.4]$, we can conclude that the researcher's sample yielded $\overline{x}=1.6$ or $\overline{x}=2.4$.

The logic associated with "$\mu \ne 2$ with $P=0.0047$" is

* $\alpha=0.0047$
* $H_0$: $\mu=2$
* $H_a$: $\mu\ne 2$

The experiment gave $\overline{x}_{\text{sample}}=2.4$ (or 1.6) $\Rightarrow$ reject $H_0$.

<img src="solns/HW6_2.svg"/>

## Interpretation results of HW 6.1 and 6.2

Write an interpretation of the results of problems 6.1 and 6.2 that is wrong in as many ways as possible. For inspiration, see cautions about interpretation in chapter 7 and 8 of Devore, [Sawilowsky, 2011, Statistal Fallacies](https://drive.google.com/file/d/13w5qqFfhgmf1K02WEsBMdPOeV0Y3nEUC/view?usp=sharing★★★★★remove★★★★★), [Greenland et al., 2016, Statistical tests, $P$ values, confidence intervals, and power: a guide to misinterpretations](https://pmc.ncbi.nlm.nih.gov/articles/PMC4877414/pdf/10654_2016_Article_149.pdf), or any other reference.

In class, we will vote on the "best worst" answer. Attempt to pack as many mistakes in as few words as possible. Save your answer in `HW6_3.pdf`.

**Comments**

There were many great answers, and I can see that students spent quite a bit of time understanding correct interpretations in order to produce incorrect statements that seems reasonable.

# HW 7

Due Friday, March 28th at 11:59 pm. I expect that most students will be mostly finished by class on Thursday, March 27th; I am giving an extra day so that you can ask questions during a class.

## Linear Regression

When fitting a straight line to data using the equation $y = bx + a$, we most often make the following assumptions about the process that generated the data. First, we assume that each of the sampled $y_i$ ($i=1,...,n$) values were generated by drawing a value from a Gaussian distribution with $\mu=0$ and standard deviation $\sigma$ and then adding to it $\beta x_i + \alpha$, where $x_i$ are values that are known with zero uncertainty. The values of $\alpha$ and $\beta$ are unknown quantities that we seek to estimate given a limited set of $n$ measurements of the population and equations for $a$ and $b$ (involving $x_i$ and $y_i$) that you typically first encounter in a physics lab.

To simulate the process of generating $y_i$ values described above, choose a value for $x_i$. Next, draw a value from a Gaussian distribution with a mean of zero and standard deviation of $\sigma$, the value of which is represented by the variable $\epsilon_i$. Then solve for $y_i$ using

$$y_i = \beta x_i + \alpha + \epsilon_i.$$

Repeating this process $n$ times will yield $n$ values of $y$ and $x$. When we do linear regression on a set of measurements, we assume that the system we took measurements from works in a way equivalent to the above process -- we give the system an input of an $x_i$ value and it returns an output $y_i$ based on this process.

In this problem, you will create a population of $N$ $(x,y)$ pairs using the above process and then draw a sample of $n$ $(x,y)$ pairs. Then, you will compute $a$ and $b$, which are estimates of the respective population parameters $\alpha$ and $\beta$.

1. Create a population of $N=1000$ $(x,y)$ pairs using $\alpha=1$, $\beta=1$, and $\sigma=0.2$. For values of $x$, use $0, 1/N, 2/N, ..., (N-1)/N$. Create a scatter plot of these $N$ $(x,y)$ values.
2. Randomly draw $n=20$ $(x,y)$ pairs with replacement from the population and plot them on the same axis as the previous plot.
3. Use the equations in your physics labs to compute $a$ and $b$ using the 20 values drawn in step 2. When your code is executed, it should print out $a$ and $b$.
4. Find a Python (if you are using Python) library that computes $a$ and $b$ for you. When your code is executed, it should print out the values of $a$ and $b$ computed with the library.

Add the values of $a$ and $b$ from parts 3. and 4. as annotations to your plot. Save your plot using `plt.savefig('HW7_1a.png', dpi=300)` if you use Python.

In your physics labs, you were typically given an equation for the uncertainty (a confidence interval) in $a$ and $b$. In this problem, you will use the non--parametric bootstrap to obtain an estimate of the uncertainty.

5. From your sample of $20$ values in part 1., randomly draw $20$ $(x,y)$ pairs with replacement $N_B=10,000$ times. For each draw, compute $a$ and $b$ (using equations or library). Use the histogram of $a$ and $b$ to estimate their 95% confidence intervals. Plot your histograms on a single page as two subplots. Add an annotation to indicate the 95% confidence intervals. Save your plot as `HW7_1b.png`.

For parts 6. and 7., see [Devore Chapter 12]((https://drive.google.com/file/d/1bN68ELL0DBrgVwbE0m74LPuTwoHqXw2M/view?usp=sharing★★★★★remove★★★★★) or [Bulmer Chapter 12](https://drive.google.com/file/d/1IuANm_ZxtuY75c9Caguv3cdG8JbmkADi/view?usp=sharing★★★★★remove★★★★★).

6. Use a $t$ test to compute the 95% confidence interval for $b$. (You'll have to research the appropriate test statistic to perform the $t$ test on.) Provide brief justifications or references for any equations. Add this confidence interval as an annotation to the plot for part 5. 

   Note that some libraries will compute confidence intervals, but I want you to look up the equations because it is not always the case that a library will compute confidence intervals, and if it does, you should compute it on your own and compare to the library result to ensure (1) the library is producing the correct result and (2) your understanding of what the library is doing is correct. Most commonly used libraries have been tested by many users, so their calculation is usually correct, and thus doing the check for (1) may seem excessive. However, quite often we mis--interpret the documentation for the library, which will be revealed by the check for (2).

7. In part 5., $N_B$ values for $a$ and $b$ were computed. Use the values to test the claim that the errors in the estimates of $a$ and $b$, given by $a-\alpha$ and $b-\beta$, respectively, are not independent. (This lack of independence was mentioned in Bulmer; take an informal observational/experimental approach to answer this question; a plot and some words will suffice).

**590 only**

8. In part 5., the non--parametric bootstrap was used to compute confidence intervals. How would the procedure be modified to use either a parametric simulation or the parametric bootstrap? (See [my notes](index.html#sampling-distribution-notes) for definitions).

9. Compute the correlation coefficient, cc, between $a-\alpha$ and $b-\beta$ using the values from part 5. Test the hypothesis $H_0$: cc $= 0$, $H_a$: cc $\ne 0$ and state at what significance level $H_0$ can be rejected (that is, compute the $P$ value).

**Extra credit**

10. In 2--D regression model, $y_i = \beta_1 x_{1i} + \beta_2 x_{2i} + + \beta_3 x_{3i} \alpha + \epsilon_i$, problems occur if $x_{1i}$ and $x_{2i}$ are correlated (called "multicollinearity"). 

   On [this web page](https://statisticsbyjim.com/regression/multicollinearity-in-regression-analysis/), an example is given using real data. 
   The author, Jim, notes that the problems created by multicollinearity include:
   
    * The coefficient estimates can swing wildly based on which other independent variables are in the model.
    * The coefficients become very sensitive to small changes in the model.
   
   Jim also notes that "Multicollinearity affects the coefficients and p-values, but it does not influence the predictions, precision of the predictions, and the goodness-of-fit statistics. If your primary goal is to make predictions, and you don’t need to understand the role of each independent variable, you don’t need to reduce severe multicollinearity.""

   Devise a numerical experiment using data that you create that demonstrates the above statements by Jim. Save your code and plots with the prefix `HW7_1_Jim`

**Answer**

See [HW7_1.py](solns/HW7_1.py)

1\. and 2\.

<img src="solns/HW7_1a.svg"/>

3\. and 4\.

```
Manual    : a = 1.046;   b = 0.880
SciPy     : a = 1.046;   b = 0.880
Difference: a = 2.2e-16; b = -2.2e-16
```

5\. Problem wording implies to use non--parametric bootstrap. Results for bootstrap will change when code is reexecuted.

```
95% CI for a using non-parametric bootstrap: [0.81, 1.18]
95% CI for b using non-parametric bootstrap: [0.66, 1.34]
95% CI for b using t distribution:           [0.64, 1.25]
Fraction of t-distribution CIs for b that trap beta: 0.951
```

<img src="solns/HW7_1b.svg"/>

<img src="solns/HW7_1c.svg"/>

6\. See above.

7\. A scatter plot of $b-\beta$ vs $a-\alpha$ shows an inverse correlation.

<img src="solns/HW7_1d.svg"/>

Another way to visually assess if they are independent is in the following plot. If $b-\beta$ and $a-\alpha$ are independent, the two histograms would have more overlap.

<img src="solns/HW7_1e.svg"/>

8\. Instead of resampling single $n=20$ sample from population with replacement $N_B$ times, draw $n=20$ values from population with replacement $N_B$ times.

9\. Results of hypothesis test are shown in title of plot for part 7.

## DFT and the Raw Periodogram I

The Fourier series model for $y$ having an odd number $N$ time steps is

$$y_t = \alpha_0 + \sum_{i=1}^{q}\left[\alpha_i \mbox{cos}(2\pi f_i t) + \beta_i \mbox{sin}(2\pi f_i t)\right] + \epsilon_t\thinspace,$$

where $\ds f_i \equiv \frac{i}{N}$ and has least-squares estimates of $\alpha$ and $\beta$ of

$\ds a_0 = \frac{1}{N}\sum_{t=0}^{N-1} y_t \equiv \overline{y}$ 
$\quad$
$\ds a_i = \frac{2}{N}\sum_{t=0}^{N-1}y_t\mbox{cos}(2\pi f_i t)$
$\quad$
$\ds b_i = \frac{2}{N}\sum_{t=0}^{N-1}y_t\mbox{sin}(2\pi f_i t)$

with $i=1,2,...,q$ and 

$
q = 
\begin{cases}
  N/2 &       \text{if } N \text{ even} \\
  (N - 1)/2 & \text{if } N \text{ odd}
\end{cases}
$

The values of $a$ and $b$ are also called the discrete Fourier transform (DFT) coefficients.

There are a total of $N$ unknown parameters in the model equation. If $N$ is even, $b_q = 0$, and so the number of free parameters in the model equation is still $N$; also, the last $a$ term simplifies: $a_q = \frac{1}{N}\sum_{t=1}^{N} y_t(-1)^t$.

(The equations for the parameter estimates $a_i$ and $b_i$ are found by multiplying the Fourier series model equation by $\mbox{cos}(2\pi f_i t)$ and $\mbox{sin}(2\pi f_i t)$ and then summing both sides over $t=1$ to $N$. In the E&M book by Griffiths, he calls this "Fourier's trick".)

The raw periodogram is defined as ([Box and Jenkins, 2016](https://drive.google.com/file/d/19hUNP5eYHSxP1oJTK_FOGKIZT1LELmo2/view?usp=sharing★★★★remove★★★★))

$$I(f_i) = \frac{N}{2}\left(a_i^2 + b_i^2\right)$$

for $i = 1,2,...,q$. To understand it, suppose $a_1=A$ and $b_1=B$, then $\left(A^2 + B^2\right)$ is the maximum value of $A\cos(2\pi t) + B\sin(2\pi t)$. When you compute the power of a wave, you compute $A^2+B^2$, so the quantity $I(f_i)$ is related to the "raw power spectrum" by a scaling factor.

Similar to the issue with "probability distribution", "power spectrum" is ambiguous. It could mean $2I/N$ so the units are the units of $y$ squared or it could be a "density", $(2I/N)/(f_1)$, so the units are (units of $y^2$)/(units of frequency). I typically avoid this issue by either labeling my y--axis as $I$ with the caption "periodogram" or by using the label $|\text{DFT}|^2$ and the caption "Magnitude of discrete Fourier transform amplitudes" if I am plotting $2I/N$.

As an example of ambiguity, consider the two plots in the [Wikipedia entry for Periodogram](https://en.m.wikipedia.org/w/index.php?title=Periodogram&oldid=1133547799). The y--axis is labeled "Spectrum" and the title is "Periodogram." In my definition above, the "spectrum" is the $2/N$ times the periodogram, $I$ so these annotations are confusing.

1. This part is unrelated to statistics, but I find myself doing this when I am trying to figure out what someone did to compute a plot and understand various other aspects of DFT calculations. The need for this is due to the definition ambiguity discussed above, indexing (MATLAB uses 1--based indexing, Python 0--based), and the fact that $q$ depends on if $N$ is even or odd.

   Consider the signal $y=[0, 1, 0, -1]$.
   
   Compute all $a$ and $b$ values using the above formulas.
   
   Use a library (e.g., `numpy.fft`) to compute $a$ and $b$. Note that most libraries compute a quantity related to $a$ and $b$ and their output is an array of complex values.

2. Create a "white noise" time series by creating a time series with $N=1000$ values drawn from a Gaussian with zero mean and unit variance and plot $I(f_i)$ vs $f_i$. The plot of $I$ should be noisy. One problem with raw periodograms is that they are noisy. Entire books are dedicated to dealing with this.

3. Plot the histogram of $I$ values.

**590 Only**

4. Look up the sampling distribution of $I$ and add it to the histogram.
5. Modify the white noise time series by adding a periodic signal $A\sin(2\pi t/100)$ and plot $I$. At what value of $A$ can you "see" evidence of the periodic signal? Suppose you were given only the values of $I$ and want to determine if there is evidence of a periodic signal. Describe in words the analysis that you would perform.

**Answer**

1\.
$\ds a_0 = \frac{1}{N}\sum_{t=0}^{N-1} y_t \equiv \overline{y}$ 
$\quad$
$\ds a_i = \frac{2}{N}\sum_{t=0}^{N-1}y_t\mbox{cos}(2\pi f_i t)$
$\quad$
$\ds b_i = \frac{2}{N}\sum_{t=0}^{N-1}y_t\mbox{sin}(2\pi f_i t)$

Using $y=[0, 1, 0, -1]$, $N=4$ and $i=1, ..., 4$

$$a_1 = (2/N)\left[0\cdot\cos(2\pi (1/4)\cdot 0) + 1\cdot\cos(2\pi (1/4)\cdot 1) + 0\cdot\cos(2\pi (1/4)\cdot 2) + (-1)\cdot\cos(2\pi (1/4)\cdot 3)\right]$$

$$a_1 = (2/N)\left[0 + 0 + 0 + 0\right] = 0$$

Using the same process as above, we find $a_2 = 0$, $b_1 = 1$, $b_2 = 0$.

`numpy.fft` computes the DFT of $y_t$ with $t=0,...,N-1$ using a formula of the form

$$Y_i = \sum_{t=0}^{N-1} y_t e^{-j2\pi t i/N}$$

The output of `numpy.fft` is an array of complex numbers, e.g.,

```
import numpy
y = np.array([0, 1, 0, -1])
Y = np.fft.fft(y)
print(Y)
# [0. + 0.j, 0. -2.j, 0. + 0.j, 0. + 2.j]
```

Expanding the complex exponential gives

$$Y_i = \sum_{t=0}^{N-1} \left[y_t\cos(-2\pi  t i/N) + jy_n\sin(-2\pi  t i/N)\right]$$

Using $f_i = i/N$, $\cos(-x)=\cos x$, $\sin(-x)=-\sin x$ gives

$$Y_i = \sum_{t=0}^{N-1} \left[y_t\cos(2\pi  f_i t) - jy_n\sin(2\pi  f_i t)\right]$$

For $N$ even, we need to compute

$\ds a_0 = \frac{1}{N}\sum_{t=0}^{N-1} y_t \equiv \overline{y}$ 

and 

$\ds a_i = \frac{2}{N}\sum_{t=0}^{N-1}y_t\mbox{cos}(2\pi f_i t)$ for $i = 1, ..., N/2$.

From this, we conclude that the $a_i$ terms are $(2/N)$(the real part of corresponding terms in the $Y_i$ array) for $i = 1, ..., N/2$. Using 

`Y = [0. + 0.j, 0. - 2.j, 0. + 0.j, 0. + 2.j]`

gives

$$a_1 = (2/N)\cdot 0 = 0$$

$$a_2 = (2/N)\cdot 0 = 0$$

Also,

$a_0 = N$real$(Y_0) = 0$

Comparing the formula for $Y_i$ above with

$\ds b_i = \frac{2}{N}\sum_{t=0}^{N-1}y_t\mbox{sin}(2\pi f_i t)$ for $i=1,...,N/2$,

we see that the $b_i$ terms are  $(-2/jN)$(the imaginary part of corresponding terms in the $Y_i$ array) for $i = 1, ..., N/2$. Using `Y = [0. + 0.j, 0. - 2.j, 0. + 0.j, 0. + 2.j]` again,

$$b_1 = (-2/4j)\cdot (-2j) = 1$$

$$b_2 = (-2/4j)\cdot (0) = 0$$

2\. See [HW7_2.py](solsn/HW7_2.py)

<img src="solns/HW7_2a.svg">

<img src="solns/HW7_2b.svg">

3\. 

<img src="solns/HW7_2c.svg">

4\. 

<img src="solns/HW7_2d.svg">

5\. When I recreate the following image many times, the value of $I$ at $f_o$ seems unusual for $A=0.2$. I've also plotted $(N/2)A^2$, which is what $I$ would be at $f_o$ if the signal was $A\sin(2\pi t/100)$. I've also plotted 1000 values from $\chi^2_2$ as a reference.

<img src="solns/HW7_2e.svg">

## Project

Perform exploratory data analysis on your project data. The objective is find ways of presenting the data that "tells the story" of its key features. What you choose to plot will depend on the data and your creativity.

If your project involves solar flare data, use the same data as used in HW #4 to start. More solar flare data is available in [the course repo](https://github.com/rweigel/stats/tree/main/project).

Save the code and plots in a subdirectory named `project` in your repository. Save your code as `project_I.py` and plots as `project_I{a,b,...}.png`.

In class on April 3rd (or March 27th if you are ready), you will

1. give a 2--minute description about the project data (where from, what values are in it, what it is used for); and
2. present at least three plots in class. If your data are time series, the first plot should be a time series of all of the data.

Do not create a PowerPoint presentation. For part 1., use the whiteboard if needed. For part 2., I will show the plots when you ask me to, and you will explain them.

# HW 8

Due April 3rd at 11:59 pm.

## Midterm Revision

Provide a revision of your mid-term by April 3rd at 4:30 pm. Turn in both your mid--term and new answers (on paper). Your mid--term grade will be based on your original and revised answers. See the [Notes](#midterm) regarding common errors.

You may not discuss these problems with any other students. You are welcome to ask me questions. If you use Discord, use a direct message.

## Project

Provide a revision to your project based on my comments (I will post comments in repositories on Saturday, March 29th for those who did not present on Thursday, March 27th).

## Bayes and Statistical Inference I

**References**

Additional background on this problem is covered in the following references. (You should be able to solve this problem without them, however.)

* [Silva 2006, Chapter 2.1](https://drive.google.com/file/d/1RdCvNifZtI2PlIDVNYpMBIrD6NClNtEe/view?usp=sharing★★★★remove★★★★). In this problem, I am walking you through the steps needed to create Figures 1. and 2. This book uses a somewhat unconventional notation by explicitly including the variable $I$. You can safely ignore it in the equations written.
* The coin-tossing experiment is covered at a basic level in Chapters 1 and 4 of [Stone, 2016](https://drive.google.com/file/d/1Zy5jLQsiyXFJxoswkoEC1OovrB9yQuHf/view?usp=sharing★★★★remove★★★★).
* A much more mathematically advanced description of this problem is given in [Liu and Wasserman 2014](https://drive.google.com/file/d/13EdWDSdM2tvR7A33msj3xCg5lOQenLNG/view?usp=drive_link★★★★remove★★★★).

Let $\theta$ be an unknown parameter, such as a length or, as considered in this problem, a probability. 

Let $\mathcal{D}$ be data from an experiment, for example, the results of coin flips, e.g., $\mathcal{D}=[H,T,H,T]$. 
With these variables, Bayes' theorem is

$$P(\theta|\mathcal{D})=P(\mathcal{D}|\theta)\frac{P(\theta)}{P(\mathcal{D})}$$

When $\theta$ can take on continuous values, we can express this equation in terms of probability densities (using lowercase $p$) by replacing $P(\theta|\mathcal{D})$ with $p(\theta|\mathcal{D})d\theta$ and $P(\theta)$ with $p(\theta)d\theta$, giving

$$p(\theta|\mathcal{D})=P(\mathcal{D}|\theta)\frac{p(\theta)}{P(\mathcal{D})}$$

Recall that probability densities $p$ have the property that $\int_{x}p(x)dx=1$, where the subscript $x$ on the integral means the range of possible values of $x$.

A typical Bayesian inference problem seeks to assign a probability of $\theta$ given a set of measurements (data). That is, to assign a value to $p(\theta|\mathcal{D})$. In class, I discussed the case where we only had one or two measurements from coin tosses, that is, $\mathcal{D}=[H]$, and $\mathcal{D}=[H, H]$, respectively. In this problem, you will consider these two cases in detail.

Recall that for a coin-tossing problem, the probability of $k$ "successes" in $N$ trials

$$P_k={N\choose k}\theta^k(1-\theta)^{N-k}$$

where the probability of success is $\theta$.

%This is a pmf because $\sum_k P_k=1$.

We can rewrite this in terms of conditional notation by noting that the probability of an outcome resulting in $\mathcal{D}$ is given by

$$P(\mathcal{D}|\theta)={N\choose k}\theta^k(1-\theta)^{N-k}$$

%Note that this is not a pmf because $\sum_{\text{all }\mathcal{D}} P(\mathcal{D}|\theta) \ne 1$. However, we can convert it to a pmf by finding the proportionality constant $A$ such that $\sum_{\text{all }\mathcal{D}} AP(\mathcal{D}|\theta) = 1$. However, this will not be necessary because this proporinality constant will appear in the numerator and denominator on the right--hand side of the Bayes equation.

For $\mathcal{D}=[H]$,

1. Use the above equation to compute the probability of $\mathcal{D}$ given a probability of heads. That is, find an expression for the likelihood term $P(\mathcal{D}|\theta)$, which will be a function that depends on $\theta$.

The $p(\theta)$ term in Bayes theorem above is the so-called prior. Assume you are an alien, know nothing about coin-manufacturing machines, and have never seen a coin toss. Based on your lack of subjective prior knowledge, you would say all values of $\theta$ are equally likely, and thus $p(\theta)=\text{const}$. This is called a "diffuse" 
prior -- we are saying that coins can have any bias with equal probability. Using the fact that $p(\theta)$ is a probability density function, $\int_{0}^1p(\theta)d\theta=1$, so $\text{const}=1$.

2. In class, I mentioned that we often don't need to worry about the term $P(\mathcal{D})$ because it is a constant that will "cancel". To elaborate, we are often interested in a ratio of probabilities such as $P(\theta_1|\mathcal{D})/P(\theta_2|\mathcal{D})$. For example, given a sequence of coin tosses from a coin manufactured by a new machine, we would want to know the ratio of the probability that a coin has a probability of heads of $\theta_1$ to the ratio that the probability of heads is $\theta_2$. However, it is sometimes useful to compute this term explicitly. In this case, the law of total probability can be used:

   When $\theta$ is a parameter that can take on discrete values only, the Law of Total Probability is

   $$P(\mathcal{D})=\sum_\theta P(\theta)P(\mathcal{D}|\theta)$$

   When $\theta$ is a continuous parameter, replace $P(\theta)$ with $p(\theta)d\theta$ and integrate instead of sum

   $$P(\mathcal{D})=\int_\theta p(\theta)d\theta P(\mathcal{D}|\theta)$$

   Compute $P(\mathcal{D})$.

3.  Plot of $p(\theta|\mathcal{D})$ vs $\theta$.

4. Repeat parts 1.-3. for $\mathcal{D}=[H,T]$.

5. You are not an alien. Suppose your subjective judgment is that it is difficult to manufacture a coin with a probability of heads that differs much from 0.5. In equation form, you decide to use a sharply peaked Gaussian to represent this experience. That is, $p(\theta) \propto e^{-(\theta-0.5)^2/0.1}$. Using this, plot $p(\theta|\mathcal{D})$ vs. $\theta$ for $\mathcal{D}=[H,T]$.


Save your hand calculations in a file named `HW8_3.pdf`. Save your code in a file named `HW8_3.py` and plots as `HW8_3a.py`, ....

**Answer**

Analytic parts in comments in [HW8_3.py](solns/HW8_3.py).

<img src="solns/HW8_3a.svg"/>

<img src="solns/HW8_3b.svg"/>

<img src="solns/HW8_3c.svg"/>

Additional plot to demonstrate that as the amount of data increases, the influence of the prior decreases.

<img src="solns/HW8_3d.svg"/>

# HW 9

9.1 due on Thursday, April 10th before class. 9.2 and 9.3 due on Friday, April 11th at 11:59 pm.

## Project

Make the additions and modifications to your project analysis as discussed in class and/or as documented in my comments in your README.md file (you should have posted your summary what was discussed in class on April 3rd and I will have made comments on your summary by April 5th before midnight).

## Bayes and Statistical Inference II

In HW 8.3, $p(\theta|\mathcal{D})$ was computed for a coin tossing experiment. $p(\theta|\mathcal{D})$ contains information that allows us to determine how confident we are that the coin had any value of $\theta$; it can also be used to determine how "confident" we are that the coin has a value over any range of $\theta$ (by integration of the pdf over that range). In frequentist analysis, this confidence is summarized by a confidence interval. In Bayesian analysis, a different term is used: a Credible Interval, defined as the shortest interval that contains a certain fraction of the probability in the posterior pdf $p(\theta|\mathcal{D})$. In this problem, use a fraction of 0.95. Computation of the Credible Interval is not as simple as that for the confidence interval. Numerically, it can be computed by brute force by generating a list of lower boundary and interval length pairs and computing the integral of $p(\theta|\mathcal{D})$ for each pair. The pair that has an integral of $0.95$ and the shortest interval length form the Credible Interval. There are also software packages that can be used.

In problem [HW9_2.py](solns/HW9_2.py), I have computed the credible interval for the posterior found in HW 8.3.5.

<img src="solns/HW9_2.svg"/>

1. Suppose $\mathcal{D}=[H, H, T, T, H, T, T, H]$. Use a diffuse prior and compute $p(\theta|\mathcal{D})$.
2. Modify [HW9_2.py](solns/HW9_2.py) so it computes the credible interval for this $\mathcal{D}$ and the diffuse prior.
3. Read [Devore 8.3](https://drive.google.com/file/d/1bN68ELL0DBrgVwbE0m74LPuTwoHqXw2M/view?usp=sharing★★★★★remove★★★★★) and think about an answer to question 4. below.

**590 Only**

4. Write a short paragraph that describes a numerical experiment that you could do to compare a credible interval to a confidence interval for the coin tossing problem using one or more of the formulas in [Devore 8.3](https://drive.google.com/file/d/1bN68ELL0DBrgVwbE0m74LPuTwoHqXw2M/view?usp=sharing★★★★★remove★★★★★).


## DFT and the Raw Periodogram II

1. Create a "white noise" time series by creating a time series with $N=1000$ values drawn from a Gaussian with zero mean and unit variance.
2. Plot the probability density function of the $I$ (periodogram) values (see HW 7).
3. The sampling distribution of $I$ is $\chi^2_2$. That is, $\text{pdf}(I) = \chi^2_2(I)$. Add this $\text{pdf}$ curve to the plot from part 2. Find the value of $I$, $I_{0.99}$, for which $0.99 = \int_0^{I_o} \text{pdf}(I)dI$.
4. What percentage of the $I$ values computed in part 1. are above $I_{0.99}$?
5. Repeat parts 1. and 4. 1000 times and compute the average of the percentage of the $I$ values that are above $I_{0.99}$.

**590 Only**

5. Previously, you computed the modified a white noise time series by adding a periodic signal $A\sin(2\pi f_o t)$, with $f_o=1/100$ and plotted  $I(f_i)$ vs $f_i$ and visually determined when you could "see" this signal in $I$. What was the corresponding value of $I(f_o)$, $I_\text{vis}$, for this, and what is $\int_0^{I_\text{vis}} \text{pdf}(I)dI$?
6. Part 5. suggests a simple hypothesis test for the case where we know the standard deviation of the white noise signal is $1$ (if it is not $1$, this approach can still be used, but the pdf is different): $H_0$: $A=0$ and $H_a$: $A\ne 0$. If we reject $H_0$ using $p=0.01$, what is the probability of a type II error when $A=0.01$?

Be prepared to explain 5. and 6. in class. I am also going to ask a very subtle question. In part 6. we tested the hypothesis that there was a signal at a single frequency, $f_o$. Suppose we want to test the hypothesis that there is a statistically significant periodic signal at any frequency.

Notes: The method outlined above for determining if there is a statistically significant peak at a given frequency assumed that we know the signal is white noise with a known variance. In reality, we cannot be certain of either. If we are certain that the signal is white noise, but the variance is unknown, Fisher's $g$--statistic can be used ([1](https://www.mathworks.com/help/signal/ug/significance-testing-for-periodic-component.html), [2](https://drive.google.com/file/d/1vyMtouwblDUob6sU-BtIchjDA9lsKqGe/view?usp=drive_link★★★★remove★★★★), [3](https://drive.google.com/file/d/1gwclmF8Xw68lHtpOxv7uNXp0pCU2nXsD/view?usp=drive_link★★★★remove★★★★)). Also note that there are alternatives to using the raw periodogram for identifying significant peaks, for example, by instead splitting the time series into segments, computing the periodgram for each segment, and averaging the segment periodograms. The point here is that identifying statistically significant peaks is non--trivial, and you should hope that your data are such that the peak is so large that a plot of the periogram is such that there is no doubt that the peak is not explained by random fluctuations in the periodogram. (But, of course, if this is the case, it is unlikely that someone has not already observed and published the observation.)

**Answer**

<img src="solns/HW9_3a.svg"/>

<img src="solns/HW9_3b.svg"/>

# HW 10

Problem 1 is due before class starts on Thursday, April 17th.

Problems 2 and 3 are due on Friday, April 18th at 11:59 pm. However, I want to go over draft solutions during class, so please work on it before then.

## Project

Continue working on the project and updating your README.md file. The requirements for the final presenation are on the main class page.

## Posterior related to Gaussian distribution - 1 unknown

Modify [HW10_1_notes.py](solns/HW10_1_notes.py) so that is uses a prior of $p(\theta)\propto e^{-\theta^2}$

## Posterior related to Gaussian distribution - 2 unknowns

**590 Only**

Modify [HW10_2_notes.py](solns/HW10_2_notes.py) to use [Jeffrey's priors](https://en.wikipedia.org/wiki/Jeffreys_prior). For this problem, this means $p(\theta_1) = \text{const}$ and $p(\theta_2) 
\propto 1/\theta_2$.

# HW 10$^+$ Notes

The following are notes related to problems that will be assigned on HWs 10, ...

These notes and problems are working towards the goal of using a library that implements Monte Carlo Markov Chain. 

## Posterior related to Gaussian distribution - 1 unknown

You are given number, $x_o$ and and told is was generated by calling a Gaussian random number generator with a standard deviation of 1 and a mean of $\theta$, for example, by executing `np.random.normal(theta, 1, size=1)`.

Given the data $\mathcal{D}=[x_o] = [0.5]$, create a plot of the posterior pdf $p(\theta|\mathcal{D})$. You can do this analytically or using an experimental approach similar to the one I covered in class. (The experimental approach is actually more difficult.) Assume that the prior, $p(\theta)$, is zero if $|\theta|>1$ and $0.5$ for $|\theta|\le 1$. 

[Chapter 5 of Stone](https://piazza.com/gmu/spring2021/ce0c/resources) may provide some additional insight into how to approach this problem. Feel free to discuss ideas for how to approach this on Discord.

Save you answer as `HW8_2.py`. When executed, the pdf should be shown.

**Answer**

See [HW10_1_notes.py](solns/HW10_1_notes.py)

The exact answer is

$$p(\theta|\mathcal{D}) = \frac{\frac{1}{\sqrt{2\pi}}{e^{(0.5-\theta)^2/2}}}{P(\mathcal{D})}$$

where

$$P(\mathcal{D})=\int_{-1}^1\frac{1}{\sqrt{2\pi}}{e^{(0.5-\theta)^2/2}}d\theta\approx 0.625$$

(One can use a program such as Wolfram Alpha to compute this integral or use the fact that the integral is [related to the Error Function](https://en.wikipedia.org/wiki/Error_function#Name) and use the error function function in `numpy`. I used the latter in my solution.)

In the following, I show results using only 10 experiments for each $\theta$ values so that it is easy to visually check the results in the second plot based on the dots in the the first plot.

<img src="solns/HW10_1_notes_a_run-1.svg"/>

<img src="solns/HW10_1_notes_b_run-1.svg"/>

<img src="solns/HW10_1_notes_c_run-1.svg"/>

<img src="solns/HW10_1_notes_d_run-1.svg"/>

The following plots show the results when $500,000$ experiments are performed for each $\theta$ value. The plot of the grid with dots is not shown because it takes too long to render this many points. 

<img src="solns/HW10_1_notes_b_run-2.svg"/>

<img src="solns/HW10_1_notes_c_run-2.svg"/>

<img src="solns/HW10_1_notes_d_run-2.svg"/>

## Posterior related to Gaussian distribution - 2 unknowns

1. You are given number, $x_o=0.5$ and told is was generated by calling a Gaussian random number generator with a mean of $\theta_1$ and standard deviation of $\theta_2$ by executing `np.random.normal(theta1, theta2, size=1)`.
    
    Given the data $\mathcal{D}=[x_o] = [0.5]$, create a plot of the posterior pdf $p(\boldsymbol{\theta}|\mathcal{D})$ (here $\boldsymbol{\theta}$ is a vector containing $\theta_1$ and $\theta_2$). You can do this analytically or using an experimental approach similar to the one I covered in class. Assume that the prior $p(\theta_1)$ is zero if $|\theta_1|>1$ and $0.5$ for $|\theta_1|\le 1$. Assume that the prior $p(\theta_2)$ is zero for $\theta_2<0$ and $\theta_2>1$ and 1 for $0\le \theta_2\le 1$. 

    **Answer**

    See [HW10_2_notes.py](solns/HW10_2_notes.py)

    <img src="solns/HW10_2_notes_a.svg"/>

    <img src="solns/HW10_2_notes_b.svg"/>

    <img src="solns/HW10_2_notes_c.svg"/>

## Monte Carlo Integration

I mentioned how Monte Carlo integration works. Draw a closed shape on a piece of paper with a known area, $A_k$. Hang the square on the wall and throw 1000 darts at the wall with your eyes closed. An estimate of the area of the arbitrary shape is $A_{k}n_{h}/n_{k}$, where $n_{h}$ is the number of darts that fell in the shape you drew and $n_{k}$ is the number of darts that hit the paper.

To simulate tossing darts, you can use a uniform random number generator. The following code simulates tossing darts at a paper that is $2x1$. 

```Python
import numpy as np
from matplotlib import pyplot as plt
x = np.random.uniform(low=-1, high=1, size=1000)
y = np.random.uniform(low=0, high=1, size=1000)

plt.plot(x, y, '.')
```

Use Monte Carlo integration to estimate the under the curve of a parabola $y=1-x^2$ from $x=-1$ to $x=1$. (That is, the area between $y=0$ and $y=1-x^2$ with $x$ in the range of $[-1, 1]$.)

When executed, your program should print the exact area and the Monte Carlo estimate of the area for $N=10^1, 10^2, ..., 10^5$.

**Answer**

See [HW10_3_notes.py](solns/HW10_3_notes.py). Note that for 1000 points, Monte Carlo answer is off by 0.03 whereas for numerical integration with 21 rectangles, answer is only off by 0.003. Monte Carlo is less efficient when the integration is over only a few dimensions.

<img src="solns/HW10_3_notes.svg"/>

```
Numerical integration (21 rectangles): 1.33000
Exact: 1.33333
Monte Carlo 1000 points: 1.36400

N = 10^1; Area = 1.20000000
N = 10^2; Area = 1.20000000
N = 10^3; Area = 1.34400000
N = 10^4; Area = 1.34680000
N = 10^5; Area = 1.33782000
```

# Midterm Study Guide

The closed--book and closed--notes midtem will have four problems:

1. Bayes -- Compute a posterier probablity as done in class examples and homework problems and provide a visual explanation of the calculation.
2. Derivation -- one of
   * expectation value (we did for mean, variance, and slope in linear regression; I'll find another problem that is short enough for a Midterm)
   * Binomial to Gaussian or Binomial to Poisson
3. Interpretation of confidence intervals, $p$--value, and rejecting $H_0$
4. Instructions/Pseduo code -- Solve a homework problem without instructions on implementation. For example
   * "Use a function `normal` that takes inputs of $\mu$, $\sigma$, and $n$ that returns $n$ gaussian distributed values drawn from a population with mean $\mu$ and standard deviation $\sigma$ to generate the sampling distribution of $\overline{x}$."
   * "Given $n$ values, compute a bootstrap sampling distribution of $\overline{x}$"
   * "Given $n$ values, compute a bootstrap sampling distribution of $\overline{x}$ and use it to estimate the 95% confidence for $\overline{x}$"

   What I am looking for in the solutions is evidence that you understand the procedure. You do not need to provide Python code or memorize its syntax. I am looking for statements in the form of instructions, which can be in the form of pseudo code. I'll give examples of this in class before the Midterm.

If you pose your own hypothetical problem and post it to Discord with your solution, I will comment on your solution (and if it is too complex for a Mid--term problem).

Grading: A grade of 85% on a given problem means I have found evidence that you understood the concept associated with the question and if I said "this calculation does not look correct", you'd would quickly identify the issue. Scores higher than 85% correspond to fewer such "minor issues". (There is an execption -- when a "minor issue" leads to a non--sensical final answer and the fact that the final answer does not make sense is not noted, I will conclude that you don't understand the concept.)

# Midterm

## 

1. Provide a visual derivation of $P(B|A)=P(A|B)P(B)/P(A)$

> Some students gave an example of the use of this formula but did not provide either a mathematical or visual derivation. I covered several derivations in class, and they also appear in many textbooks.

2. One bag contains only white balls, while another bag contains 30 white balls and 10 black balls. A bag is selected at random, and a ball from that bag is selected at random. The selected ball is white. What is the probability that the selected ball was from the bag with only white balls?

##

Derive the Gaussian distribution from the Binomial distribution.

> In class, I mentioned key steps used in statistical mechanics to arrive at the Gaussian distribution in the random walk problem: Defining $m=N_{\text{right}}-N_\text{left}$, using Stirling's approximation, using $m/N\ll 1$ for $N$ large, and $\ln(1+\epsilon)\simeq \epsilon$ for $\epsilon \ll 1$.

##

Explain the interpretation of

1. a confidence interval,
2. not rejecting a null hypothesis, and
3. a $P$ value.

Provide examples to support your explanation, if needed.

> Most students gave a definition and not an interpretation for 2. and 3. I spend much time discussing the interpretation of a confidence interval in terms of repeated experiments. The same reasoning applies to 2. and 3.

##

1. You are given a list of $100$ numbers and asked to compute a 95% confidence interval on their average. Describe how you would calculate the confidence interval using the non--parametric bootstrap. Provide enough details so that your description can be implemented in code without ambiguity.

2. Describe how you would use a parametric simulation to determine if a sample statistic is biased.

> The wording of part 2. could have been better, or I should have put part 2. as a separate problem. Stated a different way that is perhaps to revealing, I am asking: suppose you have a sample statistic that is meant to be a proxy for a population statistic. You know the population distribution and its parameters. Instead of doing this analytically as was done for $\overline{x}$, $S^2_b$, and the slope parameter in regression in class, how would you use a simulation to determine if the sample statistic is biased?