---
pagetitle: >-
    Factorial
---

# Factorial

Given a natural number $n \geq 1$, its **factorial** $n!$ is defined in a recursive fashion:

- $1! = 1$, and
- $n! = n \cdot (n - 1)!$.

::: example
The factorial of $5$ is $120$ because


- $5! = 5 \cdot 4!$
- $4! = 4 \cdot 3!$
- $3! = 3 \cdot 2!$
- $2! = 2 \cdot 1!$
- $1! = 1$


So $5!$ reduces to $5 \cdot 4 \cdot 3 \cdot 2 \cdot 1$, which is $120$.
:::

The factorial often appears in combinatorial problems.
For instance, if you have $n$ distinct elements, then they can be arranged in $n!$ ways.

::: example
There are $3! = 6$ ways to order $a$, $b$, and $c$:


- $abc$
- $acb$
- $bac$
- $bca$
- $cab$
- $cba$

:::

::: exercise
Analogous to the previous example, write down all possible ways of ordering $a$, $b$, $c$ and $d$ and confirm that this number is the same as $4!$.

::: solution
There are 24 distinct way of ordering $a$, $b$, $c$, and $d$.

1. abcd
1. abdc
1. acbd
1. acdb
1. adbc
1. adcb
1. bacd
1. badc
1. bcad
1. bcda
1. bdac
1. bdca
1. cabd
1. cadb
1. cbad
1. cbda
1. cdab
1. cdba
1. dabc
1. dacb
1. dbac
1. dbca
1. dcab
1. dcba

This is the same as $4! = 4 \mult 3! = 4 \mult 3 \mult 2! = 4 \mult 3 \mult 2 \mult 1! = 4 \mult 3 \mult 2 \mult 1 = 24$.
:::
:::

The factorial function grows very fast, even faster than an exponential function.

| $n$ | $2^n$ | $n!$ |
| --: | --:   | --:  |
| 1   | 2     | 1    |
| 2   | 4     | 2    |
| 3   | 8     | 6    |
| 4   | 16    | 24   |
| 5   | 32    | 120  |
| 6   | 64    | 720  |

Even a very fast growing exponential like $10,000^n$ will eventually grow more slowly than the factorial, even though it grows more rapidly for small values of $n$ (e.g. $10,000^{10} = 10^{4^{10}} = 10^{40}$ is much larger than $10! = 3,628,800$).

\includecollection{solutions}
