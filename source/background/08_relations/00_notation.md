---
pagetitle: >-
    Relations: Basic notation
---

# Relations: Basic notation

::: prereqs
- functions (basics)
:::

Relations are similar to functions in that they establish connections between objects.
But whereas a function associates only one output with every input, a relation is more flexible and allows connections to arbitrarily many elements.

::: example
The question *Is $x$ a biological child of $y$* is a function because it maps any two $x$ and $y$ to either true or false, but never both.
But if we slightly change the question to just *Name a biological child of $y$*, we are no longer dealing with a function because multiple answers are possible if $y$ has more than one child.
Instead, we can talk about the *biological child* relation $R$ such that $x$ is related to $y$ via $R$ iff $x$ is a biological child of $y$.
:::

## Infix notation

Given some relation $R$, we write $x \mathrel{R} y$ to indicate that $R$ relates $x$ to $y$.
We could also write $R(x, y)$, but the **infix notation** $x \mathrel{R} y$ is more common and also highlights that $R$ is not a function.

Note that without additional assumptions, $x \mathrel{R} y$ does not imply that $y \mathrel{R} x$ also holds, nor does it imply that that $y \mathrel{R} x$ doesn't hold.
Either one may be the case.

::: example
One relation you know very well is the "less than" relation $<$ over numbers.
When we write $5 < 7$, we are saying that the relation $<$ relates $5$ to $7$.
However, it is not the case that $7$ is related to $5$ via $<$, since $7 < 5$ does not hold.
:::

::: example
Suppose *John* has exactly two siblings, *Mary* and *Sue*.
Then the sibling relation establishes two connections for John: *John*-*Mary*, and *John*-*Sue*.
Using $S$ for the sibling relation, we have
$\mathrm{John} \mathrel{S} \mathrm{Mary}$
and
$\mathrm{John} \mathrel{S} \mathrm{Sue}$.

But the sibling relation is an example of a relation where $x \mathrel{R} y$ implies $y \mathrel{R} x$.
It simply is impossible for John to be a sibling of Mary without Mary also being a sibling of John.
Therefore we also have
$\mathrm{Mary} \mathrel{S} \mathrm{John}$
and
$\mathrm{Sue} \mathrel{S} \mathrm{John}$.

And of course if $x$ is a sibling of $y$ and $y$ is a sibling of some $z$ distinct from $x$, then $x$ is a sibling of $z$.
So it also holds that $\mathrm{Mary} \mathrel{S} \mathrm{Sue}$, and since $x \mathrel{S} y$ implies $y \mathrel{S} x$, we also have $\mathrm{Sue} \mathrel{S} \mathrm{Mary}$.
Overall, we have $x \mathrel{S} y$ where $x, y \in \setof{\mathrm{John}, \mathrm{Mary}, \mathrm{Sue}}$ and $x \neq y$.
:::

Keep in mind that relations can establish infinitely many connections between objects.

::: example
Consider once more the "less than" relation $<$ over numbers.
We saw that $5 < 7$ holds, but of course we also have $5 < 6$, $5 < 8$, $5 < 9$, and so on.
The relation $<$ establishes connections between $5$ and infinitely many other numbers.
:::

::: example
The **substring relation** $\sqsubseteq$ holds between two strings $u$ and $v$ iff $u$ is a substring of $v$.
For instance, $\String{ab}$ is a substring of $\String{abaa}$ and $\String{aaab}$ and $\String{bbabaa}$, among many others, and it is also a substring of itself.
In fact, it holds for any arbitrary string $u$ that there are infinitely many $v$ such that $u \sqsubseteq v$.
Even if the alphabet contains only $a$, the string $\String{aa}$ is a substring of $\String{aaa}$, $\String{aaaa}$, $\String{aaaaa}$, and so on, ad infinitum.
Hence $\sqsubseteq$ contains infinitely many statements of the form $\String{aa} R v$, where $v$ is some string.
:::


## More complex examples

There are no restrictions on what kind of objects may be related by a relation.
Relations can be defined over individuals, sets, even functions and other relations.

::: example
The subset relation $\subseteq$ is a relation between sets.
The set $\setof{1}$ is a subset of infinitely many other sets: $\setof{0,1}$, $\setof{1,2}$, $\setof{0,1,2}$, $\setof{1,3}$, and so on.
Not all sets are connected via the subset relation.
For instance, neither $\setof{1} \subseteq \setof{2}$ nor $\setof{2} \subseteq \setof{1}$ hold.
:::

::: example
Here is an example of a very abstract relation.
Consider the space of all possible functions from natural numbers to natural numbers --- that's a lot of functions.
Now let's define a boundedness relation $B$ which relates function $f$ to function $g$ iff $f(x) \leq g(x)$ for every natural number $x$.
Suppose, for instance, that $f(x) = x$ and $g(x) = x^2$.
Then $f \mathrel{B} g$, but not $g \mathrel{B} f$.

Many functions aren't related via $B$ at all.
One example of this is $f(x) = x + 1000$ and $g(x) = x^2$.
For large values of $x$, it holds that $f(x) \leq g(x)$: $f(100) = 100 + 1000 = 1,100$, which is less than $g(100) = 100^2 = 10,000$.
But for small values, we get the opposite: $f(1) = 1 + 1000 = 1,001$ but $g(1) = 1^2 = 1$.
:::

## Arity of relations

All of the examples we have seen so far where **binary** relations where a single element is related to some other element.
But just like functions can take multiple arguments and map them to a single value, a relation can connect multiple elements.

::: example
Consider the "jointly conceived" relation $J$.
For instance, John and Mary may have jointly conceived Sue, but John may have also jointly conceived and Bill with Flora.
We could think of this as a ternary relation relating two parents to one of their offspring, and we could write this as follows:
$$\mathrm{John}, \mathrm{Mary} \mathrel{J} \mathrm{Sue}$$
and
$$\mathrm{John}, \mathrm{Flora} \mathrel{J} \mathrm{Bill}.$$

You might be wondering why this could not be a binary relation as indicated below:

- $\mathrm{John} \mathrel{J} \mathrm{Sue}$
- $\mathrm{Mary} \mathrel{J} \mathrm{Sue}$
- $\mathrm{John} \mathrel{J} \mathrm{Bill}$
- $\mathrm{Flora} \mathrel{J} \mathrm{Bill}$

We can still infer that Sue was jointly conceived by John and Mary, and that Bill was jointly conceived by John and Flora.
That is true, but:

1. This is an extra inference step we have to make, the relation no longer captures this fact.
   It is just because of our world knowledge about how conception works that we know how to reconstruct the relation we are actually interested in.
1. If $\mathrel{J}$ were just a binary relation, then it would be natural to add, say, $\mathrm{John} \mathrel{J} \mathrm{Diana}$ to the statements above.
   But without a matching statement like $\mathrm{Mary} \mathrel{J} \mathrm{Diana}$, this would mean that John jointly conceived Diana all by himself, which makes no sense.
   It seems more appropriate, then, to model this as a ternary relation.
:::

We will be dealing exclusively with binary relations, so you do not have to worry about relations of higher arity and why one might want to use them in some cases.


## $x \mathrel{R}$ and $\mathrel{R} y$ notation

Given a binary relation $R$, $x \mathrel{R}$ is the set of objects that $x$ is related to, i.e. the set of $y$ such that $x \mathrel{R} y$ holds.
Similarly, $\mathrel{R} y$ is the set of objects that are related to $y$, i.e. the set of $x$ such that $x \mathrel{R} y$ holds.

::: example
Suppose that the parent-of relation $P$ establishes the following relations between elements:
$\mathrm{John} \mathrel{P} \mathrm{Sue}$
and
$\mathrm{Mary} \mathrel{P} \mathrm{Sue}$.
Then $\mathrm{John} \mathrel{P} = \setof{\mathrm{Sue}}$ and $\mathrel{P} \mathrm{Sue} = \setof{ \mathrm{John}, \mathrm{Mary}}$.
:::

::: exercise
Let $R$ be the relation that connects words to their parts of speech (N for nouns, V for verbs, A for adjectives, P for prepositions, D for determiners, and so on).
List the following for English:

- export $R$
- apple $R$
- $R$ P

:::

## Relations versus functions

Every function can be regarded as a relation.

::: example
Consider the function $f: \mathbb{N} \rightarrow \mathbb{N}$ with $x \mapsto 2x$.
It is identical to the relation $R$ with $x \mathrel{R} y$ iff $y = 2x$.
:::

The crucial difference between functions and relations is that functions are **right-unique relations**.
That's a fancy way of saying that a function cannot provide more than one output, whereas a relation can unless it is right-unique.
When we view a function $f$ as a relation $R$, then it must hold for every $x$ that $x \mathrel{R}$ is either empty or contains exactly one element.
Hence the term right-unique: if we look at the expression $x \mathrel{R} y$, $x$ is the left side and $y$ the right side.
If there cannot be more than one choice for $y$, then the right side of $x \mathrel{R} y$ is uniquely determined by $x$.

The bottom line: every function is a relation, but not every relation is a function.
If $x$ is related to two elements or more (i.e. $\card{x \mathrel{R}} \geq 2$), then $R$ cannot be a function.

::: exercise
For each one of the following, say whether it is a function or just a relation.
If you have to make additional assumptions, state them explicitly.

- the parent-of relation (e.g. $j \mathrel{P} m$ for "John is a parent of Mary")
- the parent-of relation in a world where a strict one-child policy has been enforced globally
- the relation between a car's license plate and its owners
- the prefix relation, where string $u$ is a prefix of string $v$ iff there is some string $w \in \Sigma^*$ such that $v = u \stringcat w$ (for example, $\String{ab}$ is a prefix of $\String{abbaaa}$)

:::

::: exercise
Is the following statement true or false?
Justify your answer.

Every relation $R$ can be regarded as a function that maps $x$ to $x \mathrel{R}$.
:::

## Formal definition

There are multiple ways to define binary relations depending on whether one thinks of them as relating elements drawn from a single set, or as relating elements from some set $X$ to elements of some set $Y$.
The former is more standard and will also be more natural for all the scenarios we will encounter.

::: definition
A **binary relation** $R$ over some fixed set $S$ is a (possibly infinite) set of statements of the form $x \mathrel{R} y$, where $x \in S$ and $y \in S$.
:::

Note that by this definition, relations are just sets whose elements happen to specify a relation.
This means that we can apply set-theoretic operations to relations as usual.

::: example
Suppose $R \is \setof{a \mathrel{R} b, b \mathrel{R} c}$ and $R' \is \setof{a \mathrel{R} b, c \mathrel{R} b}$.
Then $R \cup R' = \setof{a \mathrel{R} b, b \mathrel{R} c, c \mathrel{R} b}$.
:::

## Recap

- Relations are a generalization of functions in that a single element can be related to many distinct elements.
- Given some binary relation $R$, we write $x \mathrel{R} y$ to indicate that $R$ relates $x$ to $y$.
- For binary relations, we have the following notation:
    - $x \mathrel{R}$ is the set of all $y$ such that $x \mathrel{R} y$.
    - $\mathrel{R} y$ is the set of all $x$ such that $x \mathrel{R} y$.
