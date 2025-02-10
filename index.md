```mdextension
Title: Statistical Methods in Physics
Subtitle: ASTR/PHYS 390/590<br>Spring, 2025
```

# Course Information

* **Day and Time**: Thursday from 4:30 - 7:10 pm
* **Location**: 220 Planetary Hall
* **Instructor**: Bob Weigel
* **Email**: [rweigel@gmu.edu](mailto:rweigel@gmu.edu)
* **Office Hour**: Thursday 3:30-4:30 pm
* **Course URL**: [http://rweigel.github.io/stats](http://rweigel.github.io/stats)
* **Credits**: 3 (Lecture)
* **Prerequisites**:
  * 390: Grade of B or higher in PHYS 251 or permission of instructor;
  * 590: Enrollment in a COS or VSE graduate program.
* **Catalog Description**: Bayesian and frequentist statistical and data analysis methods applied to data and problems in physics.

HW: 
[1](hw.html#hw-1)
|
[2](hw.html#hw-2)
|
[3](hw.html#hw-3)

# Class Notes

## Thursday, January 30th


**In-class problems**

1. 2% of people age 50–60 who participate in routine screening have colon cancer. 80% of people with colon cancer will test positive. 9.6% of those without colon cancer will also test positive. A person in this age group had a positive test in a routine screening. What is the probability that they actually have colon cancer?

2. A box in a certain supply room contains four 40-W light-bulbs, five 60-W bulbs, and six 75-W bulbs. Suppose that three bulbs are randomly selected.

   a. What is the probability that exactly two of the selected bulbs are rated at 75-W?

   b. What is the probability that all three of the selected bulbs have the same rating?

   c. What is the probability that one bulb of each type is selected?

   d. Suppose now that bulbs are to be selected one by one until a 75-W bulb is found. What is the probability that it is necessary to examine at least 6 bulbs?

   e. How would you use a numerical simulation to estimate the answer to a. (assume you don't know the formulas for permutations and combinations)?

3. Devise a numerical experiment to test the statement of the Weak Law of Large Numbers

4. Devise a numerical experiment to test the statement of the Central Limit Theorem

## Thursday, January 23rd

* Introductions

* Discuss Syllabus Questions. **Preparation**: Read the syllabus before class.

* Cover Probability topics in [Devore Chapter 2]((https://drive.google.com/file/d/1bN68ELL0DBrgVwbE0m74LPuTwoHqXw2M/view?usp=sharing★★★★★remove★★★★★); see also  [Bulmer Chapters 1 and 2](https://drive.google.com/file/d/1IuANm_ZxtuY75c9Caguv3cdG8JbmkADi/view?usp=sharing★★★★★remove★★★★★), [Bonamente Chapter 1](https://drive.google.com/file/d/1Z4uN1ReMXAUMZck_UmavM3lIGrbE1U-C/view?usp=sharing★★★★★remove★★★★★), [Rozanov Chapters 1 and 2](https://drive.google.com/file/d/1ROIF0mLquDcoMGJtj5Oz93On_ATCcfmc/view?usp=drive_link★★★★★remove★★★★★), [Larson Chapters 1 and 2](https://drive.google.com/file/d/1Cc65FWiptQLqtXiKHpB2JJDLe-dh7WtX/view?usp=drive_link★★★★★remove★★★★★) and [DeGroot Chapter 1](https://drive.google.com/file/d/1FtvQS1303P_GA4aM3ZbQIGPbThTXmfpq/view?usp=sharing★★★★★remove★★★★★).

   **Preparation**: Read [Devore Chapter 2](https://drive.google.com/file/d/1exeJzUFx8D1PC_rDpq1ORP6Y9Ce0wzkl/view?usp=drive_link★★★★★remove★★★★★), write down all of the definitions of key terms, and be prepared to define without referring to your notes. You don't have to fully understand all of the examples; I will go over examples and problems in class, and it will help if you are familiar with all of the definitions.

   At the start of class, I will ask students for key terms, write them on the board, and then ask for volunteers to provide a definition (ideally without referring to your notes).

* Cover GitHub; **Preparation**: Create a [GitHub](https://github.com) account before class starts.

* Cover Discord

# Summary

This course covers fundamental statistical methods that apply to most data--related (both measurement and simulation) problems. I emphasize the development of a deep understanding of the interpretation of statistical results.

I encourage students doing data-related research projects to use their data for a project in which the statistical methods covered in class are applied to their data.

# Motivation and Learning Outcomes

**Motivation**

* Many entry-level jobs for BS, MS, and PhD typically involve exploratory data analysis and require a basic understanding of statistics.
* Many of our graduate students are working on data-intensive research problems that require understanding modern statistical methods.
* Many BS, MS, and PhD students have not taken a traditional statistics course as an undergraduate.

**Learning Outcomes**

Students will
1. be able to solve fundamental statistical problems analytically and numerically;
1. have an intuitive understanding of the interpretation of uncertainty;
1. be able to compute uncertainties using at least two methods;
1. generate ideas for exploratory data analysis and validation of statistical calculations;
1. learn to use at least one advanced statistical package;
1. learn to present data and results at the level of quality seen in seminars, journal articles, and meeting posters; and
1. learn to write code in a way that is easy for others to understand and modify.

# Methods of Instruction

* In-class time will be approximately 50% lecture/demonstration and 50% in-class discussion.
* I usually have you do a reading and solve a basic problem on a new topic before I discuss it in class. I find content that I present "sticks" if students have experimented with the concepts before I discuss them.
* You will be asked to participate in class discussions during class and on Discord. Talking and writing about statistics will help you understand statistics.
* Homework assignments will be approximately 50% hand-written and 50% programs. I will ask students to present their solutions during class and for others to comment.
* After the midterm, students will propose a project, and part of each subsequent homework assignment will be an additional analysis related to your project. The required analysis will be based on what you propose and ideas that are generated when you give a brief ($\sim$5--minute) update on your progress.

%* I give detailed solutions to homework problems. However, I will not always be able to provide detailed feedback or identify many errors in your code. I will discuss general types of issues that I observed on the homework problems during class.

%I may ask you to meet with me to explain your reasoning on your homework. I will comment on your how you solved the problem and how you presented your results. Like ordinary writing, they can always be improved. I want you to leave this class knowing how a working scientist organizes analyses and presents results.

# Programming

* You may use any programming language for homework and the final project. I will write my solutions in Python.
* I assume that you are proficient in Python (or another language) at the level of a B grade in PHYS 251. The topics that you should be familiar with are covered in my [notes for PHYS 251](python.html).
* I have provided an extensive set of notes on Python techniques that you will use and should be familiar with.

# Textbook

There is not a single textbook that covers all of the material in this course. I will provide hand--outs or links to references for each topic covered.

Two general references on statistics that I highly recommend are
1. [Principles of Statistics, M.G. Bulmer](https://drive.google.com/file/d/1IuANm_ZxtuY75c9Caguv3cdG8JbmkADi/view?usp=sharing★★★★★remove★★★★★) -- A short Dover book that covers fundamental statistical topics; also available used [on Amazon](https://www.amazon.com/Principles-Statistics-Dover-Books-Mathematics/dp/0486637603) for ~$5.00.
2. [Probability and Statistics for Engineering and the Sciences (8th ed), J.L. Devore](https://drive.google.com/file/d/1bN68ELL0DBrgVwbE0m74LPuTwoHqXw2M/view?usp=sharing★★★★★remove★★★★★) -- A commonly used textbook for upper-division engineering and science majors. | [Amazon](https://www.amazon.com/Probability-Statistics-Engineering-Sciences-Devore/dp/0538733527)

Many additional references and resources are listed in the [References](#references) section of this syllabus.

# Evaluation

* **Homework**: 40% - Approximately one per week; extra problems will be assigned for students registered in 590. Most homework assignments will include at least one problem that requires the use of real data. Assignments are due before class starts. 
* **Midterm**: 30%
* **Final project**: 30%
* **Final course**: Grades for undergraduates are determined from numerical course grades using 90%–100% A, 80%–90% B, 70%–80% C, 60%–70% D, < 60% F. For graduate students, 70% and lower is an F (the graduate grade scale does not have a D).

# Topics

Supplementary references and notes will be provided as needed.

## Basic Concepts in Probability

1. Mathematical, Frequentist, and Bayesian probabilities
2. Conditional probability
3. Bayes' theorem
4. Counting - permutations and combinations
5. Probability distributions
6. Overview of statistical fallacies

## Python

1. NumPy
2. Random number generators
3. Data visualization and creating publication--quality plots

## Exploratory Data Analysis

1. Histograms
2. Autocorrelation
3. Periodograms and Short--Time Fourier Transforms
4. Other options based on student interest

## Elements of Statistics

1. Expectation, mean, variance, and bias
2. Random variables, distributions, quantiles, mean, variance
3. Joint distributions, covariance, correlation, independence
4. The law of large numbers
5. Central limit theorem
6. Bootstrapping

## Hypothesis Tests and Confidence/Credible Intervals

1. Frequentist
2. Bayesian
3. Bootstrap and Jackknife

## Parameter Estimation - Basic

1. Least-squares
2. Maximum likelihood

## Parameter Estimation - Advanced

1. Linear models
2. Nonlinear models
3. The EMCEE Markov chain Monte Carlo Python library

# References

The following references are not needed for this course, but you may find them useful for alternative explanations of topics in the textbook.

## General

1. [Principles of Statistics, M.G. Bulmer](https://drive.google.com/file/d/1IuANm_ZxtuY75c9Caguv3cdG8JbmkADi/view?usp=sharing★★★★★remove★★★★★) -- A short Dover book that covers fundamental statistical topics.
1. Many of the topics covered in this course are covered in the MIT OCW course [Introduction to Probability and Statistics](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/).
1. Dealing with Uncertainty - A Guide to Error Analysis 2nd Edition, M. Drosg -- Covers uncertainty and error analysis basics at Freshman physics lab level. Very good but very expensive (> $100 on Amazon).
1. [Bonamente, 2017 Statistics and Analysis of Scientific Data](https://drive.google.com/file/d/1Z4uN1ReMXAUMZck_UmavM3lIGrbE1U-C/view?usp=sharing★★★★★remove★★★★★) - Listed as a graduate text, but level is similar to undergraduate textbooks. Covers most of the main topics discussed in this course.
1. Statistical Methods in Experimental Physics, F. James
1. Statistics, D. Freedman, R. Pisani, and R. Purves -- A basic introduction to statistics with many examples and extended discussion of topics.
1. Probability for the Enthusiastic Beginner, D. Morin -- An elementary introduction to probability.
1. [Probability and Statistics for Engineering and the Sciences (8th ed), J.L. Devore](https://drive.google.com/file/d/1bN68ELL0DBrgVwbE0m74LPuTwoHqXw2M/view?usp=sharing★★★★★remove★★★★★) -- A commonly used textbook for upper-division engineering and science majors. | [Amazon](https://www.amazon.com/Probability-Statistics-Engineering-Sciences-Devore/dp/0538733527)
1. [Probability and Statistics, M.H. DeGroot and M.J. Schervish (4th ed)](https://drive.google.com/file/d/1FtvQS1303P_GA4aM3ZbQIGPbThTXmfpq/view?usp=sharing★★★★★remove★★★★★) -- Similar in scope and coverage of Devore.
1.  [Probability Theory: A Concise Course, Y.A. Rozanov](https://drive.google.com/file/d/1ROIF0mLquDcoMGJtj5Oz93On_ATCcfmc/view?usp=drive_link★★★★★remove★★★★★)
1. [Introduction to Probability Theory and Statistical Inference (3rd ed), H.J. Larson](https://drive.google.com/file/d/1Cc65FWiptQLqtXiKHpB2JJDLe-dh7WtX/view?usp=drive_link★★★★★remove★★★★★) 
1. [Introduction to Probabability, 2019 (2nd ed) J.K. Blitzstein and J. Hwang](https://projects.iq.harvard.edu/stat110/home)

## Bayes

### General

1. Bayes' Rule with Python -- A Tutorial Introduction to Bayesian Analysis (2013), by J.V. Stone. This book is a good starting point. Chapters: [1](https://drive.google.com/file/d/1JV1EU9R0WbyY_t6BDlGR4u7N9PXzikcE/view?usp=sharing★★★★★remove★★★★★), [4](https://drive.google.com/file/d/1zx2EAsjhnnU6BDFd8In5wAwXDyYi1wVA/view?usp=sharing★★★★★remove★★★★★), [5](https://drive.google.com/file/d/1qqW8CzYLqGbkSMDi1U0tGhiIMe5biGiC/view?usp=sharing★★★★★remove★★★★★)
1. [Doing Bayesian Data Analysis by Kruschke](http://www.r-5.org/files/books/computers/algo-list/statistics/data-mining/John_K_Kruschke-Doing_Bayesian_Data_Analysis-EN.pdf) -- The best overview that I am aware of. The examples are in R, but translation to other languages is straightforward. Most of this book's value is in the concepts' descriptions.
1. [Bayesian Statistics -- an Introduction by P.M. Lee](https://www.amazon.com/Bayesian-Statistics-Introduction-Peter-Lee-dp-1118332571/dp/1118332571/) is a classic introductory textbook.
1. [How to become a Bayesian in eight easy steps: An annotated reading list, by Etz et al., 2018](https://link.springer.com/article/10.3758/s13423-017-1317-5).
1. [Data Analysis -- A Bayesian Tutorial (2006), by D.S. Sivia and J. Skilling](https://drive.google.com/file/d/1jlcywhHQlfKGADki7yxuo5T55X15Rjpd/view?usp=sharing★★★★★remove★★★★★).
1. Neural Networks for Pattern Recognition (2006), by C.M. Bishop -- Advanced undergraduates or first-year PhD students; the first few chapters have a good introduction to Bayes' rule.
1. Teaching Statistics in the Physics Curriculum: Unifying and Clarifying Role of Subjective Probability (1999), by G. D'Agostini
1. The Elements of Statistical Learning (2009; 2nd Edition), by T. Hastie, R. Tibshirani, and J. Friedman -- This is a classic book on Machine Learning/Statistical Learning.
1. Validation of Software for Bayesian Models Using Posterior Quantiles by Cook, Gelman, and Rubin, 2006 (https://www.jstor.org/stable/27594203).
1. [Section 3.4 of the lecture notes on Hierarchal Models by Junker](http://www.stat.cmu.edu/~brian/463-663/week09/Chapter%2003.pdf) contains in Section 3.4 a detailed introduction to a typical example covered in many books -- finding the posterior when the standard deviation of the population is known and a prior distribution is available.

### Bayesian vs. Frequentist

1. The primary reference is [Jaynes 1976]( https://bayes.wustl.edu/etj/articles/confidence.pdf).
2. Frequentism and Bayesianism: A Python-driven Primer (2015), by J. VanderPlas ([arxiv.org/pdf/<wbr>1411.5018.pdf](https://arxiv.org/pdf/1411.5018.pdf)).
3. Lecture notes on the comparison of frequentist and Bayesian Inference, by J. Orloff and J. Bloom ([MIT18<wbr>_05S14<wbr>_Reading20.pdf](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading20.pdf))
4. Statistical Inference Showdown: The Frequentists vs. The Bayesians (2017), by K. Dubovikov.
5. [The Earth is Round](https://psycnet.apa.org/record/1995-12080-001) covers the mis-use of significance tests in the psychological literature.

### Credible Intervals

In the following references, the terms "Bayesian Intervals", "Bayesian Confidence Intervals", and "Credible Intervals" are used to mean the same thing.

* The primary reference is [Jaynes 1976]( https://bayes.wustl.edu/etj/articles/confidence.pdf). This is not an easy read as a first introduction. The following references provide a more introductory explanation: [Kruschke and Liddell 2018](https://link.springer.com/article/10.3758/s13423-016-1221-4); [VanderPlas 2014](https://arxiv.org/pdf/1411.5018.pdf). [A blog post by VanderPlas](http://jakevdp.github.io/blog/2014/06/12/frequentism-and-bayesianism-3-confidence-credibility/) goes over one of the examples in Jaynes. Read the comments to see the disagreements about the Frequentist and Bayesian approaches.
* [Levy 2012](http://www.mit.edu/~rplevy/pmsl_textbook/chapters/pmsl_5.pdf) is also a good introduction.
* Credible intervals are described by the authors of the [easystats](https://easystats.github.io/bayestestR/articles/credible_interval.html).
* [testscience.org](https://testscience.org/characterize-system/test-evaluation-analyses/bayesian-credible-intervals/) has a brief example that compares confidence intervals with credible intervals.
* Analysis of regression confidence intervals and Bayesian credible intervals for uncertainty quantification by Liu, Ye, and Ling, 2012 (https://doi.org/<wbr>10.1029/<wbr>2011WR011289)
* [`bayes_mvs`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bayes_mvs.html) in SciPy uses the method described in  [A Bayesian perspective on estimating mean, variance, and
standard-deviation from data by Travis E. Oliphant, 2006](https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=1277&context=facpub)

### MCMC

* https://twiecki.io/blog/2015/11/10/mcmc-sampling/
* Data analysis recipes: Using Markov Chain Monte Carlo (2017), Hogg and Foreman-Mackey (available from [arxiv.org](https://arxiv.org/abs/1710.06068) and [iopscience.iop.org](https://iopscience.iop.org/article/10.3847/1538-4365/aab76e)); Provides an overview of the motivation for MCMC sampling, discussions of its use and abuse, and detailed recipes for implementation.
* [Ravenzwaaij, Cassey, and Brown, 2018](https://link.springer.com/article/10.3758/s13423-016-1015-8)

### Misc

* https://stats.stackexchange.com/questions/421221/bayesian-inference-feeding-posterior-back-in-as-prior
* https://projecteuclid.org/journals/statistical-science/volume-32/issue-1/How-Principled-and-Practical-Are-Penalised-Complexity-Priors/10.1214/16-STS603.full
* http://www2.denizyuret.com/ref/aitkin/posterior-bayes-factors.pdf
* https://towardsdatascience.com/what-is-rejection-sampling-1f6aff92330d
* https://stats.stackexchange.com/questions/2356/are-there-any-examples-where-bayesian-credible-intervals-are-obviously-inferior
* https://link.springer.com/article/10.3758/s13423-016-1221-4
* [Sawilowsky, 2011, Statistal Fallacies](https://drive.google.com/file/d/13w5qqFfhgmf1K02WEsBMdPOeV0Y3nEUC/view?usp=sharing★★★★★remove★★★★★)

## Astronomy

1. Markov Chain Monte Carlo Methods for Bayesian Data Analysis in Astronomy (2017), S. Sharma.
1. Bayesian Methods for the Physical Sciences: Learning from Examples in Astronomy and Physics (2015), S. Andreon and B. Weaver.
1. Bayesian Models for Astrophysical Data: Using R, JAGS, Python, and Stan, J.M. Hilbe, R.S. de Souza, and E.E.O. Ishida.
1. Modern Statistical Methods for Astronomy: With R Applications (2012), E.D. Feigelson and G.J. Babu.
1. Statistics, Data Mining, and Machine Learning in Astronomy: A Practical Python Guide for the Analysis of Survey Data, Željko Ivezic, Andrew J. Connolly, Jacob T VanderPlas, and Alexander Gray.
1. Computational Bayesian Statistics: An Introduction (2019), M. Antónia Amaral Turkman, Carlos Daniel Paulino, Peter Müller.

## Software

1. [Think Stats](http://greenteapress.com/thinkstats2/html/thinkstats2010.html) - A free book demonstrating standard statistical calculations in Python.
1. [EMCEE Overview](https://arxiv.org/pdf/1202.3665.pdf)
 [EMCEE software documentation](https://emcee.readthedocs.io/en/stable/)

# General Policies

## Academic Integrity

Mason is an Honor Code university; please see the Office for Academic Integrity for a full description of the code and the honor committee process. The principle of academic integrity is taken very seriously and violations are treated gravely. What does academic integrity mean in this course? Essentially this: when you are responsible for a task, you will perform that task. When you rely on someone else’s work in an aspect of the performance of that task, you will give full credit in the proper, accepted form. Any student use of Generative-AI tools should follow the fundamental principles of the Honor Code.

## Disability

Disability Services at George Mason University is committed to providing equitable access to learning opportunities for all students by upholding the laws that ensure equal treatment of people with disabilities. If you are seeking accommodations for this class, please first visit http://ds.gmu.edu/ for detailed information about the Disability Services registration process. Then please discuss your approved accommodations with me. Disability Services is located in Student Union Building I (SUB I), Suite 2500. Email:ods@gmu.edu | Phone: (703) 993-2474.

## Diversity and Inclusion

We seek to create a learning environment that fosters respect for people across identities. We welcome and value individuals and their differences, including gender expression and identity, race, economic status, sex, sexuality, ethnicity, national origin, first language, religion, age, and ability. We encourage all members of the learning environment to engage with the material personally but to also be open to exploring and learning from experiences different than their own. Mason’s nondiscrimination policy is at https://universitypolicy.gmu.edu/policies/non-discrimination-policy/.

## Communication

If you have a question whose answer may be of interest to other students, please post it to Discord and make it visible to other students. You can set the post so that you are anonymous.

If you need to send communicate with me about something private, please send it to `rweigel@gmu.edu` from your MasonLive email address.

## University Resources

* Learning Services https://learningservices.gmu.edu/
* Student Support and Advocacy Center https://ssac.gmu.edu/
* Counseling and Psychological Services https://caps.gmu.edu/
