# Notation: Big operators (Solutions)

::: exercise
Write each one of the following expressions as a formula with the addition operator $+$.

$$
5 - \sum_{1 \leq i \leq 3} i
$$

$$
\sum_{i = 1} i + i + i
$$

::: solution
$$
5 - \sum_{1 \leq i \leq 3} i = 5 - (1 + 2 + 3)
$$

$$
\sum_{i = 1} i + i + i = 1 + 1 + 1
$$
:::

:::

::: exercise
Express each formula below in a more succinct format using the sum operator $\sum$.

1. $20 + 21 + 22 + 23 + 24 + 25 + 26 + 27 + 28 + 29$
1. $2 + 4 + 6 + 8 + 10$
1. $30 + 15 + 3 + 10 + 2 + 20$
1. $-10 - 9 - 8 - 7$

::: solution
1. $\sum_{20 \leq i \leq 29} i$
1. $\sum_{i \in \setof{2,4,6,8,10}} i$
1. $\sum_{i \in \setof{2,3,10,15,20,30}} i$
1. not well-defined because subtraction isn't associative; but $(-10) + (-9) + (-8) + (-7)$ would be $\sum_{7 \leq i \leq 10} -i$
:::

:::

::: exercise
Rewrite the formula below so that it uses the subscript/superscript format.

$$
5 - \sum_{1 \leq i \leq 3} i
$$

::: solution
$$
5 - \sum_{i = 1}^3 i
$$
:::

:::

::: exercise
Consider once more the formulas below.

- $20 + 21 + 22 + 23 + 24 + 25 + 26 + 27 + 28 + 29$
- $2 + 4 + 6 + 8 + 10$
- $30 + 15 + 3 + 10 + 2 + 20$
- $-10 - 9 - 8 - 7$

Combine the sum operator with other operations in order to describe each formula in a more systematic way. 
Keep in mind that there are infinitely many ways this can be done, just pick the one that seems most plausible to you.

::: solution
1. $\sum_{0 \leq i \leq 0} (20 + i)$
1. $\sum_{1 \leq i \leq 5} 2i$
1. $\sum_{i \in \setof{2,3}} (i + 5i + 10i)$
1. still undefined
:::

:::

::: exercise
Suppose that $\mathcal{S} \is \setof{ \setof{0,3}, \setof{9,23}, \setof{2,9}}$ as before.
What is the value of the formula below, assuming that $i \oplus j = ij$ if $i \geq j$ and $ji$ otherwise
(for example, $8 \oplus 7 = 87$ and $3 \oplus 15 = 153$).

$$
\prod_{S \in \mathcal{S}} \bigoplus_{n \in S} n
$$

::: solution

\begin{align*}
\prod_{S \in \mathcal{S}} \bigoplus_{n \in S} n &=
\bigoplus_{n \in \setof{0,3}} n
\times
\bigoplus_{n \in \setof{9,23}} n
\times
\bigoplus_{n \in \setof{2,9}} n
\\
&=
0 \oplus 3
\times
9 \oplus 23
\times
2 \oplus 9
\\
&=
30
\times
239
\times
92
\\
&=
659,640
\end{align*}

:::
:::
