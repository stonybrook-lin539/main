---
pagetitle: >-
    Parts of strings
---

# Parts of strings

:::prereqs
- strings (basic notation)
:::

It is often important to refer to specific substructures of a string.
The most important notion is that of **substring**, with the special cases of **prefix** and **suffix**.
But for some applications, **subsequences** are also relevant.

## Substrings

A **substring** is a continuous part of a string.

::: example
The string $\String{abcd}$ has 11 substrings:

- $\emptystring$
- $\String{a}$
- $\String{b}$
- $\String{c}$
- $\String{d}$
- $\String{ab}$
- $\String{bc}$
- $\String{cd}$
- $\String{abc}$
- $\String{bcd}$
- $\String{abcd}$

:::

Some authors like to write $u \sqsubseteq v$ to indicate that $u$ is a substring of $v$.

Note that

1. the empty string is a substring of every string, and
2. every string is a substring of itself.

A substring $u$ of $v$ is a **proper** substring iff $u \neq v$.

::: example
All the strings listed above are proper substrings of $\String{abcd}$, except $\String{abcd}$ itself.
:::

If $u$ is substring that spans from the very beginning of $v$, we call it a **prefix**.
And if $u$ is a substring that spans to the end of $v$, we call it a **suffix**.
Make sure not to confuse these with the linguistic notions of prefix and suffix, which work very differently.

::: example
Among the strings listed above, all of the following are prefixes of $\String{abcd}$:

- $\emptystring$ (if you find this confusing, check the formal definition below)
- $\String{a}$
- $\String{ab}$
- $\String{abc}$
- $\String{abcd}$

And the all of the following are suffixes of $\String{abcd}$:

- $\emptystring$ (if you find this confusing, check the formal definition below)
- $\String{d}$
- $\String{cd}$
- $\String{bcd}$
- $\String{abcd}$
:::

Substrings, prefixes, and suffixes are formally defined via concatenation.

::: definition
Given $\Sigma$-strings $u$ and $v$, $u$ is a **substring** of $v$ ($u \sqsubseteq v$) iff there are $x, y \in \Sigma^*$ such that $v = x \stringcat u \stringcat y$.
We furthermore call $u$

- a **proper substring** iff $u \neq v$,
- a **prefix** iff $y = \emptystring$,
- a **suffix** iff $x = \emptystring$.
:::

::: exercise
For each one of the string pairs below, indicate whether the first string is a substring of the second string, a proper substring, or neither:

- $\String{a}\ \&\ \String{aaaa}$
- $\String{a}\ \&\ \String{b}$
- $\emptystring\ \&\ \String{b}$
- $\emptystring\ \&\ \emptystring$
- $\String{aa}\ \&\ \String{abbbca}$
- $\String{bc}\ \&\ \String{abbbca}$
- $\String{cb}\ \&\ \String{abbbca}$

::: solution

- $\String{a}$ is a proper substring of $\String{aaaa}$
- $\String{a}$ is not a substring of $\String{b}$
- $\emptystring$ is a proper substring $\String{b}$
- $\emptystring$ is a substring of $\emptystring$
- $\String{aa}$ is not a substring of $\String{abbbca}$
- $\String{bc}$ is a proper substring of $\String{abbbca}$
- $\String{cb}$ is not a substring of $\String{abbbca}$

:::
:::

::: exercise
For every string $u$, there are two substrings that are both prefixes and suffixes of $u$.
What are they?
For which string are these two substrings not distinct?

::: solution
The two substrings are $\emptystring$ and $u$ itself.
The empty string is the only case where the two are not distinct as $u = \emptystring$.

::: solution_explained
No matter what $u$ looks like, it is the case that $u = \emptystring \stringcat u \stringcat \emptystring$.
But by the definition of prefixes, this means that $u$ is both a prefix ($y = \emptystring$) and a suffix ($x = \emptystring$) of $u$.
But note that we can also decompose $u$ into
$x \stringcat \emptystring \stringcat u$ such that $x = \emptystring$, which means that $\emptystring$ is a prefix of $u$.
Similarly, $u = u \stringcat \emptystring \string y$ with $y = \emptystring$, and thus $\emptystring$ is also a suffix of $u$.
:::
:::
:::


## Subsequence

Whereas substrings must be continuous, **subsequences** are allowed to also be discontinuous.
However, a subsequence need not be discontinuous.

::: example
The string $\String{abcd}$ has 16 subsequences:

- $\emptystring$
- $\String{a}$
- $\String{b}$
- $\String{c}$
- $\String{d}$
- $\String{ab}$
- $\String{ac}$
- $\String{ad}$
- $\String{bc}$
- $\String{bd}$
- $\String{cd}$
- $\String{abc}$
- $\String{abd}$
- $\String{acd}$
- $\String{bcd}$
- $\String{abcd}$

Note that $\String{ca}$ is not a subsequence of $\String{abcd}$, but it is a subsequence of $\String{abcda}$.
:::

::: exercise
List all distinct subsequences of the string $\String{aaaa}$ (without duplicates).

::: solution
- $\emptystring$
- a
- aa
- aaa
- aaaa
:::
:::

Just like substrings, a subsequence $u$ of $v$ is **proper** iff $u \neq v$.

The formal definition of subsequences is quite a bit more verbose than that of substrings.
This is because the option of discontinuity requires the use of additional string variables that can be interleaved with the subsequence in order to obtain the original string.

::: definition
Let $v$ be a $\Sigma$-string and $u \is u_1 u_2 \cdots u_n$ a member of $\Sigma^n$.
Then $u$ is a **subsequence** of $v$ iff there are strings $x_0, x_1, \ldots, x_{n+1} \in \Sigma^*$ such that

$$
v = x_0 \stringcat u_1 \stringcat x_1 \stringcat u_2 \stringcat x_2 \ldots \stringcat u_n \stringcat x_{n+1}
$$

A subsequence $u$ of $v$ is **proper** iff $u \neq v$.
:::

::: exercise
For each one of the string pairs below, indicate whether the first string is a subsequence of the second string, a proper subsequence, or neither:

- $\String{a}\ \&\ \String{aaaa}$
- $\String{a}\ \&\ \String{b}$
- $\emptystring\ \&\ \String{b}$
- $\emptystring\ \&\ \emptystring$
- $\String{aa}\ \&\ \String{abbbca}$
- $\String{bc}\ \&\ \String{abbbca}$
- $\String{cb}\ \&\ \String{abbbca}$

::: solution

- $\String{a}$ is a proper subsequence of $\String{aaaa}$
- $\String{a}$ is not a subsequence of $\String{b}$
- $\emptystring$ is a proper subsequence of $\String{b}$
- $\emptystring$ is a subsequence of $\emptystring$
- $\String{aa}$ is a proper subsequence of $\String{abbbca}$
- $\String{bc}$ is a proper subsequence of $\String{abbbca}$
- $\String{cb}$ is not a subsequence of $\String{abbbca}$

:::
:::

::: exercise
Say whether the following is True or False:
Every substring of some string $s$ is also a subsequence of $s$, but not the other way round.
Justify your answer.

::: solution
This is correct.
A substring is a subsequence where all symbols happen to be adjacent.
For example, $\String{ab}$ is both a substring and a subsequence of $\String{abc}$.

In the other direction, not every subsequence is a substring.
For example, $\String{ac}$ is a subsequence of $\String{abc}$ but not a substring.
:::
:::

## Recap

- A **substring** is a continuous part of a string.
  Initial substrings are called **prefixes**, and final ones are called **suffixes**.
- A **subsequence** is a discontinuous part of a string.
- The empty string is a substring, a prefix, a suffix, and a subsequence of every string.
- Every string *s* is both a substring and a subsequence of itself.
  The substrings and subsequences of *s* that are distinct from *s* are **proper**.

\includecollection{solutions}
