---
pagetitle: What this book is about
---

# What this book is about

The *Little Book of Language, Math, and Computation* is a friendly introduction to mathematical and computational techniques that can be fruitfully applied to the study of language.
This sounds abstract, so let us look at some brief examples.

## Example 1: Building words from blocks of sounds

Words are made up from sounds, but these sounds cannot be distributed in a random fashion.
While *blunder* is an English word, *rblnuder* is not.
In fact, no English word can ever contain the sound sequence *rbln*.
Similarly, German words never end in *voiced fricatives* such as the `z` in English *zeal*. 
Voiceless fricatives such as *s* in English *seal*, on the other hand, are fine at the end.
Linguists have proposed highly detailed theories to account for the behavior of sounds, but a surprising amount of empirical ground can be covered by an extremely simplistic idea:
words are built from overlapping blocks of sounds.
With the help of mathematics, we can then ask various questions about this simplistic system:
Does it matter how large our blocks are?
What happens if blocks are allowed to vary in length?
Can we sometimes ignore certain parts of our blocks?
Quite generally, how can we modify and extend this machinery, and how does that affect its empirical predictions?
All of these questions will provide you with simple case studies of how mathematics allow us to gain a better understanding of linguistic tools, which in turns enables deeper insights into language itself.

## Example 2: Have you ever thought about *ever*?

Consider the following sentence of English:

(@) No living person has ever been to Lankhmar.

With the exception of referencing a (formerly?) famous fantasy city, it is utterly unremarkable.
But if we replace *no* with *every*, the sentence becomes ill-formed (which linguists indicate with an asterisk).

(@) *Every living person has ever been to Lankhmar.

Remove *ever*, and the sentence is fine again.

(@) Every living person has been to Lankhmar.

So now you might think: "Okay, *every* and *ever* don't like to show up together."
But they can actually show up together.

(@) Every living person who has ever been to Lankhmar must have been hallucinating.

Based on data like this, linguists have proposed that *ever* can only occur in contexts that provide certain kinds of **logical entailments**.
From a mathematical perspective, what is special about these entailments is that they correspond to **monotonic functions**.
Whenever you are using *ever*, you are unwittingly juggling a very abstract mathematical property.

What makes this even more interesting is that monotonic functions aren't just connected to *ever*.
Monotonic functions also play a major role in many other phenomena that are of interest to linguists: adjectival gradation, case stem syncretism, person case constraints, the adjunct island constraint, the ban on improper movement, and much more.
Probably most of those terms won't mean much to you, but the important point here is that they involve very different aspects of language and look very different in the formalisms linguists use to analyze them.
It is only through the lens of mathematics, and particularly monotonic functions, that we gain a unified perspective on these seemingly unrelated phenomena.

## Example 3: The limits of word building

In English, a parent of your grand parent is your *great grand parent*, their parent is your *great great grand parent*, their parent is their *great great great grand parent*, and so on.
If you wanted to, you could refer to your *great great great great great great great great great great great great great great great grand parent*, although you probably don't know who that is.
Now consider German.
In German, the word for tomorrow is *morgen*.
The day after tomorrow is *übermorgen*, the day after that is *überübermorgen*, the day after that is *überüberübermorgen*, and so on.
Again you could use a word like *überüberüberüberüberüberüberüberüberüberüberüberüberüberüberübermorgen*, even though nobody will really understand that you are referring to the day 17 days after this one.
Now contrast that to Ilocáno, an Austronesian language with about 11 million speakers in the Philippines.
In Ilocáno, the word for tomorrow is *bigat*, and you can "sandwich" it between *ka* and *an* to get *kabigatan*, which refers the day after tomorrow.
So Ilocáno *kabigatan* is the counterpart to German *übermorgen*.
You might reasonably expect, then, that we can also have *kakabigatanan* or *kakakabigatananan*.
But that doesn't seem to be possible.
In fact, there seems to be no language that allows unbounded sandwiching of this type.
Why should that be?
Why is it okay to slap *über* at the beginning of a word as often as you want, but once it comes to sandwiching you can only do it once?

We will look at one possible answer to this conundrum, which comes in the form of finite-state machines.
We will see that finite-state machines can handle a lot of linguistic phenomena, and yes, that includes the addition of arbitrarily many instances of *great* or *über* at the beginning of a word.
But they cannot do unbounded sandwiching.
This simply is a harder problem computationally speaking.
Mathematics thus allows us to take patterns and group them into difficulty classes.
Patterns that go beyond a certain threshold of difficulty do not seem to occur across languages.

## Intended audience and learning objectives

The book is aimed at undergraduate and graduate students in linguistics, mathematics, or computer science.

### For linguists

If your background is in linguistics, you will gain familiarity with mathematical reasoning and how it can supplement and support linguistic theory building.
The goal is not to turn you into a mathematician or mathematical linguist.
While you will encounter some definitions and proofs, the book doesn't teach you how to produce new mathematical results.
Instead, the focus is on showing you how this mathematical view of language can be incorporated into linguistic research in order to gain additional insights.

With respect to the linguistics audience, then, an alternative title for this book could be *Mathematical Linguistics for Consumers* (rather than producers).

### For mathematicians and computer scientists

If you come from mathematics or computer science, you will gain exposure to natural language as a rarely explored application for mathematical inquiry.
Ideally, you will find this area of application fascinating enough to continue your journey into the study of language.
This could take the form of an introductory course on theoretical linguistics, or a more advanced textbook on mathematical linguistics (see also the discussion later on in this chapter).

If the book had just been written for mathematics and computer scientists, then, it could be called *Mathematics as a gateway drug to language science*.

## Prerequisites

The book presupposes very little mathematical training.
You should be familiar with basic operations such as
addition $(5 + 3 = 8)$,
multiplication $(5 \times 3 = 35)$,
exponentiation $(5^3 = 625)$, and
numerical functions, e.g. $f(x) = 2x + 5$.

Similarly, you don't need prior training in linguistics.
While we will encounter many linguistic concepts throughout, care has been taken to introduce them in sufficient depth that everybody can follow the discussion.
The hedge "sufficient depth" is doing a lot of heavy lifting here.
This is not an introduction to theoretical linguistics.
The discussion of linguistic concepts is often abridged and deliberately lacking in nuance.
The idea is to provide enough background for developing a mathematical perspective on language, not to teach both mathematics and linguistics at the same time.

## Information for instructors

The book was developed to support the course *Mathematical Methods in Linguistics* at Stony Brook University.
The course has a very heterogeneous audience, attracting undergraduate and graduate students from linguistics, mathematics, and computer science.
The course lasts one semester, which consists of 14 weeks with two 80 minute lectures each week.
The end of this chapter includes suggested weekly progressions for such a semester format.

## Thank you

I have been working on this book since the first time I taught *Mathematical Methods in Linguistics* at Stony Brook, which was Fall 2017.
Selected chapters were also used for guest lectures at Stony Brook's *Summer Math Camp for High School Students* and *Summer Youth Camp in Computational Linguistics*.
As such, the book has benefited from a large team of involuntary beta testers, too many to name them all here.
However, some of them graciously provided explicit feedback and suggestions for improvement that ranged from spotting typos to extended discussions of why they found certain parts confusing or dull.
I would like to thank all of them for going greatly beyond the call of duty: Abdelrahim Qaddoumi, Eric Sclafani, Jacob Rowen, Nikhil Vohra, Shigeto Kamano, Stephan Julien, Yutong Zhang, Zelalem Amera, and Zhengxiang "Jack" Wang.

In addition, funding through NSF grant BCS-1845344 allowed me to hire several students to help with the project: Alina Shabaeva, Han Li, Kenneth Hanson, and Nazila Shafiei.
They proofread finished chapters, created new exercises, and drafted solutions for various exercises.
I would like to particularly thank Alina for the Python code she wrote for the randomly generated exercises on partial orders and lattices, which would have taken up more of my time than I had to spend.
And Kenneth was essential for creating the publication infrastructure for this book --- going from a bunch of [pandoc](https://pandoc.org/) files to a beautifully formatted website and just as beautifully typeset PDF requires a lot of planning and tinkering.[^1]
The original infrastructure I set up lacked both, and Kenneth stepped in to retool it into something that's both robust and flexible enough for a project of this size.

Finally, I would like to thank the whole field of mathematical linguistics for providing me with such an infinitely stimulating and supportive community.
This book is a work of passion, and without you there would be no passion.


[^1]: The reader might be wondering why I didn't simply go with [bookdown](https://bookdown.org) or a similar all-in-one solution.
      The answer is bad timing.
      When I started working on this project, bookdown was a young project and didn't have enough exposure yet to make it on my radar (this is a value judgment on my radar rather than bookdown).
      Once I became aware of it, switching over to it seemed like a lot more work than keeping the current system.
      While the combination of Python code, lua scripts, bash, and LaTeX macros might not be very user-friendly, it is incredibly flexible.
      And it leaves the door open for the one big thing I still hope to add at some point, which is interactive exercises that students can play around with in their browser.
