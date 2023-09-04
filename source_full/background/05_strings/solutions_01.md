# Parts of strings (Solutions)

## Substrings

::: exercise
For each one of the gaps below, enter $\sqsubseteq$, $\sqsubsetneq$, or $\not\sqsubseteq$ depending on whether the first string is a substring of the second string, a proper substring, or neither:

1. $\String{a} \_ \String{aaaa}$
1. $\String{a} \_ \String{b}$
1. $\emptystring \_ \String{b}$
1. $\emptystring \_ \emptystring$
1. $\String{aa} \_ \String{abbbca}$
1. $\String{bc} \_ \String{abbbca}$
1. $\String{cb} \_ \String{abbbca}$

::: solution

1. $\String{a} \sqsubsetneq \String{aaaa}$
1. $\String{a} \not\sqsubseteq \String{b}$
1. $\emptystring \sqsubsetneq \String{b}$
1. $\emptystring \sqsubseteq \emptystring$
1. $\String{aa} \not\sqsubseteq \String{abbbca}$
1. $\String{bc} \sqsubsetneq \String{abbbca}$
1. $\String{cb} \not\sqsubseteq \String{abbbca}$

:::

:::

## Subsequence

::: exercise
For each one of the gaps below, enter $\sqsubseteq$, $\sqsubsetneq$, or $\not\sqsubseteq$ depending on whether the first string is a subsequence of the second string, a proper subsequence, or neither:

1. $\String{a} \_ \String{aaaa}$
1. $\String{a} \_ \String{b}$
1. $\emptystring \_ \String{b}$
1. $\emptystring \_ \emptystring$
1. $\String{aa} \_ \String{abbbca}$
1. $\String{bc} \_ \String{abbbca}$
1. $\String{cb} \_ \String{abbbca}$

::: solution

1. $\String{a} \sqsubsetneq \String{aaaa}$
1. $\String{a} \not\sqsubseteq \String{b}$
1. $\emptystring \sqsubsetneq \String{b}$
1. $\emptystring \sqsubseteq \emptystring$
1. $\String{aa} \sqsubsetneq \String{abbbca}$
1. $\String{bc} \sqsubsetneq \String{abbbca}$
1. $\String{cb} \not\sqsubseteq \String{abbbca}$

:::

:::

::: exercise
Say whether the following is True or False:
Every substring of some string $s$ is also a subsequence of $s$, but not the other way round.
Justify your answer.

::: solution
This is correct.
Suppose $u \is u_1 \cdots u_n$ is a substring of some string $s$.
Then it must be the case that $u_1$ appears before $u_2, u_3, \ldots, u_n$, $u_2$ appears before $u_3, \ldots, u_n$, and so on.
But this is all that is required for $u_1 \cdots u_n$ to be a subsequence of $s$.
:::

:::
