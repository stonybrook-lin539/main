---
pagetitle: >-
    Crossproduct (aka Cartesian product)
---

# Crossproduct (aka Cartesian product)

::: prereqs
- sets (cardinality)
- tuples (basics)
:::

One often wants to define an entire set of tuples.
This can be done in various ways, but one of the most common is the **crossproduct**, also known as the **Cartesian product**.

## Motivation and definition

Consider the colored objects depicted below: a blue square, a red square, a blue circle, and a red circle.

~~~ {.include-tikz size=mid}
shapes.tikz
~~~

We can represent each object as a pair $\tuple{s,c}$ where $s$ and $c$ are drawn from a set $S \is \setof{\mathrm{square}, \mathrm{circle}}$ of shapes and a set $C \is \setof{\mathrm{blue}, \mathrm{red}}$ of colors, respectively.
The figure above contains every possible combination of those shapes and colors.

::: definition
For any two sets $A$ and $B$, their **crossproduct** $A \times B$ is defined as the set of all pairs $\tuple{a,b}$ such that $a \in A$ and $b \in B$.
Generalizing from that, $A_1 \times A_2 \times \cdots \times A_n$ is the set of all $n$-tuples $\tuple{a_1, a_2, \ldots, a_n}$ such that $a_i \in A_i$ for every $1 \leq i \leq n$.
:::

::: example
Given $S \is \setof{\mathrm{square}, \mathrm{circle}}$ and $C \is \setof{\mathrm{blue}, \mathrm{red}}$, the crossproduct $S \times C$ contains the pairs 

- $\tuple{\mathrm{square}, \mathrm{blue}}$,
- $\tuple{\mathrm{circle}, \mathrm{blue}}$,
- $\tuple{\mathrm{square}, \mathrm{red}}$, and
- $\tuple{\mathrm{circle}, \mathrm{red}}$.

This is different from $C \times S$, which contains

- $\tuple{\mathrm{blue}, \mathrm{square}}$,
- $\tuple{\mathrm{blue}, \mathrm{circle}}$,
- $\tuple{\mathrm{red}, \mathrm{square}}$, and
- $\tuple{\mathrm{red}, \mathrm{circle}}$.

:::

::: exercise
Suppose $S$ consists of *John*, *Mary*, and *the old man*, whereas $V$ contains only *slept* and *left*.
Compute $S \times V$.
:::

::: example
Now suppose that we also have a set $A \is \setof{ \mathrm{awesome} }$.
Then $S \times C \times A$ would be a set containing the following triples:


- $\tuple{\mathrm{square}, \mathrm{blue}, \mathrm{awesome}}$
- $\tuple{\mathrm{circle}, \mathrm{blue}, \mathrm{awesome}}$
- $\tuple{\mathrm{square}, \mathrm{red},  \mathrm{awesome}}$
- $\tuple{\mathrm{circle}, \mathrm{red},  \mathrm{awesome}}$

:::

::: exercise
List all 8 members of $A \times C \times S \times A \times C \times A$.
:::

::: exercise
If $A$ has $m$ members and $B$ has $n$ members, then the number of tuples in $A \times B$ is $m$ multiplied by $n$.
Explain why.
:::

## Exponent notation

Consider once more the general case of the crossproduct of $n$ sets, i.e. $A_1 \times \cdots \times A_n$.
When all these sets are identical (i.e. $A_i \is A$ for all $1 \leq i \leq n$), then we may simply write $A^n$ instead.
In other words, $A^n$ for the set of all $n$-tuples whose elements are drawn from $A$.

::: example
Suppose $A \is \setof{a,b}$.

- $A^2 = A \times A = \setof{a,b} \times \setof{a,b} = \setof{ \tuple{a,a}, \tuple{a,b}, \tuple{b,a}, \tuple{b,b}}$
- $A^1 = A = \setof{ \tuple{a}, \tuple{b}}$

:::

::: exercise
If $A \is \setof{a}$, then what is $A^5$?
:::

::: exercise
If $A \is \setof{\setof{a}}$, then what is $A^1$?
:::

::: exercise
Our definition only considers cases where $n$ is at least $1$.
What should $A^0$ be?
:::

::: exercise
One motivation for the exponent notation is the following equivalence: $\card{A^n} = \card{A}^n$.
Explain what this means and why this holds.
:::

::: exercise
In the previous unit, we observed that strings over $\Sigma$ are the special case where all components of all tuples are drawn from a fixed alphabet $\Sigma$.
Explain why it makes sense under this view that we used $\Sigma^n$ to denote the set of all strings of length $n$.
:::

## Crossproduct $\neq$ concatenation

You might think that crossproduct is the same thing as concatenation.
And the two are indeed similar in the sense that neither is commutative --- in general, $A \times B$ is not the same as $B \times A$, and $u \tuplecat v$ is not the same as $v \tuplecat v$.

::: example
Let $A \is \setof{a,b}$ and $B \is \setof{1}$.
Then $A \times B = \setof{ \tuple{a,1}, \tuple{b,1}}$ whereas $B \times A = \setof{ \tuple{1,a}, \tuple{1,b} }$.
:::

But while tuple concatenation is associative, the crossproduct operation is not.
Most of the time, $A \times B \times C$ and $A \times (B \times C)$ and $(A \times B) \times C$ yield different results.

::: example
Let $A \is \setof{a,b,c}$, $B \is \setof{T,F}$, and $C \is \setof{1}$.
Then $A \times (B \times C)$ contains 6 pairs:


- $\tuple{a, \tuple{T,1}}$
- $\tuple{a, \tuple{F,1}}$
- $\tuple{b, \tuple{T,1}}$
- $\tuple{b, \tuple{F,1}}$
- $\tuple{c, \tuple{T,1}}$
- $\tuple{c, \tuple{F,1}}$


While $(A \times B) \times C$ also contains 6 pairs, they are different pairs:


- $\tuple{\tuple{a, T}, 1}$
- $\tuple{\tuple{a, F}, 1}$
- $\tuple{\tuple{b, T}, 1}$
- $\tuple{\tuple{b, F}, 1}$
- $\tuple{\tuple{c, T}, 1}$
- $\tuple{\tuple{c, F}, 1}$

And these, in turn, are completely different from $A \times B \times C$, which contains 6 triples instead of 6 pairs:

- $\tuple{a, T, 1}$
- $\tuple{a, F, 1}$
- $\tuple{b, T, 1}$
- $\tuple{b, F, 1}$
- $\tuple{c, T, 1}$
- $\tuple{c, F, 1}$

:::

## Crossproduct = concatenation over sets of tuples

In a certain sense, though, there is still a principled connection between crossproduct and concatenation: crossproduct is the result of generalizing concatenation from tuples to sets of tuples.
Given two such sets $A$ and $B$, we define $A \tuplecat B$ as the set of all tuples $a \tuplecat b$, where $a \in A$ and $b \in B$.

::: example
Consider the sets $S' \is \setof{\tuple{\mathrm{square}}, \tuple{\mathrm{circle}}}$ and $C \is \setof{\tuple{\mathrm{blue}}, \tuple{\mathrm{red}}}$.
By our definition, $S' \tuplecat C'$ is a new set $SC'$ that consists of the following tuples:

- $\tuple{\mathrm{square}} \tuplecat \tuple{\mathrm{blue}} = \tuple{\mathrm{square}, \mathrm{blue}}$,
- $\tuple{\mathrm{circle}} \tuplecat \tuple{\mathrm{blue}} = \tuple{\mathrm{square}, \mathrm{blue}}$,
- $\tuple{\mathrm{square}} \tuplecat \tuple{\mathrm{red}} = \tuple{\mathrm{square}, \mathrm{red}}$,
- $\tuple{\mathrm{circle}} \tuplecat \tuple{\mathrm{red}} = \tuple{\mathrm{square}, \mathrm{red}}$.

And then $SC' \tuplecat A'$, where $A' \is \setof{\tuple{\mathrm{awesome}}}$, yields:

- $\tuple{\mathrm{square}, \mathrm{blue}} \tuplecat \tuple{\mathrm{awesome}} = \tuple{\mathrm{square}, \mathrm{blue}, \mathrm{awesome}}$,
- $\tuple{\mathrm{circle}, \mathrm{blue}} \tuplecat \tuple{\mathrm{awesome}} = \tuple{\mathrm{circle}, \mathrm{blue}, \mathrm{awesome}}$,
- $\tuple{\mathrm{square}, \mathrm{red}} \tuplecat \tuple{\mathrm{awesome}} = \tuple{\mathrm{square}, \mathrm{red}, \mathrm{awesome}}$,
- $\tuple{\mathrm{circle}, \mathrm{red}} \tuplecat \tuple{\mathrm{awesome}} = \tuple{\mathrm{circle}, \mathrm{red}, \mathrm{awesome}}$.

But if you compare these to the relevant examples above, you'll notice that $S' \tuplecat C' = S \times C$, and $SC' \tuplecat A = S' \tuplecat C' \tuplecat A' = S \times C \times A'$.
:::

::: exercise
The crossproduct $A \times B$ is the empty set if at least one of $A$ and $B$ is empty.
Explain why this makes sense both under our original definition of crossproduct and the view of crossproduct as concatenation over sets of tuples.
:::

::: exercise
If $S' \tuplecat C' \tuplecat A' = S \times C \times A$, then what does $(S \times C) \times A$ correspond to?
:::


## Why "Cartesian product"

As mentioned above, the crossproduct is also known as the Cartesian product.
Why is that?

Consider the special case of $\mathbb{N} \times \mathbb{N}$, i.e. $\mathbb{N}^2$.
Here $\mathbb{N} \is \setof{0, 1, 2, 3, \ldots}$ is the set of all natural numbers.
So $\mathbb{N} \times \mathbb{N}$ is the set of all possible pairs of natural numbers.
We can take these two components to represent $(x,y)$-coordinates in the upper right quadrant of a coordinate system.

Now suppose that we replace $\mathbb{N}$ with $\mathbb{R}$, the set of all real numbers (this includes 0, 1, -1, -3.5723, $\pi$, $\sqrt{2}$, and much more).
Then $\mathbb{R}^2$ is the familiar coordinate system with an infinite negative $x$-axis centered around 0, and an infinite $y$-axis centered around 0.
Such a coordinate system is also called a **Cartesian plane**, and that is why the crossproduct is sometimes called the Cartesian product.

By the way, this notation is also used a lot in machine learning, where $\mathbb{R}^n$ is a coordinate system with $n$ axes.
For example, $\mathbb{R}^3$ is the result of adding a $z$-axis to $\mathbb{R}^2$.
Then $\mathbb{R}^4$ adds a fourth axis, which can no longer be visualized in the usual way because humans' spatial thinking isn't well-adapted to dealing with more than three dimensions.
Modern machine learning techniques often operate with systems that have hundreds of axes.


## Recap

- The crossproduct (or Cartesian product) builds a set of $n$-tuples from $n$ sets.

::: definition
Given sets $A_1$, \ldots, $A_n$, their **crossproduct** $A_1 \times A_2 \times \cdots \times A_n$ is the set of all $n$-tuples $\tuple{a_1, a_2, \ldots, a_n}$ such that $a_i \in A_i$ for every $1 \leq i \leq n$.
:::

- $A^n$ is the set of all $n$-tuples over $A$.
- The crossproduct operation is not commutative.
  Never confuse $A \times B$ and $B \times A$.
- The crossproduct operation is not associative.
  Never confuse $A \times B \times C$, $A \times (B \times C)$, and $(A \times B) \times C$.
