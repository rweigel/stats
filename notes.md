# Probability Definitions

* Probability
  > The term probability refers to the study of randomness and uncertainty. In any situation in which one of a number of possible outcomes may occur, the discipline of probability provides methods for quantifying the chances, or likeli- hoods, associated with the various outcomes. (Devore p 50)

  > Given an experiment and a sample space $\mathcal{S}$, the objective of probability is to assign to each event $A$ a number $P(A)$, called the probability of the event $A$, which will give a precise measure of the chance that $A$ will occur. (Devore p 55)


* Experiment

  > An experiment is any activity or process whose outcome is subject to uncertainty. ...
  >
  > Thus experiments that may be of interest include tossing a coin once or several times, selecting a card or cards from a deck, weighing a loaf of bread, ascertaining the commuting time from home to work on a particular morning, obtaining blood types from a group of individuals, or measuring the compressive strengths of different steel beams. (Devore p 51)

  > An experiment is any process, real or hypothetical, in which the possible outcomes can be identified ahead of time. (DeGroot p 5)

* Sample Space, $\mathcal{S}$ (or Event Space)

  > ... the set of all possible outcomes of an experiement. (Devore p 51)

  The outcomes in a sample space are noted using the shorthand
  
  $\mathcal S = ${outcome 1, outcome 2, ...}
  
  For example, if the experiment is tossing a coin twice and counting the number of heads and tails, the three simple events are ${1H1T, 2T, 2H}$, and the sample space is

  $\mathcal S = $ {$1H1T$, $2T$, $2H$}

  If the experiment is tossing a coin twice and writing down the result of the first toss in box 1 and the result of the second toss in box 2,

  $\mathcal S = $ {$HH$, $HT$, $TH$, $TT$}

  We can define a compound event: $A$ is the outcome of the experiment yielding one tail.

* Event

  > An event is any collection (subset) of outcomes contained in the sample space $\mathcal{S}$. An event is simple if it consists of exactly one outcome and compound if it consists of more than one outcome. (Devore p 52)

  > An event is just a set. (Devore p 53)

  > An event is a well-defined set of possible outcomes of the experiment. (DeGroot p 5)

  Can we also say a sample space is the set of all possible simple events?

* Compliment -- "Not $A$" is represented by four symbols: $A^\prime$ $\quad$ $\overline{A}$ $\quad$ ~$A$ $\quad$ $\neg A$

  > The complement of an event $A$, denoted by $A'$, is the set of all outcomes in $\mathcal{S}$ that are not contained in $A$. (Devore p 53)

* Difference (Rozanov p 14): $A-B$ means the event in which $A$ occurs but not $B$.

* Subset (Rozanov p 15): $A\subset B$ means the set $A$ is a subset of $B$.

* Union -- "Or" (union; inclusive or) is typically represented by $\cup$

  > The union of two events $A$ and $B$, denoted by $A \cup B$ "$A$ or $B$" is the event consisting of all outcomes that are _either in_ $A$ _or in_ $B$ _or in both events_ (so that the union includes outcomes for which both $A$ and $B$ occur as well as outcomes for which exactly one occurs) -- that is, all outcomes in at least one of the events. (Devore p 53)

* XOR -- "Exclusive or": $A \oplus B$ means the event that is in $A$ or $B$, but not both.

* Intersection - "And" (intersect) is represented by four symbols: $\cap$ $\quad$ & $\quad$ $\,$ $\quad$ $$

  > The intersection of two events $A$ and $B$, denoted by $A \cap B$ and read "$A$ and $B$," is the event consisting of all outcomes that are in _both_ $A$ _and_ $B$. (Devore p 53)

* Null Event

  > Let $\varnothing$ denote the null event (the event consisting of no outcomes whatsoever). When $A\cap B = \varnothing$, $A$ and $B$ are said to be mutually exclusive or disjoint events. (Devore p 54)

* Mutually Exclusive -- Defined in Null Event definition. Also referred to as "pairwise disjoint".

* Axioms of Probability (Devore p 56); Often referred to as Kolmogorov's Axioms

  1. For any event $A$, $P(A) \ge 0$.
  2. $P(\mathcal{S})=1$
  3. If $A_1$, $A_2$, ... is an infinite collection of disjoint events, then
     
     $$P(A_1 \cup A_2 ....) = P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i)$$

     Corallary

     $$P(A_1 \cup A_2 .... \cup A_k) = \sum_{i=1}^k P(A_i)$$

  Note that many textbooks give the third axiom in terms of a sum over two events instead of a sum over an infinite set of events.

> Axioms do not completely determine an assignment of probabilities to events. The axioms serve only to rule out assignments inconsisten with our intuitve notions of probability. (Devore p 57)

* Geometric Series

  $$a + ar + ar^2 + ... = \frac{a}{1-r}$$

  In an experiment where the event is either true (with probability $1-p$) or false (with probability $p$) and we run experiments until we get a false, the sample space of all experiments is
  $E_1=F$, $E_2=TF$, $E_3=TTF$, ... and by Axiom 3.
  
  $1 = P(E_1) + P(E_2) + P(E_3) + ....$
  
  and we will learn later why $P(E_1)=p$, $P(E_2)=(1-p)p$, $P(E_3)=(1-p)^2p$, ...
  
  This is a geometric series with $a=p$ and $r=1-p$ and thus
  
  $1 = P(E_1) + P(E_2) + P(E_3) + ....$

*  Relative Frequency and Interpretation of Proability

  > ... most frequently used an most easily understood is based on the notation of relative frequencies. (Devore p 57)

  Repeat experiment $n$ times (each repetition is called a "replication"). If event $A$ occurs $n(A)$ times in $n$ replications, then relative frequency is $n(A)/n$.
  
  > The _objective interpretation of probability_ identifies this limiting relative frequency to $P(A)$. (Devore p 57)

  Said another way,
  
  $$P(A) = \lim_{n\rightarrow \infty}\frac{n(A)}{n}$$

  If exeriment is not repeatable, prior information must be used to determine $P(A)$ and not everyone may conclude the same $P(A)$; in this case $P(A)$ has a subjective interpretation. See DeGroot 2012 for a discussion of interpretations of probability.

  Python example of Figure 2.2 Devore:
  
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
  print(f"  rf(0) = {results.count(0) / n}")
  print(f"  rf(1) = {results.count(1) / n}")
  ```


* Law of Compliments (Devore does not use this, however)

  > For any event $A$, $P(A)+P(A')=1$, from which $P(A)=1-P(A')$. (Devore p 59)

* Corallary to Axiom 3 (Devore only calls this a proposition) 

  > For any event $A$, $P(A)\le 1$. (Devore p 59)

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

  **Visual proof for two events**

  Imagine overlapping targets $A$ and $B$ and darts are thrown towards target.

  Viusally, the number of ways $A$ or $B$ occured: $n(A \cup B) = n(A) + n(B) - n(A \text{ and } B)$
  
  Divide by the total number of dots, $n$, use the relative frequency interpretation of probability, and use $\cap$ in place of "and":

  $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

  **Example**

  If you are in a firing line and two people have guns that shoot a real bullet instead of a blank with probability of 1/3, what is the probability that you get shot (assuming the marksmen never miss?)  D draw a tree diagram and a Venn diagram to explain the answer.

  *Answer*

  $P(A \text{ or } B) = 1/3 + 1/3 - 1/9 = 5/9$

  or, $P(\overline{A\text{ or } B}) = (2/3)(2/3) = 4/9$

  Check: $P(\overline{A\text{ or } B}) = 1 - P(A \text{ or } B)$

  **Example** (Devore Chapter 2, problem 12)
  
  Consider randomly selecting a student at a certain university, and let $A$ denote the event that the elected individual has a Visa credit card and $B$ be the analogous event for a MasterCard. Suppose that $P(A) = 0.5$, $P(B)=0.4$, and $P(A\cap B) = 0.25$.
  
  1. Compute the probability that the selected individual has at least one of the two types of card (i.e., the probability of the event $A\cup B$).
  2. What is the probability that the selected individual has neither type of card?
  3. Describe, in terms of $A$ and $B$, the event that the selected student has a Visa card but not a MasterCard, and then compute the probability of this event.
  
  _Answers_:
  1. $P(A\cup B)=P(A)+P(B)-P(A\cap B) = 0.5+0.4-0.25=0.65$
  2. $P(A'\cap B') = 1-P(A\cup B) = 0.35$ (Based on visual derivation)
  3. $P(A \cup B') = P(A) - P(A\cap B) = 0.5-0.25=0.25$ (Based on visual derivation)

* Product Rule (or Law of Multiplication) (Devore does not name but gives as proposition on p 65)

  > If the first element or object of an ordered pair can be selected in $n_1$ ways, and for each of these $n_1$ ways the second element of the pair can be selected in $n_2$ ways, then the number of pairs is $n_1n_2$. (Devore p 65)

* Tree Diagram -- Use for visually justifying product rule and counting permutations (Devore p 66)

* Tuple -- A "$k$--tuple" is an ordered collection of $k$ objects. (Devore p 66)

* General Product Rule (or Product Rule for $k$-Tuples)

  > Suppose a set consists of ordered collections of $k$ elements ($k$-tuples) and that there are $n_1$ possible choices for the first element; for each choice of the first element, there are $n_2$ possible choices of the second element; ...; for each possible choice of the first $k-1$ elements, there are $n_k$ choices of the $k$th element. Then there are $n_1n_2...n_k$ possible $k$-tuples. (Devore p 66).

  Note that "elements" is used here, but in definition of tuple, objects is used.

* Permutation -- An ordered arrangement of distinct objects, where each arrangement has no duplicate objects. Usually relevant in problems that involve "without replacement".

  Suppose you have $n$ distinct objects and you want to put them in boxes labeled $1$, $2$, ..., $k$. You select one object and put it in the first box. You select a second object from the remaining $n-1$ objects and put it in box $2$, ....
  
  The number of ways to do this is denoted $P_{k,n}$ (or $_nP_k$) and is
  
  $$P_{k,n}=\frac{n!}{(n-k)!} = n\cdot (n-1) ... \cdot (n-k)=\frac{n\cdot (n-1) \cdot (n-2) ... \cdot (n-k) \cdot (n-k-1) ... 1}{\phantom{n\cdot (n-1) \cdot (n-2) ... \cdot}(n-k)\cdot(n-k-1) ... 1}$$

  Do see this, consider
  
  $$6\cdot 5\cdot 4=\frac{6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}{\phantom{6\cdot 5\cdot 4\cdot}3\cdot 2\cdot 1}$$

* Combination (un-ordered subset) -- The number of unique $k$--tuples if $k$--tuples with the same elements (but in a different order) are treated as the same. In the team picking example, there are $3$ team combinations. 

  Each permutation can be regarded as group of $k$. If we regard a group as equivalent if they have the same elements, then there are fewer groups than permuations. For example, if the two permutations

  $(1,2)$

  $(2,1)$

  are regarded as equivalent, then there is only one group containing the numbers $1$ and $2$. To determine the number of possible orderings of each permutation, ask how many ways a set of $k$ elements can be arranged. The answer is $k!$.

  So, to find the number of combinations, divide the number of permutations by $k!$.

  $$C_{n,k}=\frac{P_{n,k}}{k!}=\frac{\ds\frac{n!}{(n-k)!}}{k!}=\frac{n!}{k!(n-k)!}$$

  $C_{n,k}$ is often called a binomial coefficient and the denoted by $\ds{N\choose k}$ and referred to as "$n$ choose $k$".

# Set operations in Python

See [Python notes](python.html#sets)

# Counting

Three types of problems:

1. Product Rule:

   A. Given $k$ ordered boxes and $n_1$ choices for first box, $n_2$ for the second, ...

   B. Given $k$ ordered boxes and $n$ choices for first box, $n$ for second, ...

2. Permutations: Given **one** set of length $n$, how many distinct _ordered_ sets with no duplicates of $k$ elements can be created? (e.g., set = {a, b}, permutations are {a, b}, {b, a}. Similar to a product rule B. problem where $n_1=n$, $n_2=n-1$, ....

3. Combinations: Same as 2. except counting all sets with the same elements as equivalent. (e.g., if set = {a, b} only one combination is possible: {a, b}).

## Product rule examples

One can use a tree diagram, table, or $x$--$y$ plot to prove.

If there are $n_1$ ways of doing operation $1$ and  $n_2$ ways of doing operation 2, then both operations can be performed in $n_1n_2$ ways.  

**Example**

Take two steps, each step is North, South, East or West. 

Put one of N, S, E, W in first box and same for second box. Result is $16$ unique step pairs.

Tree diagram.

Equivalent problem: Sample with replacement from set {N, S, E, W}. 

**Example**:

If operation 1 is moving north, south, east, or west and operation 2 is moving up or down, then there are 8 possible operations of length $2$.

**Example**:

Two teams of twelve players each. How many unique handshakes between members of opposing teams?

*Answer*: $n_a=12$, $n_b=12$, $N=12\cdot 12=144$.

Demonstrate method computing using loops in Python.

Tree diagram

**Example**: Roll a die five times. How many $5$-tuples? Create a five boxes. There are six possible "choices" for first box, six possible choices for second box, ..... So there are $6^5$ possible $k$--tuples.

**Example**: Flip a coin 2 times. There number of $2$--tuples is $2\cdot 2$. (Think of two boxes and you put either a $H$ or $T$ in the first box and a $H$ or $T$ in the secon box.)
  
**Example**: Given three circles of different diameter and four squares of different side length, put a circle in the first box and a square in the second. The number of $2$--tuples is $3\cdot 4$.

**Example**: Each clinic has two $O$ doctors and three $P$ doctors and you must select two doctors from the same clinic. How many possible pairs of $O$s and $P$s are there?
  
In the first box, put one of the four $O$s. For each $O$, there are $3$ $P$s to choose from and put in the second box. So $n=4\cdot 3$.
  
If each clinic also has three $I$s and two $G$s, how many possible choices for four doctors?
  
In the third box, put one of the three $I$s; in the fourth box, put one of the three $G$s. Then $n=4\cdot 3\cdot 3\cdot 2$.

**Example**: Suppose you want to pick a team of two tennis players from $3$ players, $A$, $B$, and $C$. The number of ways you can pick the team is $3\cdot 2$: $AB$, $AC$, $BA$, $BC$, $CA$, and $CB$.

This is not the list possible teams because $AB$ is the same as $BA$ (That is, order is not important.). The list of possible teams is $3$, by inspection.

## Permutation examples

**Example**

Step {N, S, E, W}. Then take another step, but not in the same direction as first.

*Answer*: $4\cdot 3 = 12$

**Example**:

You have stickers labled $1$, ..., $6$ that are used to form a license plate.

How many unique license plates of length $6$ can you form? *Answer*: $6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1$

How many unique license plates of length $2$ can you form? *Answer*: $6\cdot 5 = 30$

**Example**

A four-volume work is placed in random order on a bookshelf. What is the probability of the volumes being in proper order (1, 2, 3, 4)?

_Answer_: $1/4!$

*Example*

A subway train made up of $n$ cars is boarded by $r$ passengers ($r\le n$), each entering a car completely at random. 

1. What is the number of ways the passengers can board?
2. What is the probability of the passengers all ending up in different cars?

_Answer_:

1. Consider list of $r$ passengers and each can be assigned number $1, ...n$: $n^r$ 
2. Have $n$ choices for first passenger, $n-1$, for second, ... $n-r-1$ for the last: $\ds\frac{n(n-1)...(n-r-1)}{n^r}$

## Combination examples

**Example**

Select two players from a list of three.

1. Assign one as captain. How many unique teams?
2. If there is no assignment of a captain, how many unique teams?

**Example**:
* How many unique ordered hands of size $5$ can be formed using a $52$-card deck?

   *Answer*: This is a permutation problem: $52\cdot 51\cdot 50\cdot 49\cdot 48$ permutations.
* How many hands of size $5$ can be formed using a $52$-card deck?

   *Answer*: Each permutation can be rearranged in $5!$ ways. So the number of hands (combinations) is $52\cdot 51\cdot 50\cdot 49\cdot 48/(5\cdot 4\cdot 3\cdot 2\cdot 1)$

