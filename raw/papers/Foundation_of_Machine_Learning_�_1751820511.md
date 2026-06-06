Foundations of Machine
learning - Lecture Notes

CS725 : Foundations of Machine learning - Lecture Notes
Ajay Nagesh

Contents
1 Basic notions and Version Space
1.1 ML : Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Structure of hypotheses space: Version Space . . . . . . . . . . . . . . . . . . . . . .
1.3 Exercise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.4 Version Space (cont.) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.5 Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4
4
5
7
8
9

2 Course Outline

10

3 Decision Trees
10
3.1 Exercise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.2 DTree Construction: splitting attribute . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3 Splitting attribute : Impurity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.4 Exercise: Illustration of impurity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4 Probability Primer
14
4.1 Basic Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.2 The three axioms of probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.3 Bayes’ Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.4 Independent events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.5 Probability Mass Function (pmf) and Probability Density Function(pdf) . . . . . . . 16
4.6 Expectation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.7 Exercise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
5 Decision Trees (continued)
19
5.1 An empirical observation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
5.2 Decision Tree: construction algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . 19
5.3 Pruning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
5.4 Exercise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
5.5 Splitting criterion modified only for pruning . . . . . . . . . . . . . . . . . . . . . . . 22
6 Probability Distributions
22
6.1 Bernoulli Random Variable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
6.2 Binomial Random Variable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
6.3 Central Limit Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

1

CONTENTS

6.4

Gaussian Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2

23

7 Hypothesis Testing
27
7.1 Basic ideas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
7.2 Example and some notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
7.3 Statistical hypothesis testing in decision trees . . . . . . . . . . . . . . . . . . . . . . 29
8 Estimation
31
8.1 Maximum Likelihood Estimation (MLE) . . . . . . . . . . . . . . . . . . . . . . . . . 33
9 Optimization
33
9.1 Optimization for multiple variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
9.2 Linear Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
9.3 KKT conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
9.4 Necessary and Sufficient Conditions : Summary . . . . . . . . . . . . . . . . . . . . . 44
9.5 Duality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
10 Naive Bayes Classifier
46
10.1 Problem formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
10.2 Estimating the Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
10.3 Conjugate prior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
10.4 Naive Bayes with Dirichlet Priors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
10.5 Naive Bayes with Gaussian Priors . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
10.6 Nature of Separating Surfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
10.7 Multivariate Gaussian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
11 Gaussian Discriminant Analysis
62
11.1 Nature of separating surface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
11.2 Curse of dimensionality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
12 Unsupervised Learning
66
12.1 Objective function (Likelihood) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
12.2 Expectation-Maximization Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . 68
13 Clustering
70
13.1 Similarity Measures for Clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
13.2 Objective Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
13.3 k-means Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
13.4 Variants of k-means . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
13.5 MDL principle and clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
13.6 Hierachical clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
13.7 Miscellaneous topics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
14 Association Rule Mining
79
14.1 A-priori Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
14.2 Association Rule Mining . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
14.3 Classification Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81

CONTENTS

3

15 Non parametric density estimation and classification
82
15.1 Histogram Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
15.2 K-Nearest Neighbour and Parzen Window Classifier . . . . . . . . . . . . . . . . . . 82
15.3 Kernel density estimators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
16 Discriminative Classification
86
16.1 Maximum Entropy models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
17 Graphical Models

89

18 Generalized Models for Classification
90
18.1 Generalized linear models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
18.2 Handling Multiclasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
18.3 Least Squares approach for classification . . . . . . . . . . . . . . . . . . . . . . . . . 92
19 Regression
94
19.1 Motivating Example : Curve Fitting . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
19.2 Linear regression and method of least squares error . . . . . . . . . . . . . . . . . . . 95
19.3 Regularised solution to regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
19.4 Linear Regression : Drawbacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
19.5 Possible solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
20 Perceptron Algorithm
105
20.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
20.2 Training algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
20.3 Issues with Perceptron . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
21 Support Vector Machines
108
21.1 Canonical SVM problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
21.2 SVM : Dual Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
21.3 Duality theory applied to KKT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
21.4 SVM dual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
21.5 Kernel Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
21.6 Requirements of Kernel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
21.7 Algorithms for solving the dual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
22 Support Vector Regression

119

23 Attribute Selection and Transformation

119

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 2: Introduction
Instructor: Ganesh Ramakrishnan

Date: 26/07/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

1

Basic notions and Version Space

1.1

ML : Definition

Definition (from Tom Mitchell’s book): A computer program is said to learn from experience E
w.r.t some set of tasks T and performance measure P, if its performance at T improves with E
as measured by P.
Consider the sample dataset iris.arff. Given a set of observations of Iris flowers (like sepal
length, width), our goal is to predict whether a given flower is Iris-Setosa or Iris-Versicor ...
Mapping the definition to the Iris flower-type prediction problem:
 E: Observations on Iris flowers (sepal length, width, ...)
 T: Identify the type of Iris flower
 P: Accuracy

Consider another dataset soybean.arff. The mapping is as follows:
 E: Observations on the soybean crop (date, plant-stand, ...)
 T: Given that the soybean is diseased, to predict the type of disease that it has.
 P: Accuracy

Consider any hypothesis h which is a function, h : x → class. For instance:
h1 (x) = stem-cancer

if x.date = october

Is this a good hypothesis ? How do we measure that ? One measure (P ) could be the following:
P (h1 ) =

#((x.date = october) AND (h(x) = stem-canker))
5
=
#(x.date = october)
90

Consider the following other hypotheses and their P values:
h2 (x) = stem-cancer
h3 (x) = stem-cancer

if

if x.plant stand = normal;

P (h2 ) =

20
354

((x.plant stand = normal) AND (x.precip = gt-norm));

4

P (h2 ) =

20
354

1

BASIC NOTIONS AND VERSION SPACE

5

Figure 1: Version Space

1.2

Structure of hypotheses space: Version Space

Let us forget about getting to “the best hypothesis” and consider the structure of the hypothesis
space. This space is also be termed as Version Space.
Formally defined as “Space of h(x) such that ∀x ∈ E, h(x) = class(x)”. Pictorially it can be
depicted as in figure 1:
A part of the version space for the soybean example is shown in figure 2.

Figure 2: Part of Version Space for Soybean example

Consider the cooked-up dataset shown is table 1. Our goal is to find a hypothesis for class C1 .
If our hypothesis language is only a conjunction of atomic statements (i.e. they are conjunctions
of stmts. of the form x.attr = value or x.attr =?), then the version space for this example is
empty. In otherwords, we cannot find a hypothesis that belongs to the hypothesis language that
we have defined, such that all the positive examples are covered and none of the negative examples
are covered. (However, note that if we decide to include negation (¬), then we can find a satisfying
hypothesis for class C1 : ¬(Y, N, ?) ⇒ C1 ).
Now consider the hypothesis h1 = (?, ?, N ) ⇒ C1 . What is P (h) ? If we consider that our
performance measure is defined as follows:
S
|{x|h(x) = cl(x) = C1 }
{x|h(x) 6= C1 & cl(x) 6= C1 }|
3
=
P =
|{x}|
4
In short, this performance measure counts all those instances of C1 that are correctly classified
by the hypothesis and all those instance that are not C1 and is not classified as C1 by the hypothesis.

1

BASIC NOTIONS AND VERSION SPACE

6

F1

F2

F3

Class

D1

Y

Y

N

C1

D2

N

N

N

C1

D3

Y

Y

Y

C1

D4

Y

N

Y

C2

Table 1: A toy dataset

Ideally, we are in the search for that hypothesis that maximizes P (h) i.e.
arg max P (h)
h∈H

Incremental building of version space
Consider the same dataset shown in table 1. As we see the examples one after another starting
from D1, the progressive construction of version spaces is shown in diagram 3.

Figure 3: Progressive construction of Version Spaces for table 1

We can observe from diagram 1, that the version space becomes empty after seeing D4. If we
expand our hypothesis language (for instance, to also include disjunctions of conjunctions), we can
construct version spaces that are not empty.

1

BASIC NOTIONS AND VERSION SPACE

7

In the lecture we saw three main type of extensions to the hypothesis language:
1. (Y ∧ Y ∧?) ∨ (N ∧ N ∧?) ⇒ C1 . This, in the class, was termed as lazy learner. This can also
be called conjunctive normal form (CNF) learner
2. (?∧? ∧ (N ∨ O) ⇒ C1 . (If, we change (D3,F3) to O)
3. (attribute1 = attribute2) ⇒ C1

Some Observations
1. Version space may be empty. Generally, we cannot always find one hypothesis that will explain
everything. So, as an approximation, we try to maximize P our performance measure.
2. Hypothesis language: There could be a bias in h. In our previous example, h1 only consisted
of a conjunction of atomic statements and we were avoiding disjunctions.
3. Active Learning: This is a learning technique where the machine prompts the user (an oracle
who can give the class label given the features) to label an unlabeled example. The goal
here is to gather as differentiating (diverse) an experience as possible. In a way, the machine
should pick those examples which challenge the existing hypothesis learnt by it.
For instance, if the machine has seen 2 examples : {Y, Y, Y } ⇒ C1 and {Y, N, N } ⇒ C1 , then
it should ask the user, {N, Y, Y } ⇒?.

1.3

Exercise

Construct version spaces for the 3 different hypothesis language extensions listed above along the
lines of diagram 3 for the same dataset (Table 1).

Further Reading
1. Machine Learning, Tom Mitchell, McGraw Hill, 1997.
mlbook.html). Chapters 1 and 2.

(http://www.cs.cmu.edu/~tom/

2. Datasets: http://storm.cis.fordham.edu/~gweiss/data-mining/datasets.html (iris.arff,
soybean.arff)

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 3: Bias, Course outline, Decision Trees
Instructor: Ganesh Ramakrishnan

Date: 29/07/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

Notation
A small change in notation to ensure conformity with the material to be covered in the future and
ease of understanding. Previously we had denoted hypothesis by h, features by x.f eature name
(where x was the example data) and class label by c1 , c2 , .... From here onwards, we will denote
features by φ(xi ), class label by y(xi ) and the hypothesis by f . So our data with its features will
be as shown in Table 2.
x1

φ(x1 )

φ(x2 )

...

...

y(x1 )

x2

...

...

...

...

...

...

...

...

...

..

...

..
..

...
...

xn

...

...

...

...

y(xn )

Table 2: Data Representation

Our objective is to maximize P (f ) and we search in the hypothesis space H for that hypothesis
f that maximizes the performance P . In otherwords,
arg max P (f )
f ∈H

1.4

Version Space (cont.)

In the previous lecture, we saw the following types(families) of f for the toy dataset in Table 1.
1. f : ∧i φi (x) = 1, then y(x) = c1 else c2
2. f : ∧i,j φi (x) = φj (x), then y(x) = c1 else c2
3. f : ∧i (φi (x) = a ∨ φj (x) = b), then y(x) = c1 else c2
4. f : ∨j (φi1 j (x) ∧ φi2 j (x)), then y(x) = c1 else c2
The version space for the fourth hypotheses language is as shown in Figure 4. Version space is
usually represented by a lattice (which is a partially ordered set with relations greatest lower bound
and least upper bound defined on every pair of elements).

8

1

BASIC NOTIONS AND VERSION SPACE

9

Figure 4: Version Space for Hypothesis language 4 (CNF)

1.5

Bias

Bias B is the assumptions we make about the target function f . Some of the effects of bias is as
follows:
1. Can help reduce version space (to the point of emptiness).
2. Can lead to better coverage of new examples.
Bias and Coverage
Given a larger version space, the chances of contradictions while classifying a new example will be
higher. Thus, while “more” examples will be covered in a larger version space, “fewer” examples
will be less ambiguously covered in the smaller version space. In general, smaller the version space
lesser is the ambiguity in coverage.
For just the first two rows of the example dataset (Table 1), the simple conjunction hypothesis
language gives a smaller version space than the CNF hypothesis language. Note that version space
is defined as the space of hypothesis which is consistent with all the training examples. Obviously,
we would like all (or atleast a majority of them) to be consistent with any new example as far as
possible.
But it can be proved that for any new example, exactly half the hypotheses in the CNF version
space will cover it and half will not cover. Now what is the point of such a coverage? This is in
contrast to the smaller version space where for most new examples, the ambiguity in coverage is
much less.
For instance: Consider a new tuple (N, Y, N ). In the smaller version space (Figure 3, 2nd subfigure)), we see that the new datapoint is covered by both the hypotheses in the version space (no

2

COURSE OUTLINE

10

ambiguity). However, in the larger version space (Figure 4), it is covered by 9 out of 13 hypotheses
and not covered by the remaining 4 (There is more ambiguity in this case).
This ambiguity can actually be captured through the concept of variance, which is what we
will look at in greater detail when we talk about the bias-variance dilemma (in our discussions on
probabilistic models).

2

Course Outline

Given bias B and the resulting version space from the bias (V.S(B, D)), the central question in
machine learning is which f to pick ? Depending on how we do this, there are a host of techniques.
Some of the classsification techniques that we cover in the course are as shown in Figure 5

Figure 5: Classification techniques to be covered in the course

3

Decision Trees

The bias in a decision tree is as shown in Figure 6
Some characteristics / considerations:
1. Each example will take a definite path. (There is no ambiguity)
2. Which φi to pick ?
For a binary classification problem, we have p(⊕|x) + p( |x) = 1. For the vote.arff example
169
268
(⊕ = republicans or = democrats), p(⊕|x) = 268+169
and p( |x) = 268+169
.

3

DECISION TREES

11

Figure 6: Decision Tree: Bias

We need to “Code up” the information to classify an example. Using information theory, we
get the following equation:
−p(⊕|x) log2 p(⊕|x) − p( |x) log2 p( |x) = Ep (x)
This is the amount of uncertainty associated (also known as entropy Ep (x)). What we are
interested is the relative chanage in entropy given a feature’s value which is EPpf (x) as shown in
Figure 7

Figure 7: Decision Tree: Information Gain (EPpf (x))
In otherwords, use that attribute that has maximum decrease in uncertainty. This measure is
also called Information Gain.

3.1

Exercise

Is the version space in Figure 4 complete ? If not, complete it.

Further Reading
1. Lattice: http://www.cse.iitb.ac.in/~cs717/notes/classNotes/completeNotes.pdf (Use
the same username and passwd). Pages 6-11.
2. Decision Trees (applets with illustrative examples): http://webdocs.cs.ualberta.ca/~aixplore/
learning/DecisionTrees/

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 4: Decision Trees, Probability primer
Instructor: Ganesh Ramakrishnan

Date: 02/08/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

Hypothesis space
It is a disjunction of conjunctions. With respect to the spect train.arff dataset, we observed
the decision tree learnt as shown in Figure 8. We can serialize the decision tree as

Figure 8: Decision Tree: spect train.arff



3.2


 
(F18 = 0) ∧ (F21 = 0) ⇒ class 0 ∨ (F18 = 0) ∧ (F21 = 1) ∧ (OD = 0)) ⇒ class 0 ...

DTree Construction: splitting attribute

Mapping to Probability theory constructs
Refer to Section 4 for the corresponding definitions and explanation.
 S = {⊕, }
 E = {{⊕, }, {⊕}, { }, {}}
 Random variable mapping : X({⊕}) = 1, X({ }) = 0, X({⊕, }) = 2, X({}) = 3
 With respect to the spect train example file:
54
P r({⊕}) = P r(X = 1) = 26
P r({ }) = P (X = 0) = 80
80

12

3

DECISION TREES

13

 To confirm, P r({⊕, }) = P r({⊕}) + P r({ }) = 1
 Are {⊕} and { } independent events ?
No. ∵ P r({⊕ ∩ }) = P r({}) = 0 6= P r({⊕}) • P r({ })
(Intuition: If an instance has ⊕ label, then it cannot have a

label.)

New event and sample space
Consider the values of F18 and class label (first and second attribute is the following):
0

 S = {(0, 0), (0, 1), (1, 0), (1, 1)}
n
o
0
0
 E = 2S = {(0, 0)}, {(1, 1)}, · · · , {(0, 0), (0, 1), (1, 0), (1, 1)}
21
5
3
51
, P r({(0, 1)}) = 80
, P r({(1, 1)}) = 80
, P r({(1, 0)}) = 80
 P r({(0, 0)}) = 80
(w.r.t spect train.arff; here the 1st arg. is F18 and 2nd arg. is class label)

 P r({(0, 1) ∪ (0, 0)}) = P r({(0, ?)} = 51+21
= 72
80
80
 Use of Bayes Theorem:


00
Let E = {(0, 0)}, {(0, 1)}, {(1, 0)}, {(1, 1)}, {} and
Let Bi = {(1, 0)} and A = {(1, ?)} = {(1, 1) ∪ (1, 0)}
P r({(1,0)})
3
i ∩A)
= P r({(1,0)})+P
P r(Bi |A) = P r(B
P r(A)
r({(1,1)}) = 5+3 (Marginalization)

 (#bits needed to convey class label as ⊕ ) ∝ ( − log2 P r(⊕) ),
(#bits needed to convey class label as ) ∝ ( − log2 P r( ) )
 Using the concept of Expectation E:
E[log2 (•)] = −P r(⊕) • log2 P r(⊕) − P r( ) • log2 P r( )
This is also called Entropy. It represents the uncertainty asssociated with the encoding.

3.3

Splitting attribute : Impurity

There are various measures used for the selection of the splitting attribute in a decision tree. They
all have the same goal of maximizing the reduction in a quantity called Impurity (Imp).(One of the
measures of impurity is Entropy) Impurity represents the relative change in amount of bits needed
to code up the information before and after a split happens in the decision tree. The idea being to
choose only those split points which require the least amount of information to be coded up as a
decision tree. The criterion for splitting is given by the following expression:
arg max Imp(D) − Imp(D1 , D2 )
φj

Imp(D1 , D2 ) is given by:
Imp(D1 , D2 ) =

|D1 |
|D2 |
Imp(D1 ) +
Imp(D2 )
|D|
|D|

where, D1 and D2 are the subsets of data resulted from the split. The different measures of entropy
are as shown in Table 3:

4

PROBABILITY PRIMER

14

Name

Imp (D)
P

Gini Index

− Ci P r(Ci ) • log(P r(Ci ))
P
Ci P r(Ci )(1 − P r(Ci ))

Min Prob. Error

arg min(1 − P r(Ci ))

Entropy

Table 3: Decision Tree: Impurity measurues

3.4

Exercise: Illustration of impurity

Consider the decision tree shown in Figure 9. Using entropy as measure, calculate the initial
impurity and the impurity after the split.

Figure 9: Impurity : before and after split

4

Probability Primer

A review of some basics of probability theory.

4.1

Basic Definitions

Definition 4.1. Sample space (S) : A sample space is defined as a set of all possible outcomes of an
experiment. Example of an experiment would be a coin pair toss. In this case S = {HH, HT, TH, TT}.
Definition 4.2. Event (E) : An event is defined as any subset of the sample space. Total number
of distinct events possible is 2S , where S is the number of elements in the sample space. For a coin
pair toss experiment some examples of events could be

4

PROBABILITY PRIMER

15

for at least one head, E = {HH, HT }
for all tails, E = {T T }
for either a head or a tail or both, E = {HH, HT, T H, T T }
Definition 4.3. Random variable (X) : A random variable is a mapping (or function) from set of
events to a set of real numbers. Continuous random variable is defined thus
X : 2S → R
On the other hand a discrete random variable maps events to a countable set (e.g. discrete real
numbers)
X : 2S → Discrete R

4.2

The three axioms of probability

Probability P r is a number corresponding to events . It satisfies the following three axioms,
1. For every event E, P r(E) ∈ [0, 1]
2. P r(S) = 1 where, S is the sample space. (Equivalently, P (∅) = 0)
3. If E1 , E2, . . . , En is a set of pairwise disjoint events, then
P r(

n
[
i=1

4.3

Ei ) =

n
X

P r(Ei )

i=1

Bayes’ Theorem

Let B1 , B2 , ..., Bn be a set of mutually exclusive events that together form the sample space S. Let
A be any event from the same sample space, such that P (A) > 0. Then,
P r(Bi ∩ A)
P r(B1 ∩ A) + P r(B2 ∩ A) + · · · + P r(Bn ∩ A)
Using the relation P (Bi ∩ A) = P (Bi ) · P (A/Bi )
P r(Bi /A) =

P r(Bi ) · P r(A/Bi )
P r(Bi /A) = Pn
j=1 P r(Bj ) · P r(A/Bj )

4.4

(1)

(2)

Independent events

Two events E1 and E2 are called independent iff their probabilities satisfy
P (E1 E2 ) = P (E1 ) · P (E2 )

(3)

where P (E1 E2 )meansP (E1 ∩ E2 )
In general, events belonging to a set are called as mutually independent iff, for every finite
subset, E1 , · · · , En , of this set
n
n
\
Y
P r( Ei ) =
P r(Ei )
(4)
i=1

i=1

4

PROBABILITY PRIMER

4.5

16

Probability Mass Function (pmf ) and Probability Density Function(pdf )

Definition 4.4. pmf :- It is a function that gives the probability that a discrete random variable is
exactly equal to some value(Src: wiki).
pX (a) = P r(X = a)
Definition 4.5. Cumulative distribution function(Discrete case) : F (a) = P r(X <= a)
Definition 4.6. pdf :- A probability density function of a continuous random variable is a function that describes the relative likelihood for this random variable to occur at a given point in the
observation space(Src: wiki).
Z
P r(X ∈ D) =
p(x)dx where D is set of reals and p(x) is density function.
D

Definition 4.7. Cumulative distribution function(Continuous case):
Z a
F (a) = P r(X <= a) =
p(x)dx
−∞

f (a) =

dF (x)
|x=a
dx

Joint distribution function
If p(x,y) is a joint pdf i.e. for continuous case:
Rb Ra
F (a, b) = P r(X <= a, Y <= b) = −∞ −∞ p(x, y)dxdy
2

F (x,y)
|a,b
p(a, b) = ∂ ∂x∂y

For discrete
P case i.e.
P p(x,y) is a joint pmf:
F (a, b) = x<=a y<=b p(x, y)
Marginalization
Marginal probability is then the unconditional probability P(A) of the event A; that is, the probability of A, regardless of whether event B did or did not occur. If B can be thought of as the event
of a random variable X having a given outcome, the marginal probability of A can be obtained
by summing (or integrating, more generally) the joint probabilities over all outcomes for X. For
example, if there are
T two possible
T outcomes for X with corresponding events B and B’, this means
that P (A) = P (A B) + P (A B 0 ). This is called marginalization.
Discrete case:P
P (X = a) = y p(a, y)
Continuous
R ∞ case:
Px (a) = −∞ p(a, y)dy

4

PROBABILITY PRIMER

4.6

17

Expectation

Discrete case: Expectation is equivalent to probability weighted sums of possible values.
E(X) = Σi xi P r(xi ) where X is a random variable
Continuous case: Expectation is equivalent to probability density weighted integral of possible
values. R
∞
E(X) = −∞ xp(x)dx
If the random variable is a function of x, then Discrete case:
E(f (X)) = Σi f (xi )P r(xi ) where X is a random variable
Continuous
R ∞case:
E(X) = −∞ f (x)p(x)dx

Properties of E(x)
E[X + Y ] = E[X] + E[Y ]
For any constant c and any random variable X
E[(X − c)2 ] ≥ E[(X − µ)2 ]
where µ = E[X]
E[cX] = cE[X]

4.7

Exercise

Example 1. A lab test is 99% effective in detecting a disease when in fact it is present. However,
the test also yields a false positive for 0.5% of the healthy patients tested. If 1% of the population
has that disease, then what is the probability that a person has the disease given that his/her test
is positive?
Soln. Let, H be the event that a tested person is actually healthy.
D be the event that a tested person does have the disease.
T be the event that the test comes out positive for a person.
We want to find out P r(D/T )
H and D are disjoint events. Together they form the sample space.
Using Bayes’ theorem,
P (D/T ) =

P r(D) · P r(T /D)
P r(D) · P r(T /D) + P r(H) · P r(T /H)

Now, Pr(D) = 0.01 (Given)
Since Pr(D)+Pr(H)=1, Pr(H)=0.99
The lab test is 99% effective when the disease is present. Hence, Pr(T/D)=0.99

(5)

4

PROBABILITY PRIMER

18

There is 0.5% chance that the test will give false positive for a healthy person. Hence, Pr(T/H)=0.005
Plugging these values in equation (5) we get,
0.01 ∗ 0.99
0.01 ∗ 0.99 + 0.99 ∗ 0.005
2
=
3

P r(D/T ) =

What does this mean? It means that there is 66.66% chance that a person with positive test
results is actually having the disease. For a test to be good we would have expected higher certainty.
So, despite the fact that the test is 99% effective for a person actually having the disease, the false
positives reduce the overall usefulness of the test.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 5: Decision Trees: Construction, Other considerations
Instructor: Ganesh Ramakrishnan

Date: 06/08/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

5

Decision Trees (continued)

The splitting attribute is selected greedily as mentioned in the last class and is based on maximum
reduction in impurity. The expression is given by:
arg max



X

Imp(D) −

V (φi ),φi

v∈V (φi )


|Dv |
Imp(Dv )
|D|

The second term in the above expression is the expected new impurity. V is a function which
returns the split values given an attribute φi . So V (φi ) can be varied for any φi . It could have
many values or a range of values. A example of V (φi ) is V (φi ) = {1, 3, 5} which translates to the
following split points φi < 1, 1 ≤ φi < 3, 3 ≤ φi < 5, φi ≥ 5

5.1

An empirical observation

Since smaller range if attribute valuesin each split in Vi tends to lead to more skewed class distribution in that split, larger |V (φi )| generally yields larger reduction in impurity. This makes the
algorithm to choose more skewed and complex trees and leads to the problem of overfitting, if
not fixed. In overfitting, the system learns a model which is specific to the training collection and
does not generalize well on unseen data.
Need to address this empirical observation
This can be done by the maximization of the following expression:
!
|Dv |
v∈V (φi ) |D| Imp(Dv )
P
v|
− v∈V (φi ) |D
|D| log(Dv )
P

Imp(D) −

The second term in the above expression is called 4Imp(D). The intuition for using this term
is that, if the skew is more, the lower will be the denominator and is better at countering lowered
impurity. In otherwords, it prefers a less skewed tree as shown in Figure 10.

5.2

Decision Tree: construction algorithm

The algorithm goes on until all the data points at the leaf are of the one class and does not
terminate if such a condition is violated. But the two stopping criterion added to the algorithm
make it terminate even if such a condition does not occur.

19

5

DECISION TREES (CONTINUED)

20

Figure 10: Skewness and empirical observation

Algorithm 1 T = dtree (D, φi , V )
if φ = empty then
return a tree with only one branch cj , where cj is the majority class in D {Stopping criterion}
end if
if all instances in D have label = ci then
return a tree with only one branch ci {Stopping criterion}
end if

φj = arg maxV (φi ),φi 4Imp(D) ∀v ∈ V (φi )
Tv = dtree(Dv , φ − φi , V )
return a tree rooted at φi and having all the Tv branches

5.3

Pruning

Simpler trees are preferred over their complex counterparts for the following reasons:
1. They are faster to execute
2. They perform better on unseen data. In otherwords, they “generalize well”. For instance, a
simpler tree learnt in the class had lower accuracy on the train set but higher accuracy on
the unseen test set.
Trees can get unnecessarily deep and complex. So they are various strategies/heuristics to
decrease the complexity of the tree learnt. Some of the options are as follows:
1. Early termination. Stop if 4Imp(D) < θ, where θ is some threshold.
2. Majority class ≥ α%, for some value of α
3. Pruning: The idea is to build complex trees and prune them. This is a good option, since
the construction procedure can be greedy and does not have to look ahead. Some concepts
of Hypothesis testing is used to achieve this. (For instance, χ2 -test).
4. Use an objective function like


maxφi 4Imp(D, i) − Complexity(tree)
The complexity is characterised by the description length principle (MDL)

5

DECISION TREES (CONTINUED)

5.4

21

Exercise

Become familiar with the chebyshev’s inequality, law of large numbers, central limit theorem and
some concepts from Linear Algebra like vector spaces.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 6: Probability distributions, Hypothesis Testing
Instructor: Ganesh Ramakrishnan

Date: 09/08/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

5.5

Splitting criterion modified only for pruning

1. Use only part of the data for pruning
2. Stop when 4Imp < θ (Problem: How to decide on θ ?)
3. Minimum Description Length (MDL) principle. (4Imp − complexity(tree) < θ)
4. Significance tests (or hypothesis testing). Can be considered as the statistical version of 2.

6

Probability Distributions

6.1

Bernoulli Random Variable

Bernoulli random variable is a discrete random variable taking values 0,1
Say, P r[Xi = 0] = 1 − q where q[0, 1]
Then P r[Xi = 1] = q
E[X] = (1 − q) ∗ 0 + q ∗ 1 = q
V ar[X] = q − q 2 = q(1 − q)

6.2

Binomial Random Variable

A binomial distribution is the distribution of n-times repeated bernoulli trials. A binomial random
variable is discrete variable where the distribution is of number of 1’s in a series of n experiments
with {0,1} value, with the probability that the outcome of a particular experiment is 1 being q.

P r[X = k] = nk q k (1 − q)n−k
E[X] = Σi E[Yi ] where Yi is a bernoulli random variable
E[X] = nq
V ar[X] = Σi V ar[Yi ] (since Yi ’s are independent)
V ar[X] = nq(1 − q)
An example of Binomial distribution is the distribution of number of heads when a coin is tossed
n times.

22

6

PROBABILITY DISTRIBUTIONS

6.3

23

Central Limit Theorem

If X1 , X2 , .., Xm is a sequence of i.i.d. random variables each having mean µ and variance σ 2
Then for large m, X1 + X2 + .. + Xm is approximately normally distributed with mean mµ and
variance mσ 2
If X ∼ N (µ, σ 2 )
1
e
Then P [x] = σ √
2
2π

−(x−µ)2
2σ 2

It can be shown by CLT
n −nµ
√
∼ N (0, 1)
 X1 +X2 σ+..+X
2 n
2

 Sample Mean: µ̂ ∼ N (µ, σm )

6.4

Gaussian Distribution

Information Theory
Let us denote I(X=x) as the measure of information conveyed in knowing value of X=x.

Figure 11: Figure showing curve where Information is not distributed all along.

Figure 12: Figure showing curve where Information is distributed.

Question: Consider the two graphs above. Say you know probability function p(x). When is
knowing value of X more useful (that is, carries more information)?

6

PROBABILITY DISTRIBUTIONS

24

Ans: It is more useful in the case(2), because more information is conveyed in Figure 11 than in
Figure 12.
Expectation for I(X=x):
 If X and Y are independant random variables from the same distribution.

I(X = x, Y = x) = I(X = x) + I(Y = y)

(6)

One way of expressing the above is:
I(P (x)P (y)) = I(P (x)) + I(P (y))

(7)

where P(x),P(y) are the probability functions respectively.
 If p(x)>P (y) , then

I(p(x))<I(p(y))
There is only one function which satisfies the above two properties.
I(p(x)) = −c log(p(x))
 The Entropy in the case of discrete random variable can be defined as:
X
EP [I(p(x))] =
−c log[p(x)]

(8)

(9)

x

 In the case of continuous random variable it is,
Z
EP [I(p(x))] =
−c log[p(x)]

(10)

x

The constant ’C’ in the above two equations is traditionally 1.
Observations:
 For a discrete random variable (with countable domain), the information is maximum for the
uniform distribution.
 For Continuous random variable ( with finite mean and finite variance), the information is
maximum for the Gaussian Distribution.

Finding argmax Ep in an infinite domain, subject to
p

R
and

xp(x)dx = µ

6

PROBABILITY DISTRIBUTIONS
R

25
(x − µ)2 p(x)dx = σ 2

The solution would be
−(x−µ)2
2

2σ
p(x) = e σ√
2π

Properties of gaussian univariate distribution
 If X ∼ N (µ, σ 2 )

p(x) = σ√12π e

−(x−µ)2
2σ 2

where − ∞ < x < ∞

then w1 X + w0 ∼ N (w1 µ + w0 , w12 σ 2 )
(can prove this using moment generating function)
Φ(N (µ, σ 2 )) = EN (µ,σ2 ) [etx ] = eµt+

(σt)2
2

Recall
E(X) = dφ(p)
dt
2

φ(p)
var(x) = d dt
2
2

2
2 2
EN (µ,σ2 ) [et(w1 x+w0 ) ] = (w1 µt + w0 t + (σt)
2 × w1 ) ∼ N (w1 µ + w0 , w1 σ )

 Sum of i.i.d X1 , X2 , ......, Xn ∼ N (µ, σ 2 ) is also normal (gaussian)

X1 + X2 + ...... + Xn ∼ N (nµ, nσ 2 )
In genaral if Xi ∼ N (µi , σi2 ) =⇒

Pn

i=1 Xi ∼ N (

P

µi ,

P

σi2 )

 Corollary from (1) If X ∼ N (µ, σ 2 )

∼ N (0, 1) (Useful in setting interval estimate)
z = X−µ
σ
(take w1 = σ1 and w0 = σµ )
Note:- If X1 , X2 , ....Xm ∼ N (0, 1)
P 2
2
1. y =
i Xi ∼ χm . That is, y follows the chi-square distribution with m-degrees of
freedom.
2. y = Xz 2 ∼ tn . (where z ∼ N (0, 1))). That is, y follows the students-t distribution.
Xi

6

PROBABILITY DISTRIBUTIONS

26

Figure 6.4 : Figure showing the nature of the (chi − square) distribution with 5 degrees of
freedom
 Maximum Likelihood estimate for µ and σ 2

Given

X1 , X2 , ....Xm ..... Random Sample.

µ̂M LE = argmaxµ

Qm

√1
i=1 [ σ 2π e

= argmaxµ σ√12π e
µ̂M LE =

Pm

i=1 Xi

m

−

P

−(Xi −µ)2
2σ 2

]

(Xi −µ)2
2σ 2

= sample mean

 With out relaying on central limit theorem Properties (2) and (1)

i.e. Sum of i.i.d’s X1 , X2 , ......, Xn ∼ N (µ, σ 2 )
2

µ̂M LE = N (µ, σm )
Similarly
2
σ̂M
LE =

Pm

2
i=1 (Xi −µ̂M LE )

m

is χ2 distrbution

∼ χ2m

 Coming up with conjugate prior of N (µ, σ 2 )

Case (1) σ 2 is fixed and prior on µ
⇒ µ ∼ N (µ0 , σ02 )

7

HYPOTHESIS TESTING

27

Case (2) µ is fixed and σ 2 has prior
⇒ σ2 ∼ Γ
case (3) if µ and σ 2 both having the prior
⇒ (µ, σ 2 ) ∼ Normal gamma distribution ∼ Students-t distribution

7

Hypothesis Testing

7.1

Basic ideas

Given a random sample for a random variable X = (X1 , X2 , . . . Xn ), we define a function S :
(X1 , X2 , . . . Xn ) → R. This function is called statistic (or sample statistic). 
P

For instance, the sample mean is nXi and sample variance is
Given X and 2 hypotheses H0 and H1 defined by:

P

i

P

X

Xi − n i
n−1

2

H0 : (X1 , X2 , . . . Xn ) ∈ C
H1 : (X1 , X2 , . . . Xn ) ∈
/C
where, C is some tolerance limit also called the confidence region. It is generally defined in
terms of some statistic.
The following types of errors are defined as a consequence of the above hypotheses. They are:
 Type I error: Probability of rejecting H0 , if H0 was actually true.
This is given by: P rH0 ({X1 , X2 , . . . Xn } ∈
/ C)
 Type II error: Probability of accepting (or not-rejecting) H0 , if H0 was actually false.
This is given by: P rH0 ({X1 , X2 , . . . Xn } ∈ C)

Given a significance level α (some bound on the Type I error), we want to find a C such that,
P rH0 ({X1 , X2 , . . . Xn } ∈
/ C) ≤ α

7.2

Example and some notation

Given a random sample {X1 , X2 , . . . Xn } and each taking on one of k different categorical values. We
denote P r(Xi = j) by pj , which is the probability of random variable Xi taking the categorical value
j. This distribution is called categorical distribution (also called as multinomial distribution - http:
//en.wikipedia.org/wiki/Categorical_distribution). This can be viewed as a multivariate
bernoulli distribution.
Suppose we define a statistic: Y1 , Y2 , . . . Yk such that,
Yi = # of Xj ’s that took the value i
There are 2 types of representations possible to enocde such random variables.

7

HYPOTHESIS TESTING

28

Dirac-delta function
Here we represent the statistic Yi as
Yi =

n
X

δ(Xj , i)

j=1

where δ(Xj , i) = 1 when Xj = ith attribute and 0 otherwise.
For example, if 5 of (X1 , . . . Xn ) have value = 3, then Y3 = 5.
Random vectors
In this representation, X is represented by random vector xk as follows:

x1 1
. 
M = .. 

xk 0

0
..
.

...

0

...

0

1






Here Xj ’s are the vectors and the statistic Yi is given by:
n
X
Xj )[i]
Yi = (
j=1

where [i] is the ith element of the vector obtained by summing individual random vectors.
A goodness of fit test
Let H0 the hypothesis be defined as the distance between the sample and expected average is within
some tolerance. if µi be the probability of Xj = i i.e. µi = pi . Then, expectation E(Yi ) = nµi and
H0 is mathematically derived as :
H0 : t =

k 
X
(Yi − nµi )2 
i=1

nµi

≤c

Here, t is called the test statistic. Alternatively,
Pr

!
(Yi − nµi )2
≥c ≤α
nµi
i=1

k
X

Given α, we need to compute c. Assuming large values
of n, the above
will be a
"
! summation
#
Pk (Yi −nµi )2
chi-square distribution with n − 1 degrees of freedom.
∼ χ2n−1 . There exits
i=1
nµi
a table for determining c given the value of α.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 7: Hypothesis testing and splitting criterion in DTrees
Instructor: Ganesh Ramakrishnan

Date: 12/08/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

7.3

Statistical hypothesis testing in decision trees

Previously, we discussed the problem of complex decision trees and the need to obtain simpler trees
by pruning. One important question to answer while constructing a simpler decision tree is Do
we have to split a node (using some attribute) or not ? Consider the situation in Figure 13. The
numbers n1 , n2 etc. indicate the number of tuples of the particular type.

Figure 13: Splitting criterion

If the ratio of the separation of tuples remains the same (or is similar) to that before the split,
then we might not gain much by splitting that node. To quantify this idea, we use the concept of
significance testing. The idea is to compare 2 probability distributions.
Let us consider a 2-class classification problem. If p be the probability of taking the left branch,
then the probablity of taking the right branch is 1 − p. Then we obtain the following:
n11 = pn1
n21 = pn2
n12 = (1 − p)n1
n22 = (1 − p)n2
Consider the original ratio (also called reference distribution) of positive to total no. of tuples.
If the same ratio is obtained after the split, we will not be interested in such splits. i.e.,
n1
n11
=
n1 + n2
n11 + n21
29

7

HYPOTHESIS TESTING

or in general

30

nj1
nj
=
n1 + n2
n1i + n2i

∀j no. of classes & i = 1, 2

Since, these splits only add to the complexity of the tree and does not convey any meaningful
information not already present. Suppose we are interested not only in equal distribution but also
approximately equal distributions i.e.,
n11
n1
≈
n1 + n2
n11 + n21
The idea is to compare two probability distributions. It is here that the concept of hypothesis
testing is used.
1
The ratio n1n+n
is called the reference distribution. In general, it is:
2
nj
p(cj ) = µj = P
i ni

for a given class j (pre-splitting distribution)

Hypothesis testing: problem 1
Let X1 , . . . Xn be i.i.d random samples. For our example, class labels of instances that have gone
into the left branch. The representation of these random variables can be any of the
Pn 2 types
discussed in the last class. As per the random vector representation,
statistic
is
Y
=
j
i=1 Xi [j].
Pn
As per the dirac-delta representation, the statistic is Yj =
i=1 δ(Xi , j). The statistic for the
example, # of instances in the left branch that have class j.
The hypotheses:
H0 :

X1 , . . . , Xn ∈ C

H1 :

X1 , . . . , Xn ∈
/C

The distribution of samples in the left branch is same as before splitting i.e. µ1 , . . . µk .
Given a random sample, we need to test our hypothesis i.e., given an α ∈ [0, 1], we want to
determine a C such that
P rH0 ({X1 , . . . Xn } ∈
/ C) ≤ α

Type I error

Given an α ∈ [0, 1], probability that we decide that the pre-distribution and the left-branch
distribution are different, when in fact they are similar, is less than or eqaul to α.
[Currently we are not very much interested in the Type II error, i.e. P rH1 ({X1 , . . . Xn } ∈ C)].
Here, C is the set of all possible “interesting” random samples. Also,
0

P rH0 ({X1 , . . . Xn } ∈
/ C ) ≤ P rH0 ({X1 , . . . Xn } ∈
/ C)

0

∀C ⊇ C

We are interested in the “smallest” / “tightest” C. This is called the critical region Cα . Consequently,
P rH0 ({X1 , . . . Xn } ∈
/ Cα ) = α
1 text written in red refers to the decision tree problem

8

ESTIMATION

31

Goodness-of-fit test for DTrees
We are interested in the hypothesis H0 where new-distribution = old-distribution(µ1 , . . . µj ).
EH0 [Yj ] =
=

n
X
i=1
n
X

EH0 [δ(Xi , j)]
µj ∗ 1 + (1 − µj ) ∗ 0

i=1

= nµj

(
C=

(X1 , . . . Xn )

0

i=1

(
=

(X1 , . . . Xn )

)

k
X
(Yj − EH (Yj ))2

k
X
(Yj − nµj )2
i=1

≤c

EH0 (Yj )
nµj

where c is some constant

)
≤c

As we have seen before, the above expression ∼ χ2k−1 . We then use the chi-square tables to find
c given the value of α.
Heuristic used for DTree construction
Pk (Y −nµ )2
 Compute i=1 j nµj j ∼ ts ∀ splits, where ts is the test statistic.
 Stop building the tree, if for a given α,

ts ≤ cα

∀ splits

 Compute cα such that P rχ2k−1 (x ≥ cα ) = α

8

Estimation

In estimation, we try to determine the probability values (till now we used to consider the ratio as
the probability). Essentially, our µj should actually denoted by µ
cj , since it is an estimate of the
actual probability µj (which we do not know).
The question posed in estimation is How to determine µ
cj ?
If {X1 , . . . Xn } are the class labels from which we want to estimate µ, then:
 
µ
c1
"
#
n Y
k
k
 
Y

X
 .. 
δ(Xi ,j)
s.t.
µi = 1
=
arg
max
P
r
µ
 . 
j
 
µ1 ,...,µk
i=1
i=1 j=1
µ
ck

8

ESTIMATION

32

This is also known as the maximum likelihood estimator (MLE) for the multivariate bernoulli
random variable. For k = 2,
= arg max
µ1 ,µ2

n
hY

δ(Xi ,1) δ(Xi ,2)
µ2

µ1

i

i=1

h P

i
P
δ(Xi ,1)
δ(Xi ,2)
1 − µ1 i
= arg max µ1 i
µ1

Further Reading
Read section 4.1.3 from the convex optimization notes
(http://www.cse.iitb.ac.in/~cs725/notes/classNotes/BasicsOfConvexOptimization.pdf )

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 8: Maximum Likelihood Estimation, Optimization Basics
Instructor: Ganesh Ramakrishnan

Date: 16/08/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

8.1

Maximum Likelihood Estimation (MLE)

Continuing from the prvious lecture, Let the random sample X be as follows
Random Sample (X) ∼ (X1 , . . . Xi . . . Xn )
where each random variable Xi takes on of k values from V1 . . . Vk
The maximux likelihood objective function will be as follows:
µ
bM L = arg max
µ1 ...µk

k X
n
X

δ(Xi , Vi ) log2 µj

j=1 i=1

such that,
X

µi = 1

;

0 ≤ µi ≤ 1

, for i = 1 . . . k

i

For k = 2 (i.e. we have µ2 = 1 − µ),
" n
#
X
 n

X
µ
bM L = arg max
δ(Xi , V1 ) log2 µ
δ(Xi , V2 ) log2 (1 − µ)
µ

i=1

i=1

such that, µ ∈ [0, 1]
The expression in between [ ] is called the objective function f , which need to be optimized
(maximised in this case). This particular form of the objective function is called the log-likelihood
function. The interval from which the values of µ can come from is called the domain D. In this
case it is a closed and bounded interval. To find the optimized value we will use the principles from
Optimization theory.

9

Optimization

Refer to the optimization theory notes (http://www.cse.iitb.ac.in/~cs725/notes/classNotes/
BasicsOfConvexOptimization.pdf). All references to sections, theorems will be with respect to
these notes. It will be denoted for instance as CoOpt,4.1.1.
For some basic definitions of optimization, see sections CoOpt,4.1.1 and CoOpt,4.1.2. To find
the maximum minimum values of an objective function, see section CoOpt,4.1.3 from Theorem 38
to Theorem 56. A set of systematic procedures to find optimal value is listed in Procedures 1, 2, 3
and 4 (CoOpt, pages 10, 16, 17 ).

33

9

OPTIMIZATION

34
0

For our optimization problem, the optimum value occurs when f (b
µM L ) = 0, which implies
Pn
Pn
δ(Xi , V1 )
δ(Xi , V2 )
⇒ i=1
− i=1
=0
µ
bM L
(1 − µ
bM L )
Pn
i , V1 )
i=1 δ(X
P
=µ
bM L
⇒ Pn
n
δ(X
,
V
)
+
i
1
i=1
i=1 δ(Xi , V2 )
So, necessary condition for local extreme value is
Pn
δ(Xi , V1 )
µ
bM L = i=1
n
In this case, this is the only possible value. However, there a couple of issues that needs to be
sorted out.
 Is it an extreme value value at all ? If so, is it local or a global extreme value ?
 Is it a maximum or a minimum value ?

The theorems listed above will give the necessary and sufficient conditions for maximum value
of the objective function f is as follows:
 Necessary Conditions
0

1. f = 0 at µ
bM L
0
2. f ≥ 0 before µ
bM L
0
3. f ≤ 0 after µ
bM L
 Sufficient Conditions
0

1. f = 0 at µ
bM L
0
2. f > 0 before µ
bM L
0
3. f < 0 after µ
bM L
We would like our log-likelihood function to be strictly concave function in [0, 1].
Using CoOpt, page 17, Procedure 4, we can narrow down on the possible values (where the
function attains maximum value) as
)
(
Pn
i=1 δ(Xi , V1
µ
bM L ∈ 0, 1,
n
However, f (0) = −∞, f (1) = −∞. From this we can conclude, it is indeed the case that,
Pn
i=1 δ(Xi , V1 )
µ
bM L is
n
We can come to same conclusion through the another path, that of CoOpt, Theorem 55. The
reasoning is as follows. Let the log-likelihood objective function be denoted by LL(µ)

Pn
−
00
i=1 δ(Xi , V1 ) 


LL (µ) =

µ2

< 0 , µ ∈ [0, 1]
Pn

−
i=1 δ(Xi , V2 ) 

=

(1 − µ)2

9

OPTIMIZATION

35
00

So, minimum value is at 0 or 1, since LL (µ) < 0,
00

∀µ ∈ [0, 1], which implies that

if LL (µ) = 0, for µ ∈ [0, 1] then µ
b is argmax LL
P
The more general LL objective function with the constraints i µi = 1, 0 ≤ µi ≤ 1, for i =
1 . . . k geometrically forms what is known as a simplex. (http://en.wikipedia.org/wiki/Simplex)

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 9: Optimization Basics, Linear Algebra
Instructor: Ganesh Ramakrishnan

Date: 19/08/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

9.1

Optimization for multiple variables
arg max LL(µ1 . . . µk |x1 . . . xn ) = arg max
µ1 ...µk

µ1 ...µk

= arg max
µ1 ...µk

such that, 0 ≤ µi ≤ 1 and

n X
k
X

δ(Xi , Vj )logµj

i=1 j=1
k
X

nj logµj , where nj =

j=1

m
X

δ(Xi , Vj )

j=1

P

i µi = 1

Directional derivative, Level curves, Gradient
The notion of directional derivative (D), can be obtianed from CoOpt, Section 4.1.4 and that of
level curves from CoOpt, Figure 4.12 and the associated explanation. Briefly, for a function f (x̄),
defined on domain D, is given by
Level Curve (C) = {x̄ | x̄ ∈ D, f (x̄) = c}
The level curves applet can be found at http://www.slu.edu/classes/maymk/banchoff/LevelCurve.
html.
Let us consider the simple case of 2-dimensions, and say n1 = 10 and n2 = 15, and k = 2, if
LL(µ1 , µ2 ) = c, then
n1 loge µ1 + n2 loge µ2 = c
⇒ µ2 = e

c−n1 loge µ1
n2

Directional derivative along the standard axis for the sample objective function is
D[1 0](LL)= nµ1
1

D[0 1](LL)= nµ2
2

By, CoOpt, Theorem 57,
D[ √1

2

1
√
]
2

1 n1
1 n2
(LL(µ1 , µ2 )) = √
+√
2 µ1
2 µ2

Gradient ∇ is given as
36

9

OPTIMIZATION

37









n1
µ1
∇LL =  ∂LL  =  n2 
∂µ2
µ2
∂LL
∂µ1

In general for arbitrary k, (∇LL is in n-dim space)
 ∂LL   n 
1

∂µ

µ

∂LL
∂µk

nk
µk

 1   1
 ..   .. 
 .   . 

  
 ∂LL   ni 
 

∇LL =  ∂µi 
 =  µi 
 .   . 
 .   . 
 .   . 

  
By, CoOpt, Theorem 58,
arg max Dv (LL) = D ∇LL (LL)
v

k∇LLk

Hyperplane, norms, local minima and maxima, Hessian
Hyperplane H is given by
H = {p | (p − q)T v = 0}
By CoOpt, Theorem 59, Grad vector is perpendicular to the tangent hyperplance at the level
curve.
Norm is function denoted by kxk and has the following properties
1. kxk ≥ 0
2. kcxk = |c|kxk
3. kx + yk ≤ kxk + kyk
Some common norms
1. L1 norm = |x
p1 | + · · · + |xn |
2. L2 norm = 2 (x21 + · · · + x2n )
1
3. Lk norm = (|xk1 | + . . . |xkn |) k
By, CoOpt, Theorem 60, if µ01 . . . µ0k is a point of local min/max, then ∇LL(µ0 ) = 0, if it exists.
Note, that this is only a necessary but not a sufficient condition.

9

OPTIMIZATION

38

CoOpt, Theorem 61, defines the notion of the Hessian matrix, given as follows:

 ∂ 2 LL
∂ 2 LL
∂ 2 LL
.
.
.
2
∂µ
∂µ
∂µ
∂µ
2
1
k

 2 1
∂ 2 LL

 ∂ LL
.
.
.
2

 ∂µ1 ∂µ2
∂µ2


∇2 LL =  ..

..

 .
.



 .
..
∂ 2 LL
...
∂µ2k


− n21
 µ1



=




0



0 


− nµ22
2

..

.
− nµ2k






k

9.2

Linear Algebra

Some basics of linear algebra relavant to our optimization problem are listed here. The link for the
linear algbra notes is http://www.cse.iitb.ac.in/~cs725/notes/classNotes/LinearAlgebra.
pdf. The notation used to refer to this linear algebra notes is LinAlg, Section 3.11.
Eigenvalues and Eigenvectors
Refer to LinAlg, Section 3.11 for the same. Some of their properties are as follows:
 If Ax = λx then (A + kI)x = (λ + k)x. This is very imporatant in ML. We will revisit this
property in gaussian discriminant analysis, SVMs etc.
 If A is a triangular matrix, then λi = aii
2
 if AxP
= λx then A2 x = λP
x
Q
 Also
λ1 = trace(A) = j ajj and λi = det(A)

Matrix factorization using Eigenvectors, positive definite matrices
Refer to LinAlg, Section 3.12. Positive definite matrices are denoted by A pd 0 and positive
semi-definite matrices are denoted by A <psd 0.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 10: Optimization continued
Instructor: Ganesh Ramakrishnan

Date: 23/08/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

From the previous lecture, our objective function was
arg max LL(µ1 . . . µk |n1 , . . . nj ) = arg max

X

nj log µj

j

P
subject to the constraints
µj = 1 and µj ∈ [0, 1]. Here n1 , . . . nj are accumulated from
X1 , . . . Xn . From CoOpt, Theorem 61, we have the one of the conditions for local optimality
(maximum) as the Hessian to be positive definite. i.e


− nµ21
 1



n2


− µ2


2
2
∇ LL = 
0
..


.




− nµ2k

0

0

k

CoOpt, Theorem 62 and Corollary 63 list the necessary and sufficient conditions for local maxima (resp. minima) as follows: (reproduced here for convenience, please refer to CoOpt notes for
details and proof)
Necessary Conditions
∇f (x∗ ) = 0
∇2 f (x∗ ) 4 0

(∇2 f (x∗ ) < 0 , minima resp.)

Sufficient Conditions
∇f (x∗ ) = 0
∇2 f (x∗ ) ≺ 0

(∇2 f (x∗ )  0 , minima resp.)

Some points to note here. If ∇2 f (x∗ ) is neither < 0 nor 4 0, then x∗ is called a saddle point.
Also to visualize, negative definiteness implies upward curvature of the function surface.
However, for our given function, the gradient does not disappear. Then, how do we find the
maximum value for our objective function ? How about taking a relook at the method for finding
the maximum value. Some considerations:
1. How about restricting
P the attention to the domian set of interest ? (for us it is µi ∈ [0, 1]
with the constraint
µi = 1
39

9

OPTIMIZATION

40

2. In this restricted region compute the extreme values.
By CoOpt. Theorem 65, we know that for a closed and bounded set, there exists a global
maximum and global minimum. Restricting ourselves to Euclidean spaces, some definitions are as
follows:
 Bounded: ∃ sphere S in Rk s.t D ⊆ S
 Open: ∀x ∈ D, ∃ a sphere S(x) of radius  > 0 centered at x, s.t. S(x) ⊆ D
 Closed: complement Dc is open.
 Boundary: B(D) = {y | @ > 0, s.t sphere(∈, x) ⊆ D}

So, the naive method adapted to our case is as follows
 Step 1: See if ∇f = 0
 Step 2: Find max of f along boundaries (relative to Rk−1 )
 Step 3: Find max of f along boundaries (relative to Rk−2 )
 Step 4: Find max of f along boundaries (relative to Rk−3 )
 ...

For definitions of relative boundary, relative interior and an example concerning the same. refer
to CoOpt, pg 250, 251.
Example
Let k = 4. The objective function is
n1 ln µ1 + n2 ln µ2 + n3 ln µ3 + n4 ln µ4
such that,
µ1 + µ2 + µ3 + µ4 = 1 and µi ∈ [0, 1]
In step 1 we calculate the ∇f . In step 2, we find the boundary relative to R3 , where µx = 1 or
µx = 0. So we get the following equations
µ1 + µ2 + µ3 = 1
µ4 = 1
µ1 + µ2 + µ4 = 1
µ3 = 1
...

In step 3, we find boundaries relative to R2 and so on. As an exercise, complete this example.

Another approach (using level curves)
In general we have
max f (x)
s.t g(x) = 0

(LL(µ1 , . . . µk ))
X
(
µi − 1 = 0)

9

OPTIMIZATION

41

Consider level curves for f (x). If x∗ ∈ local arg max f (x), subject to constraints, we have the
following observations
 If ∇f has component perpendicular to the direction of ∇g
 The above statement implies that we can move along g(x) = 0 while increasing value above
f (x∗ )
 This is in violation of the assumption that x∗ is local argmax

From this, we can conclude that if x∗ is local argmax, then ∇f has no component perpendicular
to ∇g. Therefore, at x∗ ,
g(x∗ ) = 0
∇f (x∗ ) = λ∇g(x∗ )
i.e. they are parallel to each other.
Read CoOpt, Section 4.4.1 on Lagrange Multipliers for a detailed exposition of the material
covered next. Say x∗ ∈ local arg max f (x) such that some equality constraints are satisfied. i.e.
x∗ ∈ local arg max f (x)
s.t. g1 (x) = 0
g2 (x) = 0
..
.
gn (x) = 0
Components of ∇f (x∗ ) perpendicular to the space spanned by {∇gi (x∗ )}i=1,...m should be 0.
i.e.
∇f (x∗ ) =

m
X

λi ∇gi (x∗ )

(Linear Combination)

i=1

gi (x∗ ) = 0 , ∀i = 1, . . . m
Suppose we have inequality constraints instead of equality. i.e.
x∗ ∈ local arg max f (x)
s.t. g1 (x) ≤ 0

We have the following possibilities:
P1
g(x∗ ) = 0
∗

∗

∇f (x ) = λ∇g(x ) , λ ≥ 0

9

OPTIMIZATION

42

P2
g(x∗ ) < 0
∇f (x∗ ) = 0
Summarising P1 and P2, we have,
∇f (x∗ ) − λ∇g(x∗ ) = 0
λ≥0
∗

λg(x ) = 0
For multiple inequality constraints, g1 , . . . gm , we have,
∇f (x∗ ) −

m
X

λi ∇gi (x∗ ) = 0

i=1

λi ≥ 0

, ∀i = 1, . . . m

∗

, ∀i = 1, . . . m

λi gi (x ) = 0

Exercise
For the log-likelihood function (our objective function), compute the above form of the equation
(Lagrangian)

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 11: Optimization, KKT conditions
Instructor: Ganesh Ramakrishnan

Date: 26/08/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

For the log-likelihood function f =
optimality (Lagrangian)
n 

Pk

j=1 nj µj , we get the following necessary condition for

1

µ

 1
 .. 
 . 
 
 k
 X ∂µ
X
X ∂µi
 ni 
i
µ −λ
µ
−
1
−
α
−
βi
=0
i
i
 i
∂µi
∂µi
 . 
i=1
 . 
 . 
 
nk
µk

The constraints on αi s and βi are as follows:
gi ≤ 0
gk+j ≤ 0
h=0

:

:
:
k
X

−µi ≤ 0

∼

αi

µj − 1 ≤ 0

∼

βi

µj − 1 = 0

∼

λ

j=1

9.3

KKT conditions

Refer to CoOpt, Section 4.4.4 for a detailed explanation and proofs. Suppose we have the problem
µ
b = arg min f (µ)
µ

s.t. gi (µ) ≤ 0
h( µ) = 0
We will have the necessary conditions for optimality as follows (also known as the Karash-KuhnTucker or KKT conditions)
 n 
− µ1
 1
 .. 
 . 


 ni  P k
Pk

−
1. 
 µi  + j=1 αj (−1) + j=1 βj (1) + λ = 0
 . 
 . 
 . 


− nµkk
43

9

OPTIMIZATION

44

2. −c
µj ≤ 0
µ
cj − 1 ≤ 0
3. αj ≥ 0
βj ≥ 0
4. −αj µ
cj = 0
βj µ
(cj − 1) = 0
Pk
5.
cj + 1 = 0
j=1 µ
From 4., we have µj 6= 0 ⇒ αj = 0. Also from 4., if no nj = 0, βj = 0,
P
nj
= 1 ⇒ λ = nj ⇒
λ
nj
µ
cj = P
nj

P

P

µ
cj = 1. i.e.

n

We still need to verify that µ
cj = P nj j is indeed the globally optimal value. For this we have to
use CoOpt, Theorem 82, which provides us the sufficient conditions for global optimality.
Convex Analysis
For the 1-dim case and α ∈ [0, 1], the condition for convexity is as follows:
f (αx + (1 − α)y ≤ αf (x) + (1 − α)f (y)
For strict convexity :
f (αx + (1 − α)y < αf (x) + (1 − α)f (y)
Convex sets: S is convex if
∀x, y ∈ S,

αx + (1 − α)y ∈ S where α ∈ [0, 1]

For the n-dim case, x, y and ∇f are vectors (so denoted in bold). We have the condition of
convexity as:
f (αx + (1 − α)y < αf (x) + (1 − α)f (y)
For detailed definitions of convex sets, affine sets, convex functions and examples of the same
refer from CoOpt. Section 4.2.3 onwards.

9.4

Necessary and Sufficient Conditions : Summary

We will consider both the 1-dim and n-dim cases. In both the cases the domain D must be convex.
Also the conditions involving gradient and hessian should be held only for all x in the interior of
the domain. The conditions are summarised in Table 4.
If we reverse all the inequalities we get the conditions for concavity.
Our function (LL)
P
The domain D = {µj | µj = 1, µj ∈ [0, 1]} is convex. Hessian is positive definite.Constraints gj ’s
are convex and constraint h : 1T µ − 1 = 0 is affine. It satisfies all the conditions for optimality.

9

OPTIMIZATION

45

1-dim
0

N-dim

0

(f (x) − f (y))(x − y) ≥ 0
0

f (y) ≥ f (x) + f (x)(y − x)

Theorem (CoOpt)

T

(∇f (x) − ∇f (y)) (x − y) ≥ 0

51 / 78

T

f (y) ≥ f (x) + ∇ f (x)(y − x)

46 / 75

00

∇2 f (x) < 0

51 / 52 / 79 (Sufficient)

00

∇2 f (x) < 0

51 / 52 / 79 (Necessary)

f ≥0
f ≥0

Table 4: Necessary and Sufficient conditions for Optimility

9.5

Duality

Dual function
Let L be the primal function given by:
L(µ, α, β, λ) = −

k
X

k
X
X
X
nj log µj + λ(
µi − 1) −
αi µi +
βi (µi − 1)

j=1

i=1

i

i

Here, µ is called the primal variable and α, β, λ are called the dual variables. The dual function
of L is given by:
L∗ (α, β, λ) = minµ L(µ, α, β, λ)
This dual objective function is always concave. Also note the following
 For a concave problem : Local Max = Global Max
 For a convex problem : Local Min = Global Min

Duality Gap
Consider the primal problem:
p∗ = min −

X

nj log µj

s.t. µi ∈ [0, 1]
X
µi = 1
The corresponding dual problem is given by
d∗ = maxαj ≥0,βj ≥0 L∗ (α, β, λ)
We can show that p∗ ≥ d∗ and the expression p∗ − d∗ is called the duality gap.

Exercise
Prove the functions in CoOpt, Table 4 are convex.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 12: Naive Bayes Classifier
Instructor: Ganesh Ramakrishnan

Date: 30/08/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

10

Naive Bayes Classifier

Until now we only considered the case of only one feature function per data tuple. Now we will
consider the case where each data tuple itself contains a lot of different features. The notation of
this is as follows
Xi : Data tuple that belongs to class cj with probability P r(cj ) (class prior)
φ1 (Xi ), φ2 (Xi ) . . . φm (Xi ) : Set of m features on the data tuple
[V11 . . . Vk11 ][V12 . . . Vk22 ] . . . [V1m . . . Vkm
] : Set of values taken by each feature function
m
m
[µ11,j . . . µ1k1 ,j ][µ21,j . . . µ2k2 ,j ] . . . [µm
1,j . . . µkm ,j ] : Set of parameters of distribution that characterizes

the values taken by a feature for a particular class
As an example from document classification task we have the following:
Xi : A particular document
cj : Document is categorized as sports document
φ1 : Some word form for hike; Corresponding values Vi1 can be hikes, hiking, ...
φk : Presence or absence of word race. Here values are binary (|km | = 2)

10.1

Problem formulation

We are interested in the following probability distribution:


P r φ1 (Xi ) . . . φm (Xi )|cj
By the naive bayes assumption which states that features are conditionally independent given
the class, we have the following
m



Y 
P r φ1 (Xi ) . . . φm (Xi )|cj =
P r φl (Xi )|cj
l=1

As the name suggests, this is a naive assumption especially if there is lots of training data.
However, it works very well in practice. If use a lookup table using all the feature values together,
we have [k1 ∗ k2 · · · ∗ km ∗ (#classes)] parameters to estimate. In contrast, in the naive bayes we

46

10

NAIVE BAYES CLASSIFIER

47

have to estimate [(k1 + k2 + · · · + km ) ∗ (#classes)] parameters. This is a great simplification in
size of parameter space.
To find the “best” class given xi , i.e.


P r cj , φ1 (Xi ), . . . , φm (Xi )


P r(cj |Xi ) = P
0
0 P r c , φ1 (Xi ), . . . , φm (Xi )
j
cj


Qm
P r(cj ) l=1 P r φl (Xi )|cj
=
P r(φi (Xi ) . . . φm (Xi ))
We have to minimize the “risk”.
Misclassification Risk
A risk is a function which we try to minimize to assign the best class label to a datapoint. The
treatment of risk minimization is related to decision theory. This function R takes as arguments a
policy p and the datapoint Xi . For the misclassification risk, the policy is the point came from ci
but the algorithm assigned it class cj . We have the following expression:
R(p, Xi ) =

|c|
X

pol(cj )(1 − P r(cj |Xi ))

j=1

where pol(cj ) is given by
pol(cj ) = 1

if policy says classify into cj

pol(ci ) = 0 ∀i 6= j
As per misclassification risk (i.e. in order to minimize it) we have


Qm
P r(cj ) l=1 P r φl (Xi )|cj
c∗ = arg max
P r(φi (Xi ) . . . φm (Xi ))
cj
m


Y
= arg max P r(cj )
P r φl (Xi )|cj
cj

l=1

kl
m hX


i
Y
= arg max P r(cj )
δ φl (Xi ), Vpl ∗ µlp,j
cj

l=1

p=1

where P r(cj ) is the class prior as defined before.

10.2

Estimating the Parameters

We have the data set D given by
h
i
D = (X1 , cX1 ), . . . (Xn , cXn )

10

NAIVE BAYES CLASSIFIER

48

h
i
The maximum likelihood estimators are denoted by µ̂M L , PˆrM L (cj ) . They are calculated as
follows
µ̂M L , Pˆr(cj ) = arg max

m
Y

P r(c(Xi )) ∗

µ,P r(c) i=1

= arg max

|c|
Y

m
Y

P r(φl (Xi )|c(Xi ))

l=1

P r(cj )

#cj

∗

µ,P r(c) i=1

kl
m Y
Y

µlp,j

nlp,j

l=1 p=1

where,
#cj = No. of times c(Xi ) = cj across all i’s in the dataset
nlp,j = No. of times φl (Xi ) = Vp and c(Xi ) = cj across all the i’s
X


nlp,j =
δ φl (Xi ), Vpl δ c(Xi ), cj
i
|c|

P r(c(Xi ) =

X


δ c(Xi ), cj P r(cj )

j=1

P r(φl (Xi )|c(Xi )) =

kl
X


δ φl (Xi ), Vpl ∗ µlp,c(Xi )

p=1

So, the final log-likelihood objective function is:

arg max
µ,P r(c)

kp
|c|
m X
i
hX
X
(#cj ) log P r(cj ) +
nlp,j log(µlp,j )

(11)

l=1 p=1

j=1

under the constraints
|c|
X

P r(cj ) = 1

j=1
kl
X

µlp,j = 1 ∀l, j

p=1

P r(cj ) ∈ [0, 1]
µlp,j ∈ [0, 1]

∀j

∀p, l, j

Intuitively, working out the KKT conditions on the above objective function, we get the estimators as follows
µ̂lp,j = Pn

nlp,j

l
p0 =1 np0 ,j

cr(cj ) = P#cj
P
k #ck

10

NAIVE BAYES CLASSIFIER

49

However, there is a problem with the above estimators. To illustrate that let us take the example
of a pair of coins being tossed. Let coin1 be tossed 5 times and suppose we get heads all the 5
times. Then if feature φ = heads, µ1h,1 = 1 and µ1t,1 = 0. But we know that
P r(coin1|φ(X) = t) ∝ P r(coin1) ∗ µ1t,1
But from the above parameters, the probability P r(coin1|φ(X) = t) = 0. This may fine if we
have made a million observations. However, in this case it is not correct.
We can modify Equation 11 and get a slightly modified objective function that can alleviate
this problem in a hacky manner by considering:

arg max
µ,P r(c)

kp
|c|
m X
hX
X
X
2 i
(#cj ) log P r(cj ) +
nlp,j log(µpp,j ) −
µlp,j
j=1

l=1 p=1

(12)

p,j,l

The new term introduced in Equation 12 is called the regularization term. It is done to introduce
some bias into the model.
A small note: Suppose φl (Xi ) ∼ Ber(µl1,c(Xi ) . . . µlkl ,c(Xi ) ), then µ̂lp,j is a random variable since
it is a function of the Xi ’s and it will belong to the normal distribution as n → ∞

Exercise
1. Work out the KKT conditions for Equation 11
2. Work out the KKT conditions for Equation 12
3. Is the objective function in Equation 12 concave ?

Further Reading
1. http://www.cs.cmu.edu/~tom/mlbook/NBayesLogReg.pdf
2. http://www.cse.iitb.ac.in/~cs725/notes/classNotes/misc/CaseStudyWithProbabilisticModels.
pdf, Sections 7.6.1, 7.7.1, 7.7.2, 7.7.3, 7.4, 7.7.4
3. http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.63.2111&rep=rep1&type=
pdf
4. Christopher Bishop, PRML (Pattern Recognition and Machine Learning), Sections 2.1.1,
2.2.1, 2.4.2 and 2.4.3

10.3

Conjugate prior

Suppose we have a multivariate bernoulli distribition of the µ’s and let P r(µ = µ1 ) = P r(µ = µ2 ) =
. . . P r(µ = µk ) = k1 . As an example condider the toss of a dice. Suppose at ∞, all observations are
say a particular value Vi then, we will have P r(µ = µ1 ) = 0, . . . P r(µ = µi ) = 1 . . . P r(µ = µk ) = 0
Using Bayes rule
P r(D|µ̄)P r(µ̄)
P r([µ1 . . . µk ]|D) = P
P r(D|µ̄0 )P r(µ̄0 )
µ¯0

10

NAIVE BAYES CLASSIFIER

50

If P r(µ) has a form such that P r(µ|D) has the same form, we say that P r(µ) is the conjugate
prior to the distribution defining P r(D|µ).
Some of the conjugate priors that we will see in the next class
 Dirichlet and Multivariate Bernoulli
 Beta and Bernoulli
 Gaussian and Gaussian

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 13: Naive Bayes (cont.)
Instructor: Ganesh Ramakrishnan

Date: 02/09/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

Naive Bayes with Dirichlet prior2
Qm
Naive Bayes assumption: Pr(φi (xi )...φn (xi )|cj ) = l=1 P r(φl (xi )|cj )
nl
= P p,j
Minimum Likelihood Estimation: (µlˆ )
p,j M L

kl
l
q=1 nq,j

Now,
R1
Prior P (µ) ∈ [0, 1]& 0 p(µ)dµ = 1
1 ,X2 ,..Xn |µ).P (µ)
Now, P (µ|X1 , X2 , ..Xn ) = R 1 PP(X
(X ,X ,..X |µ).P (µ)dµ
n1

0

n2

1

2

n

(1−µ)
= R µµn1 (1−µ)
n2 dµ
2 +1)!
= µn1 (1 − µ)n2 (n1n+n
1 !n2 !
a−1

(1−µ)b−1 (a=b−1)!
what will be the form of P (µ|D)? P (µ|X1 , X2 , ..Xn ) =
(a−1)!(b−1)!
a−1+n1
b−1+n2
µ
(1−µ)
(n1 +n2 +a+b−1)!
Beta(µ|a + n1 , b + n2 )
(n1 +a−1)!(n2 +b−1)!
a
so P (µ = 1) Beta(µ|1, 1) Expected value of Beta E(Beta(µ|a, b)) = a+b

HW. If P (µ) had the form µ

Why it is rasonable:
a
 E[µ]Beta(µ|a,b) = a+b
is intuitive

 a=b=1 gives uniform distribution
 Form of the posterior and prior are the same.
n1 +a
 As n1 + n2 ← ∞, spread of the distribution ← 0, a and b becomes immaterial. ( n1 +n
=
2 +a+b
n1
)
n1 +n2
E(µ)
← µM
ˆL
B(µ|n1 +a,n2 +b)
1 −1
µMˆAP = argmaxP (µ|D) = a+na+n
1 +b+n2 −2

µ

As n1 , n2 ← ∞, µMˆAP = µM
ˆL
Qt
P (Xn+1 , ..Xn+t |µ) =R i=1 P (Xi+1 |µ)
R
P (Xn+1 |X1 ..Xn ) = P (Xn+1 |µ)P (µ|X1 ..Xn )dµ = µXn +1 (1 − µ)1−Xn+1 P (µ|X1 ..Xn )dµ
= E[µ] if Xn+1 = 1
= 1 − E[µ] if Xn+1 = 0
µ2 (n1 +n2 −1)!
Beta(µ1 ,µ2 |a,b) = µ1(a−1)!(b−1)!
Q ai −1 √P
µ
aj
Dir(µ1 , µ2 , ..µk |a1 , a2 , ..ak ) = i iQ √aj j
j

2 lecture scribed by Amrita and Kedhar with inputs from Ajay Nair

51

10

NAIVE BAYES CLASSIFIER

52

E(µ)Dir = [ Pa1ai Pa2ai .. Pakai ]T
i

i

i

ak +nk T
a1 +n1
a2 +n2
Expression for µ ˆ
Bayes = E(µ) = [ P ai +ni P ai +ni .. P ai +ni ]
i

i

Expression for µM
ˆ L = E(µ) = [ Pn1ni Pn2ni .. Pnkni ]T
i

i

i

i

1 −1
k −1
Pa2 +n2 −1
Expression for µMˆAP = E(µ) = [ (Pa1a+n
.. (Paka+n
]T
i i +ni )−K (
i ai +ni )−K
i i +ni )−K
P (Xn+1 |X1 ..Xn ) = [E(µ)] if Xn+1 = Vi

Dirl,j (µl1i j ..µlli j |al1i j ..al1i j ) =
E(µ)Dir = [

Q

ali,j −1
l
i (µi,j )
Q
l
i Γ(ai,j )

Γ(ali,j + (al2,j ) + ..(alk,j )

al
al
al
P 1,jl P k,jl
P k,jl T
i ai,j
i ai,j
i ai,j
al +nl1,j
al2,j +nl2,j
al +nlk,j T
P 1,jl
P
P k,jl
l
l
l
l
i ai,j +ni,j
i ai,j +ni,j
i ai,j +ni,j
al2,j +nl2,j
al +nl
al1,j +nl1,j
P l
P lk,j lk,j
P
l )−K
l +nl )−K (
+n
a
(
a
(a
l
l
i i,j
i i,j +ni,j )−Kl
i
i,j
i,j
i,j
al1,j +nl1,j
al2,j +nl2,j
alk,j +nlk,j T
P l
P l
P l
l
l
l
i ai,j +ni,j
i ai,j +ni,j
i ai,j +ni,j

..

(µlj )Bayes = [

]

..

]

(µlj )M AP = [

..

(µlj )Bayes = [

..

]T

]

Assume X is the event of a coin toss. Let X1=0 (TAILS say), X2=1, X3=0, X4=1, X5=1. We
are interested in predicting the event X6=1 given the above. This can be calculated by different
approaches. The ML, MAP and the Bayes Estimator are called the pseudo Bayes, and Bayesian
estimator is called the pure Bayes.
Maximum likelihood
µM
ˆ L is the probability of X = 1 from the data.
(1−X6)

P (X6|X1..X5) = µM
ˆ L X6 (1 − µM
ˆ L)
MAP
µMˆAP is the probability of X = 1 from the data.

P (X6|X1..X5) = µMˆAP X6 (1 − µMˆAP )

(1−X6)

Bayes Estimator
µbayes
ˆ is the probability of X = 1 from the data.
(1−X6)

P (X6|X1..X5) = µbayes
ˆ X6 (1 − µbayes
ˆ )
Bayesian method
Z 1
P (X6|X1..X5) =

(1−X6)

µX6 (1 − µ)

P (µ|X1..X5)dµ

0

The explanation for this equation is as follows:
Z
P (X6|µ, X1, ..X5)P (µ|X1..X5)P (X1..X5)dµ
P (X6|X1..X5) =
P (X1..X5)

10

NAIVE BAYES CLASSIFIER

53

this marginalises on the probability µ. Simplifying futher,
Z
P (X6|X1..X5) = P (X6|µ, X1, ..X5)P (µ|X1..X5)dµ
Thus

Z 1
P (X6|X1..X5) =
0

(1−X6)

µX6 (1 − µ)

P (µ|X1..X5)dµ

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 14: Naive Bayes Classifier (cont.)
Instructor: Ganesh Ramakrishnan

Date: 06/09/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

10.4

Naive Bayes with Dirichlet Priors

Uptil now the set of distribitions we have seen are as follows:
1. Bernoulli distribution (whose conjugate is Beta)
2. Multivariate Bernoulli distribution (whose conjugate is Dirichlet)
3. Naive Bayes with Multivariate Bernoulli distribution
4. Naive Bayes with Dirichlet prior on Multivariate Bernoulli distribution
(whose prior is per-class set of Dirichlet)
The setting for the Naive Bayes with Dirichlet prior on Multivariate Bernoulli distribution is as
follows:
 For each data point Xi which belongs to class cj there are a set of m features given by
φ1 (Xi ) . . . φl (Xi ) . . . φm (Xi )|cj
 Each of these features have a probability distribution given by p(µ1j ) . . . p(µlj ) . . . p(µm
j ) where
p(µ1j ) . . . p(µm
)
are
the
parameters
to
be
determined
from
the
data.
j

Final Estimators
For the problem under consideration, the final estimators are as follows:
nlp,j
= Pkl
l
M LE
q=1 nq,j


h
il
nlp,j + alp,j
µ̂lp,j
= E(µ|X1 . . . Xn )
= Pkl
 also called Laplace Smoothing
l
l
Bayes
p,j
q=1 nq,j + aq,j


h
il
nlp,j + alp,j − 1
µ̂lp,j
= arg max p(µ|X1 . . . Xn )
= Pkl

l
l
M AP
p,j
q=1 nq,j + aq,j − 1


µ̂lp,j



where alp,j are multivariate dirichlet prior parameters

Essentially we are trying to find p(x|D) but we approximate it to p(x|ˆ(µ) and we determine
various types of estimators from this like MLE, MAP and Bayes.

54

10

NAIVE BAYES CLASSIFIER

55

If we consider a purely bayesian perspective from first principles, we have:
Z
p(x|D) =
p(x, µ|D)dµ
µ
Z
=
p(x|µ, D) ∗ p(µ|D)dµ
µ
Z
=
p(x|µ) ∗ p(µ|D)dµ From the i.i.d assumption
µ

So finally we have

p(x|D) =

Z k
Y

δ(x,Vi )

µi

Dir(n1 + a1 , . . . nk + ak )dµ1 . . . dµk

(13)

µ i=1

µ̂M LE is the loosest approximation from a Bayesian perspective. (since there is no prior in
MLE). For instance, in coin toss example, if we don’t see tails p(tails) = 0 in MLE. In practice,
µ̂M AP and µ̂Bayes are the most important estimators.

10.5

Naive Bayes with Gaussian Priors

Until now we assumed that each feaure can take k different discrete values. Now we extend our
notions to continuous distributions. Specifically we consider Gaussian or Normal Distribution for
our exposition here. The treatment for continuous distributions closely follows that of our discrete
case. It is as follows:
1. Gaussian
2. Independent Gaussian
3. Naive Bayes with Independent Gaussians (φ1 (Xi ) . . . φm (Xi )|cj )
4. Naive Bayes with Gaussian priors on Independent Gaussians
φ1 (Xi ) . . . φm (Xi )|cj
p(µ1j ) . . . . . . p(µm
j )
As an aside, we will use the following conventions
 µ̂(X1 . . . Xn ) ∼ estimator. It is a random variable and will have a distribution
 µ̂(x1 . . . xn ) ∼ estimate. It is a value.

Gaussian
Let us consider the first case of Xi s following a normal distribution. , The pdf of a normal distribution is
(x−µ)2
1
p(x|µ, σ 2 ) = √ e− 2σ2
σ 2π
Given D = {X1 , . . . Xn }, We have
LL(µ, σ 2 |D) = log

n
hY

i
(Xi −µ)2
1
√ e− 2σ2
σ 2π
i=1

(14)

10

NAIVE BAYES CLASSIFIER

=−

56

n
Xh
i=1

√ i
(Xi − µ)2
−
n
log
σ
2π
2σ 2

2
{µ̂M L , σ̂M
L } = arg max −
µ,σ 2

n h
X
(Xi − µ)2

2σ 2

i=1

− n log σ − n log

√

2π

i

The critical question is whether the objective function in Equation 14 concave ? As an exercise
compute the Hessian of Eq. 14 and check if it is negative semi-definite. Once this is ascertained,
we can apply the KKT conditions for optimality:
 
 P
2 
n
0
− i=1 (Xiσ̂−µ̂)
2
= 
∇LL = Pn (Xi −µ̂)2
n
0
− σ̂
i=1
σ̂ 3
⇒

n
X

= nµ̂M LE

i=1

P
µ̂M LE =
Also

∼ N (µ,

n
X
(Xi − µ̂)2

⇒

i=1
2
σ̂M
LE =

Xi
n

σ̂ 3

=

n
X
(Xi − µ̂)2
i=1

n

σ2
)
n

n
σ̂
∼ αχ2n−1

Priors for µ (σ 2 is fixed and known)
µ ∼ N (µ0 , σ0 )
p(µ|X1 , . . . Xn ) ∝ p(X1 , . . . Xn |µ)p(µ)
n
 1 n Y
(µ−µ0 )2
(Xi −µ)2
2
√
e− 2σ2 e 2σ0
=
σ 2π i=1
∝e

(µ−µn )2
2
2σn

(this can be proved)

 nσ 2 

σ2
0
where µn =
µ
+
µ̂M LE
0
nσ02 + σ 2
nσ02 + σ 2
1
1
n
and 2 = 2 + 2
σn
σ0
σ
P r(µ|X1 , . . . Xn ) ∼ N (µn , σn2 )
As n → ∞, µ tends to assume only µ̂M LE i.e. spread is zero. So P r(µ|X1 , . . . Xn ) ∼ N (µ̂M LE , 0).
Also both µ̂Bayes and µ̂M AP peak at µn

10

NAIVE BAYES CLASSIFIER

57

Naive Bayes with Independent Gaussian
Now let us consider the following:
P (Xi |cj , µ̄lj , (σ̄jl )2 )
where each Xi has m featuresφ1 (Xi ) . . . φm (Xi )
Each of these features follow a gaussian distribution.
By the naive bayes assumption, we have :
P r(Xi |cj , µ̄lj , (σ̄jl )2 ) =

m
Y

P r(φt (Xi )|cj , µ̄lj , (σ̄jl )2 )

t=1

The ML estimators are as follows:
(µ̂lj )M L =

Pn

i=1 φl (Xi )

Pl
(σˆjl )2M L =

i=1

n


φl (Xi ) − µˆlj

2

n

l
For fixed (σjl )2 in Bayesian setting and µlj ∼ N (µl0,j , (σ0,j
)2 ), the MAP and Bayes estimators
for mean are as follows:
!
!
l


(σjl )2
n(σ0,j
)2
l
ˆ
ˆ
l
l
µj Bayes = µj M AP = µn =
µ0,j +
(µ̂lj )M LE
l )2 + (σ l )2
l )2 + (σ l )2
n(σ0,j
n(σ0,j
0
j

As an exercise write down the expression for (σ̂jl )M AP .

Exercise
1. Compute the form of Equation 13
2. Compute the Hessian of Equation 14. Prove that the function in Eq. 14 is concave.
3. Derive the expression for (σ̂jl )M AP in the Naive Bayes with independent Gaussians’ setting.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 15: Nature of Separating Surfaces, Multivariate Gaussian
Gaussian Discriminant Analysis
Instructor: Ganesh Ramakrishnan

Date: 09/09/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

10.6

Nature of Separating Surfaces

Decision Trees
In the case of decision trees, the separating surface was intersection of axis parallel hyperplanes. It
is as shown in Figure 14.

Figure 14: Decision Surface of DTrees

58

10

NAIVE BAYES CLASSIFIER

59

Naive Bayes with Bernoulli
Here ∀x in decision surface,
p(cj1 |x) = p(cj2 |x)

for some 2 classes cj1 and cj2

⇒ p(x|cj1 )p(cj1 ) = p(x|cj2 )p(cj2 )
⇒

kl 
m Y
Y

µlp,j1

δ(φl (x),Vpl )

p(cj1 ) =

l=1 p=1

⇒

kl 
m Y
Y

µlp,j2

δ(φl (x),Vpl )

p(cj2 )

l=1 p=1

kl
m X
X
l=1

h

i
p(cj1 )
=0
δ(φl (x), Vpl ) log µlp,j1 − log µlp,j2 + log
p(cj2 )
p=1

(taking log on both sides)

If φl = 0|1,
m
l
X k
X
l=1

h

i
p(cj1 )
=0
φl (x) log µlp,j1 − log µlp,j2 + log
p(cj2 )
p=1

This surface looks like a general hyperplane. It is linear in φ’s
Naive Bayes with Independent Univariate Gaussian
Here ∀x in decision surface,
p(cj1 |x) = p(cj2 |x)

for some 2 classes cj1 and cj2

⇒ p(x|cj1 )p(cj1 ) = p(x|cj2 )p(cj2 )
" m
#
" m
#
−(φl (x)−µlj )2
−(φl (x)−µlj )2
1
2


Y
Y
1
1
2(σ l )2
2(σ l )2
j
j
1
2
√ e
√ e
⇒
p(cj1 ) =
p(cj2 )
σjl 1 2π
σjl 2 2π
l=1
l=1
m h
m
X
−(φl (x) − µlj1 )2
(φl (x) − µlj2 )2 i
σjl i
p(cj1 ) X h
+
⇒
+
log
+
log l 2 = 0
l
l
2
2
p(cj2 )
2(σj1 )
2(σj2 )
σj1
l=1

l=1

The decision surface is quadratic in φ’s. For the same set of points as in Figure 14, the decision
surface for Naive Bayes with Gaussians is as shown in Figure 15. A very clear decision surface does
not emerge for this case unlike the case for decision trees. For another set of points the decision
surface looks as shown in Figure 16.

10.7

Multivariate Gaussian

Next let us consider the case of multivariate normal distribution also known as multivariate gaussian.
Consider the features as
φ1 (X) . . . φm (X) ∼ N (µ, Σ)
where µ is a 1 × x vector and Σ is a m × m matrix called the co-variance matrix. (In this section
µ and Σ are vectors and matrix respectively even if they are not denoted in bold-face)
N (x1×m |µ, Σ) =

1
m
2

(2π) |Σ|

1
2

e−

(x−µ)T Σ−1 (x−µ)
2

10

NAIVE BAYES CLASSIFIER

60

Figure 15: Decision Surface of Naive Bayes with Gaussians

For example if m = 2, and
h

µ = µ1

µ2

N (x|µ, Σ) ∝ e

−

i


σ12

Σ=
0

0



σ22



(x1 −µ1 )2
(x −µ )2
− 2 22
2
2σ1
2σ2

= N (x1 |µ1 , σ12 )N (x2 |µ2 , σ22 )
In general, if

σ2
 1



Σ=




0


σ22
..

0

.
2
σm









then,
N (x|µ, Σ) =

m
Y

N (xi |µi , σi2 )

i=1

So Naive Bayes assumption is a special case of mutivatiate gaussian.

10

NAIVE BAYES CLASSIFIER

61

Figure 16: Decision Surface of Naive Bayes with Gaussians (another set of points)

Estimators for mutivariate Gaussian
Let D = {X1 , . . . Xi . . . Xn } be the set of data points and let
h
i
φ(Xi ) = φ1 (Xi ) . . . φm (Xi )
So, φ(Xi ) represents a vector. MLE for µ and Σ assuming they came from the same multivariate
Gaussian N (µ, Σ):
µ̂M L , Σ̂M L = arg max p(D)
µ,Σ

= arg max
µ,Σ

= arg max
µ,Σ

n
Y

1

i=1

(2π) 2 |Σ| 2

m

1 e

−(φ(xi )−µ)T Σ−1 (φ(xi )−µ)
2

m h
X
−(φ(xi ) − µ)T Σ−1 (φ(xi ) − µ)
i=1

2

−

i
n
mn
log |Σ| −
log(2π)
2
2

(15)

We assume symmetric Σ. It can be shown thar a non-symmetric Σ has an equivalent symmetric
Σ (see further reading) . The necessary conditions for local maxima can be computed by finding
the ∇LL function above. As an exercise find ∇LL for Equation 15.

11

GAUSSIAN DISCRIMINANT ANALYSIS

The ML estimators are:
Pn
φ(xi )
µ̂M L = i=1
nh

T i
Pn
φ(x
)
−
µ̂
φ(x
)
−
µ̂
i
ML
i
ML
i=1
Σ̂M L =
n

62

(sum of rank 1 matrices and is symmetric)

Bias of the Estimator
By definition, an estimator e(θ) is called unbiased estimator of θ if E[e(θ)] = θ.
µ̂M L is an unbiased estimator. This is shown as follows:
Pn
E(φ(xi ))
E(µ̂M L ) = i=1
Pn n
µ
= i=1 = µ
n
However Σ̂M L is a biased estimator since it can be shown that
E(Σ̂M L ) =

n−1
Σ
n

If we define a new estimator say Σ̂new which is given by:
Pn
(φ(xi − µ̂M L ))(φ(xi − µ̂M L ))T
Σ̂new = i=1
n−1
This can be shown to be an unbiased of Σ. (See further reading about the bias of an estimator.)

Exercise
1. Find ∇LL for equation 15 w.r.t [µ1 . . . µm Σ11 . . . Σ1m Σ21 . . . Σmm ]T
2. Were θ̂M L , the parameters of bernoulli, multivariate bernoulli and gaussian, unbiased ?

Further Reading
1. Equivalence of symmetric and non-symmetric matrices: Chapter 2, PRML, Christopher
Bishop
2. Unbiased Estimator: http://en.wikipedia.org/wiki/Bias_of_an_estimator

11

Gaussian Discriminant Analysis

Gaussian Discriminant Analysis is another classifier which is like Naive Bayes with Gaussian but
with the naive assumption done away with. Consider the set of class labels:
C1 , . . . Cj , . . . C|c|
where each of them come from a normal distribution as follows:
N (µ1 , Σ1 ) . . . N (µj , Σj ) . . . N (µ|C| , Σ|C| )

11

GAUSSIAN DISCRIMINANT ANALYSIS

63

We can show that the ML estimators are as follows:
(µˆj )M L =
(Σˆj )M L =

Pn
φ(x )δ(class(xi ), cj )
i=1
Pn i
i=1 δ(class(xi ), cj )

Pn

T
M L )(φ(xi ) − (µ̂j )M L ) δ(class(xi ), cj )
i=1 (φ(xi ) − (µ̂j )P
n
i=1 δ(class(xi ), cj )

The decision surface of this classifier is quadratic in µ.

,17
CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 16,17: Gaussian Discriminant Analysis, Clustering
Instructor: Ganesh Ramakrishnan

Date: 20/09/2011, 23/09/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

11.1

Nature of separating surface

There are 2 types of mixture of Gaussians.
1. Different µj ’s and Σj ’s. This was the case we saw in the last class. We had written down
the equation for (µˆj )M L and (Σˆj )M L . We had also briefly noted that the decision surface is
quadratic. It can also be shown from the following equation for a mixture of 2 gaussians.
T

−1

T

−1

e(−1/2)(x−µ2 ) Σ2 (x−µ2 )
e(−1/2)(x−µ1 ) Σ1 (x−µ1 )
=
m/2
1/2
(2π)
|Σ1 |
(2π)m/2 |Σ2 |1/2
The decision surface looks as shown in Figure 17

Figure 17: Decision Surface of Gaussian Mixture (Case 1)

64

11

GAUSSIAN DISCRIMINANT ANALYSIS

65

2. Different µj ’s and shared Σ. In this case the estimators are as follows:
Pn
φ(x )δ(class(xi ), cj )
Pn i
(same as before)
(µˆj )M L = i=1
i=1 δ(class(xi ), cj )
h
i
Pn
T
(φ(x
)
−
(µ̂
)
)
(φ(x
)
−
(µ̂
)
)
i
j ML
i
j ML
i=1
(Σ̂)M L =
n
The nature of the separating surface is linear. When we equate the following terms, xT Σ−1 x
gets cancelled.
(1/2)(x − µ1 )T Σ−1 (x − µ1 ) = (1/2)(x − µ2 )T Σ−1 (x − µ2 )
The separating surface looks as shown in Figure 18

Figure 18: Decision Surface of Gaussian Mixture (Case 2)

11.2

Curse of dimensionality

The number of parameters to be determined increase non-linearly as the number of dimensions.
This is termed as the curse of diminsionality. For the cases from previous section, the curse of
dimensionality is evidently seen in the first case. It is ameliorated in the second case. The number
of parameters to be determined for the 2 cases are as follows:

|C|
1. No. of params = m + m(m+1)
2
2. No. of params = |C|m + m(m+1)
2

12

UNSUPERVISED LEARNING

66

Other perspectives for curse of dimensionality
1. Consider a p × p grid of cells as shown in Figure 19a with unity being the length of each cell.
In 2-dim there are p2 -cells. In m-dim there will be pm unit cells. For a learning problem,
we have to smear the data points over all the cells. Adding new diminsions (features) will
make the smearing skewed (as the number of data points remain the same even in higher
dimensions)

(a) p2 cells

(b) 1 −  annulus

Figure 19: Curse of Dimensionality

2. Consider a ring of radius r = 1 as shown in Figure 19b. Now fix a small  value and consider
a second ring of radius 1 − . In 2 dimensions, the ratio of area of the annulus to the entire
2
2
m
m
area is 1 −(1−)
= 2 − 2 . In m-dimensions it is 1 −(1−)
. As m grows, the volume of the
12
1m
annulus grows more than in lower dimensions.
For more information on curse of dimensionality, refer to PRML, Chapter 2

12

Unsupervised Learning

So far we have been studying supervised learning wherein during the training we are also provided
with the class label of a particular example. The data is in the form D(xi , class(xi )). Also we
assumed the generative model of classification i.e the class labels generate the examples. This is
depicted as shown in Figure 20.

Figure 20: Generative Model

Now, we consider another type of learning in the same generative model setting. Here the class

12

UNSUPERVISED LEARNING

67

labels are not known during training. This is also called unsupervised learning. So the data is of
the form D(xi ). We will look at clustering, a type of unsupervised learning.
Here we will learn from a set of data points x1 , x2 , . . . , xn , whose class labels are not known

12.1

Objective function (Likelihood)

Let there be a total of |C| no. of classes. The likelihood function is written as follows:
L(x1 , . . . , xn ) =

n
Y

p(xi )

i=1

=

|C|
n X
Y

p(xi , cj )

i=1 j=1

=

|C|
n X
Y

p(xi |cj )p(cj )

i=1 j=1

LL(x1 , . . . , xn ) =

n
X

log

|C|
X


p(xi |cj )p(cj )

(log-likelihood)

j=1

i=1

In the above equation, we are tempted to move the log inside the summation. But to achieve
this, we have to find a bound on the log-likelihood. We try to find the lower bound, since our
original intention is to maximize LL. If we maximize the lower bound on LL we are better off.
Let rewrite the LL function in terms of some reference distribution qneq0 as follows:
"
#
#
"
|C|
|C|
n
n
XX
X
X
p(xi , cj )
p(xi , cj )
q(cj |xi ) log
≥
(16)
q(cj |xi )
log
LL =
q(cj |xi )
q(cj |xi )
i=1 j=1
j=1
i=1
log is strictly concave function. Also
X
log(σi αi xi ) =
αi log xi

⇐⇒ xi = xj ,

∀i 6= j

i

So equality hold in Equation 16 iff,

⇒
⇒

p(xi , cj )
= λ(xi ) (for some λ which is independent of j)
q(cj |xi )
p(cj |xi )p(xi )
= λ(xi ) ∀j
q(cj |xi )
0
p(cj |xi )
= λ (xi ) (absorb p(xi ) into λ(xi ))
q(cj |xi )
0

⇒ p(cj |xi ) = λ (xi )q(cj |xi ) ∀j
⇒

|C|
X
j=1

0

p(cj |xi ) = 1 = λ (xi )

|C|
X
j=1

0

q(cj |xi ) = λ (xi )

12

UNSUPERVISED LEARNING

68

So equality hold iff,
p(cj |xi ) = q(cj |xi ) , ∀j

(17)

So the lower bound on log-likelihood is written as

|C|
n
XX

#
|C|
|C|
n
n
XX
XX
p(xi , cj )
LL ≥
q(cj |xi ) log
=
q(cj |xi ) log p(xi , cj ) −
q(cj |xi ) log q(cj |xi )
q(cj |xi )
i=1 j=1
i=1 j=1
i=1 j=1
"

(18)
The first term looks like log p(xi , cj )q(cj |xi ) . It is the expected log-likelihood under the q distribution and is written as Eq(cj |xi ) [LL]. The second term is the entropy and is written as Hq .
Some observation on log-likelihood and its lower bound.
1. LL has params q(cj |xi ) = θj = {µj , Σj } and p(cj ). LL is not convex in either of them.
2. Lower bound of LL has params q(cj |xi ), p(cj ) and params of p(xi |cj ). It is not convex in any
of these parameters.
So neither the lower bound of LL nor LL is convex. So can only find a local optimum. We next
look at the procedure for finding the local optimum of this objective.

12.2

Expectation-Maximization Algorithm

We use procedures like co-ordinate descent to find the local optimum. This is also called ExpectationMaximization (EM) algorithm. It can be looked upon as batch co-ordinate ascent over the lowerbound of LL.
we
to be estimated into two sets. They are
 In EM
 algorithm,

 divide the set of parameters
P
q(cj |xi ) and θj , p(cj ) . The constraint is that j q(cj |xi ) = 1, ∀i.
Broadly speaking, we hold one set of parameters constant and optimize for the other set alternatively. The two steps are as follows:
1. E-step (Expectation Step): Here we obtain the distribution q for which expectation is
maximum.
h
i
q̂(cj |xi ) = arg max Eq (LL) + Hq = p(cj |xi ) (by Eq. 17)
q(cj |xi )

We keep p(cj ) and θj fixed during this step.
2. M-step (Maximization Step): Here we keep the q(cj |xi ) fixed and compute:
θ̂j , p̂(cj ) = arg max

|C|
n X
X

θj ,p(cj ) i=1 j=1

q(cj |xi ) log p(xi , cj )

12

UNSUPERVISED LEARNING

69

Application of EM to Mixture of Gaussians
This is also called the probabilistic k-means clustering algorithm. We have:
p(xi ) =

|C|
X

p(xi |cj )p(cj )

j=1

=

|C|
X
j=1

"

1
(2π)m/2 |Σ|1/2

−(xi −µj )T Σ

e

−1
(xi −µj )
j

#

2

p(cj )

The E and M steps are as follows:
1. E-step:
p(xj |cj )p(cj )
q(cj |xi ) = P
j p(xi |cj )p(cj )
2. M-step:
p̂(cj ), µ̂j , Σ̂j = arg max
pcj ,µj ,Σj

" n |C|
XX
i=1 j=1

q(cj |xi ) log

1
(2π)m/2 |Σ|1/2

e

−1
−(xi −µj )T Σ
(xi −µj )
j
2

!#

Exercise
Prove the following parameter estimates obtained from the steps of EM algorithm for the mixture
of gaussians.
1. µ̂j =
2. Σ̂j =

Pn

i=1 q(cj |xi )xi

n
Pn

T
i=1 q(cj |xi )(xi −µ̂j ) (xi −µ̂j )
n

3. p̂(cj ) = n1

Pn

i=1 q(cj |xi )

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 18: Clustering: Similarity / Distance measures
Instructor: Ganesh Ramakrishnan

Date: 27/09/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

EM for mixture of gaussians : Issues
1. It is not clear how to decide on the value of k (No. of clusters or mixture components)
2. Only locally optimal
3. No hard partitioning of points (will return a probability distribution for cluster membership)
4. Assumption about cluster shape (ellipsoid and convex)
5. Does not scale well with higher dimensions (primarily due to Σj ’s)
6. Compute intensive (If we have n points in m dimensions and we are finding k clusters, then
each step of clustering takes O(nkm2 ))
7. Not perfectly robust to outliers

13

Clustering

Now we will study various types of clustering algorithms like k-means, k-mediods and so on. These
are special variants of mixture of Gaussians. They also come under the generative model framework.
(P r(x|C)).
The notes will follow the material from Jiawei Han’s texbook, Data Mining: Concepts and
techniques, Chapter 7. Read this in conjunction with the slides present at http://www.cse.iitb.
ac.in/~cs725/notes/classNotes/JaiweiHanDataMining.ppt.
The broad steps in clustering algorithms are as follows:
1. Feature pre-processing on the datapoints
2. Distance/similarity measure formulation
3. Formulation of the objective function
4. Solving the objective function for optimality
(thereby deriving the clusters that the datapoints belong to.)

13.1

Similarity Measures for Clustering

Consider a set of n feature vectors that describe various aspects about customers in a supermarket.
Let the features be denoted by
φ = {φ1 . . . φm1 φm1 +1 . . . φm2 φm2 +1 . . . φm }
Let there be n such datapoints denoting n customers. There can be 3 different types of features
1. Numeric features: Features such as age and salary which can take a whole range of values.
2. Discrete features: Features such as gender = male, female and marital status = {married,
single}
70

13

CLUSTERING

71

3. Ordinal features: Features where there is some notion of partial/total order among the values.
For instance designation can take values ceo, manager, superintendent, engineer, worker or
car driven can take values {luxury, sports, sedan, compact, mini} or customer class can be
{gold, silver, bronze, none}
Feature preprocessing
Some kind of preprocessing is done on the features so that we dont have features which drastically
vary in the values they take. Usually some kind of normalization is performed across all the values
of a particular feature (column normalization). The other type of normalization across all the
features of a particular datapoint (row normalization) is also useful sometimes, but is rare.
For numeric features, some normalizations are as follows:
1.

φi − φmin
i
max
− φmin
φi
i

2.

φi
φmax
i

3.

φi − φmean
i
φstd
i

∈ [0, 1]

mean
|
j |φi (xj ) − φi

P
(where φmean
is the mean of values and φstd
=
i
i

n

)

For discrete features not much preprocessing is necessary. The ordinal features are mapped to
numeric values and then preprocessing is applied on them.
A thing to note here is that feature processing is not unique to clustering and is widely used in
other machine learning techniques. It significantly helps in classification as well.
Distance measures
The distance (or similarity) metric is denoted by dij (or sij respectively). It is the distance between
any two datapoints i and j. Some examples of distance metrics are as follows:
1. Mahalanobis Distance: Given by the expression ||φ(x) − µ||22 ⇒ (φ(x) − µ)T Σ(φ(x) − µ). EM
algorithm has this in some sense.
2. If φ(x) are numeric / ordinal, then a measure defined (after applying post-column normalization):
m
X
p 1/p
φl (xi ) − φl (xj )
l=1

For different values of p, we get different distances:
(a) p = 1: Manhattan distance
(b) p = 2: Euclidean distance
(c) p > 2: Minkowski distance
3. If φ(x) are binary, we define measures based on contingency matrix defined over any two
features φi and φj .


#(i = 1, j = 1) = p #(i = 1, j = 0) = q

M =
#(i = 0, j = 1) = r #(i = 0, j = 0) = s

13

CLUSTERING

72

if p + q + r + s = n, some symmetric and asymmetric measures
(a) dij = q+r
n : symmetric
q+r
(b) dij = p+s
: symmetric (odd’s ratio)
(c) dij = 1 − (p/n) : asymmetric
(d) dij = 1 − (s/n) : asymmetric
p
) : asymmetric
(e) dij = 1 − ( p+q+r
(Jaccard distance: refer: http://en.wikipedia.org/wiki/Jaccard_index )
4. If φ(x) are discrete then :
k (j))
 dij = 1 − #(φk (i)=φ
: Symmetric measure
n

 Expand φ to multiple binary features φ1 . . . φk , if the original φ, takes k values. Now
we can have the various symmetric and asymmetric measures defined for binary features
above.

5. If φ(x) is a combination of numeric/ordinal and discrete
num/ordinal

+ w2 ∗ dij
tot dij = w1 ∗ ddiscrete
ij

s.t. w1 + w2 = 1, w1 , w2 ∈ [0, 1]

Similarity measures are usually metric measures. So Sij = 1 − dij . Also sometimes they could
be non-metric measures, for instance, cosine similarity given by:
φT (xi )  φ(xj )
||φ(xi )||2 ||φ(xj )||2

Further Reading
1. Jiawei Han, Micheline Kamber: Data Mining: Concepts and Techniques , Chapter 7
2. Hastie, Tibshirani, Friedman: The elements of Statistical Learning Springer Verlag
3. Ian H. Witten, Eibe Frank, Mark A. Hall: Data Mining: Practical Machine Learning Tools
and Techniques: for reference on data structures for efficient clustering / classification.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 19: Clustering: Objective function,
k-means algorithm and its variants
Instructor: Ganesh Ramakrishnan

Date: 30/09/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

13.2

Objective Function

In the case of mixture of Gaussians, the objective function to maximize was lower-bounded as
follows:
LL ≥ Eq (LL) + Hq
In the case of clustering using k-means algorithm, we can write the objective function as :
−

k X
X

φ(x) − µj

2

j=1 x∈Cj

It can be seen as a discrete optimization problem, given by:
#
"
k X
n
X
2
∗
Pij ||φ(x) − µj ||
O = maxPij ,µj −
j=1 i=1

s.t. Pij = 0 or 1
k
X

Pij = 1

j=1

In this optimization program, the region specified by constraints is non-convex. So the entire
program is not convex.
Suppose we have the objective function:
"
O

0

∗

= maxPij ,µj −

k X
n
X

#
2

Pij ||φ(x) − µj ||

j=1 i=1

s.t. Pij ∈ [0, 1]
k
X

Pij = 1

j=1
0

0

We can show that O∗ is a lower bound of O ∗ i.e O∗ ≤ O ∗ . We can approximate the new
0
objective (O ∗ ) function to the old (O∗ ) by
Pij∗ > θ → P̂ij = 1
Pij∗ ≤ θ → P̂ij = 0
73

13

CLUSTERING

74

For some arbitrary threshold θ. (For e.g.: θ = 0.5)
A brute force way of solvinf the problem is computationally infeasible. (O(k n )). One can use a
branch and bound technique (early termination of some branches) to solve the problem. However,
finding the bounds are hard.

13.3

k-means Algorithm

To solve O∗ we can use an algorithm called k-means. It is a batch co-ordinate ascent algorithm on
Pij ’s and µj ’s. At the beginning we have the assumption that the cluster centers are the average if
the points belonging to the cluster. i.e
P
Pij φ(xi )
µj = iP
i Pij
We will start with an arbitrary assignment of points to clusters. The steps of one iteration of
the algorithm are:
Step 1:
P
µj =

Pij φ(xi )
iP
i Pij

Step 2:
"
Pij∗ ∈ arg max
Pij

−

k X
n
X

#
Pij φ(xi ) − µj

2

j=1 i=1

for each i
If

0 2 
Pij = 1 and j ∈ arg max − φ(xi ) − µj
then leave Pij unchanged for that i
j0

else
Pij =


 1


0


0 2 
if j = arg max − φ(xi ) − µj
j0

otherwise
0

Check after every iteration if any new Pij is different from old Pij . If yes continue. If no halt.
Note: An iteration of k-means algorithm is of order O(nk). k-means algorithm is also called
k-centroids algorithm.
Disadvantages of k-means
1. Fixed value of k: So determining the right value of k is very critical to the success of the
approach.
2. Sometimes there is a problem owing to the wrong initialization of µj ’s.
3. Mean in “no-man’s land”: Lack of robustness to outliers.

13

CLUSTERING

13.4

75

Variants of k-means

Some of the variants of k-means are discussed in this section. For more details read Chapter 7 of
Jiawei Han’s book. The variants are k-mediods, k-modes, CLARA and CLARANS.
k-mediods
Here the assumption is µj = φ(xi ) for some value of i. In otherwords, the cluster’s centroid coincides
with one of the actual points in the data. Each step of the k-mediod algorithm is k(n−1)n ∼ O(kn2 )
k-modes
For discrete valued attributes, in the k-modes algorithm we have:
X
 

µj = arg max
δ φl (xi , v) ∀l = 1 . . . m
v∈{1,...Vl } x ∈C
i

j

For continuous valued attributes, we may need to fit some distribution and find the mode for
each feature over the cluster.
CLARA and CLARANS
In CLARA the µ’s should be φ(xi ) only for xi ∈ S where S is a fixed sample i.e. µij = φ(xi ) for
some xi ∈ S. Each step of this algorithm is k ∗ |S| ∗ (n − 1) ∼ O(k|S|(n − 1)) where |S| > k.
CLARANS is same in all respects as CLARA except that S is different in each iteration.

Exercise
1. Write the steps of the k-mediod algorithm.
2. Given the following objective function with the constraints:
#
"
n
k X
X
2
Pij ||φ(x) − µj ||
maxPij ,µj −
j=1 i=1

s.t. Pij ∈ [0, 1]
k
X

Pij = 1

j=1

Check if this is a convex optimization program and solve.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 20: Clustering and MDL, Hierachical Clustering
Instructor: Ganesh Ramakrishnan

Date: 07/10/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

13.5

MDL principle and clustering

The principle of minimum description length (MDL) is a general one and not necessarily specific
to clustering. We can see the clustering objective as one that tries to achieve the MDL objective.
The explanation is as follows:
Consider a small change in the k-means clustering objective. Now the objective also optimizes
over the number of clusters k. So we have,
arg max −
Pij ,µj ,k

k
X
X n

Pij ||φ(xi ) − µj ||2

j=1 i=1

However, letting the algorithm choose the value of k will lead to a case where k = n where each
point is a cluster of its own. This kind of trivial clustering is definitely not desirable.
Now let us consider the problem of communicating the location of points to another person over
a SMS. The more information we pass the more is the cost. So we want to minimize the amout
of information set yet be precise enough so that the other side reconstruct the same set of points
given the information.
In the extreme case we send actual co-ordinates of the points. This is a very costly information
transfer but allows the other person to accurately reconstruct the points.
Another option would be to communicate cluster information. So in this we send across the
cluster centroids, the difference of points with its corresponding centroid and the magnitude of the
difference. So in this case, the amount of information to be sent across is much less given that the
magnitude of the points may be large but their difference will be small. Hence. information to be
encoded is less. This is akin to the MDL principle.
Let us denote the data by D and theory about the data T (cluster information and so on). Let
the information that is to be encoded be denoted by I bits. So we can approximate I(D) as I(D, D)
and is given by the expression:
I(D) ≈ I(D, D) > I(D|T ) + I(T )
where I(D) represents the co-ordinate of every point. I(D|T ) is cluster information of a point
like membership of point to a cluster and relative co-ordinate (difference) of point w.r.t to the corresponding cluster. I(T ) is overall clustering information like number of clusters, order of magnitude
of points in each cluster and means of every cluster.
P (D, T ) is similar in spirit to the Bayes rule. We have P (D, T ) = P (D|T )P (T ) or
log P (D, T ) = log P (D|T ) + log P (T )
So we can modify the original objective as follows:
arg max −
Pij ,µj ,k

k X
n
X

Pij ||φ(xi ) − µj ||2 − γk

j=1 i=1

76

13

CLUSTERING

77

The first term of the objective is I(D—T) and the second term is -I(T). The second term is also
called the regularizer.
In essence, according to the MDL principle, we need to define I(D|T ) and I(T ) and choose T
such that it minimizes I(D|T ) + I(T ). This is also aligned with the Occam Razor principle.

13.6

Hierachical clustering

The choices to be made during this type of clustering are as follows:
1. Bottom-up (agglomerative) vs. Top-down (divisive).
2. Which two clusters to merge (single-link, complete-link, average distance): Merge clusters
that have the least mutual distance. Altenatively, which clusters to break.
3. When to stop merging clusters (closely linked to the distance measure). Stop when the
distance between two clusters is > θ (some threshold). Altenatively, when to stop splitting
the clusters.
Some of the issues are :
1. Can’t undo clustering decision.
2. Lack of flexibility in choice of clustering algorithm
3. Do not scale well.
However, the main advantage of hierarchical clustering is that it is easy to visualize. So a
choosen k from hierarchical clustering can be used in k-means or any other clustering algorithm
run from scratch.
Some of the algoritms studied here were Birch clustering and Chameleon.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 21: Clustering: Miscellaneous topics, Apriori Algorithm
Instructor: Ganesh Ramakrishnan

Date: 08/10/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

13.7

Miscellaneous topics

Observations / Issues with Density-based clustering (DBScan)
1. Distance between any 2 self-elected centers is > .
2. Each cluster is an  ball.
To address Issue 1 we could do the following:
1. A point x is a center if ball(, x) contains at least minimum set of points m.
2. Centres may give up individual cluster and merge with other cluster. (x is only a potential
center)
Grid-based clustering
An algorithm called STING was discussed in class. Some of the salient steps of the algorithm (see
Han’s book for more details)
1. Partition the space recursively according to different levels of resolution.
P
P
2. Compute (n, Xi , Xi2 , distrib type, min, max) for each lowest level cell directly from data.
P
P
3. Compute (n, Xi , Xi2 , distrib type, min, max) for each higher cell successively from the
statistics of its lower level cells (i.e. children)
4. Scan every point. For each point, compute significance tests in all leaves. Find the best fit
and move up.
To find the type of distribution in step 2, we use the concept of goodness-of-fit. Step 3 of the
algorithm is of order O(grid hierarchy size).

Exercise
1. Construct a case where DBScan will discover non-convex clusters.
2. Construct a case where DBScan will discover one cluster inside another.

Further Reading
Read more about goodness-of-fit, MDL, Hypothesis Testing and cross-validation

78

14

ASSOCIATION RULE MINING

14

79

Association Rule Mining

All algorithms so far cluster points. Now we try to cluster features. Get all feature sets that have
count (support) > S. These are called interesting features. A brute force way of doing this is of
order O(2m ) where m is the number of features.

14.1

A-priori Algorithm

This is a smarter way of achieving the same objective. It is in the following spirit: If count(φ1 ) > S
and count(φ2 ) < S (not interesting), then obviously count(φ1 , φ2 ) < S (not interesting). So we will
refrain from looking at such feature pairs.
In general, we construct the following sets

S1 = φ1 |count(φ1 ) > S

S2 = {φi , φj }|φi , φj ∈ S1 , i 6= j, count(φi , φj ) > S
This is count is calculated using implementations of efficient data-structures called inverted
index, precomputed from data. Forward index contains a mapping from examples to features i.e
ei → {φj } where as the inverted index contains the reverse mapping from features to examples that
contain them i.e. φj → {ei }.
In calculating S3 , we have two options :

Option 1: S3 = S1i ∪ S2j S1i ∈ S1 , S2j ∈ S2 , count(S1i ∪ S2j ) > S

Option 2: S3 = S2i ∪ S2j |S2i ∩ S2j | = 1, S2i ∈ S2 , S2j ∈ S2 , count(S2i ∪ S2j ) > S
When we generalize Option 2, we get the following general expression:
 i
j
j
j
j
i
i
i
Sn = Sn−1
∪ Sn−1
|Sn−1
∩ Sn−1
| = n − 1, Sn−1
∈ Sn−1 , Sn−1
∈ Sn−1 , count(Sn−1
∪ Sn−1
)>S
The final set of all interesting sets S ∗ =

m
[

Si

i=1

Excercise
Write the generalized expression for Option 1 above.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 22: Association Rule Mining,
Non-parametric density estimation
Instructor: Ganesh Ramakrishnan

Date: 11/10/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

14.2

Association Rule Mining

3

In data mining, association rule learning is a popular and well researched method for discovering
interesting relations between variables in large databases 4 . Association rules have been introduced
for discovering regularities between products in large scale transaction data recorded by point-ofsale (POS) systems in supermarkets.
Simple Association Rule: The problem of Association Rule can be defined as follows:
Given I={i1 , i2 , . . . , in } be a set of n binary attributes called items. and D = {φ1 , φ2 , . . . , φm } be
a set of transactions called the database, where each phii contains one or many of the attributes in
I. Now the goal is to find an association rule R:
φi1 ∧ φi2 ∧ . . . ∧ φik ⇒ φij
such that Sup(R) > s i.e., Support(φi1 ∧ φi2 ∧ . . . ∧ φik ⇒ φij ) > s and
Conf (R) > c where
Conf (φi1 ∧ φi2 ∧ . . . ∧ φik ⇒ φij ) =

Sup(φi1 , φi2 , . . . .φik , φij )
Sup(φi1 , φi2 , . . . .φik )

(19)

which can be otherwise stated as:
Conf (body ⇒ head) =

Sup(body, head)
Sup(body)

(20)

Types of Association Rule Mining
Association Rule Mining also called Item Set Mining, has following subcategories as well.
1. Constraint based mining: In this type of rule mining, constraints can be placed on what
should be discovered and what should be not.
2. Handling Quantitaive attributes:
3. Multi-level Association Rule: This type of association rule mining gets rules by placing
higher threshold for smaller sets ensuring concrete rules and then in the next level decrease
threshold to get ruels for next level and so on.
3 Lecture scribed by Kedhar
4 http://en.wikipedia.org/wiki/Association_rule_learning

80

14

ASSOCIATION RULE MINING

81

Figure 21: Figure showing constrained clustering

14.3

Classification Methods

Classification methods can be classified into three categories depending upon human intervention.
They are:
 Supervised methods: These methods require human supervision. They are classified further as:

– Non Metric Classifier learning
– Probabilistic and generative approaches like Naive Bayes and Gradient Descent etc.
 Unupervised methods: These type of methods do not require any sort of human intervention. Some examples are:

– Clustering
– Association rule mining
 Semi-supervised: These type of methods require some sort of human intervention in some
stages. Some examples are:

– Active Learning: In this approach, there is some input from the user on the instance to
be used to learn some rules or do some classification.
– Active Labelling: User will supervise the system on what features should be used for the
problem.
– Several other graphical model learning techniques

15

NON PARAMETRIC DENSITY ESTIMATION AND CLASSIFICATION

15

82

Non parametric density estimation and classification

Consider D = {φ(x), C(x)} be the set of input, where C(x) is the class to which x belong to. Now
given the instance x, the problem is to classify it into one of the classes. Using the Bayes theorem,
we have:
Pr(C/x) = Pr(x/C)∗Pr(C)
Pr(x)

15.1

Histogram Method

: Let x1 , x2 , . . . , xn be 1-dimensional data points. To classify these n points, in this method,
construct ‘t0 bins, each of same width. Populate the t bins with these instances (as in histogram
completion).
Let x ∈ Bi , then
|Bi |
(21)
Pr(x) = Pn
j=1 |Bj |
Using the histogram computaion, we can do histogram seperately for everey class to compute
Pr(x/C). Extending the concept to instances with m-dimensions, the number of bins would be
tm , which increases exponentially with the dimensions of the instances. Hence, this method do not
seem to be a good one.
If Pr(x) ∼true density (Pr(x) can be replaced by Pr(x/C)).
Now consider area A given by PA .
Z
PA = P (x ∈ A) = Pr(x)dx = Px ∗ |A|
(22)
if A is small. Now considering
 k points from T, we have
P (k points from T ∈ A)= nr ∗ (PA )k ∗ (1 − PA )n−k (Binomial distribution)
Then the expectation,
E(number of points that lie in A) = E(k) = nPA .
Its variance is given by var(k) = n ∗ PA ∗ (1 − PA ).
These deriviations are key fot K-Nearest Neighbours and Parzen Window Classifier.

15.2

K-Nearest Neighbour and Parzen Window Classifier

In the section 15.1, if k ≈ n ∗ PA and PA ≈ Px ∗ |A|, we have
Px ≈

k
n ∗ |A|

(23)

In 23, We fix the value of k and determine A in which these k lie. This is K-Nearest Neighbour
classifier. Otherwise, fix the region A and then determine k based on the training sample, this is
Parzen window kernel density classifier.

15

NON PARAMETRIC DENSITY ESTIMATION AND CLASSIFICATION

83

Figure 22: Figure showing clustering using histogram method

K-Nearest Neighbour classification
In this method, the goal is to find out the K-nearest neighbours to the given instance x∗ .
k
Now, Pr(x) = n∗|A|
.
1
Let x1 , x2 , . . . .xk be the K-nearest neighbours and let kj be the number of points from K-NN that
belong to class Cj .
kj
n ∗ |A|

(24)

kj
kj
n∗|A| ∗ Pr(Cj )
=
∗ Pr(Cj )
k
k
n∗|A|

(25)

Pr(x/Cj ) =
and
Pr(Cj /x) =

From the above equation, it can be understood that Standard KNN takes uniform Pr(C − j).

15

NON PARAMETRIC DENSITY ESTIMATION AND CLASSIFICATION

84

Now the class(C∗ ) to which x∗ belong to can obtained as:
C∗ = argmaxCj

kj
∗ Pr(Cj )
k

(26)

Notes:K-Nearest Neighbour classifier is also called memory based classifier. Its a lazy classifier
and non-smooth one.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 23: Non-parametric density estimation,
Probabilistic discriminative classification models
Instructor: Ganesh Ramakrishnan

Date: 14/10/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

15.3

Kernel density estimators

Let us consider a hypercube of dimension h. Assume that the volume is fixed (alternately h or σ
(in case of smoother version - see below)). ph (x) is given by:
Kh (x)
Kh (x)
=
nV
nhm
n
X K(x, xi
=
nhm
i=1

ph (x) =

In the case of Rectangular kernel, K is given by:
(
1
iff |x − xi | ≤ [h/2 h/2 . . . h/2]Tmdim
K(x, xi ) =
0
otherwise
In the smoother version called the Gaussian kernel, we have pσ (x) as
n

1X
Kσ (x, xi )
pσ (x) =
n i=1
where Kσ is given by:

||x−xi ||2
1
√ e− 2σ2
σ 2π
m
Generally, we can absorb h in the K function and we have,

Kσ =

n

1X
K(x, xi )
n i=1
1 X
K(x, xi )
p(x|cj ) =
nj x ∈c
p(x) =

i

p(cj |x) =

j

p(x|cj )p(cj )
p(x)

(by Bayes’s rule)
X
arg max p(cj |x) = arg max p(cj ) × (1/nj )
K(x, xi )
j

j

= arg max
j

xi ∈cj

1 X
n x ∈c
i

j

85

K(x, xi )

(since p(cj ) = nj /n)

16

DISCRIMINATIVE CLASSIFICATION

86

The equation above is of the parzen window classifier.
Unfortunately, this requires the kernel to be evaluated on too many points, which translates to
high memory and computation requirements.
Note: Kernel density estimation on a sparse set of points (instead of all points like before; can
we do kernel density estimation on a “good” set of points ?). This is one way of looking at Support
Vector Machines(to be seen later). This can also be seen as a weighted kernel density estimation
p(cj |x) ∝

n
X

αi K(x, xi )

i=1

where αi ’s are the parameters to be discovered and are in some range. Also most αi ’s are 0. This
gives the sparsity that we discussed before.

16

Discriminative Classification

Most models seen so far try to model the likelihood of the data i.e p(x|cj ). So we indirectly obtain
p(cj |x) using the Bayes’ rule:
p(x|cj )p(cj )
p(cj |x) =
p(x)
What if we model p(cj |x) directly ? This is called probabilistic discriminative classification
model.

16.1

Maximum Entropy models

Given no other information, if we have to model p(cj |x), we have to consider a uniform distribution.
When there is a uniform distribution, the entropy has the maximum value. Therefore, in this
paradigm, we try to maximize the entropy. Hence the name Maximum entropy models.
maxp(cj |xi ) −

|c|
n X
X

p(cj |xi ) log p(cj |xi )

i=1 j=1

s.t. (1)

|c|
n X
X

n

p(xi , cj )φl (xi , cj ) =

i=1 j=1

1 X
φl (x, c(xi ))
n|c| i=1

, ∀l

i.e. Ep(xi ,cj ) (φl ) = Avg(φl )

(expected entropy w.r.t distribution = actual entropy seen in data)
X
(2)
p(cj |xi ) = 1, ∀i and p(cj |xi ) ∈ [0, 1]
j

The above formaluation is a concave optimization program. Optimality occurs at (see practice
h/w 2, problem 3):
− 1 − log p(cj |xi ) +

m
X
l=1

e

⇒p(cj |xi ) = P|c|

Pm

i=1 λl φl (xi ,cj )

e
j =1
0

Pm

0

2
λl φl (xi , cj ) + ηi + θij − θij
=0

i=1 λl φl (xi ,cj 0 )

16

DISCRIMINATIVE CLASSIFICATION

87

Where λl parameters are obtained from the 1st constraint and η and
Pmθ from the 2nd constraint.
We can show that the equivalent dual problem (using p(cj |xi ) ∝ e i=1 λl φl (xi ,cj ) ) as:
maxλl LL = maxλl

n
X

log p(c(xi )|xi )

(27)

i=1

This form of p(cj |xi ) is an important element of the exponential family of distributions. (See
further reading below for a detailed description of exponential family)
e.g.: Logistic Regression

Assume φl,cj (x, c) is a set of features indexed by pair (l, cj ), ∀cj and ∀l. The corresponding
parameters are λl,cj . Also assume that:
(
φl (x)
iff c = cj
φl,cj (x, c) =
0
otherwise
Now p(cj |x) is given by:
p(cj |x) ∝ e

P

l,ck λl,ck φl,ck (x,cj )

P

=e

l λl,cj φl (x)

And the classifier C ∗ is given by:
C ∗ = arg max
cj

X λ φ (x)
e l,cj l
l,cj

this is also called the logistic regression classifier. The logistic regression classifier’s decision
surface is linear in the φ space.
Note: How to learn λ ?
1. Gradient descent: Updates are given by (for the dual problem in Eq. 27):
λnew = λold − α∇LL
. Where the jth component of ∇LL is given by:
n
X

φl (xi , c(xi )) −

i=1

|c|
n X
X

pold (cj |xi )φl (xi , cj )

i=1 j=1

Here, pold (cj |xi )φl (xi , cj ) is computed using λold
2. Newton method: Updates are given by
λnew = λold − (∇2 LL)−1 ∇LL
. ∇2 LL is given by: ∇2 LL = φT M φ

16

DISCRIMINATIVE CLASSIFICATION

88

Further Reading
Exponential family : Read Section 7.4 of http://www.cse.iitb.ac.in/~cs725/notes/classNotes/
misc/CaseStudyWithProbabilisticModels.pdf

Exercise
Write the expression for M in the Newton updates expression of ∇2 LL.
See Convex optimization notes section 4.5.2.(http://www.cse.iitb.ac.in/~cs725/notes/classNotes/
BasicsOfConvexOptimization.pdf)

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 24: Graphical models primer
Instructor: Ganesh Ramakrishnan

Date: 18/10/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

17

Graphical Models

In this lecture a general introduction to graphical models was presented. The two broad categories of
graphical models namely undirected and directed models were discussed. Properties of conditional
independence and how a graph is factored based on this was also discussed. It was stressed upon
that the absence of an edge is more important than the presence of an edge.
Some ways of inferencing in graphical models were briefly touched upon.

Further Reading
1. Graphical Models slides presented in class : http://www.cse.iitb.ac.in/~cs725/notes/
classNotes/graphicalModels.ppt
2. Detailed graphical models notes : http://www.cse.iitb.ac.in/~cs725/notes/classNotes/
misc/CaseStudyWithProbabilisticModels.pdf

89

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 25: Linear Models, Regression, Least Squared Error
Instructor: Ganesh Ramakrishnan

Date: 21/10/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

18

Generalized Models for Classification

The goal in classification is to take an input vector x and assign it to one of K discrete classes Ck
where k = 1, ..., K. In most cases, the classes are taken to be disjoint, so that each input is assigned
to one and only one class. The input space is thus divided into decision regions whose boundaries
are called decision boundaries or decision surfaces. We consider only linear models for classification
in this lecture, which means that the decision surfaces are linear functions of the input vector x
and hence are defined by (D − 1)-dimensional hyperplanes within the D-dimensional input space.
The simplest method of classification (for 2 classes) is to design a function f such that
(
vc+ if xi ∈ C+
f (xi ) =
vc− if xi ∈ C−
Three broad types of classifiers
1. The first method involves explicit construction of w for wT φ(x) = 0 as the decision surface.
2. The second method is to model P (x|C+ ) and P (x|C− ) together with the prior probabilities
P (Ck ) for the classes, from which we can compute the posterior probabilities using Bayes’
theorem
P (x|Ck )P (Ck )
P (Ck |x) =
P (x)
These types of models are called generative models.
3. The third method is to model P (C+ |x) and P (C− |x) directly. These types of models are called
discriminative models. In this case P (C+ |x) = P (C− |x) gives the required decision boundary.

18.1

Generalized linear models

In these models we adopt linear regression to model the classification problem. This is done by
modeling a function f as follows:
f (x) = g(wT φ(x))
where g is known as activation function and φ the vector of basis functions. Classification is achieved
by:
(
vc+ if θ > 0
g(θ) =
vc− if θ < 0
The decision surface in this case is given by wT φ(x) = 0
90

18

GENERALIZED MODELS FOR CLASSIFICATION

91

Examples
An example of generative model is as follows:
P (x|C+ ) = N (µ+ , Σ)
P (x|C− ) = N (µ− , Σ)
With prior probabilities P (C+ ) and P (C− ) known, we can derive P (C+ |x) and P (C+ |x). In this
case it can be shown that the decision boundary P (C+ |x) = P (C− |x) is a hyperplane.
An example of discriminative model is
T

P (C+ |x) =

ew φ(x)
1 + ewT φ(x)

P (C− |x) =

1
1 + ewT φ(x)

Examples of first model (which directly construct the classifier) include
 Linear Regression
 Perceptron
 Fisher’s Discriminant
 Support Vector Machines

18.2

Handling Multiclasses

We now consider the extension of linear discriminants to K > 2 classes. One solution is to buid a
K-class discriminant by combining a number of two-class discriminant functions.
 one-versus-the-rest: In this approach, K − 1 classifiers are constructed, each of which separtes
the points in a particular class Ck from points not in that classes
 one-versus-one: In this method, K C2 binary discriminant functions are introduced, one for
every possible pair of classes.

Attempting to construct a K class discriminant from a set of two class discriminants leads to
ambiguous regions. The problems with the first two approaches are illustrated in Figures 23 and
24, where there are ambiguous regions marked with ’ ?’.
Avoiding ambiguities
We can avoid above mentioned difficulties by considering a single K-class discriminant comprising
K functions gCk (x). Then x is assigned to a class Ck that has the maximum value for gCk (x)
If gCk (x) = wCTk φ(x) the decision boundary between class Cj and class Ck is given by gCk (x) =
gCj (x) and hence corresponds to
(wCTk − wCTj )φ(x) = 0

18

GENERALIZED MODELS FOR CLASSIFICATION

92

Figure 23: Illustrates the ambiguity in one-versus-rest case

Figure 24: Illustrates the ambiguity in one-versus-one case

18.3

Least Squares approach for classification

We now apply the Least squares method to the classification problem. Consider a classification
problem with K classes. Then the target values are represented by a K component target vector
t. Each class is described by its own model
yk (x) = wkT φ(x)
where k ∈ {1, ...K}. We can conveniently group these together using vector notation so that
y(x) = WT φ(x)
where W is a matrix whose k th column comprises the unknown parameters wk and φ(x) is the
vector of basis function values evaluated at the input vector x. The procedure for classification is
then to assign a new input vector x to the class for which the output yk = wkT φ(x) is largest.
We now determine the parameter matrix W by minimizing a sum-of-squares error function.
Consider a training data set {xn , tn } where n ∈ {1, .., N }, where xn is input and tn is corresponding
target vector. We now define a matrix Φ whose nth row is given by φ(xn ).


φ0 (x1 ) φ1 (x1 ) . . . φK−1 (x1 )


 φ0 (x2 ) φ1 (x2 ) . . . φK−1 (x2 ) 

Φ=
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


φ0 (xN ) φ1 (xN ) . . . φK−1 (xN )

18

GENERALIZED MODELS FOR CLASSIFICATION

93

Figure 25: Data from two classes classified by least squares (magenta) and logistic (green)

Figure 26: Response of the classifiers to addition of outlier points
We further define a matrix T whose nth row is given by the vector tTn . Now, the sum-of-squares
error function can then be written as
err(W) =

1
T r{(ΦW − T)T (ΦW − T)}
2

We can now minimize the error by setting the derivative with respect to W to zero. The solution
we obtain for W is then of the form
W = (ΦT Φ)−1 ΦT T
Limitations of Least Squares
Even as the least-squares approach gives a closed form solution for the discriminant function parameters, it suffers from problems such as lack of robustness to outliers. This is illustrated in Figures
25 and 26 where we see that introduction of additional data points in the Figure 26 produce a
significant change in the location of the decision boundary, even though these points would be
correctly classified by the original boundary in Figure 25. For comparison, least squares approach
is contrasted with logisitc regression, which remains unaffected due to the additional points.

19

REGRESSION

19

94

Regression

Suppose there are two sets of variables x ∈ <n and y ∈ <k such that x is independent and y
is dependant. The regression problem is concerned with determining y in terms of x. Let us
assume that we are given m data points D = hx1 , y1 i, hx2 , y2 i, .., hxm , ym i. Then the problem is
to determine a function f ∗ such that f ∗ (x) is the best predictor for y, with respect to D. Suppose
ε(f, D) is an error function, designed to reflect the discrepancy between the predicted value f (x0 )
of y0 and the actual value y0 for any hx0 , y0 i ∈ D, then
f ∗ = arg min ε(f, D)

(28)

f ∈F

where, F denotes the class of functions over which the optimization is performed.

19.1

Motivating Example : Curve Fitting

Learn f : X → Y such that E(f, X, Y1 ) is minimized. Here the error function E and form of the
function to learn f is chosen by the modeler.
Consider one such form of f ,
f (x) = w0 + w1 x + w2 x2 + ... + wt xt
The sum of squares error is given by,
m

E=

1X
(f (xi ) − yi )2
2 i=1

So the expression is,
K

1X
[(w0 + w1 x + w2 x2 + ... + wt xt ) − y1 (i)]2
arg min
w=[w1 ,w2 ,...wt ] 2 i=1
If there are m data points, then a polynomial of degree m − 1 can exactly fit the data, since the
polynomial has m degrees of freedom (where degrees of freedom=no. of coefficients)
As the degree of the polynomial increases beyond m, the curve becomes more and more wobbly,
while still passing through the points. Contrast the degree 10 fit in Figure 28 against the degree 5
fit in Figure 27. This is due to the problem of overfitting (overspecification)
Now E is a convex function. To optimize it, we need to set ∇w E = 0. The ∇ operator is also
called gradient.
Solution is given by,
X = (φt φ)−1 φt Y
If m << t then
 φ becomes singular and the solution cannot be found OR
 The column vectors in φ become nearly linearly dependent

19

REGRESSION

95

Figure 27: Fit for degree 5 polynomial.

RMS (root mean sqare) error is given by :
r
RM S =

2E
k

Generally, some test data (which potentially could have been part of the training data) is held
out for evaluating the generalized performance of the model. Another held out fraction of the
training data, called the validation dataset is typically used to find the most appropriate degree
tbest for f .

19.2

Linear regression and method of least squares error

Depending on the function class we consider, there are many types of regression problems. In Linear
regression we consider
Pp only linear functions, functions that are linear in the basis function. Here
F is of the form { i=1 wi φi (x)}. φi : Rn → Rk Here, the φi ’s are called the basis functions (for
example, we can consider φi (x) = xi , i.e., polynomial basis functions) .
Any function in F is characterized by its parameters, the wi ’s. Thus, in (28) we have to find
f (w∗ ) where
w∗ = arg minε(w, D)
w

Least square solution
The error function ε plays a major role in the accuracy and tractability of the optimization problem.
The error function is also called the loss function. The squared loss is a commonly used loss
function. It is the sum of squares of the differences between the actual value and the predicted

19

REGRESSION

96

Figure 28: Fit for degree 10 polynomial. Note how wobbly this fit is.

value.
ε(f, D) =

X

(f (xi ) − yi )2

hxi ,yi i∈D

So the least square solution for linear regression is given by
w∗ = arg min
w

p
m
X
X
j=1

(wi φi (xj ) − yj

2

i=1

The minimum value of the squared loss is zero. Is it possible to achieve this value ? In other
p
X
words is ∀j,
wi φi (xj ) = yj possible ?
i=1

The above equality can be written as ∀u, φT (xu )w = yu
or equivalently
φw = y where




φ1 (x1 ) · · · φp (x1 )
y1




..
..
..
 and y =  .. 
φ=
.
.
.


 . 
φ1 (xm ) · · · φp (xm )
ym
It has a solution if y is in the column space (the subspace of Rn formed by the column vectors)
of φ. It is possible that there exists no w which satisfies the conditions? In such situations we can
solve the least square problem.

19

REGRESSION

97

C(φ)
ŷ

y

Figure 29: Least square solution ŷ is the orthogonal projection of y onto column space of φ
Geometrical interpretation of least squares
Let ŷ be a solution in the column space of φ. The least squares solution is such that the distance
between ŷ and y is minimized. From the diagram it is clear that for the distance to be minimized,
the line joining ŷ to y should be orthogonal to the column space. This can be summarized as
1. φw = ŷ
2. ∀v ∈ {1, ..p}, (y − ŷ)T φv = 0 or (ŷ − y)T φ = 0

ŷT φ

= yT φ

T

ie, (φw) φ

= yT φ

T

T

ie, w φ φ

= yT φ

ie, φT φw

= φT y

∴ w

= (φT φ)−1 y

In the last step, please note that, φT φ is invertible only if φ has full column rank.
Theorem: If φ has full column rank, φT φ is invertible. A matrix is said to have full column rank
if all its columnPvectors are linearly independent. A set of vectors vi is said to be linearly
independent if i αi vi = 0 ⇒ αi = 0.
Proof: Given that φ has full column rank and hence columns are linearly independent, we have
that φx = 0 ⇒ x = 0.
Assume on the contrary that φT φ is non invertible. Then ∃x 6= 0 3 φT φx = 0.
⇒ xT φT φx = 0
⇒ (φx)T φx = ||φx||2 = 0
⇒ φx = 0. This is a contradiction. Hence the theorem is proved.

19

REGRESSION

19.3

98

Regularised solution to regression

In last lecture, we derived solution for the regression problem formulated in least-squares sense
which was aimed at minimizing rms error over observed data points. We also analysed conditions
under which the obtained solution was guaranteed to be a global minima. However, as we observed,
increasing the order of the model yielded larger rms error over test data, which was due to large
fluctuations in model learnt and consequently due to very high values of model coefficients (weights).
In this lecture, we discuss how the optimization problem can be modified to counter very large
magnitudes of coefficients. Subsequently, solution of this problem is provided through lagrange
dual formulation followed by discussion over obtained solution and impact over test data. Towards
the end of the lecture, a very gentle introduction to axiomatic probability is provided.
Problem formulation
In order to cease coefficients from becoming too large in magnitude, we may modify the problem
to be a constrained optimization problem. Intuitively, for achieving this criterion, we may impose
constraint on magnitude of coefficients. Any norm for this purpose might give good working solution. However, for mathematical convenience, we start with the euclidean (L2 ) norm. The overall
problem with objective function and constraint goes as follows:

minimize

(Φw − Y )T (Φw − Y )

such that

||w||22 ≤ ξ

w

(29)

As observed in last lecture, the objective function, namely f (w) = (Φw−Y )T (Φw−Y ) is strictly
convex. Further to this, the constraint function, g(w) =k w k22 −ξ, is also a convex function. For
convex g(w), the set S = {w|g(w) ≤ 0}, can be proved to be a convex set by taking two elements
w1 ∈ S and w2 ∈ S such that g(w1 ) ≤ 0 and g(w2 ) ≤ 0. Since g(w) is a convex function, we have
the following inequality:
g(θw1 + (1 − θ)w2 ) ≤ θg(w1 ) + (1 − θ)g(w2 )
≤ 0; ∀θ ∈ [0, 1], w1 , w2 ∈ S

(30)

As g(θw1 + (1 − θ)w2 ) ≤ 0; ∀θ ∈ S, ∀w1 , w2 ∈ S, θw1 + (1 − θ)w2 ∈ S, which is both sufficient
and necessary for S to be a convex set. Hence, function g(w) imposes a convex constraint over the
solution space.
Bound on λ in the regularized least square solution
As discussed earlier, we need to minimize the error function subject to constraint w≤ ξ . Applying
KKT conditions to this problem, if w∗ is a global optimum then from the first KKT condition we
get,
∇w∗ (f (w) + λg(w)) = 0
where, f (w) = (Φw − Y )T (Φw − Y ) and g(w) = kwk2 − ξ
Solving we get,
2(ΦT Φ)w∗ − 2ΦT − 2λw∗ = 0

(31)

19

REGRESSION

99

i.e.
w∗ = (ΦT Φ + λI)−1 ΦT y

(32)

From the second KKT condition we get,
kw∗ k2 ≤ ξ

(33)

λ≥0

(34)

λkw∗ k2 = λξ

(35)

From the third KKT condition,

From the fourth condition

Thus values of w∗ and λ which satisfy all these equations would yield an optimum solution.
Consider equation (32),
w∗ = (ΦT Φ + λI)−1 ΦT y
Premultiplying with (ΦT Φ + λI) on both sides we have,
(ΦT Φ + λI)w∗ = ΦT y
∴ (ΦT Φ)w∗ + (λI)w∗ = ΦT y
∴ k(ΦT Φ)w∗ + (λI)w∗ k = kΦT yk
By triangle inequality,
k(ΦT Φ)w∗ k + (λ)kw∗ k ≥ k(ΦT Φ)w∗ + (λI)w∗ k = kΦT yk

(36)

Now , (ΦT Φ) is a nxn matrix which can be determined as Φ is known .
k(ΦT Φ)w∗ k ≤ αkw∗ k for some α for finite |(ΦT Φ)w∗ k. Substituting in previous equation,
(α + λ)kw∗ k ≥ kΦT yk
i.e.
λ≥

kΦT yk
−α
kw∗ k

(37)

Note that when kw∗ k → 0, λ → ∞. This is obvious as higher value of λ would focus more on
reducing value of kw∗ k than on minimizing the error function.
kw∗ k2 ≤ ξ
Eliminating kw∗ k from the equation (14) we get,
∴λ≥

kΦT yk
√
−α
ξ

(38)

This is not the exact solution of λ but the bound (15) proves the existance of λ for some ξ and Φ.

19

REGRESSION

100

Figure 30: RMS error vs. degree of polynomial for test and train data

RMS Error variation
Recall the polynomial curve fitting problem we considered in earlier lectures. Figure 30 shows RMS
error variation as the degree of polynomial (assumed to fit the points) is increased. We observe
that as the degree of polynomial is increased till 5 both train and test errors decrease. For degree
> 7, test error shoots up. This is attributed to the overfitting problem (The datasize for train set
is 8 points.)
Now see Figure 31 where variation in RMS error and Lagrange multiplier λ has been explored
(keeping the polynomial degree constant at 6). Given this analysis, what is the optimum value of λ
that must be chosen? We have to choose that value for which the test error is minimum (Identified
as optimum in the figure.).
Alternative objective function
Consider equation (31). If we substitute g(w) = kwk2 − ξ, we get
∇w∗ (f (w) + λ · (kwk2 − ξ)) = 0

(39)

min(k Φw − y k2 +λ k w k2 )

(40)

This is equivalent to finding
For same λ these two solutions are the same.This form or regression is known as Ridge regression.
If we use L1 norm then it’s called as ’Lasso’. Note that w∗ form that we had derived is valid only
for L2 norm.

19.4

Linear Regression : Drawbacks

The following are the problems with linear regression model for classification:

19

REGRESSION

101

Figure 31: RMS error vs. 10λ for test and train data (at Polynomial degree = 6)

1. Sensitivity to outliers
2. Masking
Sensitivity to outliers
Outliers : They are points which have noise and adversely affect the classification.

Figure 32: Outliers

In the right hand figure , the separating hyperplane has changed because of the outliers.

19

REGRESSION

102

Masking
It is seen empirically that linear regression classifier may mask a given class. This is shown in
the left hand figure. We had 3 classes one in between the other two. The between class points are
not classified.

Figure 33: Masking
The right hand figure is the desirable classification.
The equation of the classifier between class C1(red dots) and class C2(green dots) is
(ω1 − ω2 )T φ(x) = 0
and the equation of the classifier between the classes C2(green dots) and C3(blue dots) is
(ω2 − ω3 )T φ(x) = 0

19.5

Possible solutions

1. Mapping to new space
We will transform the original dimensions to new dimensions. New dimensions are function
of original dimensions. This is a work around solution.
0

φ1 (x) = σ1 (φ1 , φ2 )
0
φ2 (x) = σ2 (φ1 , φ2 )

0

0

Here we try to determine the transformations φ1 and φ2 such that we can get a linear
classifier in this new space. When we map back to the original dimensions , the separators
may not remain linear.
0

Problem : Exponential blowup of number of parameters (w s) in order O(nk−1 ).

19

REGRESSION

103

Figure 34: Mapping back to original dimension class separator not linear
2. Decision surface perpendicular bisector to the mean connector.

Figure 35: Class separator perpendicular to the line joining mean

Decision surface is the perpendicular bisector of the line joining mean of class C1 (m1 ) and
mean of class C2 (m2 ).
m1 = (1/N1 )
class C1 .

P

m2 = (1/N2 )
class C2 .

P

n∈C1 xn where m1 is the mean of class C1 and N1 is the number of points in

n∈C2 xn where m2 is the mean of class C2 and N2 is the number of points in

||φ(x) − m1 || < ||φ(x) − m2 || => x ∈ C1

19

REGRESSION

104

||φ(x) − m2 || < ||φ(x) − m1 || => x ∈ C2

Comment : This is solving the masking problem but not the sensitivity problem as this
does not capture the orientation(eg: spread of the data points) of the classes.
3. Fisher Discrimant Analysis.
Here we consider the mean of the classes , within class covariance and global covariance.
Aim : To increase the separation between the class means and to minimize within class
variance. Considering two classes.
SB is Inter class covariance and SW is Intra class covariance.
m1 = (1/N1 )
class C1 .

P

m2 = (1/N2 )
class C2 .

P

n∈C1 xn where m1 is the mean of class C1 and N1 is the number of points in

n∈C2 xn where m2 is the mean of class C2 and N2 is the number of points in

N1 + N2 = N where N is the total number of training points.
SB = (m2 − m1 )(m2 − m1 )T
SW =

P

n∈C1 (xn − m1 )(xn − m1 )

T

+

T
n∈C2 (xn − m2 )(xn − m2 )

P

J(w) = (wT SB w)/(wT Sw w)
By maximizing J(w) we get the following:
−1
(m2 − m1 )
wαSw

Summary
Sensitivity to outliers

Masking

Perpendicular Bisector of means connector

Does not solve

Solves

Fischer Discriminant

Does not solve

Solves

We have seen that the fisher discriminant analysis is better compared to the other two possible
solutions.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 26: Perceptron Algorithm, Support Vector Machines
Instructor: Ganesh Ramakrishnan

Date: 02/11/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

20

Perceptron Algorithm

We saw a class of classifiers that model wT φ(x) directly. Among them were least squared error
classification, perpendicular bisector of line connecting the mean points and fisher discriminant
analysis. All these models have the problem that they are not robust to outliers. They are extremely
sensitive to them, in the sense that a few outlier points can drastically change the position and
orientation of the decision surface.

20.1

Introduction

Desirables for avoiding sensitivity to outliers
1. Few points properly classified and far away from the separating surface (decision boundary)
should not influence the decision boundary much.
2. (Possibly) few misclassified points far away from the separating surface should also not influence the decision boundary.
In Perceptron algorithm the main idea is to learn w (for wT φ(x) = 0) only from misclassified
examples weighing them by their distance from the separating hyperplane.
A misclassified example is defined as
wT φ(xi ) > 0 for yi = −1
wT φ(xi ) < 0 for yi = +1
Combining the above two equations we get,
yi wT φ(xi ) < 0

20.2

Training algorithm

As said earlier, perceptron explicitly accounts for the signed distribution of misclassified points from
hyperplane. wT φ(x) = 0.
Distance from hyperplane can be calculated as follows

105

20

PERCEPTRON ALGORITHM

106

wT φ(x) = 0
φ(x0 )
φ(x)
D
w
D = wT (φ(x) − φ(x0 )
Since wT (φ(x0 )) = 0, we get distance = wT (φ(x)). Note: We study perceptron (and later SVM)
for 2-class classification problems only. We label them as y=1 and y=-1. A point is misclassified if
yi wT (φ(x)) < 0
Algorithm 2 Perceptron Algorithm
w=ones() {Initialization}
loop
if given < x, y >, wT Φ(x).y ≤ 0 then
w = w + Φ(x).y
end if
end loop

Intuition
T
ywk+1
φ(x)

=

y(wk + yφ(x)T φ(x)

= ywkT φ(x) + y 2 kφ(w)k2
>

ywkT φ(x)

Note: We applied the update for this point, (since ywkT φ(x) ≤ 0) We have ywkT φ(x) > ywkT φ(x).
So we have more hope that this point is classified correctly now. More formally, perceptron tries
to minimize the error function
X
E=−
yφT (x)ω
x∈M

where M is the set of misclassified examples.

20

PERCEPTRON ALGORITHM

107

Stochastic Gradient Descent algorithm
Perceptron algorithm is similar (Its not exactly equivalent)
X to a gradient descent algorithm, which
can be shown as follows: Since ∇E is given by ∇E = −
yφ(x). So,
x∈M

wk+1 = wk − η∇E
X
= wk + η
yφ(x)

(This takes all misclassified points at a time)

x∈M

But what we are doing in standard Perceptron Algorithm, is basically Stochastic Gradient
Descent:
X
X
∇E = −
yφ(x) = −
∇E(x) , where E(x) = yφ(x)
x∈M

x∈M

wk+1 = wk − η∇E(x)
(for any x ∈ M )

= wk + ηyφ(x)

If ∃ an optimal separating hyperplane with parameters w∗ such that,
φT (x)w∗ = 0
then perceptron algorithm converges.
Proof :lim kwk+1 − ρw∗ k2 = 0

k→∞

(If this happens for some constant ρ, we are fine.)

kwk+1 − ρw∗ k2 = kwk − ρw∗ k2 + kyφ(x)k2 + 2y(wk − ρw∗ )T φ(x)
Now, we want L.H.S. to be less than R.H.S. at every step, although by some small value, so
that perceptron will converge overtime.
So, if we can obtain an expression of the form:
kwk+1 − ρw∗ k2 < kwk − ρw∗ k2 − θ2
Then, kwk+1 −ρw∗ k2 is reducing by atleast θ2 at every iteration. So, from the above expressions,
we need to find θ such that,
kφ(x)k2 + 2y(wk − ρw∗ )T φ(x) < −θ2
(Here, kyφ(x)k2 = kφ(x)k2 because kyk = 1, y is either +1 or −1)


∗ 2
k
So, the no. of iterations would be: O kw0 −ρw
2
θ
Some observations
1. ywkT φ(x) ≤ 0 (∵ x was misclassified)

21

SUPPORT VECTOR MACHINES

108

2. Γ2 = max kφ(x)k2
x∈D

3. δ = max −2yw∗ T φ(x)
x∈D

Here, margin = w∗ T φ(x) = dist. of closest point from hyperplane and, D is the set of all points,
not just misclassifed ones.
δ = max −2yw∗ T φ(x)
x∈D

= min yw∗ T φ(x)
x∈D

Since, w∗ T φ(x) ≥ 0, so, δ ≤ 0. So, what we are interested in, is the ’least negative’ value of δ
From the observations, and eq.(2), we have:
0 ≤ kwk+1 − ρw∗ k2 ≤ kwk − ρw∗ k2 + Γ2 + ρδ
Taking, ρ =

2Γ2
, then,
−δ

0 ≤ kwk+1 − ρw∗ k2 ≤ kwk − ρw∗ k2 − Γ2

Hence, we have, Γ2 = θ2 , that we were looking for in eq.(3). ∴ kwk+1 − ρw∗ k2 decreases by atleast
Γ2 at every iteration.
Here the notion of convergence is that wk converges to ρw∗ by making atleast some decrement
at each step. Thus, for k → ∞, kwk − ρw∗ k → 0. Hence, the proof of convergence.

20.3

Issues with Perceptron

1. In the non-separable case it may oscillate a lot and is super-sensitive to initialization of nonseparable cases.
2. Can tend to overfit. (when we have very less bias)

21

Support Vector Machines

The main idea behind support vector machines is to find a w that mazimises the unsigned distance
of the closest point to the separating surface.
So we have the formulation as follows:
max
w

max
w

min

(wT φ(xi ) + w0 )yi
||w||

1
||w||

min

i

i

(wT φ(xi ) + w0 )yi

However, the catch is : if w∗ , w0∗ is a solution, then λw∗ , λw0∗ is also a solution.

(41)
(42)

21

SUPPORT VECTOR MACHINES

109

Figure 36: Different types of points

21.1

Canonical SVM problem

Since many solutions are possible by scaling w and w0 as noted above, we restricy our attention to
a canonical (w, w0 ) for which, min(wT φ(xi ) + w0 )yi = 1
i

So we get,
max
w

1
||w||

, s.t. ∀i, (wT φ(xi ) + w0 )yi ≥ 1

(43)

Any scaled solution (w∗ , w0∗ ) to Equation 43 is a solution to Equations 41/42. Equivalent to
Equation 43 is also the following equation (By monotonic transformations)
min||w||2
w

, s.t. ∀i, (wT φ(xi ) + w0 )yi ≥ 1

The above objective ||w||2 is called the regularizer / bias.
Slack: to handle non-separability
2

min ||w|| + c

w,w0

X

ξi

s.t.∀i
yi (φ

T

(44)

i

(45)
(xi )w + w00 ) ≥ 1 − ξi

(46)

where,

(47)

∀iξi ≥ 0

(48)

In soft margin we account for the the errors. The above formulation is one of the many formulation
of soft SVMs. In the above formulation, large value of c means overfitting.
Three types of g points
In Figure 36 we can see three types of points. They are:

21

SUPPORT VECTOR MACHINES

1. Correctly classified but ξi > 0 or violates margin
2. Correctly classified but ξi = 0 or on the margin
3. Inorrectly classified but ξi > 1

110

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 27: SVM: Dual Formulation, Notion of Kernel
Instructor: Ganesh Ramakrishnan

Date: 05/11/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

21.2

SVM : Dual Formulation

Primal formulation
p∗ = min f (x)

(49)

x∈D

(50)

s.t. gi (x) ≤ 0

(51)

i = 1, . . . , m

(52)

Dual Formulation
d∗ = max min f (x) +
λ∈R x∈D

m
X

!
λi gi (x)

(53)

s.t. λi ≥ 0

(54)

i=1

Equation 53 is and convex optimization problem. Also, d∗ ≤ p∗ and (p∗ − d∗ ) is called the duality
gap.
If for some (x∗ , λ∗ ) where x∗ is primal feasible and λ∗ is dual feasible and we see the KKT
conditions are satisfied and f is and all gi are convex then x∗ is optimal solution to primal and λ∗
to dual.
Also, the dual optimization problem becomes,
L(x∗ , λ)
d∗ = max
λ∈Rm
s.t. λi ≥ 0∀i
m
X
where L(x, λ) = f (x) +
λi gi (x)

(55)
(56)
(57)

i=1

L∗ (λ) = min L(x, λ)
x∈D

= min L(x, λ)
x∈KKT

(58)
(59)

λi ≥ 0∀i

(60)

p ∗ = d∗

(61)

It happens to be,

111

21

SUPPORT VECTOR MACHINES

21.3

112

Duality theory applied to KKT

m
m
m
X
X
X


¯ w0 , ᾱ, λ̄) = 1 ||w||2 + c
L(w̄, ξ,
ξi +
αi 1 − ξi − yi φT (xi )w + w0 −
λi ξi
2
i=1
i=1
i=1

(62)

Now we check for KKT conditions at the point of optimality,
KKT 1.a
∇w L = 0
n
X
=⇒ w −
αj yj φT (xj ) = 0

(63)
(64)

j=1

KKT 1.b
∇xii L = 0

(65)

=⇒ c − αi − λi = 0

(66)

∇w 0 L = 0
n
X
=⇒
αi yi = 0

(67)

KKT 1.c

(68)

i=1

KKT 2
∀i

(69)
T



yi φ (xi )w + w0 ≥ 1 − ξi

(70)

ξi ≥ 0

(71)

KKT 3
αj ≥ 0 and λk ≥ 0

(72)

∀j, k = 1, . . . , n

(73)

KKT 4



αj yi φT (xj )w + w0 − 1 + ξj = 0

(74)

λk ξk = 0

(75)

(a)

w∗ =

m
X
j=1

αj yi φ(xj )

(76)

21

SUPPORT VECTOR MACHINES

113

w∗ is weighted linear combination of points φ(x)s.
(b)
If 0 < αj < c then, by Equation 66

0 < λj < c and by Equation 75, ξj = 0 and yi φT (xj )w + w0 = 1

If however, αj = c then λj = 0 and yi φT (xj )w + w0 ≤ 1.

If α0 then λj = c and ξj = 0, we get yi φT (xj )w + w0 ≥ 1. Then αj = 0

21.4

SVM dual

SVM can be formulated as the following optimization problem,
m
X
1
2
ξi }
min{ kwk + C
w
2
i=0

subject to constraint,
∀i : yi (φT (xi )w + w0 ) ≥ 1 − ξi
The dual of the SVM optimization problem can be stated as,
max{−

m m
m
X
1 XX
yi yj αi αj φT (xi )φ(xj ) +
αj }
2 i=1 j=1
j=1

subject to constraints,
X

∀i :

αi yi = 0

i

∀i : 0 ≤ αi ≤ c
The duality gap = f (x∗ ) − L∗ (λ∗ ) = 0, as shown in last lecture. Thus, as is evident from the
solution of the dual problem,
m
X

w∗ =

αi∗ yi φ(xi )

i=1

To obtain wo∗ , we can use the fact (as shown in last lecture) that, if αi ∈ (0, C), yi (φT (xi )w +
w0 ) = 1. Thus, for any point xi such that, αi ∈ (0, C), that is, αi is a point on the margin,
wo∗

=
=

1 − yi (φT (xi )w∗ )
yi
T
yi − φ (xi )w∗

The decision function,
g(x)

= φT (x)w∗ + w0∗
m
X
=
αi yi φT (x)φ(xi ) + w0∗
i=0

21

SUPPORT VECTOR MACHINES

21.5

114

Kernel Matrix

A kernel matrix
 T
φ (x1 )φ(x1 ) φT (x1 )φ(x2 ) . . .
 T
 φ (x2 )φ(x1 ) φT (x2 )φ(x2 ) . . .

K=
...
...
...


.
.
.
.
.
.
...

T
T
φ (xn )φ(x1 ) φ (xn )φ(x2 ) . . .



...

φT (x1 )φ(xn )

...


φT (x2 )φ(xn ) 


...


...

φT (xn )φ(xn )

...
...
...

In other words, Kij = φT (xi )φ(xj ). The SVM dual can now be re-written as,
1
max{− αT Ky α + αT ones(m, 1)}
2
subject to constraints,
X

αi yi = 0

i

0 ≤ αi ≤ c
Thus, for αi ∈ (0, C)
w0∗

=
=

yi − φT (xi )w
m
X
yi −
αj∗ yj φT (xi )φ(xj )
j=0

=

yi −

m
X

αj∗ yj Kij

j=0

Generation of φ space
For a given x = [x1 , x2 , . . . , xn ] → φ(x) = [xd1 , xd2 , xd3 , . . . , x1d−1 x2 , . . . ].
For n = 2, d = 2, φ(x) = [x21 , x1 x2 , x2 x1 , x22 ], thus,
φT (x).φ(x̄)

=

=

m
X m
X

xi xj .x̄i x̄j

i=1 j=1
m
X

(

xi x̄i ).(

i=1
m
X

m
X
j=1

xi x̄i )2

=

(

=

(xT x̄)2

i=1

In general, for n ≥ 1 and d ≥ 1, φT (x).φ(x̄) = (xT x̄)d .
A polynomial kernel, in general, is defined as Kij = (xTi xj )d .

xj x̄j )

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 28: SVM: Kernel Methods, Algorithms for solving Dual
Instructor: Ganesh Ramakrishnan

Date: 07/11/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

21.6

Requirements of Kernel

1. Since
Kij

= φT (xi )φ(xj )
= φT (xj )φ(xi )

Hence K should be a Symmetric Matrix.
2. The Cauchy Schwarz Inequality
(φT (x)φ(x̄))2 ≤ kφT (x)k2 kφ(x̄)k2
⇒ Kij 2 ≤ Kii Kjj
3. Positivity of Diagonal
K = V ΛV T

Where V is the eigen vector matrix (an orthogonal matrix), and Λ is the Diagonal matrix of
eigen values.
Goal is to construct a φ. Which can be constructed as
√
φ(xi ) = λi Vi (λi ≥ 0)
2

Kii = λi kVi k

Hence K must be
1. Symmetric.
2. Positive Semi Definite.
3. Having non-negative Diagonal Entries.

115

21

SUPPORT VECTOR MACHINES

116

Examples of Kernels
d

1. Kij = (xi T xj )

2. Kij = (xi T xj + 1)

d

3. Gaussian or Radial basis Function (RBF)
Kij = e−

kxi −xj k
2σ 2

(σ ∈ R, σ 6= 0)

4. The Hyperbolic Tangent function
Kij = tanh(σxTi xj + c)
Properties of Kernel Functions
If K 0 and K 00 are Kernels then K is also a Kernel if either of the following holds
1. Kij = K 0 ij + K 00 ij
2. Kij = αK 0 ij (α ≥ 0)
3. Kij = K 0 ij K 00 ij
Proof : (1) and (2) are left as an exercise.
(3)
Kij

=

0
00
Kij
Kij

=

φ0T (x0i )φ0 (x0j ) ∗ φ00T (x00i )φ00 (x00j )

Define φ(xi ) = φ0T (x0i )φ00T (x00i ). Thus, Kij = φ(xi )φ(xj ).
Hence, K is a valid kernel.

21.7

Algorithms for solving the dual

Duality offers multiple alternative check points to see if the solution is optimal. They are
1. KKT conditions satisfied ∀i
2. Primal objective ≈ Dual objective
We prefer solving the dual since we have the kernel and can avoid computing complex φ.
(K = xT x̄ i.e φ(x) = x .. However, linear kernel has simple φ and could be solved in primal form)
Sequential Minimal Optimization Algorithm (SMO)
It turns out that for most solutions, most αi = 0. So general (LCQP) solvers are an overkill. To
explot this, we use batch co-ordinate wise ascent. One of the best performers is the sequential
minimal optimization (SMO) algorithm.
This optimizes for 2 α’s at a time. The steps of the algorithm are:
1. Start with all αi = 0

21

SUPPORT VECTOR MACHINES

117

2. Seclect any 2 αs, say α1 and α2 that violate the KKT
3. Solve for α1 and α2

min

α1 ,α2

1
αi + α12 K11 + α22 K22 + α1 α2 K12 y1 y2
2
i6=1,2
X
X
+ α1 y1
K1i αi yi + α2 y2
K2i αi yi

− α1 − α2 −

X

i6=1,2

s. t.

(77)

i6=1,2

X

α1 y1 + α2 y2 = −

αj yj = α1old + α2old

j6=1,2

α1 , α2 ∈ [0, c]
4. From the second last constraint, we can write α1 in terms of α2 .
α1 = −α2

y2
y2
+ α1old + α2old
y1
y1

Then the objective is just a function of α2 , let the objective is −D(α2 ). Now the program
reduces to
min

− D(α2 )

s. t.

α2 ∈ [0, c]

α2

2)
Find α2∗ such that ∂D(α
= 0. We have to ensure that α1 ∈ [0, c]. So based on that we will
∂α2
have to clipp α2 , ie, shift it to certain interval. The condition is as follows

0 <= −α2
5.

y2
y2
+ α1old + α2old
<= c
y1
y1

 case 1: y1 = y2

α2 ∈ [max(0, −c + α1old + α2old ), min(c, α1old + α2old )]
 case 2: y1 = −y2

α2 ∈ [max(0, α2old − α1old ), min(c, c − α1old + α2old )]
If α2 is already in the interval then there is no problem. If it is more than the maximum
limit then reset it to the maximum limit. This will ensure the optimum value of the objective
constrained to this codition. Similarly if α2 goes below the lower limit then reset it to the
lower limit.

21

SUPPORT VECTOR MACHINES

118

Chunking and Decomposition Methods
We are interested in solving dual of the objective because we have already seen that most of the
dual variable will be zero in the solution and hence it will give a sparse solution (based on the KKT
conidtion).

Dual:

X

min

−

s. t.

X

α

αi +

1 XX
αi αj yi yj Kij
2 i j

(78)

αi yi = 0

i

αi ∈ [0, c]
The above program is a quadratic program. Any quadratic solvers can be used for solving (78),
but a generic solver will not take consider speciality of the solution and may not be efficient. One
way to solve (78) is by using projection methods(also called Kernel adatron). You can solve the
above one using two ways - chunking methods and decomposition methods.
The chunking method is as follows
1. Initialize αi s arbitrarily
2. Choose points(I mean the components αi ) that violate KKT condition
3. Consider only K working set and solve the dual for the variables in working set
∀α ∈ working set
min
α

s. t.

1 X X
αi αj yi yj Kij
2
αi inW S
i∈W S j∈W S
X
X
αi yi = −
αj yj

−

X

i∈W S

αi +

(79)

j/
∈W S

αi ∈ [0, c]
old
new
4. set αnew = [αW
S , αnonW S ]

Decompsition methods follow almost the same procedure except that in step 2 we always take
a fixed number of points which violate the KKT conditions the most.

Further Reading
For SVMs in general and kernel method in particular read the SVM book An Introduction to
Support Vector Machines and Other Kernel-based Learning Methods by Nello Cristianini and John
Shawe-Taylor uploaded on moodle.

CS 725 : Foundations of Machine Learning

Autumn 2011

Lecture 29: Support Vector Regression, Attribute Selection
Instructor: Ganesh Ramakrishnan

Date: 11/11/2011

Computer Science & Engineering

Indian Institute of Technology, Bombay

22

Support Vector Regression

Please refer to previous years’ notes (http://www.cse.iitb.ac.in/~cs725/notes/classNotes/
lecturenote_2010.pdf) Section 22.2 for this topic.

23

Attribute Selection and Transformation

Please refer to the following material for this topic:
1. Chapter 7 of book Data Mining by I.H. Witten and E. Frank
2. Slides at http://www.cse.iitb.ac.in/~cs725/notes/classNotes/dataprocessing.pdf

119

