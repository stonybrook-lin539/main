---
pagetitle: >-
    Pairs
---

# Pairs

::: prereqs
- sets (basic notation)
:::

**Pairs** are the simplest instance of **tuples**.
We start with pairs because they are a very common use of tuples and still convey the central intuitions very clearly.

## Notation and basic concepts

A **pair** consists of exactly two elements.
We write $\tuple{a, b}$ to denote the pair that contains $a$ and $b$.
We also call $a$ the first **component** of the pair $\tuple{a, b}$, and $b$ its second component.
Crucially, the order of components matters.

::: example
Even though $\setof{1,5} = \setof{5,1}$, the pair $\tuple{1,5}$ is distinct from the pair $\tuple{5,1}$.
:::

In formal terms, $\tuple{a,b} = \tuple{c,d}$ iff $a = c$ and $b = d$.

::: example
We have $\tuple{1,5} = \tuple{1,5}$ because $1 = 1$ and $5 = 5$.
This holds even if we write the pairs differently.
For example, let $f(x) = x - 1$.
Then $\tuple{1,5} = \tuple{f(2), f(6)}$ because $1 = f(2)$ and $5 = f(6)$.
:::

It is also possible for pairs to contain the same object twice.

::: example
Continuing the previous example, the pair $\tuple{1, f(2)}$ is identical to $\tuple{1, 1}$.
This is a perfectly valid pair.
:::

Pairs may contain complex objects, including other pairs.

::: example
The following is a pair: $\tuple{ \setof{a}, \tuple{a, \setof{a}}}$.
Its two components are

1. the set containing $a$, and
1. a pair that consists of
    1. $a$ and
    1. the set containing $a$
:::

Note that just like $a \neq \setof{a}$, it also holds that $a \neq \tuple{a}$.
A container with $a$ in it is not the same thing as $a$ by itself.

::: exercise
For each one of the following, say whether it is a pair.

- $\tuple{3, a}$
- $\tuple{a, b}$
- $\tuple{a, b}$ if $a = b$
- $\tuple{\mathit{pair}}$
- $\tuple{\tuple{3, a}, \tuple{a, b}}$ if $a = b$
- $\tuple{3, a, a, b}$
- $\tuple{3, \setof{a, a}, b}$
- $\tuple{\tuple{a,b}}$
- $\tuple{\setof{\tuple{a,b}, \tuple{c,d}}}$
- $\tuple{\setof{a}, \setof{a, a}}$
- $\tuple{a, \tuple{b, \tuple{c, \tuple{d, \tuple{e, \tuple{f,g}}}}}}$
- $\tuple{1, \mathbb{N}}$, where $\mathbb{N}$ is the set of natural numbers (0, 1, 2, 3, ...)
:::

::: exercise
Fill in the gaps with $=$ and $\neq$ as appropriate, assuming that $a \neq b$:

- $\tuple{a,b} \_ \tuple{b,a}$
- $\tuple{a,a} \_ \tuple{b,b}$
- $\tuple{a,b} \_ \tuple{\setof{a}, \setof{b}}$
- $\tuple{\setof{a}, \setof{b}} \_ \tuple{\setof{a,a}, \setof{b,b,b}}$
:::

::: exercise
Fill in the gaps with $=$ and $\neq$ as appropriate, assuming that $a = b$:

- $\tuple{a,b} \_ \tuple{b,a}$
- $\tuple{a,a} \_ \tuple{b,b}$
- $\tuple{a,b} \_ \tuple{\setof{a}, \setof{b}}$
- $\tuple{\setof{a}, \setof{b}} \_ \tuple{\setof{a,a}, \setof{b,b,b}}$
:::


## Sets VS pairs

Just like sets, pairs are containers that can contain objects of arbitrary complexity.
But unlike sets, pairs care about order and the same object can be contained in a pair more than once.
Also, every pair has exactly two elements.

Usually it is clear whether one should use sets or pairs.
If order is crucial, a set won't cut it.
It it crucial to know whether we have an object once or twice, a set won't cut it.
But it is common to use pairs for mathematical convenience even in some cases where sets would suffice.

::: example
The unit on the mathematics of tiers defined an $n$-grammar with tiers as a set of tier-annotated $n$-grams, which is a pair $\tuple{g, T}$ such that $g$ is an $n$-gram and $T$ is a tier alphabet.
A concrete example of this would be $\tuple{\String{aa}, \setof{a,b}}$, i.e. the bigram $\String{aa}$ over the tier that only contains $a$s and $b$s.

Strictly speaking we do not need to use a pair here, a set would have been sufficient.
That is because the two components of the pair are of different types: one is an $n$-gram, the other a set of symbols.
If we write, say, $\setof{ \setof{a,b}, \String{aa} }$, it does not matter that there is no linear order, we can still infer right away that $\String{aa}$ must be the bigram and $\setof{a,b}$ the tier alphabet.
And we don't have to worry about duplicates either since we always have exactly one $n$-gram and one tier alphabet.

Nonetheless it is nicer to use pairs instead of sets in this case.
Consider the tier-annotated $n$-gram $\tuple{u, v}$.
Even though we used the arbitrary variables $u$ and $v$ here, you can still readily infer that $u$ is the $n$-gram and $v$ the tier alphabet.
Sure, we could have chosen more helpful variable names, but we didn't have to.
On the other hand, $\setof{u, v}$ would have been ambiguous as to which element is the $n$-gram and which is the tier alphabet.
Crucially, this ambiguity would remain even if we use more meaningful variables names, as in $\setof{g, T}$.
You may well have intended for $g$ to be the $n$-gram and for $T$ to be the tier alphabet, but the math does not actually enforce that.
Remember that mathematicians do not like to make extra assumptions: unless you explicitly say that $g$ is the $n$-gram and $T$ the tier alphabet, we also have to consider the interpretation where $T$ is the tier alphabet and $g$ is the $n$-gram.
This will quickly become problematic.
It is much nicer and explicit to use pairs instead because no matter whether you write $\tuple{g, T}$, $\tuple{u, v}$, it will always be the case that the first is the $n$-gram and the second the tier alphabet.
No ambiguity, no unintended side effects.
:::

::: exercise
Continuing the example above, consider the tier-annotated $n$-gram $\tuple{\mathit{tier alphabet}, \mathit{ngram}}$.
Which one is the $n$-gram, and which one is the tier alphabet?
:::

## Pairs as sets

The **Kuratowski definition** defines pairs as a particular kind of set: the pair $\tuple{a,b}$ is equivalent to the set $\setof{ \setof{a}, \setof{a,b}}$.
This definition is quite frequent in the linguistic literature, but the way it has been used is problematic for several reasons.
If you are interested in this definition and why linguists should be careful in how they invoke it, check out the dedicated unit at the end of this chapter.

## Recap

- **Pairs** are ordered containers with exactly two elements.
  We write $\tuple{a,b}$ to denote the pair whose first **component** is $a$ and whose second component is $b$.
- We have $\tuple{a,b} = \tuple{c,d}$ iff $a = c$ and $b = d$.
  This implies $\tuple{a,b} \neq \tuple{b,a}$ unless $a = b$.
- Sometimes we may pairs to avoid ambiguities and/or make the notation easier to read even if sets would technically suffice.

\includecollection{solutions}
