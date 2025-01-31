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
* In class, I generated a plot by tossing a coin $n$ times and then recording the relative frequency for that $n$. I did this for $n=1, .... 1000$, so I did $1000$ independent coin tossing trials. Another student tossed a coin $1000$ times (one trial) and used the first $n$ numbers to compute the relative frequency for that $n$ (it also appears that this is how Devore generated Figure 2.2). Be prepared to discuss the difference in interpreation of the results from the two approaches.

## Sample Space

1. An experiment involves tossing a coin 3x. What is the sample space of this experiment?
2. How many of the outcomes in the sample space had two heads? 
3. Define event $A$ to be that the experiment yields two heads. Define event $B$ as the experiment yielding two tails. What is $A \cup B$ and $A \cap B$?

## Set Notation

The law of addition for any three events $A$, $B$, and $C$, is

$P(A\cup B\cup C) = P(A) + P(B) + P(C) - P(A\cap B) - P(A\cap C) - P(B\cap C) + P(A\cap B\cap C)$

Provide a visual way of justifying this. Be prepared to present your answer in class.

## Law of Addition and Set Notation

Suppose 55\% of people exercise and 45\% drink alcohol. Also, 70\% do at least one of these.

What is the probability that a randomly selected person:
1. exercises and drinks alcohol?
2. does not do at least one of the two activities?

Use a Venn diagram (or any visual method) in the way that was used in class to demonstrate your answers.

## Set Operations in Python

My basic [Python notes](python.html#sets) has examples of methods that can be used for sets in Python.

In class, we solved the Visa/Mastercard problem using the Law of Addition and also a Venn Diagram. We can also solve this using Python set operations. We were given that the probability of a student having a Visa is 0.5. So we suppose there are 100 students and students 1 through 50 have a Visa: $V =$ {$1, 2, ..., 50$}. We were given that the probability of a student having a MasterCard is 0.4 and also the probability that they have both is 0.25. We can codify this by saying students 26 through 65 have a MasterCard: $M =$ {$26, 27, ..., 65$}. The remaining students we label as $X =$ {$66, 67, ..., 100$}.

Generate sets `V`, `M`, and `X` in Python. They use set operations and the `len()` function to answer the following.

1. What is the probability that the selected individual has at least one of the two types of cards.

2. What is the probability that the selected individual has neither card type?

3. Find the probability that the student has a Visa but not MasterCard.

(Hint: For 2. and 3., you will need to create a set $M'$ using the the sample space $S={1, 2, ..., 100}$, $M$, and a set operation.)

## Random Walk Simulation

A random walk is a process analogous to flipping a fair coin. An example in physics is a cylinder constrained to move in one dimension being struck by air particles (and the cylinder moves without friction). Each strike sends the cylinder a small step to the left or right. The probability of a step to the left is the same as that of a step to the right. See also [Chapter 1 of Kittel and Kroemer](http://www.fulviofrisone.com/attachments/article/413/Kittel%20-%20Thermodynamics.pdf) for a description in the context of statistical physics.

Suppose we want to know the probability that after three strikes, the cylinder is one step the right of its initial position using a simulation (we will cover an exact answer later).

We could do an experiment where we randomly select values of $-1$ or $1$ with equal probability using `random.choice([-1, 1])` three times (`np.random.choice()` can also be used for efficiency). A result could be `[1, 1, -1]`. The final position after these steps is `sum([1, 1, -1]) = 1`. To compute the probability that the final position is $1$, we can repeat this experiment many times and count the number of times the final position is $1$.

1. How many possible step configurations are possible? That is, what is the sample space of the experiment of taking three steps to right or left, with equal probability for each direction?
2. Write a program for a simulation that gives an estimate the probability that the cylinder is one step to the right of its initial position after three steps.

%3. What is the general formula for the probability that the cylinder is $k$ steps away from its initial position after $N$ steps?

%4. Simulate $10,000$ steps and plot a histogram of the final position relative to its initial position. Add dots to show the values predicted from the formula found in part 3.

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

What is the probability that the cab involved in the accident was Blue rather than Green?  Use the two approaches (equation- and diagram- based) employed in the example problem related to the breast cancer example covered in class.

Save your answer as `HW2_2.pdf`.

**590 Students**: Create a plot that answers the question: How does the answer depend on the witness's reliability (ability to correctly identify)? We will critique these plots with regard to how clearly they answer the question during class (I won't show the names of those who created the plot). Save your plot as `HW2_2.png`.

## Law of Large Numbers

The Law of Large Numbers tells us that as $n\rightarrow \infty$ the sample average defined by

$$\overline{X}\equiv\frac{1}{n}\sum_{i=1}^n X_i$$

will be near the population average $\mu$ with a given probability. Given $n$ samples from a population, we don't expect $\overline{X}$ to exactly match $\mu$. The Law of Large Numbers allows us to make a statement about the difference $\overline{X}-\mu$. Specifically, the statement involves the probability that $|\overline{X}-\mu|$ is smaller that a certain value.

To answer the following questions, you do not need to understand the Law of Large Numbers. However, if you are interested, more formal definitions and proofs are given in

* [Orloff and Bloom, Reading 6b](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading6b.pdf)
* [Bulmer, Chapter 6](https://drive.google.com/file/d/1IuANm_ZxtuY75c9Caguv3cdG8JbmkADi/view?usp=sharing★★★★★remove★★★★★)
* [DeGroot, Chapter 6](https://drive.google.com/file/d/1FtvQS1303P_GA4aM3ZbQIGPbThTXmfpq/view?usp=sharing★★★★★remove★★★★★)
* [Rozanov, p 69](https://drive.google.com/file/d/1ROIF0mLquDcoMGJtj5Oz93On_ATCcfmc/view?usp=drive_link★★★★★remove★★★★★)

### a

1. Draw $n=100$ values from a population of Gaussian-distributed numbers with mean $\mu=0$ and standard deviation $\sigma=1$.
2. Compute $\overline{X}$.
3. Repeat 1. and 2. $10,000$ times and plot a histogram of $\overline{X}$.

Save your program as `HW2_3a.py` and the associated plot as `HW2_3a.png`. When I execute your program, I should see a histogram with _**the average of**_ $\overline{X}$ displayed in the title and it should write the file `HW2_3a.png`.

### b

1. For $n=100$, what fraction of the $10,000$ $\overline{X}$s were in the range $[-0.01, 0.01]$?
2. How does the fraction depend on $n$? <sup>+</sup>
3. For $n=100$, what is the range $[-\epsilon,\epsilon]$ for which $99$% of the $10,000$ $\overline{X}$s fall in?
4. How does $\epsilon$ depend on $n$? <sup>+</sup>
5. How does your answer change if the distribution changes (that is, if you draw values from a distribution other than Gaussian)?

<sup>+</sup> You may explain this using one or more of words, tables, and plots.

Save your program as `HW2_3b.py`. Save your answers in a file named `HW2_3b.pdf`.

**590 students**: Be prepared to discuss in class how this experiement is related to the Weak Law of Large Numbers.

## Central Limit Theorem

The Central Limit Theorem says that for large $n$, $\overline{X}\equiv\frac{1}{n}\sum_{i=1}^n X_i$ is Gaussian-distributed with mean $\mu$ and standard deviation $\sigma/\sqrt{n}$.

Important: this theorem (usually) applies even if the distribution of the values used in computing 
$\overline{X}$ are not Gaussian--distributed.

With the Central Limit theorem, we can make statements such as "I took a sample of $n$ values and computed $\overline{X}$. If I took many samples and computed many $\overline{X}s$, 95\% of the time the range $[\overline{X}-1.96\sigma/\sqrt{n},\overline{X}+1.96\sigma/\sqrt{n}]$ would include ("trap") $\mu$.

In the previous problem, you computed a histogram of $10,000$ $\overline{X}$. Based on the Central Limit Theorem

1. This histogram should be approximately Gaussian;
2. The mean of $\overline{X}$ should be approximately $\mu$, which is the population standard deviation; and
3. This standard deviation of $\overline{X}$ should be approximately $\sigma/\sqrt{n}$, where $\sigma$ is the population standard deviation.
4. 95\% of the time the range $[\overline{X}-1.96\sigma/\sqrt{n},\overline{X}+1.96\sigma/\sqrt{n}]$ should include ("trap") $\mu$

Create one or two plots that demonstrate these points. Pay careful attention to your annotations. Save your code as `HW2_4.py` and plots as `HW2_4.png` (use subplots).

## Reading

Background reading on Discrete Probability Distributions: [Devore Chapter 3]((https://drive.google.com/file/d/1bN68ELL0DBrgVwbE0m74LPuTwoHqXw2M/view?usp=sharing★★★★★remove★★★★★)

Alternatives: [Bulmer Chapters 1 and 2](https://drive.google.com/file/d/1IuANm_ZxtuY75c9Caguv3cdG8JbmkADi/view?usp=sharing★★★★★remove★★★★★), [Bonamente Chapter 3](https://drive.google.com/file/d/1Z4uN1ReMXAUMZck_UmavM3lIGrbE1U-C/view?usp=sharing★★★★★remove★★★★★), [Rozanov Chapter 5](https://drive.google.com/file/d/1ROIF0mLquDcoMGJtj5Oz93On_ATCcfmc/view?usp=drive_link★★★★★remove★★★★★), [Larson Chapter 4](https://drive.google.com/file/d/1Cc65FWiptQLqtXiKHpB2JJDLe-dh7WtX/view?usp=drive_link★★★★★remove★★★★★) and [DeGroot Chapter 5.1-5.6](https://drive.google.com/file/d/1FtvQS1303P_GA4aM3ZbQIGPbThTXmfpq/view?usp=sharing★★★★★remove★★★★★).
