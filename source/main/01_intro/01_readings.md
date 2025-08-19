---
pagetitle: >-
    Supplementary readings, or: What's unique about this book?
---

# Supplementary readings, or: What's unique about this book?

This book is far from the only game in town when it comes to mathematics and linguistics, and that's a good thing.
It is impossible for a single resource to please everyone.
Some readers may want more mathematical rigor, others want to focus on the intuitions.
Some want a comprehensive tome, others a slim pamphlet.
When I set out to write this book, I wanted to create something that provides a new route into mathematical linguistics, something that works for those readers who bounced off the existing resources or didn't have them on their radar to begin with.
So let's take a look at what is already out there and how this book differs from that.

## Comparison to other textbooks

In a fit of solipsistic idiosyncrasy, I will discuss the books in the order I read them as a student.

### Partee et al (1990): Mathematical Methods in Linguistics (Second edition)

This is arguably the best-known introduction to mathematical approaches to linguistics.
It was a remarkable achievement at its time, and depending on your interests it may still be the best book for you.
At almost 700 pages, *Mathematical Methods in Linguistics* is very comprehensive and covers many topics at greater length than my book.
For example, I cover sets in a few short background units, whereas *Mathematical Methods in Linguistics* devotes its entire first chapter to sets.
So if you feel like the treatment of some mathematical concept is too abridged in my book, you might find a more satisfactory treatment in Partee et al (1990).

The downside of Partee et al (1990) is that linguistic applications are mostly limited to semantics, the study of meaning.
The focus on semantics greatly shapes what mathematical topics are covered, and hence you won't find topics like vectors or matrix multiplication that are becoming increasingly important in linguistics.
Where the book ventures beyond semantics, e.g. in its chapters on automata theory, it fails to make a compelling case for their relevance to language.
In a way, my book is the very opposite of Partee et al's in that I talk about pretty much everything except semantics.
Overall *Mathematical Methods in Linguistics* is still an excellent read, but it should probably be called *Mathematics for Semanticists*.

### Gamut (1990): Logic, Language, and Meaning (Volumes 1 & 2)

This one already tells you in the title that it will be heavy on logic and meaning, i.e. semantics.
I prefer its treatment of formal logic to that in other textbooks, and it includes less common topics such as many-valued logic and categorial grammar.
But as with Partee et al's *Mathematical Methods in Linguistics*, the focus on logic and semantics means that readers won't get to see many of the ways mathematics can be applied to language.

### Keenan & Moss (2016): Mathematical Structures in Language

This is a much thinner book than *Mathematical Methods in Linguistics*, and it does quite a few things to set itself apart.
While the second half of the book is all about semantics, the first half does branch out into rarely seen topics such as feature systems in phonology (the grammar of sounds).
Most importantly, perhaps, this book puts major emphasis on mathematical proofs.
If you are aspiring mathematical linguist, proofs will be essential in your research, and *Mathematical Structures in Languages* is a good place to learn the basics of constructing mathematical proofs.
But if you just want to learn some hand-on techniques for modeling language in an insightful manner, the abundance of proofs may prove distracting (yes, the pun is as lame as it is intended).
By contrast, I largely omit mathematical proofs in this book, including just enough of them to illustrate what a mathematical proof is and why it is insightful and extremely powerful.
The emphasis is on the hands-on application of mathematical insights rather than the creation of new ones.
If you find that too limiting and want to dive into constructing your own proofs, check out *Mathematical Structures in Language*.

### Kornai (2008): Mathematical Linguistics

This is a very different kind of textbook as it targets mathematically minded readers with no prior training in linguistics --- in particular mathematicians and computer scientists.
As a result, the book covers a very different range of topics than the textbooks listed above, including information theory, speech processing, and handwriting recognition, among others.
This makes for a very unique contribution, but also one that is an acquired taste.
Linguistically-minded readers may find the choice of topics dry or boring, shying away from the phenomena and issues that make linguistics exciting to them.
And readers without any linguistic training may still find it hard to follow the linguistic parts of the book.
Overall, it is still a worthwhile read with many things you can't find anywhere else.
I simply advise against it being your first read on mathematics or linguistics (my book is meant to work just fine as a first read, and hopefully I have succeeded at that).

### Kracht (2003): The Mathematics of Language

I consider this is the best book on this list, but it is also the least read and/or understood.
If you are an advanced reader with lots of mathematical maturity and an excellent command of linguistics, Kracht's *Mathematics of Language* is a dream come true, a treasure trove of definitions, theorems and proofs.
If you are on your way to becoming a researcher in mathematical linguistics, it will be one of the most enjoyable reads of your life.
If you're none of the above, this is a 600 page paperweight.
The book will simply be impenetrable to you, and that is a shame because it has so many important things to tell you.
Hopefully, after reading my book and one of the others listed above, you will be ready to take on Kracht's *magnum opus*.
It will still be challenging, but you should have a good chance of survival.

### Jurafsky & Martin (2000/2008/in progress): Speech and Language Processing

This is different from all the books above in that it is an introduction not to mathematical linguistics but to computational linguistics, in particular Natural Language Processing (NLP).
There are several reasons why it merits inclusion in this list, though.
It is a book that most students should be able to tackle after working through this one.
It presents additional applications of many concepts covered in this book, e.g. n-grams and matrix multiplication.
It uses a fair amount of mathematical notation, but largely avoids elaborate definitions and proofs.
It also covers important topics that aren't in any of the books above, most importantly sentence parsing, which is the process of assigning hidden structure to sentences.

A brief remark on the various editions:
The second edition is a revised and extended version of the first edition, and to the best of my knowledge there is no reason to ever prefer the first over the second.
The third edition, however, drops some of the topics of the second edition that aren't all that important anymore in this age of neural networks and large language models.
However, some of the topics that were dropped were among the most interesting from a linguistic perspective, e.g. the discussion of finite-state optimality theory.
So my personal recommendation is to read the second edition and then supplement that with the third edition's chapters on neural networks, which are a lot of fun and do a great job of illustrating the role of matrix multiplication in neural networks.

## Summary: What's unique here?

This book differentiates itself in several ways from existing textbooks.

### Choice of topics: Structure over meaning

While a lot of existing textbooks focus on the use of mathematics in semantics (the study of meaning), semantics plays a very minor role in this book.
Logic is covered a bit, but only in connection to talking about structures (i.e. model theory).
Quite generally, "structure over meaning" was one of the leading design principles for the book.
The discussion tends to revolve around phonology (sound grammar), morphology (word grammar), and syntax (sentence grammar), which are the three primary domains of linguistic structure.
The book also ventures into topics like grammatical inference and machine learning that are rarely covered in linguistics textbooks.
Again, this involves structure, albeit a at a level that goes beyond individual languages.

### Target audience: consumers, not producers

Books in mathematical linguistics are often written for aspiring mathematical linguists.
As such, they emphasize the mathematical framework of definitions, theorems, and proofs.
They seek to give readers all the tools they need to **produce** new results in mathematical linguistics.
That is a valid goal, and the field definitely needs books like this.
But every book with this goal necessarily sets a very high bar for its readers to clear, and that makes it a lot less approachable to most readers.

This book instead tries to get readers to a level where they can **consume** results from mathematical linguistics.
Readers learn how to take existing insights from mathematical linguistics and apply them to language. 
The focus is on model building instead of theorem proving.
The hope is that this will be more appealing to readers who bounce of formal proofs.
Reading this book won't turn you into a mathematical linguist, but it will allow you to understand mathematical linguistics and how you can leverage its insights for whatever your primary area of interest may be.

### Non-linear structure

While I didn't mention this in the discussion above, this book is also unique in that it adopts a non-linear structure that explicitly separates the mathematical concepts from their application to language.
This is a major difference to Partee et al (1990), Gamut (1990), and Keenan & Mos (2016), where the two are frequently interleaved.
It is also a major difference to Kracht (2003), which presumes a lot of mathematical basics instead of gently introducing them to the reader.
My book is an attempt to have one's cake and eat it too by covering the mathematical background without letting it disrupt the flow of the main content, which is the application of mathematics to language.
This design goal has specific implications for the structure of this book and how it should be maneuvered by the reader. 
That is our next topic of discussion.
