# Basic Concepts in Probability

## Probability Interpretation

In the following, minimal definitions of the three dominant types of probability are given. Although it is useful to know these definitions, in practice, they are not critical for making interpretations and conclusions.

Most of the work in this course will involve the estimation of uncertainty and making conclusions using both Frequentist and Bayesian methods.

For an extended discussion see [DeGroot and Schervish, Chapter 1.2].

### Classical 

Given

1. an experiment with a finite number of mutually exclusive outcomes; and
2. each outcome is _equiprobable_, i.e., "equally likely because of the nature of the experiment." 

[Bulmer, p 1]

> Let $A$ denote some event associated with the possible outcomes of the experiement. Then the probability $P(A)$ of the event $A$ is defined as the fraction of the outcomes in which $A$ occurs. More exactly,

$$P(A)=\frac{N(A)}{N}$$

Examples:

1. Tossing "fair" coin coin
2. Rolling a "fair" die

In general, computing $N(A)$ is not trivial. This is discussed more in [Counting](#counting). (In addition to being difficult, humans show a bias when guessing probabilities without the aid of calculation -- this means physical intuition often fails [10.5709/acp-0163-9].)

In the above definition, only equiprobable events were allowed. It is natural to ask if the questions above could be answered if the events were not equiprobable. This is covered later and requires a different definition of probability.

----
**Example - Tossing a Fair Coin** [Bulmer, p2]

Experiment: toss a fair coin once. There are $N=2$ mutually exclusive outcomes that are equiprobable. If event $A$ is the event of heads, $N(A) = 1$ so that $P(A)=0.5$.

**Example - Tossing a Fair Coin 2x**

Experiment: toss a fair coin 2x. What is the probability of the event of getting one head and one tail?

There are two possible outcomes of the experiment that lead to the event $A$ (one head and one tail). There are four possible mutually exclusive outcomes of the experiment (HH, HT, TH, and TT) and these outcomes are equiprobable. The probability of the event is thus $0.5$. To justify the statement that in general computing $N(A)$ is not trivial, consider the question of the probability of the event of one head in three tosses.

**Example - Throwing a die** [Bulmer, p2]

----

### Frequentist

In the absence of an ideal experiment, we need an operational definition of probability.

Frequency ratio [James, p10] or relative frequency [Bulmer, p2; Wilks, p10] is 

For $N$ experiments where event $A$ occurs $n(A)$ times

$$\text{Frequency ratio of }A\equiv F_r(A)= \frac{n(A)}{N}$$

If the experiments were identical and independent 

$$\text{Frequentist probability of }A \equiv P(A) = \lim_{N \to \infty}\frac{n(A)}{N}$$

[James, p10; Bulmer, p 3]. That is, the frequentist probability $P(A)$ is the fraction of experiments for which $A$ occurred in a large series of trials.

Quite often we use frequency ratio and probability interchangeably. For example, we may say "the probability of rain on a given day in Los Angeles is 0.01". Technically, we should say "the frequency ratio of rain on a given day in Los Angeles is 0.01" unless we consider the number of measurements used to compute the frequency ratio as approaching infinity or we are living in a simulation in which rain occurs in Los Angeles with the probability of rain set at 0.1.

The _weak law of large numbers_ [Bulmer, p70] applied to the frequency ratio: given arbitrarily small $\delta > 0$ and $\epsilon > 0$, there is an integer $N$ for which the frequency ratio will be in a small window centered on $P(A)$ with a probability near 1, that is,

$$P(A)-\epsilon\le \frac{n(A)}{N} \le P(A) + \epsilon$$

with a probability greater than $1-\delta$.

It follows from _The Strong Law of Large Numbers_ that $\lim_{N \to \infty}{n(A)}/{N}$ exists and is equal to $P(A)$ with probability of 1 [Bulmer, p 70].

----
**Problems**

**Coin toss**

```
N     n(H)    Freq. Ratio
```

**Weak Law of Large Numbers applied to $F_r$**

1. Flip a coin $N=1,000$ times and print $n(H)/N$. This is an experiment.
2. Repeat 1. $N_e=10,000$ times. Print the fraction of experiments for which $0.499\le n(H)/N \le 0.501$.
3. What does $N$ need to be so that at least 98% of the experiments had $0.499\le n(H)/N \le 0.501$.
4. Discuss your results from 3. in the context of the Weak Law of Large Numbers.

If each toss is considered an experiment, and the probability of a heads does not change from toss to toss, we could estimate the frequentist probability by increasing the number of tosses. The law of large numbers tells us that as we increase $n$, the frequency ratio will approach 0.5. We can verify this claim with an experiment.

----


### Bayesian (or Subjective)

Bayesian probability is a "degree of belief".

[Wilks, p 10]

> Probability represents the degree of belief, or quantified judgement, of a particular individual about the occurrence of an uncertain event.

[James, p11]

> In order to define a probability that can be applied to non-repeatable experiments, we must abandon the concept of frequency and replace it by something else. Among the various possibilities, the most important is certainly the _degree of belief_ which is the basis of _Bayesian probability_."

### Frequentist vs. Bayesian comparison


There are many [interpretations of the meaning of probability](https://plato.stanford.edu/entries/probability-interpret/), the two most common in the scientific literature are Frequentist and Bayesian. The two dominant approaches to estimating uncertainties are also Frequentist and Bayesian.

Quite often, people choose a “side” -- to me, this is a signal of inexperience or a signal that someone enjoys starting a never-ending debate. My perspective is that there is not one ideal definition of probability or approach for all problems. If both approaches are applicable and the assumptions reasonable, the conclusions derived from them should be the same. If both approaches use the same assumptions and answer the same question, they should give identical answers.

\[Liu and Wasserman, 2014, Ch 12.1\]

> Remark. There are, in fact, many flavors of Bayesian inference. Subjective Bayesians interpret probability strictly as personal degrees of belief. Objective Bayesians try to find prior distributions that formally express ignorance with the hope that the resulting posterior is, in some sense, objective. Empirical Bayesians estimate the prior distribution from the data. Frequentist Bayesians are those who use Bayesian methods only when the resulting posterior has good frequency behavior. Thus, the distinction between Bayesian and frequentist inference can be somewhat murky. This has led to much confusion in statistics, machine learning and science.

\[Orloff and Bloom, ???\]

> While professional divisions remain, the consensus forming among top statisticians is that the most effective approaches to complex problems often draw on the best insights from both schools working in concert.

I think the debate does damage to the credibility of statistical analysis. The majority of articles that I have found that compare the Frequentist and Bayesian approaches emphasize problems where one approach gives the wrong answer. However, the wrong answer is often obtained because of an error.

The approach that I take to statistical analysis is to take two approaches. Quite commonly, I’ll use a traditional parametric statistics approach and a bootstrap approach. In the parametric statistics approach, one must make an assumption about the population. The bootstrap does not require this assumption. If my conclusion depends on the approach taken, I have more work to do.

The approach that you will need to use depends on the audience. If the readers expect uncertainties to be framed by Bayesian analysis and discussed using Bayesian terminology, I will present that (and use frequentist analysis if applicable to check my answers). And vice-versa.

A quarter is tossed 20 times. Heads were observed 9 times. 

1. Estimate the probability of heads, $P$ for this coin.
2. What is the error bar for $P(H)$?
3. Is the coin "fair" ($P(H)=0.5$)?

---
Note the ambiguity in questions 2. and 3. in comparison to 1. 

I'll answer these questions without the use of theoretical distributions.

**Frequentist**

1. The frequency ratio is $9/20=0.45$. A frequentist may conclude that "the maximum likelihood estimate of the probability of heads is 0.45". Maximum likelihood estimates will be covered later in this course. Implicit in this statement is that a certain approach and certain set of assumptions are needed. You've seen this before. When you compute error bars on the average of a set of measurements, you typically assume that the data were drawn from a population with a certain distribution.
2. We could simulate 10,000 experiments of the tossing of a coin with $P(H)=0.45$ 20 times. The standard deviation of the 10,000 frequency ratios could be used as the error bar.
3. We could simulate 10,000 experiments of tossing a coin with $P(H)=0.5$ 20 times. If 99% of the experiments had a frequency ratio between 0.45 and 0.55, we may conclude "it is likely the coin is fair". To quantify how unlikely, we could say $0.45 \le F \le 0.55$ occurs in less than 1% of the experiments. Note that we don't provide an answer to the question of "what is the probability that the coin is fair". We only say "if the coin is fair, the experimental results very unlikely".

**Bayesian**

1. Simulate the flip of a coin with $P(H)=0.45$. The peak of the histogram will occur at 0.45. This is the most probable $P$.
2. Same as frequentist.
3. The probability that the coin is fair is given by the height of the histogram from the simulation in 1. 

In principle, the frequentist approach could use these assumptions. But to do so would require the use of Bayes' rule.

Further reading:

1. https://stats.stackexchange.com/questions/230415/is-there-any-mathematical-basis-for-the-bayesian-vs-frequentist-debate
2. https://www.statisticshowto.com/axiomatic-probability/

## Definitions, Axioms, and Laws

### Definitions

-   **Event**  - A set, or class, or group of possible uncertain outcomes. A compound event can be decomposed into two or more subevents. What is defined by an event depends on the context.
- **Elementary Event** - 
-   **Sample Space or Event Space**  - the set of all possible elementary events. Sample spaces are often visualized using Venn diagrams.
-   **Independence**  - Note that statistical dependence does not necessarily imply physical cause-and-effect relationship. You should be able to give many example of this on cue.
- **Exclusive** - 
- **Exhaustive** -
- **Mutually Exclusive**
- **Nusance Parameters** [Wall, p25]
- **Marginalization** [Wall, p25]
- **Marginal Probabilities**
-   **Venn diagram**

### Axioms

Both Frequentist and Bayesian Probability follow from the following probability axioms [Wilks, p 9]. The axioms presented by [James, p10] are

> We define $\Omega$ to be the set of all possible _elementary events_ $X_i$ which are _exclusive_; that is, the occurrence of one of them implies that none of the others occurs. Then we define the probability of the occurrence of $X_i$, $P(X_i)$, to obey the Kolmogorov axioms:
> 1. $P(X_i)\ge 0$ for all $i$
> 2. $P(X_i\text { or }X_j)=P(X_i) + P(X_j)$
> 3. $\sum_{\Omega}P(X_i) = 1$

Axiom #2 means that if two events are mutually exclusive, then the probability of one or the other of occurring is the sum of the probabilities of each occurring. As an example, consider a coin toss (event) that must yield a head or tails. If the probability of heads is 0.5 and the probability of tails is 0.5, the probability of either a heads or tails is 1.0. Sometimes you will see axiom 2 written with the union and intersect set symbols: $P(X_i \cup X_j)=P(X_i) +P(X_j)\text{ if } X_i \cap X_j$

### Laws

#### Law of Multiplication

If two events $A$ and $B$ are independent

$$P(A\text{ and }B)=P(A)P(B)$$

If two events $A$ and $B$ are dependent

$$P(A\text{ and }B)=P(A)P(B|A)$$

$$P(A\text{ and }B\text{ and }C)=P(A\text{ and }(B\text{ and }C))=P(A)P(B\text{ and }C|A)$$

Limits

If $B$ always occurs, then $P(A\text{ and }B)=P(A)$. If $B$ never occurs, then $P(A\text{ and }B)=0$. If $A$ and $B$ never occur together, then $P(A\text{ and }B)=0$.

Informal derivation

(The actual derivation from Kolmogorov's axioms is not trivial [Wall, p24].)

Give each $n_A$ students a coin labeled $A$ at random. Next, give $n_B$ students a  coin labeled $B$ at random. How many students are expected to have two coins? How many are expected to have no coins?

After handing out the coins, select all students with $A$ coins. The fraction that will have a $B$ coin is (approximately) $n_B/N$. So

$$n(A\text{ and }B) = n(A)\frac{n(A)}{N}$$

The fraction that are expected to have both and $A$ and $B$ coin is found by division of both sides by $N$

$$\frac{n(A\text{ and }B)}{N}=\frac{n(A)}{N}\frac{n(B)}{N}$$

If the frequency ratios in this equation are treated as probabilities, then

$$P(A\text{ and }B)=P(A)P(B)$$

Use

What is the probability of each possible outcomes of two flips of a fair coin?


#### Law of Addition

If $A$ and $B$ are mutually exclusive

$$P(A\text{ or }B) = P(A) + P(B)$$

If $A$ and $B$ are not mutually exclusive 

$$P(A\text{ or }B) = P(A) + P(B) - P(A\text{ and }B)$$

Informal derivation

[[Image:Image2.png|left|thumb|Image of two targets]]

$$n(A\text{ or }B) = n(A) + n(B)$$

If $A$ and $B$ can co-occur, then

$$n(A\text{ or }B) = n(A) + n(B) - n(A \text{ and } B)$$

Note that the two dots in the overlapping segment were double counted; the last term removes the extra count.

Example Use

Two marksmen have guns that shoot a real bullet instead of a blank with probability of 1/3, what is the probability that you get shot, assuming the marksmen never miss Draw a tree diagram and a Venn diagram to explain the answer.

Answer

$$P(A\text{ or }B) = 1/3+1/3-1/9=5/9$$

or,

$$P( \sim(A\text{ or }B) ) = (2/3)(2/3) = 4/9$$

check:

$$P( \sim(A\text{ or }B) ) = 1 - P(A\text{ or }B)$$

### Conditional Probability

### Law of Total Probability

[Weiss, p196]

Also referred to as the stratified sampling theorem.

> If events $A_j$ are mutually exclusive and exhaustive, that is, exactly one of the events must occur. Then for any event $B$,
>
>$$P(B) = \sum_{j=1}^kP(A_j)P(B|A_j)$$

### Bayes' theorem

You only need the law of multiplication to derive Bayes' theorem. The law of multiplication is

$$P(A\text{ and }B)=P(A)P(B|A)$$

The labels $A$ and $B$ are arbitrary. Swapping them gives:

$$P(B\text{ and }A)=P(B)P(A|B)$$

$P(B\text{ and }A)$ means the same thing as $P(A\text{ and }B)$ (technically, the set intersection $A\text{ and }B$ is commutative). Equating the above two equations gives

$$P(B)P(A|B)=P(A)P(B|A)$$

The more common form for Bayes' theorem is

$$P(A|B)=P(B|A)\frac{P(A)}{P(B)}$$

In this form,

- $P(A|B)$ is called the posterior
- $P(B|A)$ is called the likelihood (poor choice of name)
- $P(A)$ is called the prior. If $B$ and $A$ are independent, then $P(A|B)=P(A)$, so $P(A)$ is the probability **prior** to knowing any relationship between $A$ and $B$.
- $P(B)$ is called a normalizing factor [Wall, p26] or, when $B$ is evidence and $A$ is a hypothesis, then $P(B)$ is also referred to the evidence []. 

Another form of Bayes' theorem, valid when the events $A_j$ are mutually exclusive and exhaustive, has the denominator re-written using the law of total probability.

$$P(A|B)=\frac{P(A)P(B|A)}{\sum_{j=1}^kP(A_j)P(B|A_j)}$$


Visual Derivation

Question: What is n(A '''or''' B) in Image 1?  That is, how many dots have labels of A or B? (Give a number)

{| class="wikitable collapsible collapsed"
! align="left" | Answer
|-
|
All of them = n(A) + n(B) = 11 
|}

'''Question:''' What is n(A '''and''' B) in Image 1?  That is, how many dots have labels of both A and B?  (Give a number)

{| class="wikitable collapsible collapsed"
! align="left" | Answer
|-
|
zero
|}
|}

{| border="0" cellpadding="2" width="100%" align="left"
|-
|style="vertical-align:top" |
[[Image:Image2.png|left|thumb|Image 2]]
|style="vertical-align:top"|

'''Question:''' What is n(A '''and''' B) in Image 2?  That is, how many dots have labels of both A and B?  (Give a number)

{| class="wikitable collapsible collapsed"
! align="left" | Answer
|-
|
two
|}

'''Question:''' What is n(B '''and''' A) in Image 2?  That is, how many dots have labels of both B and A?  (Give a number)

{| class="wikitable collapsible collapsed"
! align="left" | Answer
|-
|
two
|}

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

== Bayes' Theorem Typical Question ==

{| border="0" cellpadding="2" width="100%" align="left"
|-
|style="vertical-align:top" width="50%" |
'''Question:''' 1% of women at age forty who participate in routine screening have breast cancer. 80% of women with breast cancer will get positive mammographies. 9.6% of women without breast cancer will also get positive mammographies. A woman in this age group had a positive mammography in a routine screening. What is the probability that she actually has breast cancer?

Do this primarily using equations and primarily using a diagram.

{| class="wikitable collapsible collapsed"
! align="left" | Answer I
|-
|
* P(N) = 0.99 (probability of No cancer)                                                
* P(C) = 0.01 (probability of Cancer)                                                   
* P(+M|C) = 0.8 (probability of +Mamography given cancer)                               
* P(C|+M) = ? (probability of cancer given +Mamography)                                 
                                                                                      
We can't apply Bayes' rule                                                            
:<math>P(C) = P(+M)\frac{P(C|+M)}{P(+M|C)}</math>                                     
rewritten as
:<math>P(C|+M)\frac{}{}=\frac{P(C)\cdot P(+M|C)}{P(+M)}</math>                          
immediately, because we need P(+M).  To get this, first compute the number of patients that get a positive mammography                                                     
:<math>n_{+M}\frac{}{}=n_{C}P(+M|C)+n_{N}P(+M|N)</math>                                              
where <math>n_{X}</math> is the number of patients in category X.  Divide through by the total number of patients to get                                                                
:<math>P(+M)\frac{}{}=P(C)P(+M|C)+P(N)P(+M|N)</math>
then
:<math>P(C|+M)\frac{}{}=\frac{P(C)\cdot P(+M|C)}{P(C)P(+M|C)+P(N)P(+M|N)}</math>                          
inserting numbers gives
:<math>P(C|+M) = \frac{0.01\cdot 0.8}{0.01\cdot 0.8+0.99 \cdot 0.096} = 0.077639751552795</math>                                                                             
So the probability that she actually has breast cancer is about 8%.                   

(Often students report their answer to many more than 2 significant digits.  How would you calculate the appropriate number of significant digits and the uncertainty in your reported answer, based on the numbers given?)
|}


{| class="wikitable collapsible collapsed"
! align="left" | Answer II
|-
|
In many cases people try to explain things like this using probabilities and Bayes' rule [http://yudkowsky.net/rational/bayes].  However, I generally find that it is easier to just draw a diagram and do the math; you will be using Bayes' rule, but may not even know it.  In the lecture notes I tried to emphasize that you "walk into" Bayes' rule when you just look at a Venn diagram and try to answer questions about it.

To explain this calculation to someone, I would draw/say this:

Out of 1000 women, the 10 will have cancer (1%).  Eight of the 10 (80%) will have a positive mammography, the other two will have a negative mammography.
This leaves 990 without cancer.  However, 990*0.096=95 of these cancer-free women will still have a positive mammography.  These numbers are illustrated in the diagram below.

The number of black squares is the number of women of the 1000 that had a positive mammography; of these women, 8 were are the cancer group and 95 are in the cancer-free group.  If you had a positive mammography, you are in this group of 8+95=103 women, out of which 8/103, or about 8%, have cancer.
{| class="wikitable collapsible"
! align="left" |
|-
|
[[Image:Bayes.png|thumb|600px||1000 women who took a mammography test are each represented as squares.  The women represented by black squares had a positive mammography.  If you had a positive mammography, chances are very good that you are in the (large) cancer-free group.  Related discussion: [http://www.decisionsciencenews.com/2010/12/03/some-ideas-on-communicating-risks-to-the-general-public/]]]
[[:Media:Bayes.xls|Spreadsheet used to create image]]
|}
|}
<br style="clear:both"/>

== Bayes' rule ==

A cab was involved in a hit-and-run accident at night. Two cab companies, the Green and the Blue, operate in the city. You are given the following data:
* 85% of the cabs in the city are Green and 15% are Blue. A witness identified the cab as Blue. The court tested the reliability of the witness under the circumstances that existed on the night of the accident and concluded that the witness correctly identified each one of the two colors 80% of the time and failed 20% of the time.
* What is the probability that the cab involved in the accident was Blue rather than Green?  Use the two approaches (equation- and diagram- based) employed in the example problem related to the breast cancer example covered in class.

== Bayes' rule and Venn Diagrams ==

=== ===

A cab was involved in a hit-and-run accident at night.  Two cab companies, the Green and the Blue, operate in the city.  You are given the following data:
* 85% of the cabs in the city are Green and 15% are Blue.
* A witness identified the cab as Blue.  The court tested the reliability of the witness under the circumstances that existed on the night of the accident and concluded that the witness correctly identified each one of the two colors 80% of the time and failed 20% of the time.

What is the probability that the cab involved in the accident was Blue rather than Green?  Use both the diagram and equation method.

Answer the same question after replacing the first bullet above with

* The two companies operate the same number of cabs, but Green cabs are involved in 85% of the accidents.  Use both the diagram and equation method.

(From Chapter 16 of [http://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow]).  See also [http://library.mpib-berlin.mpg.de/ft/gg/GG_How_1995.pdf].

=== ===

1% of women at age forty who participate in routine screening have breast cancer. 80% of women with breast cancer will get positive mammographies. 9.6% of women without breast cancer will also get positive mammographies. A woman in this age group had a positive mammography in a routine screening. What is the probability that she actually has breast cancer?

=== ===
Use any diagram, including a Venn diagram or diagrams similar to the ones used to explain Bayes' theorem in class, to give a visual explanation of your answer.

=== ===
Derive Bayes' rule.  Include diagrams.

Discussion problem (this is a "part 1" question, which means it is given a binary grade).  Post your answers on your wiki page.

- Read Example 2.4 and 2.5 of Wilks.
- Read [http://www-stat.stanford.edu/~ckirby/brad/papers/2005NEWModernScience.pdf] (more related articles are located at [http://www-stat.stanford.edu/~ckirby/brad/papers/]).
- Find a paper related to space sciences that uses a "Bayesian" approach and add it to your NASA/ADS library and include a link. In two or three sentences, state the sense in which they used a Bayesian approach. 
- Write down at least three questions that you have based on your readings of the two documents and your skimming of a space sciences-related paper that uses a Bayesian approach.

Optional further reading [http://math.ucr.edu/home/baez/bayes.html] [http://www.physicstoday.org/resource/1/phtoad/v65/i7/p54_s2] [http://www.physicstoday.org/resource/1/phtoad/v65/i7/p45_s1]



## Counting

Counting is everything -- In the sense that this is how we think about probability problems when we want to explain it in detail.

Motivation - many continuous distributions can be derived from a counting experiment + limiting constraints.  Often we can decide if an experiment is worth trying by first determining the probability of success.  For example, should I try to find life on other planets?  How long would a satellite need to be in orbit before its chances of observing an event was greater than 10%?  A fundamental part of statistical mechanics involves the counting of the number of states of a system. 

Counting problems are simple to write but difficult to solve.  If you are stuck on a problem, it is usually helpful to try to re-phrase the problem in terms of a tree diagram.

Connection to Statistical Mechanics in Physics
: <math>S = \frac{}{}\mbox{kln}(\Omega)</math>,
where k is Boltzmann's constant, and <math>\Omega</math> is the number of microstates, which depends on the volume of the system, the number of particles in the system, and the energy of each particle.  To derive the thermodynamic properties of a system, count the number of possible states.

### Permutation

**An ordered arrangement of objects**.  Usually relevant in problems "without replacement" and problems where a list of objects is considered different if the order changes.

Example: One red and one blue ball is placed in a container.  The number of permutations of two balls drawn without replacement is 2.

### Combination

**A grouping of objects**.  Usually relevant in problems where some objects are identical or when a re-ordered list of objects is considered as identical the ordered list.

Example: One red and one blue ball is placed in a container.  The number of combinations of two balls drawn with replacement is 4.

### n permute k

The number of ways of ordering `k` objects from a list of `n` distinguishable (unique) objects is

$${_nP_k} = \frac{n!}{(n-k)!}=n\cdot (n-1)\cdot ...\cdot (n-k+1)$$

This quantity is also referred to as "n permute k".

Example:

You have 52 cards.  If you lay out five cards on the table, number of the orderings of 5 cards is ${52!}/{(52-5)!}$.

### n choose k

The number of combinations (or subgroups) of $k$ objects that can be created with $n$ distinguishable objects is

$${_nC_k} = {n\choose k}\frac{n!}{k!(n-k)!}$$

This quantity is also referred to as "n choose k", or the _binomial coefficient_.

Example:

How many ways can you order a list of 5 unique cards?

You have 52 cards.  If you lay out five cards on the table, the number of unique ordered lists (_permutations_) of 5 cards is

$$\frac{52!}{(52-5)!}$$

In most games of cards, how you order you cards in your hand does not matter.   How many unique 5-card hands ('''permutations''') are possible?

$$\frac{}{}{_5P_1}=5!$$

So divide the number of unique order lists of cards by $5!$ to get

$$\frac{52!}{(52-5)!5!}=\frac{}{}{_{52}C_5}=\frac{_{52}P_5}{5!}$$

----

Note:
For back-of-the-envelope calculations and $n$ greater than about 15, it is useful to remember [Stirling's approximation](http://en.wikipedia.org/wiki/Stirling%27s_approximation), which is used extensively in statistical mechanics

$$\ln n! \approx n\ln n - n$$

and remember that

$$e^x \approx 10^{0.4\cdot x}$$

**A look ahead**

$_nC_k$ appears in the Binomial distribution, which is the "mother of all distributions".  From it we can derive the normal distribution, poisson distribution, etc.

Binomial Theorem

$$(x+y)^n=\sum_{k=0}^n{n \choose k}x^ky^{n-k}\quad\quad\quad$$, 

where

$${n \choose k}=\frac{n!}{k!\,(n-k)!}$$

are the binomial coefficients.


## Probability Distributions

# Statistics

Statistics is concerned with

* Describing or summarizing the data (histogram, periodogram, slopes, and summary statistics including mean, standard deviation etc.)
* Quantifying uncertainty - two sources (1) measurement uncertainty and (2) method (analysis method) uncertainty.
* Making inferences (conclusions) - while accounting for uncertainty

Statistical methods are a fundamental part of the modeling process. Two extremes of the modeling process:

1.  Forward - Start with a physical laws. Use physical laws, or approximations, to derive a deterministic system of equations. Apply boundary conditions and solve system of equations. Manipulate free parameters until output of system of equations matches measurement. 
2.  Inverse - Determine an  _effective_  system of equations using ("inverting") the data.
3.  

## Overview of statistical fallacies

The Equiprobabability Bias: https://pubmed.ncbi.nlm.nih.gov/25674192/

https://www.geckoboard.com/best-practice/statistical-fallacies/
https://www.realclearscience.com/articles/2017/04/05/common_statistical_fallacies_and_paradoxes_110241.html
https://flowingdata.com/2012/05/03/common-statistical-fallacies/
http://www.statlit.org/pdf/2008KlassASA.pdf
Kramer_2011_Statistical_Fallacies

