---
pagetitle: >-
    Range and surjections
---

# Range and surjections

We already saw that functions can be total or partial.
Total functions map each element of their domain to some element of the co-domain, whereas partial functions are undefined on some elements of their domain.
A similar split can be found for co-domains, where there may be some elements in the co-domain that no elements of the domain are mapped to.
This is why we have to distinguish a function's co-domain from its **range**.

## Definition of range

Given a function $f: D \rightarrow C$, we use the term **range** to refer to the set of elements of $C$ that are an output for at least one input in $D$.
More precisely, $c \in C$ is in the range of $f$ iff there is some $d \in D$ such that $d \mapsto c$.

::: example
Consider the function $f: \mathbb{N} \rightarrow \mathbb{N}$ with $x \mapsto 2x$.
Not every natural number is a possible output of this function:

1. $f(0) = 0$
1. $f(1) = 2$
1. $f(2) = 4$
1. $f(3) = 6$
1. and so on

The range thus does not contain all members of $\mathbb{N}$.
Instead, it consists of all even natural numbers, and nothing else.
:::

::: example
Now suppose that we have $f: \mathbb{R} \rightarrow \mathbb{N}$ with $x \mapsto 2x$.
For every natural number $n$, $\frac{n}/2$ is a real number and thus an element of $\mathbb{R}$.
Hence it must be the case that for every natural number $n$ there is at least one element $e$ in the domain of $f$ such that $f(e) = n$.
So this is an example where a function's range is identical to its co-domain.
:::

::: exercise
For each one of the following functions, describe its range and say whether it is the same as the function's co-domain.
Justify your answer.
As with many other exercises, getting the correct answer is less important than giving a good argument for your answer.

1. $f: \mathbb{N} \rightarrow \mathbb{N}$, $x \mapsto x + 1$
1. $f: \mathbb{N} \rightarrow \mathbb{N}$, $x \mapsto x - 1$
1. $\mathrm{len}: \Sigma^* \rightarrow \mathbb{N}$ with $s \mapsto \length{s}$ (remember that $\length{s}$ denotes the length of string $s$)
1. the child-of kinship relation among humans, limited to women (for instance, $\mathrm{child}(\mathrm{Sue}) = \mathrm{Mary}$ iff Sue is a child of Mary)
1. a benchmark that sorts graphics card models by their speed for neutral network training

::: solution
1. The range of $f$ is the set of positive natural numbers, which is distinct from the co-domain $\mathbb{N}$.
1. The range of $f$ is the same as the co-domain $\mathbb{N}$.
   For every $x \in \mathbb{N}$, there is some $y \in \mathbb{N}$ such that $y - 1 = x$.
   Hence the range is at least $\mathbb{N}$.
   Since $0 - 1 = -1$ is not a member of the co-domain $\mathbb{N}$, $f(0)$ is undefined and $-1$ is not part of the range of $f$.
1. For every natural number $n$ there is at least one string in $\Sigma^*$ whose length is $n$ (including the empty string $\emptystring$ with length 0).
   Hence the range of $\mathrm{len}$ is identical to its co-domain $\mathbb{N}$.
:::
:::

## Surjective functions

In the special case where a function's range is identical to it's co-domain, we say that the function is **surjective** or **onto**.
Hence if we say that, say, $f$ is a function from $D$ onto $C$, the use of the tiny word *onto* signals that $f$ is surjective, and hence every $c\in C$ has some $d \in D$ such that $f(d) = c$.

## Recap

::: definition
The **range** of a function $f: D \rightarrow C$ is the set of all $c \in C$ such that there is some $d \in D$ with $f(d) = c$.
The range of $f$ is sometimes denoted $\mathrm{range}(f)$ or $\mathrm{ran}(f)$.
If $\mathrm{range}(f) = C$, then $f$ is a **surjection**.
:::

\includecollection{solutions}
