---
pagetitle: How to read this book
---

# How to read this book

As you can tell from its title, this is a book about language, mathematics, and computation.
Except that this isn't really a book, at least not in the usual sense.
This book doesn't follow a familiar linear structure, it is non-linear by design.
Before venturing forth, you should get yourself acquainted with the overall structure.

## Parts, chapters, units

The books is split into multiple **parts**: *Main units*, *Background units*, and *Additional practice exercises*.
Each part consists of multiple **chapters**.
Chapters correspond to broad topics such as n-gram models or finite-state automata.
Each chapter is broken down into **units**, with each unit illustrating a core aspect of the chapter topic or one of its linguistic applications.
The main body of each unit is interspersed with offset blocks for examples, exercises, or advice.
The end of a unit usually contains a brief recap with bullet points.

::: example
This, for example, is an example block giving you an example of what an example block looks like.
:::

::: exercise
Look at the table of contents for this book and identify parts, chapters, and units.
:::

::: advice
Take a brief glimpse at some of the units in this book to get a feel for their length and flow.
:::

I tried my best to keep each unit short enough that it could make for a comfy bedtime read.
While I didn't always succeed, I believe I did so most of the time.

## Prerequisites

The real meat of this book is in the *Main units* part.
*Main* units show you how mathematical and computational concepts can be applied to language and what we can learn from doing so.
But the *Main* units do not actually teach you said math.
Instead, all information on mathematical topics is kept separate, for easy reference, in the units of the *Background units* part.

::: example
The chapter on n-gram models in the part *Main units* uses sets and functions, but those concepts aren't fully explained there.
Instead you have to read specific *Background* units.
:::

You are not supposed to read the *Background* units in a linear fashion.
Instead, the *Main* units will tell you when it is time to consult a *Background* unit.
If there is a specific mathematical concept that you need to be familiar with in order to fully appreciate a *Main* unit, that unit will start with a list of prerequisites, e.g.:

::: prereqs
- sets (operations, set-relations)
:::

This means that you have to know about set operations like union and intersection, and the typical relations that can hold between sets (e.g. subset and superset).
If you don't have the required background, you should go to the *Background* chapter about sets and read the units on operations and set-relations.
These units may themselves have prerequisites.
But the book is structured in such a manner that as long you follow the *Main* units from start to finish without skipping anything (except optional chapters, see below), you will also move through the *Background* units in a linear fashion so that you should never have to read a *Background* unit for which you don't meet the prerequisites yet.

::: example
[Georg Ferdinand Luwdig Philipp Cantor](https://en.wikipedia.org/wiki/Georg_Cantor)
wants to read up on n-grams models.
He picks the first unit and is happy to see that it has no prerequisites.
But as the second unit is more formal, it requires some knowledge of set theory and functions:

::: prereqs
- set theory (operations, set-relations)
- functions (notation)
:::

While Cantor groks sets like nobody else, he is a little rusty on his function notation.
So he goes to the part *Background units* and checks out the unit on function notation.
The unit also requires some set theory, but since Cantor is on top of that he can read the unit right away.
Once he's done, he continues with the second unit on n-gram models.
:::

## Optional chapters

Some chapters in *Main units* are marked as optional.
This means that they can be skipped without missing any prerequisites of later chapters.

::: example
The chapter on n-grams in language technology introduces the concept of multisets.
But since no other *Main* units use multisets, you can skip this optional chapter without missing any background material that is needed for subsequent *Main* units.
:::

## Exercises

The exercises in *Main units* and *Background units* are created manually and don't come with solutions (although your instructor may distribute official solutions in class).
The part *Additional practice exercises* contains automatically generated exercises, and those do come with solutions.
They mostly test your command of very mechanical concepts, e.g. computing the union of two sets.
The idea is to give you ample opportunities to practice these calculations until they are second nature to you.
Since they are automatically generated, these exercises aren't exactly fun or stimulating.
To be honest, they are quite the grind.
But that's the point: if you struggle with a basic concept, you can keep grinding it out one problem set at a time until it finally clicks for you.

## Recap

- The book consists of multiple parts, each part consists of chapters, and chapters consist of units.
- Don't read the *Background* units from start to finish, it will be incredibly dull.
  Instead, work your way through the *Main* units and only check out a *Background* unit when it is listed as a prerequisite.
- Each unit has exercises interspersed with the main text.
  But if you want to practice more, check out the automatically generated exercises in *Additional practice exercises*.
