kDimensions

a visual introduction to

deep learning

meor amer

about this book
Deep learning is the algorithm powering the current renaissance of artificial
intelligence (AI). And its progress is not showing signs of slowing down. A
McKinsey report estimates that by 2030, AI will potentially deliver $13 trillion to
the global economy, or 16% of the world's current GDP. This opens up exciting
career opportunities in the coming decade.

But deep learning can be quite daunting to learn. With the abundance of learning
resources in recent years has emerged another problem—information overload.

This book aims to compress this knowledge and make the subject approachable.
By the end of this book, you will be able to build a visual intuition about deep
learning and neural networks.
who should read this book
If you are new to deep learning, or machine learning in general.

If you already know some background about deep learning but want to gain
further intuition.
book format
This book uses a visuals-first approach. Each page of this book begins with a
visual and is supported by concise text.

This book doesn’t include math derivations and code examples. There are some
parts where basic math is involved, but generally it is kept to a minimum.

about the author
My journey into AI began in 2010 after my son was born with a limb difference. I
became interested in machine learning for prosthetics and did an MSc at
Imperial College London majoring in neurotechnology.

I have also worked in the telecoms data analytics space, serving clients in over 15
countries.

Above all, I am passionate about education and how we learn. I am currently
working on projects that explore ways to create alternative learning experiences
using visuals, storytelling, and games.
email: contact@kdimensions.com

table of contents
Introductio

Prediction & Decision
Machine Learning
Deep Learning
Algorithm
Data
Computation
Roadmap
Key Concepts



Foundation

A Neuron
Weighted Sum
Weights and Biases
Activation
Data
Dataset
Training
Testing



1 - Linear Regressio

Introduction
Goal and Dataset
Predict-Measure-Feedback-Ad
just
Weighted Sum and Activation
Loss Function
Mean Squared Error
Minimizing Loss
Gradient
Gradient Descent
Learning Rat
Epoch
Cost and Metric
Performance



2 - Non-Linear Regressio
Introduction
Goal and Dataset
Architecture
Predict
Measure
Feedback
Computation graph




4

6

12

13

14

15

19

20




Backpropagation
Adjust
Performance
Linear activation
Linearity
Non-linearity
Relu activation
Performance
Activation functions



3 - Binary Classificatio
22

24

25

27

30

34

38

40




43

45

50


52

58

59

64

68

73

76

81

83

86




93

99

102

108

112

114

117



Introduction
classification vs. regression
Goal and Dataset
Architecture
Sigmoid activation
Binary cross entropy
Accuracy
Performance
Confusion Matrix
Precision-Recall
F1 Score



4 - Multi-class Classificatio
Introduction
Goal and Dataset
One-hot Encoding
Architecture
Softmax Activation
Categorical Cross Entropy
Performance
Improving performance
Hyperparameters
Data Techniques



119

129

135

137

139

141

142

145

148




150

152

153

156

158

166

169

170

174

176

177




180

181

183

184

188

195

197


202

210





The Bigger Pictur

Neural Networks
Feedforward
Convolutional
Recurrent
Generative Adversarial
other Architectures
Conclusion
Key Concepts Revisite
suggested resources

217

219

225

230

232

233

234

235

experience

prediction

decision

prediction and decision
Prediction is a key ingredient in decision-making under uncertainty. — Prediction Machines book.


Much that goes on in our lives involves some form of prediction. These
predictions differ in one way, namely, how sure we are of them. In some tasks,
they don't feel like predictions because we feel so sure about them. In some
others, we know next to nothing about them, so they become mere guesses.

All of this depends on how simple a task is and, more importantly, how much
experience we have with it.

To illustrate this, let's look at some examples.

introduction

4

language
translation

customer
service

driving

prediction

decision

what is the
person saying?

reply

will the

customer churn?

discount

is that an
obstacle?

steer

examples
Let's take the example of language translation. As we listen to someone speaking,
we are predicting what the person means. The more experience we have with this
language, the better our prediction becomes, and the better our decision, that is
our reply, becomes.

Take another example in a business setting. Our experience dealing with
customers can help us see patterns in their behavior, so we’ll notice if they are
likely to churn.

As for driving, the more miles we clock, the more skilled we become and the
more adept we are at evaluating our surroundings.
introduction

5

data

prediction

decision

what is machine learning?
In many of these tasks, machine learning can handle the prediction on our behalf.

In recent years, the adoption of machine learning has accelerated. Many
industries and verticals are already deploying use cases that automate predictions
using machine learning.

In the machine’s world, the experience comes in the form of data. Just as we learn
from experience, the machine learns from data.

That is what machine learning is all about—learning from the data and turning it
into predictions.

introduction

6

machine learning in the real world
In fact, machine learning can even handle the decision part. In some domains,
most notably self-driving cars, we are not far from seeing full automation
becoming the norm.

But in most other domains, this is still far from reality. For this reason, the focus
of this book is on the prediction part.

And indeed, it is upon us to ensure healthy technological progress, where people
can thrive with the help of machines rather than being inhibited by them. That's
the sweet spot that we are collectively trying to find.

introduction

7

speed

prediction

$

$$$
accuracy

the value of machine learning
So, what is the value of having machines that can make predictions on our
behalf?

In the book Prediction Machines, the authors argued for a few reasons why
prediction machines are so valuable, the first being that ‘they can often produce
better, faster, and cheaper predictions than humans can’.

introduction

8

prediction

...

cost

accelerating human progress
The cheaper the cost of prediction, the more tasks we can take on. The world is
full of challenges waiting to be solved. Machine learning enables us to scale our
efforts in ways that have not been possible before, presenting us with the
opportunity to take on these challenges.

introduction

9

before

after

...

evolution in roles
Some may worry that this will spell the end of most jobs, and rightly so. But
looking at the bigger picture, there will in fact be even more job opportunities.

The World Economic Forum’s The Future of Jobs Report 2020 estimates that by
2025, 85 million jobs may be displaced. But on the other hand, 97 million new
roles may emerge. This already takes into account the economic slowdown due to
the pandemic, and still, the net effect is positive.

Job roles will evolve, and the machine’s role is to serve us so we can pursue more
creative and challenging endeavors.

introduction

10

DATA 

COMPLEXITY

MACHINE LEARNING

RULES-BASED SYSTEM

HUMAN 
JUDGMENT

RULES

COMPLEXITY

When to use machine learning?
We can think of prediction automation in three phases. 

The first, that is without automation, is relying on human judgment, either based
on data or experience.

The second is using a rules-based system. We translate our experience into rules
that software can understand and execute based on data as inputs.

The third is machine learning, which uses data to create its own rules, guided by
the goal defined by humans.

As the data and rules become more complex, it makes sense to use machine
learning. Otherwise, it may not be cost-effective to do so.
introduction

11

DATA 

COMPLEXITY
deep learning
classicAl machine learning

RULES

COMPLEXITY

what is deep learning?
Within machine learning, there are various types of algorithms. Think of
machine learning algorithms as competing techniques to get the best out of the
data. Some algorithms are better in certain aspects, but there’s not one that's the
best in all departments.

Deep learning is a type of algorithm that's adaptable to varying complexities of
data and rules.

It’s not necessarily the most accurate, but it's extremely adaptable. And this
comes from its modular and flexible form, which will become evident throughout
this book.
introduction

12

algorithm

algorithm
In fact, deep learning has revived the push toward Artificial Intelligence (AI) over
the past decade.

The progress is gathering pace now is because of three main reasons. The first is
the algorithm, which in truth, has been around for many decades. 

But that alone is not enough.

introduction

13

data

data
The second reason is data. 

The impetus came from the Internet and followed by social media, smartphones,
digital transformation, and a long list of other waves of innovation. They produce
new forms of data that we've never seen before, generated in large volumes.

This data contains invaluable information that we can now extract with the help
of algorithms.

introduction

14

computation

cPU

queue

GPU

queue

computation
The third reason is computational power.

Machine learning involves performing a significant amount of mathematical
computation on the data. In deep learning, this is multiplied many times over.
The standard Central Processing Unit (CPU) architecture is not capable of
handling this task efficiently. 

Enter the Graphics Processing Units (GPU). Originally designed for games, it has
emerged as the perfect solution for deep learning. 

This is a hot area of research as we speak. Even more efficient hardware designs
are yet to come.
introduction

15

algorithm

data

computation

the driving forces
Together, these three factors are the driving forces behind today’s rapid advances
in deep learning. 


introduction

16

computer 

vision

tree
tree
pole

car

natural

language

processing

sentence

sentiment

it’s a great daY

positive

i don’t like mondays

negative

...
applications
Today, there are widespread applications in computer vision, natural language
processing, business automation, and beyond. And it is just the beginning.

introduction

17

focus oF

this book

code

depth

compression

visuals

math

what can you expect from this book?
By the end of this book, you will be able to build a visual intuition about deep
learning and neural networks.

This book doesn’t cover mathematical proofs and code examples. As you advance
your learning further, these are the domains you should progress into. They will
provide you with the depth you need to be successful in this field.

introduction

18

task

the bigger
picture

4
multi-class

classification

3
binary

classification

2
non-linear

regression

1
1

LInear

regression
foundations
algorithm

roadmap
We'll see how deep learning works via four tasks - linear regression, non-linear
regression, binary classification, multi-class classification. 

They are correspondingly split into four chapters, in which new concepts are
introduced one at a time and built upon the previous ones. Therefore, it is
recommended that you read the chapters in sequence.

On either side of these four chapters, we'll have a short section for foundations
and a final section where we take a brief look beyond those covered in the four
chapters.

introduction

19

Data

task

features
target
training
testing

linear
non-linear
regression
classification

predict
weighted sum
activation

neural network
adjust
weights
biases

neurons
layers
architecture

measure
cost
metrics

feedback
gradients
backpropagation

key concepts
Here is a summary of the key concepts that we’ll explore in this book. As you go
through the book, it'll be useful to return to this page from time to time to keep
track of what you have learned.

Let’s begin!

introduction

20

task

foundations

multi-class

classification

binary

classification

non-linear

regression

LInear

regression
foundations
algorithm

foundations

21

A Neuron
We have so far used the term deep learning, but from now on, we’ll use neural
network instead. These terms are used interchangeably and refer to the same
thing. But as we start to go into the inner workings, neural network is a more
natural term to use.

To begin our journey, let's start with a neuron. The neuron is the smallest unit and
the building block of a neural network.

A neuron takes a set of inputs, performs some mathematical computations, and
gives an output.



foundations

22

inputs
The inputs and outputs are numbers, either positive or negative. In this example,
the neuron takes two inputs. However, there is no limit to the number of inputs a
neuron can take.

foundations

23

input

x1

weight

w1

bias

=
+

x2

w2

weighted

sum

b

=

z

=
z = w1x1 + w2x2 + b

weighted sum
The first computation that a neuron performs is the weighted sum. It multiplies
each input by its corresponding weight. Then all the inputs are summed and a
term called bias is added.

foundations

24

weight

weight

bias

weights and biases
These weights and biases are called the parameters of the neural network.

These adjustable parameters are the medium through which a neural network
learns, which we'll explore in detail in this book.

foundations

25

example #1
3.0

0.5

=

1.5

4.5

1.0

+
1.5

2.0

=

5.5

=

3.0

example #2
3.0

-0.5

=

-1.5

0.5

+
2.0

1.0

=

-1.5

-2.0

=

2.0

Example
Here we have a neuron with two inputs, 3.0 and 2.0. Given different weight
values, it will correspondingly output different values.



foundations

26

weighted sum

activation

x1
z

a

y

x2

activation
The second computation performed by the neuron is called an activation. This is
done by taking the output of the weighted sum and passing it through an
activation function.

foundations

27

linear activation
The activation function gives the neural network the ability to express itself. This
will not make much sense now but will become clear by the end of this book.

There are a few common activation functions. To start with, here we have a linear
activation function. It’s as basic as it gets - it simply outputs the same input it
receives. Plotted on a chart, it gives a straight-line relationship between the input
and the output.

foundations

28

z

weighted
sum

a

activation


Recap
Let’s do a quick recap. When inputs are passed through a neuron, it performs a
sequence of computations.

First it performs a weighted sum by multiplying each input by its corresponding
weight, summing them, and finally adding a bias term.

Then it performs an activation via an activation function, which in our case, is a
linear function.

foundations

29

Data
Neural networks are nothing without data. Let’s now turn our attention to data
and what it brings.

foundations

30

Learning
Data is to the neural network as experience is to humans.

A machine learning algorithm, in this case a neural network, uses data to find
useful patterns and relationships. It uses these insights to learn and update itself.

foundations

31

structured

data

xx x

x

semi-structured

data

xx : {


x xx x
xx x x
}

xx : x,

x : xxxxx,

xxx : {

xx : xxx,

xxxx : xx,

}


unstructured

data

xxx xx xxxxxx x xx
xx x xxx x xx xxxx.
xxx, x xxx.


x xxx xxxx, x xx
xxxxx xx, xxxx x xx x.
xxx x xx xx xxx x xx
xx xx.

Types of data
Data can come in many different forms. The most obvious form of data is the
tabular format. This is an example of structured data, where each data point and
its properties can be deciphered in a straightforward manner.

But data can come in other forms too.

foundations

32

Sources of data
In fact, most of the data around us are in the unstructured form. According to
projections from IDC, 80 percent of worldwide data will be unstructured by 2025.

And indeed, most of the exciting innovations in deep learning today come from
unstructured data, such as text, images, videos, and so on.



foundations

33

a dataset
Now let’s look at how we should prepare a dataset for the neural network.

A dataset is composed of many data points. A data point is a single observation
that we collect and record.

foundations

34

distance
(Mi)

rating

1.5

3.6

Example
Let's take the example of hotel room rates, a dataset we'll use throughout this
book.

Each data point represents a hotel. Here we have a hotel with a distance of 1.5
miles from the city center and a guest rating of 3.6 stars.

foundations

35

features

distance

(mi)

rating

Features
These two pieces of information are called features. Features describe the
properties of a data point.

Each data point in a dataset is described with the same features, of course with
different values, making each of them unique.

From now on, we'll refer to these two features as distance and rating for short.

foundations

36

target

price

($)

Target
Recall that the goal of a neural network is to make predictions.

In this example, we want to predict the average daily room rate (or price for short)
for any given hotel. This means, given the two features earlier, we want to predict
how much each hotel will cost.

The is called the target. In other resources, you may also find the term label being
used.


foundations

37

dist
(Mi)

rating

PRICE
($)

0.8

2.7

147

1.5

3.6

136

...

...

...

19.4

4.8

209

training
We'll give the neural network enough data points containing the features and
target values, which it will learn from.

A machine learning task where we specify the target is called supervised learning,
which will be our focus in this book.

foundations

38

training

features
model
target

Training
We have just described a process called training. 

During training, the neural network learns from the data and updates its
parameters. By this point, we'll have a trained model.

In short, given a dataset containing features and target, we get a model.

That is why the training process is sometimes also called ‘fitting the model to the
data’.


foundations

39

training

data

test

data

Testing
Once the training is complete, we need a way to know how the model is
performing.

For this, we'll keep a portion of the dataset for testing.

foundations

40

TESTiNG

features
target
model

testing
During testing, we'll provide the neural network with just the features, without
the target. Now that it’s already trained, it’s job is to predict the target values.

In the coming four chapters, we'll revisit these training and testing steps.


foundations

41

get the full book
Thank you so much for reading the sample of this book. I hope you have found it
to be useful.

If you would like to purchase the full copy of the book, you can do so by clicking
on the button below.



Get the Full Book

praise for the book
“This book takes an impressive no frills approach for people who want to learn about the
underpinnings of neural networks in the most time-effective way possible.”

— Sebastian Raschka, Ph.D. (author of Python Machine Learning)


“This book is like a CEO summary of deep learning. This is an ideal introduction for
people who have limited time but still want to go beyond trivial, hand-waving
explanations about the core concepts in deep learning.”

— Ronald T. Kneusel, Ph.D. (author of Practical Deep Learning: A PythonBased Introduction and Math for Deep Learning)



contact
I’d love to know if you have any feedback or questions. If you do, you can e-mail
them to contact@kdimensions.com.

Thanks again for reading!

Meor Amer

