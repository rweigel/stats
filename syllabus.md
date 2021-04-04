<p class='title'>AstroStats</p>

<p class='subtitle'>ASTR/PHYS 390/590</p>

# Course Information

*   **Day and Time**: Thursday from 4:30 - 7:10 pm
*   **Location**: Online
*   **Instructor**: Bob Weigel
*   **Email**: [rweigel@gmu.edu](mailto:rweigel@gmu.edu)
*   **Office Hour**: Thursday 3:30-4:30 pm
*   **Course URL**: [http://rweigel.github.io/astrostats](http://rweigel.github.io/astrostats)
*   **Credits**: 3 (Lecture)
*   **Prerequisites**:
    *   390: Grade of B or higher in PHYS 251 or permission of instructor;
    *   590: Enrollment in a COS or VSE graduate program.
*   **Catalog Description**: Bayesian and frequentist statistical and data analysis methods applied to data and problems in astrophysics and the space sciences.

**Homeworks**: [1](hw.html#hw-1) | [2](hw.html#hw-2) | [3](hw.html#hw-3) | [4](hw.html#hw-4) | [5](hw.html#hw-5) | [6](hw.html#hw-6) | [7](hw.html#hw-7) | [8](hw.html#hw-8)


[Midterm](hw.html#midterm)

# Motivation

*   Many entry-level jobs for BS, MS, and PhD typically involve exploratory data analysis and require a basic understanding of statistics.
*   Many of our graduate students are working on data-intensive research problems that require an understanding of modern statistical methods.
*   Many BS, MS, and PhD students have not had a traditional statistics course as an undergraduate.

# Methods of Instruction

* In-class time will be approximately 50% lecture/demonstration and 50% in-class discussion.
* I usually have you do a reading and basic follow-up problems before I discuss a topic in class. I find content that I present "sticks" if students have experiemented with the concepts before I discuss them.
* You will be asked to participate in class discussions during class and on Piazza. Talking and writing about statistics will help you understand statistics.
* Homework assignments will be ~50% hand-written and ~50% programs. I will ask students to present their solutions during class and for other students to comment.
*   I give detailed solutions to homework problems. However, I will not be able to provide detailed feedback or identify many errors in your code. I will discuss general types of issues that I observed on the homework problems during class.
    *  As a result, I may ask you to meet with me to explain your reasoning. I will comment on your how you solved the problem and how you presented your results. Like ordinary writing, they can always be improved. I want you to leave this class knowing how a working scientist organizes analyses and presents results.

# Programming

* Any programming language may be used for homework and the final project. I will write my solutions in Python.
* I assume that you are proficient in Python (or another language) at the level of a B grade in PHYS 251. The topics that you should be familiar with are covered in my [notes for PHYS 251](python).
*  I have provided an extensive set of notes on Python techniques that you will use and should be familiar with.

# Textbook

Practical Statistics for Astronomers, 2nd Edition (2012), by J.V. Wall and C.R. Jenkins | [Amazon](https://www.amazon.com/Practical-Statistics-Astronomers-Cambridge-Observing/dp/0521732492) | [Author's web page](https://www.astro.ubc.ca/people/jvw/ASTROSTATS/index.html) |

This textbook covers modern statistical methods used in astronomy. It is not a comprehensive textbook, however. The textbook is most useful as a reference to understand the approaches and types of problems considered in the astronomical literature. For this reason, I will supplement this textbook with copies of background material. I'll typically provide two references that explain the background material.

Two general references on statistics that I highly recommend are
1. Principles of Statistics, M.G. Bulmer -- A short Dover book that covers fundamental statistical topics in and parsimonious manner. [Available used on Amazon](https://www.amazon.com/Principles-Statistics-Dover-Books-Mathematics/dp/0486637603) for ~$5.00.
2. Probability and Statistics for Engineering and the Sciences (8th ed), J.L. Devore -- A commonly used textbook for upper-division engineering and science majors. | [Amazon](https://www.amazon.com/Probability-Statistics-Engineering-Sciences-Devore/dp/0538733527) |

In the [References](#references) section of this syllabus, many additional references and resources are listed.

# Evaluation

*   **Homework**: 40% - Approximately one per week; extra problems will be assigned for students registered in 590. Most homework assignments will include at least one problem that requires the use of astronomy or space science data. Assignments are due before class starts.
*   **Midterm**: 30% - In-class and hand-written.
*   **Final project**: 30% - Students registered in 590 students will have an extra part for the final project.
*   **Final course**: Grades for undergraduates are determined from numerical course grades using 90%–100% A, 80%–90% B, 70%–80% C, 60%–70% D, < 60% F. For graduate students, 70% and lower is an F (the graduate grade scale does not have a D).

# Weekly Schedule

## January 28th

* Introductions
* Brief introduction to course
* Discussion of topics on the syllabus
* **Course Logistics**; I will go over the following on the first day of class. You do not need to do anything before then.
    * Make sure that you can log on to Piazza. You should have received an email from Piazza before the start of the first class.
    * Create a GitHub account with your GMU username (the name in your email address, lowercase) and a repository named `astrostats` (lowercase). Give `rweigel` read/write permissions. If you already have a GitHub user id and would like to use it, send me it.
    * During class discussion, I will ask you to turn on your webcam. Please let me know if you have an issue with this (e.g., you are working in a room with a family in the background or are calling in from a locker room).
*   **Course comments**
    * Approximately 1/2 of the students in this class are undergraduates, the other 1/2 are graduates. We did this because this is the first time that the course has been taught. There will be an adjustment period as I figure out how best to handle differentials in experience with statistics, programming, and data analysis.
    * Ideally, this course would have a pre-requisite of an undergraduate statistics course. The motivation for offering this course was to familiarize students researching astronomy with modern statistical methods (Bayesian and Monte Carlo). As a result, I am going to cover the minimal amount of background needed to get to these modern methods.
*   Python IDEs and [Google Colab](https://colab.research.google.com/) introduction
*   Review of Python
*   [Review of Python/NumPy](python.html#numpy) (and MATLAB, if needed) 
*   [HW #1 discussion](hw.html)
*   Follow-up notes:
    1.   The recording is at https://www.youtube.com/watch?v=yxFzL_TD900 In the future, I'll provide a link to a Zoom page. This week I had to do it differently because I had to trim off conversations I had after class.
    2.   W.M. mentioned `np.where` as an option for finding elements in an `ndarray`. I don't recall ever using this function but can see where it would be useful (people coming from IDL would probably use this function more often because IDL has an equivalent function. I come from a MATLAB background and tend to use the method shown in class). I've added an example of its use on my [Python notes page](https://rweigel.github.io/astrostats/python.html#finding-elements).
    3.  In the HW, I ask for you to provide written solutions in a `.md` or `.pdf` file. `.md` is the extension for Markdown, which is a plain-text file written in a certain way. To create a Markdown file on Github, simply click "Create File", then enter, for example, `HW1_1b.md` and then enter text. Markdown is an analog to HTML except it is much easier to write Markdown. I'll provide more details in the next class period. As an alternative, just write your answers in an MS Word document, save it as a PDF, and then upload it to GitHub.
    4.  I expect that students may encounter issues submitting their first assignment to GitHub. If you have any issues, meet with me before or after class. I won't count assignments as late if you contacted me about a submission issue.
    5.  In class, I discussed setting the seed for a random number generator if you want to get the same result when you run the code multiple times. I mentioned that I did not know if the choice of seed mattered. For a good random number generator, the randomness of the generated sequence should be independent of the choice of seed. I found a site that explains the basics of random number generation using very simple algorithms; see [Peter Alfeld's Random Number Generator notes](https://www.math.utah.edu/~alfeld/Random/Random.html). On HW1, **do not** use `np.random.seed` as I did in class. I'll explain more about when you want to use it the next time that we meet.
    6.  I still can't think of the error I encountered when I created an array using `x = np.array([1,2,3])`, which created an integer array instead of a floating-point array. If anyone can think of a simple example where you get an unexpected result because `x` is an integer array, show us during the next class period. 

## February 4th
- [HW #1](hw.html#hw-1) due before class starts
- The Discord server is up. You can ask questions there as an alternative to Piazza. If you want to meet with me, we can meet on either Discord or Zoom (it is a little easier to initiate a meeting on Discord, but Discord is not offically sanctioned by GMU).
- We will continue to meet for class and office hours on Zoom. Don't worry about missing somthing important on Discord. I'll post it on the course web page.
- Extended discussion of [HW #1](hw.html#hw-1)
- Basic Concepts in Probability
- Follow-up notes
    * If ambiguity or error in a problem statement, **please** post a question on Piazza or Discord! 
    * The recording is on my [Zoom page](https://gmu.zoom.us/rec/share/Fqvgv9j-bH5vpC7JLoJ8o5ABF-1OUbPXzVOPF3mu442nwAby3fWwlUybSzEpZvH-.B3rl8OT1FN2X965N).
    * When I go through your assignments, I may move your HWs out of a subdirectory to remind you to not do that. I want everyone's repository to contain the same structure and file names so that my automation software for pulling and pushing works.
    * When I was discussing the combination problem for the number of unique license plates that could be created given stickers with the numbers 0-9 assuming that license plates with the same set of numbers in any order are treated as not-unique, I wrote down as an example "899 = 989 = 998" are equivalent. These three are not options because a number is repeated. I should have written, "For example, 123 and all permutations are equivalent license plates". In spite of this mistake, someone gave the correct answer - that there are 3! permutations of any three numbers, so if the number of possible license plates is 9!/7! assuming the order of the numbers matters, then the number of possible license plates is 9!/(7!3!) assuming license plates with the same numbers in any order are equivalent.
    * I am working on posting my solutions to HW1 and also posting HW2. I expect to have HW2 posted by Saturday at noon, which is about a day later than I planned (I typically post the next HW a day after class because I often modify what I planned to assign based on what happened in class). I'll update the [course page](https://rweigel.github.io/astrostats/) and make a Piazza post when I have posted HW2.

## February 11th

*   [HW #1](hw.html#hw-1) notes based on grading.
    * Discuss W.M.'s solution.
*   Discord - Justin's timing experiment and Nasser's question
*   [HW #2](hw.html#hw-2) due before class starts
*   Discuss HW #2 solutions 
*   In-class work on problems related to HW #2 and HW #3

## February 18th

*   [HW #3](hw.html#hw-3) due before class starts
*   Discuss HW #3 solutions
*   In-class work on problems related to HW #3
*   From this point on, I'll be covering topics in the order that they appear and Wall and Jenkins. Up until now, the problems have been mostly about programming techniques that you'll need. The problems did not require knowledge of statistics, but you'll want to think back to these problems as the results and their interpretation will be important.

## February 25th

*   [HW #4](hw.html#hw-4) due before class starts
*   I've written up my notes from our discussion of HW #3. I've also added additional details on problem 3.3 regarding probability densities and the interpretation of the the posterior.
*   Discuss question on Discord about `np.vectorize`.
*   Discussion of problems 4.2 and 4.3.
*   Discussion of reading.
*   Discussion of problem 4.4.   

## March 4th

* Discussion of [HW #5](hw.html#hw-5)
* Discussion of [elements of statistics](notes.html#statistics)

## March 11th

* Discussion of [HW #6](hw.html#hw-6)
* Discussion of $P$s (probability mass functions), pdfs (probability density functions), and their generation in Python
* Discussion of degrees--of--freedom
* Discuss absolute paths in code

## March 18th

* [HW #7](hw.html#hw-7) due
* Discuss PA's HW5.1 soln.
* Discuss plot labels, `np.round`, and `format`.
* Discuss number of decimals in numbers.
* [Midterm](midterm.html#midterm) assigned

## March 25th

* [Midterm](midterm.html#midterm) due before class
* Discuss `np.full((3, ), np.nan)`
* General observations on HW6
* Discuss [Midterm](midterm.html#midterm)

## April 1st

* Discuss [paper](http://articles.adsabs.harvard.edu//full/1990ApJ...364..104I/0000104.000.html) on alternatives to ordinary least squares (OLS)
* Review of Bayes' Theorem and [HW 3.3](hw.html#bayes-rule-for-statistical-inference)

## April 8th

* [HW #8](hw.html#hw-8) due

## April 15th

## April 22nd

## April 29th

## May 6th

Thursday, May 6th from 4:30 -- 7:10 pm

Final exam ([full schedule](https://registrar.gmu.edu/wp-content/uploads/Spring-2021-Final-Exam-Schedule.pdf))

# Topics

The topics listed below are covered in Chapters 2-7 of the textbook. Supplementary references and notes will be provided as-needed.

## Python

1. NumPy
2. Random number generators
3. Data Visualization

## Basic Concepts in Probability

1. Mathematical, Frequentist, and Bayesian probabilities
2. Conditional probability
3. Bayes' theorem
4. Counting - permutations and combinations
5. Probability distributions
6. Overview of statistical fallacies

## Elements of Statistics

1. Expectation, mean, variance, and bias
2. Random variables, distributions, quantiles, mean, variance
3. Joint distributions, covariance, correlation, independence
4. The law of large numbers
5. Central limit theorem
6. Bootstrapping

## Hypothesis Tests

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

1. Principles of Statistics, M.G. Bulmer - A short Dover book that covers fundamental statistical topics in and parsimonious manner. Available on Amazon for $3.00.
1. Many of the topics covered in this course are covered in the MIT OCW course [Introduction to Probability and Statistics](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/). 
1. Dealing with Uncertainty - A Guide to Error Analysis 2nd Edition, M. Drosg - Covers basics of uncertainty and error analysis at Freshman physics lab level. Very good but very expensive (> $100 on Amazon).
1. Statistical Methods in Experimental Physics, F. James - A standard reference that you should have a copy of.
1. Statistics, D. Freedman, R. Pisani, and R. Purves - A basic introduction to statistics with many examples and extended discussion of topics.
1. Probability for the Enthusiastic Beginner, D. Morin - A very basic introduction to probability.
1. Probability and Statistics for Engineering and the Sciences (8th ed), J.L. Devore - A commonly used textbook for upper-division engineering and science majors.
1. Probability and Statistics, M.H. DeGroot and M.J. Schervish (4th ed) -- Similar in scope and coverage of Devore. 

## Bayes

### General

1. Neural Networks for Pattern Recognition (2006), by C.M. Bishop - Advanced undergraduates or first-year PhD students; the first few chapters have a good introduction to Bayes' rule.
2. Frequentism and Bayesianism: A Python-driven Primer (2015), by J. VanderPlas ([arxiv.org/pdf/<wbr>1411.5018.pdf](https://arxiv.org/pdf/1411.5018.pdf)).
3. Bayes' Rule - A Tutorial Introduction to Bayesian Analysis (2013), by J.V. Stone
4. Lecture notes on the comparison of frequentist and Bayesian Inference, by J. Orloff and J. Bloom ([MIT18<wbr>_05S14<wbr>_Reading20.pdf](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading20.pdf))
5. Teaching Statistics in the Physics Curriculum: Unifying and Clarifying Role of Subjective Probability (1999), by G. D'Agostini
6. Statistical Inference Showdown: The Frequentists vs. The Bayesians (2017), by K. Dubovikov [link]
7. Data Analysis - A Bayesian Tutorial (2006), by D.S. Sivia and J. Skilling
8. The Elements of Statistical Learning (2009; 2nd Edition), by T. Hastie, R. Tibshirani, and J. Friedman -- This is a classic book on Machine Learning/Statistical Learning.

http://www.stat.columbia.edu/~gelman/research/published/Cook_Software_Validation.pdf

https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2011WR011289

### Credible Intervals

In the following references, the terms "Bayesian Intervals", "Bayesian Confidence Intervals", and "Credible Intervals" are used to mean the same thing.

* The primary reference is  [Jaynes 1976]( https://bayes.wustl.edu/etj/articles/confidence.pdf). This is not an easy read as a first introduction. The following references provide a more introductory explanation: [Kruschke and Liddell 2018](https://link.springer.com/article/10.3758/s13423-016-1221-4); [VanderPlas 2014](https://arxiv.org/pdf/1411.5018.pdf). [A blog post by VanderPlas](http://jakevdp.github.io/blog/2014/06/12/frequentism-and-bayesianism-3-confidence-credibility/) goes over one of the examples in Jaynes. Read the comments to see the disagreements about the Frequentist and Bayesian approach.
* [Levy 2012](http://www.mit.edu/~rplevy/pmsl_textbook/chapters/pmsl_5.pdf) is also a good introduction.
* Credible intervals are described by the authors of the [easystats](https://easystats.github.io/bayestestR/articles/credible_interval.html).
* [testscience.org](https://testscience.org/characterize-system/test-evaluation-analyses/bayesian-credible-intervals/) has a brief example that compares confidence intervals with credible intervals.

### MCMC

* https://twiecki.io/blog/2015/11/10/mcmc-sampling/
* Data analysis recipes: Using Markov Chain Monte Carlo (2017), Hogg and Foreman-Mackey (available from [arxiv.org](https://arxiv.org/abs/1710.06068) and [iopscience.iop.org](https://iopscience.iop.org/article/10.3847/1538-4365/aab76e)); Provides an overview of the motivation for MCMC sampling, discussions of its use and abuse, and detailed recipies for implementation.

## Astronomy  

1. Markov Chain Monte Carlo Methods for Bayesian Data Analysis in Astronomy (2017), S. Sharma.
1. Bayesian Methods for the Physical Sciences: Learning from Examples in Astronomy and Physics (2015), S. Andreon and B. Weaver.
1. Bayesian Models for Astrophysical Data: Using R, JAGS, Python, and Stan, J.M. Hilbe, R.S. de Souza, and E.E.O. Ishida.
1. Modern Statistical Methods for Astronomy: With R Applications (2012), E.D. Feigelson and G.J. Babu.
1. Statistics, Data Mining, and Machine Learning in Astronomy: A Practical Python Guide for the Analysis of Survey Data, Željko Ivezic, Andrew J. Connolly, Jacob T VanderPlas, and Alexander Gray.
1. Computational Bayesian Statistics: An Introduction (2019), M. Antónia Amaral Turkman, Carlos Daniel Paulino, Peter Müller.

## Software

1. [Think Stats](http://greenteapress.com/thinkstats2/html/thinkstats2010.html) - A free book that demonstrates standard statistical calculations in Python.
1. [EMCEE Overview](https://arxiv.org/pdf/1202.3665.pdf)
 [EMCEE software documentation](https://emcee.readthedocs.io/en/stable/)

# General Policies

## Academic Integrity

Any instance of cheating or plagiarism is a violation of the Honor Code Pledge and will result in a score of zero on the exam or paper and referral to the Honor Committee. The website for the Office of Academic Integrity is https://oai.gmu.edu/.

## Disability

If you have a disability and need academic accommodations, please contact Disability Services. Their website is https://ds.gmu.edu/. All academic accommodations must be arranged through Disability Services.

## Diversity and Inclusion

We seek to create a learning environment that fosters respect for people across identities. We welcome and value individuals and their differences, including gender expression and identity, race, economic status, sex, sexuality, ethnicity, national origin, first language, religion, age, and ability. We encourage all members of the learning environment to engage with the material personally but to also be open to exploring and learning from experiences different than their own. Mason’s nondiscrimination policy is at https://universitypolicy.gmu.edu/policies/non-discrimination-policy/.

## Communication

If you have a question whose answer may be of interest to other students, please post it to Piazza and make it visible to other students. You can set the post so that you are anonymous. 

If you need to send communicate with me about something private, please send it to `rweigel@gmu.edu` from your MasonLive email address.

## University Resources

* Learning Services https://learningservices.gmu.edu/
* Student Support and Advocacy Center https://ssac.gmu.edu/
* Counseling and Psychological Services https://caps.gmu.edu/
