---
pagetitle: What this book is about
---

# What this book is about

The *Little Book of Language, Math, and Computation* is a friendly introduction to mathematical and computational techniques that can be fruitfully applied to the study of language.
This sounds abstract, so let us look at some brief examples.

## Example 1: Building words from blocks of sounds

fixme

## Example 2: Have you ever thought about *ever*?

fixme

## Example 3: The limits of word building

fixme

## Intended audience and learning objectives

The book is aimed at undergraduate and graduate students in Linguistics, Mathematics, or Computer Science.

### For linguists

Linguistics students will gain familiarity with mathematical reasoning and how it can supplement and support linguistic theory building.
The goal is not to turn these students into mathematicians or mathematical linguists.
While they will encounter some definitions and proofs, the book doesn't teach students how to produce new mathematical results.
Instead, the focus in on teaching students how this mathematical view of language can be incorporated into linguistic research in order to gain additional insights.

With respect to the linguistics audience, then, an alternative title for this book could be *Mathematical Linguistics for Consumers* (rather than producers).

### For mathematicians and computer scientists

Students in mathematics and computer science will gain exposure to natural language as a rarely explored area of application for mathematical inquiry.
Ideally, they will find this area of application fascinating enough to continue their journey into the study of language.
This could take the form of an introductory course on theoretical linguistics, or a more advanced textbook on mathematical linguistics (see also the discussion later on in this chapter).

If the book had just been written for mathematics and computer scientists, then, it could be called *Mathematics as a gateway drug to language science*.

## Prerequisites

The book presupposes very little mathematical training.
Readers should be familiar with basic operations such as addition, multiplication, exponentiation, and numerical functions, e.g. $f(x) = 2x + 5$.

Similarly, readers don't need prior training in linguistics.
While we will encounter many linguistic concepts throughout, care has been taken to introduce them in sufficient depth that everybody can follow the discussion.
The hedge "sufficient depth" is doing a lot of heavy lifting here.
This is not an introduction to theoretical linguistics.
The discussion of linguistic concepts is often abridged and deliberately lacking in nuance.
The idea is to provide enough background for developing a mathematical perspective, not to teach both mathematics and linguistics at the same time.

## Information for instructors

The book was developed to support the course *Mathematical Methods in Linguistics* at Stony Brook University.
The course has a very heterogeneous audience, attracting undergraduate and graduate students from linguistics, mathematics, and computer science.
The course lasts one semester, which consists of 14 weeks with two 80 minute lectures each week.
The end of this chapter includes a suggested weekly progression for instructors.

## Thank you

I have been working on this book since the first time I taught *Mathematical Methods in Linguistics* at Stony Brook, which was Fall 2017.
Selected chapters were also used for guest lectures at Stony Brook's *Summer Math Camp for High School Students* and *Summer Youth Camp in Computational Linguistics*.
As such, the book has benefited from a large team of involuntary beta testers, too many to name them all here.
However, some of them graciously provided explicit feedback and suggestions for improvement that ranged from spotting typos to extended discussions of why they found certain parts confusing or dull.
I would like to thank all of them for going greatly beyond the call of duty: Abdelrahim Qaddoumi, Eric Sclafani, Jacob Rowen, Nikhil Vohra, Shigeto Kamano, Stephan Julien, Yutong Zhang, Zelalem Amera, Zhengxiang "Jack" Wang.

In addition, funding through NSF grant BCS-1845344 allowed me to hire several students to help with the project: Alina Shabaeva, Han Li, Kenneth Hanson, and Nazila Shafiei.
They proofread finished chapters, creating new exercises, and drafting solutions for the exercises.
I would like to particularly thank Alina for the Python code she wrote for the randomly generated exercises on partial orders and lattices.
And Kenneth was essential for creating the publication infrastructure for this book --- going from a bunch of [pandoc](https://pandoc.org/) files to a beautifully formatted website and just as beautifully typeset PDF requires a lot of planning and tinkering.[^1]
The original infrastructure I set up lacked both, and Kenneth stepped in to retool it into something that's both robust and flexible enough for a project of this size.

Finally, I would like to thank the whole field of mathematical linguistics for providing me with such an infinitely stimulating and supportive community.
This book is a work of passion, and without you there would be no passion.


[^1]: The reader might be wondering why I didn't simply go with [bookdown](https://bookdown.org) or a similar all-in-one solution.
      The answer is bad timing.
      When I started working on this project, bookdown was barely a year old and didn't have enough exposure yet to make it on my radar (this is a value judgment on my radar rather than bookdown).
      Once I became aware of it, switching over to it seemed like a lot more work than keeping the current system.
      While the combination of Python code, lua scripts, bash, and LaTeX macros might not be very user-friendly, it is incredibly flexible.
      And it leaves the door open for the one big thing I still hope to add at some point, which is interactive exercises that students can play around with in their browser.
