# HW 1

Due Thursday, September 3rd at 11:59 pm.

1. Save your answers in a GitHub repository named `stats`. Under `Setting` in the GitHub repository, set me (`rweigel`) as a collaborator.
2. Save your answers in the following format:
   1. Save code as `HW1_X.ext`, where `X` is the problem number and `ext` is the extension (e.g., `py` or `m`).
   2. Save scanned hand-written answers as `HW1_X.pdf`. Use a scanner app to create the document (don't take a photo and convert it to PDF).
   3. Save plots as `HW1_X.png`. If there are multiple plots for a problem, save them as `HW1_Xa.png`, `HW1_Xb.png`
3. Guess the relative frequency that instructions 1. and 2. above are followed precisely.

If you have difficulty with any of the above, we can discuss it at the end of class.

## Objective Interpretation of Probability

The _objective interpretation of probability_ is that the the probability of event $A$ is the limit of the relative frequency of $A$, $R_f=n(A)/n$, as the number of experiments, $n$, used to compute the relative frequency approaches $\infty$:

$$P(A) = \lim_{n\rightarrow \infty}\frac{n(A)}{n}$$

The following program computes the relative frequency of heads for an experiment of $n$ tosses where a zero or 1 is randomly selected with equal probability. Each experiment corresponds to a list of $n$ heads or tails.

1\.

Save your code as `HW1_1.py`. Save your plot as `HW1_1.png`.

Modify this program so that it computes the relative frequency for trials of size $n=1, 2, ..., 1000$ and plot $R_f$ vs $n$. See also Figure 2.2 of [Devore](https://drive.google.com/file/d/1MB1aYqKonKjNiSYy1vNWMqm6MZqRuMe6/view?usp=drive_link★★★★remove★★★★).

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

2\. For a trial of size $n=3$, how many possible outcomes are there? That is, how many elements are in the sample space? (You do not need to list them.) Put your answer in a comment in in `HW1_1.py`.

3\. (590 only)

Modify this program so a loop is not required by using a NumPy function. Save your answer in `HW1_1.py`.

4\.

In class, I will raise the following questions (you don't need to turn anything in):

* How would you characterize the decreasing variation around $0.5$ as a function of $n$? What calculation would you do and what plot would you make?

* Suppose that you wanted to know the probability of getting three heads in $n=3$ tosses _and_ you don't know the formula for computing this. How you you use a computer program to _estimate_ this probability?

<details>
<summary>Answer</summary>
See [solns/HW1_1.py](https://github.com/rweigel/stats/tree/main/solns). Problem is solved with and without using NumPy.

<img src="solns/HW1_1.png" width="500px"/>

There is another way to answer this question. You can perform independent experiments of size $n=1, 2, ...$ and report the relative frequency for each independent experiment. The result is shown in the following plot.

<img src="solns/HW1_1_alt.png" width="500px"/>

</details>

## Random Walk Simulation

A random walk is a process analogous to flipping a fair coin. An example in physics is a cylinder constrained to move in one dimension being struck by air particles (and the cylinder moves without friction). Each strike sends the cylinder a small step to the left or right. The probability of a step to the left is the same as that of a step to the right. See also [Chapter 1 of Kittel and Kroemer](http://www.fulviofrisone.com/attachments/article/413/Kittel%20-%20Thermodynamics.pdf) for a description in the context of statistical physics.

Suppose we want to know the probability that after three strikes, the cylinder is one step the right of its initial position using a simulation (we will cover an exact answer later).

We could do an experiment where we randomly select values of $-1$ or $1$ with equal probability using `random.choice([-1, 1])` three times (`np.random.choice()` can also be used for efficiency). A result could be `[1, 1, -1]`. The final position after these steps is `sum([1, 1, -1]) = 1`. To compute the probability that the final position is $1$, we can repeat this experiment many times and count the number of times the final position is $1$.

1. How many possible step configurations are possible? That is, what is the sample space of the experiment of taking three steps to right or left, with equal probability for each direction?
2. Write a program for a simulation that gives an estimate the probability that the cylinder is one step to the right of its initial position after three steps.

Save your code in a file named `HW1_2.py`.

<details>
<summary>Answer</summary>
1. $2^3=8$.

2. See [HW1_2.py](https://github.com/rweigel/stats/tree/main/solns), which has the following output.

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
</details>

## Sample Space

1. An experiment involves tossing a coin 3x. What is the sample space of this experiment?
2. How many of the outcomes in the sample space had two heads? 
3. Define event $A$ to be that the experiment yields two heads. Define event $B$ as the experiment yielding two tails. What is $A \cup B$ and $A \cap B$?

Save your answer in a file named `HW1_3.pdf`.

<details>
<summary>Answer</summary>

1. The sample space has 8 elements ($2^3$). This list can be found using a tree diagram as shown below.

    ```
            H       HHH
        H -
            T       HHT
    H -        
            H       HTH
        T -
            T       HTT

            H       THH
        H -
            T       THT
    T -        
            H       TTH
        T - 
            T       TTT

    ```
2. $3$ by inspection of the table above. Also, suppose that we have three unique coins $T$, $H_1$, and $H_2$. There are $3!$ unique permutations. If we drop the subscripts, then the number of unique permutations is divided by 2. So $3!/2=3$.

3. By inspection of the list from 1., $A \cup B = 6$ and  $A \cap B = \emptyset$.

In the above, I assumed "experiement yields two heads" to mean "the experiment yielded exactly two heads" and not "the experiement yielded two or more heads".
</details>

## Law of Addition and Set Notation

Suppose 55\% of people exercise and 45\% drink alcohol. Also, 70\% do at least one of these.

What is the probability that a randomly selected person:
1. exercises and drinks alcohol?
2. does not do at least one of the two activities?

Use a Venn diagram (or any visual method) in the way that was used in class to demonstrate your answers.

Save your answer in a file named `HW1_4.pdf`.

<details>
<summary>Answer</summary>

Given: $P(E) = 0.55$, $P(A) = 0.45$, and $P(E\cup A) = 0.7$

1. $P(E \cap A) = P(E) + P(A) - P(E \cup A) = 0.3$
2. $P\big( (E \cup A)' \big) = 1 - P(E \cup A) = 1 - 0.7 = 0.3$
</details>

# Quiz 1

Study the cab example in the [Bayes' rule section of the notes](notes.html).

At the start of the Sept. 3rd class, I will ask you to solve a similar problem without notes. This will be the first quiz. This quiz will not be graded. If you attend class, you'll get full credit.

Problem given:

* 2\% of the population has cancer
* A screening test for cancer is correct 80\% of the time.
* Your screening test claimed cancer.

What is the probability that you actually have cancer?

<details>
<summary>Answer</summary>

$$\frac{16}{196+16} = \frac{0.02\cdot 0.8}{0.02\cdot 0.8 + 0.98\cdot 0.2}\simeq 7.5{\%}$$

where the first fraction is determined using Method II in the cab problem and the second using Method III.
</details>

# HW 2

Due Thursday, September 10th at 11:59 pm.

## Bayes' Rule

2\% of the population has cancer. A screening test claims cancer in people with cancer 80\% of the time and it claims cancer in people without cancer 9.6\% of the time.

You take a test and it claims cancer.

1. What is actual probability that you have cancer?
2. Why is this answer different from the quiz answer?

Save your answer as `HW2_1.pdf` and upload it to your GitHub account.

## Counting Problems

Find a problem in a textbook involving permutations and/or combinations (cite your source unless you made up the problem) and provide a solution. Be prepared to explain the problem and its solution in class.

Try to find a problem that is challenging and find a way to explain your solution in multiple ways (e.g., table, tree diagram, code, etc.).

If the problem is complex and difficult to explain, make up a similar but simpler problem first so that the full problem's solution is easier to understand.

Save your answer as `HW2_2.pdf` and upload it to GitHub. I'll randomly select students to explain their answer at the whiteboard during class.

## Expectation Values

The binomial probability mass function is 

$$P(X=x)={n \choose x}p^x(1-p)^{n-x}$$

(sometimes the simpler but equivalent notation $P(x)$ is used).

The expectation value of $h(X)$ is

$$E[h(X)] = \sum_{\text{all vals of }X} h(x) p(x)$$

1. By hand, compute $E[X]$ when $n=3$ and $p=1/2$. That is, compute $E[h(X)]$ when $h(X)=X$.

2. (590 only) Prove that $E[X]=np$.

   Hint: Rewrite so that you can use the fact that
   
   $$(p+q)^n = \sum_{x=0}^n{n\choose x} p^x q^{n-x} = 1$$
   
   because $p+q=1$.

%$E[X] = \sum_{x=0}^3 x P(x) = \sum_{x=0}^3 x {n\choose x} p^{1/2}q^{1/2}$

%$E[X] = 0\cdot \frac{3!}{0!3!}(\frac{1}{2})^3 + 1\cdot\frac{3!}{1!2!}(\frac{1}{2})^3 + 2\cdot\frac{3!}{2!1!}(\frac{1}{2})^3 + 3\cdot\frac{3!}{3!0!}(\frac{1}{2})^3$

%$E[X] = 0 + 3(\frac{1}{2})^3 + 2\cdot 3(\frac{1}{2})^3 + 3\cdot 1(\frac{1}{2})^3$

%$E[X] = 0 + 3(\frac{1}{2})^3 + 6(\frac{1}{2})^3 + 3(\frac{1}{2})^3$

%$E[X] = 0 + 3/8 + 6/8 + 3/8 = 12/8 = 1.5$

Save your answer as `HW2_3.pdf` and upload to GitHub.

## Binomial Distribution

In [Devore 3.4](https://drive.google.com/file/d/11Ggp-RNoknu7ARu95s54hvOsQMv0AgR-/view?usp=sharing★★★★★remove★★★★★), an experiment that conforms to the Bernoulli trials constraints is referred to as a "Binomial Experiment."

A Bernoulli trial has 

* two possible outcomes;
* the probability of "success" is $p$ and the probability of "failure" is $1-p$;
* these probabilities don't change

For $n$ trials, the probability of $x$ successes is given by the Binomial distribution:

$$P(x)={n \choose x}p^x(1-p)^{n-x}$$

1. Use a random number generator to simulate 10,000 Binomial experiments with $n=100$ and $p=0.4$ and plot $P(x)$. That is, execute 10,000 experiments in which the experiment is selecting 100 values from the list `[0, 1]` with the probability of selecting a $1$ being $p$. On the same axes, plot $P(x)$ expected from the equation above using the given $n$ and $p$. 

2. In the next class, I'll show that as $n\rightarrow \infty$, and for $x \ll np$,

   $$P(x)\rightarrow \frac{1}{\sqrt{2\pi n p q}} e^{-(x-np)^2/2npq}$$

    where $q \equiv 1-p$ (the symbol $\equiv$ means "is defined to be").

    Plot this $P(x)$ on the same axes as $P(x)$ in part 1.

Save your code as `HW2_4.py` and the plot as `HW2_4.png`.

4. Discussion questions for class (you do not need to turn anything in for this).
   * What is an interpretation of the meaning of the constraint $x \ll np$?
   * You are given a list of $10,000$ `0`s and `1`s and a claim that the values were generated by Bernoulli trials. How would you test this claim?

**Partial Answer**

<img src="solns/HW2_4.svg">

# Quiz 2

The quiz on Sept 10th will be on of the problems on counting that I covered in class (recall that there were three types: product rule, permutations, and combinations). The quiz will is closed book, closed notes, and closed computer and will be graded.
