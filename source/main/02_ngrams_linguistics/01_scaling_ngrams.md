---
pagetitle: Analyzing negative n-gram grammars
---

# Analyzing negative $n$-gram grammars

In the previous unit, we entertained the idea that natural language phonotactics can be described in terms of a collection of forbidden sound sequences.
Such a collection is called a forbidden $n$-gram grammar, and each $n$-gram represents one forbidden sound sequence of length $n$.
But this idea ran into a problem.
In German, words cannot start with *rb*, which is captured by adding the trigram *{{{L}}}rb* to the list of illicit $n$-grams (remember that {{{L}}} is a special symbol that indicates the left edge of a word).
But German also has word-final devoicing, which means that no word can end in a voiced *s*-sound, which corresponds to *z* in English orthography.
Using this notational convention, we can represent the illicit sequence as *z{{{R}}}* (with {{{R}}} as the right edge counterpart of {{{L}}}).
This is a bigram, whereas *{{{L}}}rb* is a trigram.
What are the consequences of mixing bigrams and trigrams in a single $n$-gram grammar?
Does this introduce inconsistencies such that a word is both forbidden and allowed? 
Let's try to answer this question.
Fair warning: this will be a bit of a pain, and that's actually the point of this unit.

## A plea for proofs

Unless you're a mathematician, your first instinct will be to work through one or more examples.
If we, say, construct 100 grammars that include bigrams and trigrams and don't run into any problems, it's probably fine to mix and match. 
But this has several downsides:

- **So much work...**  
  Constructing and testing 100 grammars doesn't exactly sound like fun.
  Sure, you could write a program to do it for you, but that's also work.
  And your program might have bugs, which takes us to the next point.

- **No guarantees**  
  Just because your simulations produce a certain result does not mean that things always work this way.
  If you ask 1000 people if they've ever read Werner Schwab's *Fäkaliendramen* (feces dramas), the answers will probably all be No.
  But if your sample happened to include lots of Austrian literature buffs, you'll hear Yes a lot more often.
  Similarly, the grammars you construct for your simulation might exhibit a special property that allows them to pass the test.
  There might still be grammars that do not display this property and fail.
  If you construct the grammars with a program, your code might be written in a way that only produces grammars of a specific type.
  Bottom line: if you are testing based on examples, you can never be sure that your examples cover all possible cases that need testing.

- **No scalability**  
  Alright, suppose you actually wrote a program that is free of any bias and ran a huge number of simulations for grammar with mixed bigrams and trigrams.
  You now feel very confident that mixing of bigrams and trigrams is unproblematic.
  What about 4-grams?
  5-grams?
  127-grams?
  How do you know that your results will carry over from bigrams and trigrams to arbitrary $n$-grams?

Computer-aided simulations are a very common tool nowadays, but that does not mean that they are perfect.
They are hard to design, often require significant resources, and do not provide complete insight into how the specific aspects of a system determine its behavior.
That's not to say that simulations are a bad thing --- if you are dealing with a very complex system, they're often the best tool at your disposal.
But there are other tools around, and in many cases they are a superior choice.
Mathematics furnishes the most powerful tool of them all: proofs!

A mathematical proof starts out from a fixed set of assumptions and shows how these assumptions entail a specific property.
We will see a concrete example in a moment, but let's first focus on the specific advantages of proofs:

- **Laziness**  
  Hard proofs are very, very hard.
  They are much harder than designing a simulation.
  But unless you are a professional mathematician, most proofs you'll ever see are fairly easy.
  And easy proofs require very little effort.
  You can often work them out in less than 30 minutes, and they only take a few lines to write down.

- **Guarantees**  
  Of course a proof may contain mistakes, just like a program may contain bugs.
  But since your average proof is much smaller than your average program, mistakes in a proof tend to be easier to spot than bugs in a program.
  Fixing a mistake in a proof also tends to be much simpler than determining whether a simulation has hidden biases and correcting for that.
  And most importantly, once you have a correct proof, you have a guarantee: as long as the assumptions of the proof hold, the property established by proof holds, too.

- **Scalability**  
  Since a proof holds as long as its initial assumptions are satisfied, it can be extended to any object that satisfies these assumptions.

This may all sound awfully abstract to you.
So let's finally turn to our first proof, because the proof of the pudding is in the eating (sorry, I couldn't resist).
We will show that a negative $n$-gram grammar that also contains, say, bigrams and trigrams can be converted to an equivalent $n$-gram grammar that only contains $n$-grams.
While reading through the proof, keep in mind the three properties above (laziness, guarantees, scalability), and think about how they're instantiated in the proof.

## Our first proof: Mixed $n$-gram grammars

### Formalizing the problem

Our initial question is whether there is any problem with mixing bigrams and trigrams in a single grammar.
This is not a very precise question.
What exactly constitutes a problem?
If you have to write on a tiny piece of paper that can barely hold a single bigram, adding a trigram to the mix creates problems.
Such pesky tribulations of daily life are obviously not our concern here.
Remember that we use negative $n$-gram grammars as a model of natural language phonotactics.
So their job is to describe which potential words are well-formed and which are ill-formed.
We would have a problem if this failed for some reason: a word is both well-formed or ill-formed, a word that is ill-formed suddenly becomes well-formed when bigrams and trigrams are mixed, or the other way round.

We will show that none of these issues ever arise; we do so by establishing a **normal form theorem**.
Whenever a grammar contains $n$-grams of different sizes, it can be converted to a grammar where all $n$-grams are of the same size.
This converted grammar is equivalent to the original in the sense that they make the same phonotactic judgments: the first grammar deems a word well-formed iff the second one does, too, and the two also agree on which words are ill-formed.
The second grammar thus behaves exactly like the first, but has a normalized form without any $n$-grams of different length.
That's why the second grammar is called a **normal form** of the first one.
**Theorem** is just a fancy term for a statement that follows from a fixed set of assumptions.
So we are proving a theorem about the existence of a normal form, hence the term **normal form theorem**.

In order to avoid an overload of notation and terminology, we state the theorem in a slightly inaccurate manner as follows:

::: theorem
Let $G$ be some negative $n$-gram grammar such that $k$ is the length of the longest $n$-gram.
Then there exists an equivalent negative grammar $G'$ such that every $n$-gram of $G'$ has length $k$.
:::

### Proof

We start with a few key observations.

First, every language has only finitely many sounds.
The precise number does not matter here, it could be 2, it could be 2 trillion trillion.
The important thing is that it is finite.
We use $\card{\Sigma}$ as the special symbol for this number.

::: example
If a language only has the sounds *a*, *u*, *i*, *b*, *m*, *d*, *g*, and *h*, then $\card{\Sigma}$ for that specific language is $8$.
:::

Second, the theorem assumes that the longest $n$-gram is of length $k$.
Since each position is filled by either a sound or one of two edge markers ({{{L}}} or {{{R}}}), there are $\card{\Sigma} + 2$ choices for each one of those $k$ positions.
This allows us to precisely calculate the number of distinct $n$-grams of length $k$:

$$\overbrace{(\card{\Sigma}+2) \times \cdots \times (\card{\Sigma+2)})}^{k\ \mathrm{times}} = (\card{\Sigma}+2)^k$$

Crucially, this implies that for every possible value of $k$, there are only finitely many $n$-grams of length $k$.
And that in turn implies that $G$ contains only finitely many $n$-grams.

::: example
Suppose that the language only has the sounds *a* and *d*, barely enough for *dada*.
It's value for $\card{\Sigma}$ is $2$.
Let us calculate how many trigrams there are.
Since we are dealing with trigrams, $k=3$.
Given the formula above, this means there are $(\card{\Sigma}+2)^k = (2+2)^3 = 4^3 = 64$ different trigrams.
Not all of them are ever useful.
In particular, no word ever contains an edge marker in the middle, so *a{{{L}}}a* and *a{{{R}}}a* serve no purpose.
It is also impossible for {{{R}}} to occur to the left of {{{L}}}, which rules out trigrams like *{{{R}}}a{{{L}}}* and *{{{R}}}{{{L}}}a*.
And since we only have $k-1$ edge markers on each end of the string, we do not need {{{L}}}{{{L}}}{{{L}}} or {{{R}}}{{{R}}}{{{R}}} either.
Filtering out those useless trigrams leaves us with the following:


|                    |                   |                        |                           |
| :-:                | :-:               | :-:                    | :-:                       |
| aaa                | daa               | {{{L}}}aa              | {{{L}}}{{{L}}}a           |
| aad                | dad               | {{{L}}}ad              | {{{L}}}{{{L}}}d           |
| aa{{{R}}}          | da{{{R}}}         | {{{L}}}a{{{R}}}        | {{{L}}}{{{L}}}{{{R}}}     |
|                    |                   |                        |                           |
| ada                | dda               | {{{L}}}da              |                           |
| add                | ddd               | {{{L}}}dd              |                           |
| ad{{{R}}}          | dd{{{R}}}         | {{{L}}}d{{{R}}}        |                           |
|                    |                   |                        |                           |
| a{{{R}}}{{{R}}}    | d{{{R}}}{{{R}}}   | {{{L}}}{{{R}}}{{{R}}}  |                           |
|                    |                   |                        |                           |

But even if we had included all useless trigrams, that would not change the fact that there are only finitely many trigrams over *a*, *d*, and the edge markers.
:::

::: exercise
Calculate the number of bigrams that only use *a*, *b*, *c*, and edge markers.
Write down a table with all those bigrams, including useless ones.
How many of the bigrams are useless?
:::

These observations form the starting point for our conversion procedure.
Suppose that we pick one of the finitely many $n$-grams of our grammar $G$.
Call this $n$-gram $g$.
If the length of $g$ is already $k$, we do not need to do anything to make it an $n$-gram of length $k$.
But if its length $i$ is strictly less than $k$, we need to replace $g$ by something equivalent of length $k$.
More precisely, we replace $g$ with every possible $n$-gram of length $k$ that contains $g$ as a **substring**.
By this we mean that $g$ occurs inside of these $n$-grams.

::: example
Consider once more our toy language that only has the sounds *a* and *d*.
We have already constructed the set of all possible (and useful) trigrams for this language in the previous example.
Now suppose that we have a negative grammar $G$ that contains two $n$-grams, one being the trigram *ada* and the other the bigram *dd*.

We want to convert $G$ into an equivalent grammar $G'$ that only uses trigrams.
Since *ada* is already a trigram, we keep it as is.
Let us keep track of this by marking it in bold face in our table of possible trigrams.

|                    |                   |                        |                           |
| :-:                | :-:               | :-:                    | :-:                       |
| aaa                | daa               | {{{L}}}aa              | {{{L}}}{{{L}}}a           |
| aad                | dad               | {{{L}}}ad              | {{{L}}}{{{L}}}d           |
| aa{{{R}}}          | da{{{R}}}         | {{{L}}}a{{{R}}}        | {{{L}}}{{{L}}}{{{R}}}     |
|                    |                   |                        |                           |
| **ada**            | dda               | {{{L}}}da              |                           |
| add                | ddd               | {{{L}}}dd              |                           |
| ad{{{R}}}          | dd{{{R}}}         | {{{L}}}d{{{R}}}        |                           |
|                    |                   |                        |                           |
| a{{{R}}}{{{R}}}    | d{{{R}}}{{{R}}}   | {{{L}}}{{{R}}}{{{R}}}  |                           |
|                    |                   |                        |                           |

The only other $n$-gram in $G$ is *dd*.
As *dd* is a bigram, we replace it with every trigram that contains the substring *dd*.
So let us go through our table of trigrams and also mark every trigram that contains *dd*: add, dda, ddd, dd{{{R}}}, {{{L}}}dd.

|                    |                   |                        |                           |
| :-:                | :-:               | :-:                    | :-:                       |
| aaa                | daa               | {{{L}}}aa              | {{{L}}}{{{L}}}a           |
| aad                | dad               | {{{L}}}ad              | {{{L}}}{{{L}}}d           |
| aa{{{R}}}          | da{{{R}}}         | {{{L}}}a{{{R}}}        | {{{L}}}{{{L}}}{{{R}}}     |
|                    |                   |                        |                           |
| **ada**            | **dda**           | {{{L}}}da              |                           |
| **add**            | **ddd**           | **{{{L}}}dd**          |                           |
| ad{{{R}}}          | **dd{{{R}}}**     | {{{L}}}d{{{R}}}        |                           |
|                    |                   |                        |                           |
| a{{{R}}}{{{R}}}    | d{{{R}}}{{{R}}}   | {{{L}}}{{{R}}}{{{R}}}  |                           |
|                    |                   |                        |                           |

After the replacement step, we are left with a negative grammar $G'$ that contains six forbidden $n$-grams, all of which are trigrams.
Those are exactly the six trigrams that are marked in bold above: ada, add, dda, ddd, dd{{{R}}}, {{{L}}}dd.

:::

Carrying out the procedure above for each one of the finitely many $n$-grams in our original grammar $G$ yields a new grammar $G'$ where all $n$-grams are of length $k$.

::: exercise
Suppose that the grammar $G$ in the example above had also contained the unigram *d* in addition to *dd* and *ada*.
Using the procedure above, construct the corresponding negative trigram grammar $G'$.
:::

::: exercise
Now suppose instead that $G$ had only contained the unigram *d*.
Using the procedure above, construct the corresponding negative trigram grammar $G'$.
Do you notice anything?
What might this tell you about $G$ in the previous exercise?
:::

::: exercise
Now suppose that the inventory of sounds also contains *b* in addition to *a* and *d*.
Using the procedure above, construct the negative trigram grammar for the original grammar $G$ that contains only *dd* and *ada*.
:::

Crucially, the new grammar $G'$ constructed this way is equivalent to our original grammar $G$.
By "equivalent" we mean that the following holds for every string:
$G$ and $G'$ both deem the string well-formed, or $G$ and $G'$ both deem the string ill-formed.
There is no string that is well-formed for $G$ but ill-formed for $G'$, or the other way around.

To see this, suppose that some string is ill-formed according to $G$.
Then some $n$-gram $g$ of $G$ must occur in the string, otherwise the string would not be deemed ill-formed by $G$.

- **Case 1**  
  If $g$ has length $k$, then it is also an $n$-gram of $G'$, so $G'$ would consider the string illicit, too.

  ::: example
  Remember that our example grammar $G$ disallows *ada* and *dd*.
  Since *ada* already has maximal length in $G$, we carried it over to $G'$ without changes.
  So if some word is forbidden by $G$ because it contains *ada*, it will also be forbidden by $G'$, which does not allow *ada* either.
  :::

- **Case 2**  
  Now assume that $g$'s length is less than $k$.
  Then $G'$ contains at least one $n$-gram of length $k$ that has $g$ as a substring and that occurs in the illicit string.

  Here is why:

  - Remember that a string for an $n$-gram grammar is padded with $n-1$ edge markers.
    So with respect to $G'$, whose longest $n$-gram has length $k$, every string has $k-1$ edge markers to its left and $k-1$ edge markers to its right.
    This means every string has at least length $2 \mult (k - 1) = 2k - 2$, which is at least as big as $k$.

  - Consider once more the illicit string, whatever it may be.
    Somewhere inside the string is an offending instance of the illicit $n$-gram $g$.
    Now keep in mind that 1) by assumption $n < k$, and 2) we just established that every string is at least of length $2k - 2$, which is at least as big as $k$.
    Hence there must be symbols to the left and/or right of $g$, at the very least some edge markers.
    But $G'$ contains every $n$-gram of length $k$ that contains $g$ as a substring.
    So if a string contains $g$, it also contains at least one of these illicit $n$-grams of $G'$.

  ::: example
  Continuing the previous example, consider the word *dadd*.
  It is considered illicit by $G$ because it contains *dd*.
  This string is also considered illicit by $G'$.
  With edge markers, the word is *{{{L}}}{{{L}}}dadd{{{R}}}{{{R}}}*.
  During the construction process for $G'$, we replaced *dd* with several trigrams, two of which occur in this word:

  - add
  - dd{{{R}}}

  This is why $G'$ agrees with $G$ that *dadd* is ill-formed.
  :::

The discussion above shows that every string that is deemed illicit by $G$ is also illicit with respect to $G'$.
We still have to show the opposite, i.e. that every string deemed illicit by $G'$ is also illicit with respect to $G$.
Fortunately, this is much easier.
Suppose that a string is ruled out by $G'$ because it contains the $n$-gram $g$.

- **Case 1**  
  $G$ contains $g$, too.
  Then $G$ also deems the string illicit.

- **Case 2**  
  $G$ does not contain $g$.
  Then $G$ must contain some substring $s$ of $g$.
  But every string that contains $g$ also contains every substring of $g$, including $s$.
  Consequently, $G$ deems the string illicit, too.

Since $G$ and $G'$ agree on which strings are illicit, they necessarily agree on which strings are well-formed.
So by carrying out the procedure above for every $n$-gram of $G$, one obtains a grammar $G'$ that is equivalent to $G$ but only contains $n$-grams of a fixed length.

::: exercise
Let $G$ be our example grammar containing *dd* and *ada*, and $G'$ the equivalent grammar containing *ada*, *add*, *dda*, *ddd*, *dd{{{R}}}*, and *{{{L}}}dd*.
For each one of the following strings, say whether it is deemed well-formed by $G$ and/or $G'$.
If a grammar considers a string ill-formed, indicate which forbidden $n$-grams it contains.

- aadaa
- aaaaa
- dadda
- dd

:::

## Some thoughts

You might cry foul at this point.
I promised you that proofs are easy and quickly written down with a few lines, and the one above is neither.
It's very long, and it's cumbersome to read, and the sentences are hard to make sense of.
But that's because everything was explained in plain English rather than mathematical notation.
This made the proof harder to read and much longer, and it also means that we had to rely on examples to explain what exactly is intended at each step of the proof.
The next unit will present the same proof in mathematical notation, and while it may be initially harder for you, this format will be a lot easier for you once you have some experience.

In fact, the mathematical notation will make it very easy to see the intuition that underlies the proof above.
We are, effectively, exploiting a part-whole relation between $n$-grams of different length.
Think of it as follows:
Suppose we have a rule system that allows us to build balls, cubes, and pyramids from wood, metal, or plastic.
We now get a new guidelines that says "don't build anything wooden".
You can think of this as a unigram constraint against *wooden*.
But since what we can build it limited to balls, cubes, and pyramids, we could just as well say "don't build any wooden balls, wooden cubes, or wooden pyramids".
That is to say, we could replace the unigram with the collection of bigram constraints that an *wooden balls*, *wooden cubes*, and *wooden pyramids*.
Either way, we will from here on out only be building balls, cubes, and pyramids that are metal or plastic.
The strategy above does the very same thing, replacing each short $n$-gram with a collection of longer $n$-grams that cover all logically possible ways the short $n$-gram can be combined with other symbols.

This idea might have gotten lost among the walls of text above, but the very succinct mathematical exposition in the next unit will make it crystal-clear.
In fact, this is why it is so helpful to learn math.
Many things are intuitive enough that they can be explained in plain English.
But it is clumsy, imprecise, and takes longer.
Specialized notation and terminology makes things easier to talk and think about, not harder.

## Recap

- In a **strict** negative $n$-gram grammar, all $n$-grams must have the same length.
  In a **mixed** negative $n$-gram grammar, this requirement is lifted and $n$-grams may be of different lengths.
- Every mixed negative $n$-gram grammar can be converted into an equivalent strict negative $n$-gram grammar.
  This is an instance of a **normal form theorem**.
- We can use mathematical proofs to establish results that are guaranteed to hold whenever the conditions assumed by the proof are met.
  In contrast to simulations, proofs allow us to leave some parameters unspecified, e.g. the length of the n-grams.
  In addition, we do not need to worry about accidental gaps or biases in our simulations because a proof states explicitly which assumptions it is built on.
