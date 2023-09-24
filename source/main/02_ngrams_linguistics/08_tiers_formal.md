---
pagetitle: >-
    The mathematics of tiers (work in progress)
---

# The mathematics of tiers (work in progress)

Tiers are a nice linguistic metaphor, but what is going on here at a formal level?
Exactly the same thing as with stop word removal.
We have a function that removes all irrelevant elements, and then we apply a specific procedure to the output of this function.
For stop word removal, that follow-up procedure was the construction of a bag of words.
With tier projection, we instead test the output for well-formedness with respect to an $n$-gram grammar.

## The mathematics of tiers

Remember that $\mathit{del}_S$ is a function that takes a string as its input and deletes all symbols that belong $S$.
Tier projection works pretty much the same, except that one usually specifies which symbols to keep rather than which to delete.
So given a set $T$ of tier symbols, $\mathit{del}_T$ takes a string as its input and keeps only those symbols that belong to $T$.
This difference is very similar to the split between positive and negative grammars: $T$ specifies what may be kept, $S$ what must not be kept.
We can unify stop word removal and tier projection to a single function $\mathit{del}_X$, where $X$ is some set with a specified polarity.
With $\mathit{del}_{^+X}$, only the symbols in $X$ are kept, whereas $\mathit{del}_{^-X}$ removes all symbols that belong to $X$ (and only those).

::: exercise
Compute the values for all of the following:


- $\mathit{del}_{^-\setof{a,b}}(\mathit{aaccbad})$
- $\mathit{del}_{^+\setof{a,b}}(\mathit{aaccbad})$
- $\mathit{del}_{^+\setof{a,b}}(\mathit{aababad})$
- $\mathit{del}_{^-\setof{a,b}}(\mathit{aababad})$
- $\mathit{del}_{^-\setof{a,b}}(\emptystring)$
- $\mathit{del}_{^+\setof{a,b}}(\emptystring)$

:::

You might think that this isn't a true unification, we have just moved the difference between stop word removal and tier projection into the polarity distinction.
But just as with $n$-gram grammars, polarity doesn't actually matter.
For every set $A$ of symbols drawn from some fixed alphabet $\Sigma$, there is some set $B$ such that $\mathit{del}_{^-A}(s) = \mathit{del}_{^+B}(s)$ and $\mathit{del}_{^+A}(s) = \mathit{del}_{^-B}$ for every string $s$ over $\Sigma$.

::: exercise
Explain why this holds.
Illustrate your argument with a few examples.
:::

This is a pretty nifty result.
Intuitively, stop word removal and tier projection seem completely unrelated.
One is about cleaning up data for practical applications, the other about simplifying linguistic analysis.
But mathematically, they are exactly the same thing.
In later units, we will see many more examples of this unifying power of math.

::: exercise
The term **culminativity** refers to the property that every word has exactly one primary stress.
Suppose that our alphabet is $\setof{\sigma, \acute{\sigma}}$, where $\sigma$ denotes an unstressed syllable and $\acute{\sigma}$ one with primary stress.
Specify a set $^+T$ of tier symbols and a bigram grammar $G$ to capture culminativity (*hint*: {{{L}}} and {{{R}}} can be used with tiers, too).
:::

key properties preserved because it's still just $n$-gram grammars, but over a tier instead of the string itself

- The stop word removal function $\mathit{del}$ is also the function for constructing phonological tiers.
- Math allows us to unify things that look very different at the surface.
  In particular, linguistic theory and language technology seem like very different beasts, but they actually share a lot of math.
