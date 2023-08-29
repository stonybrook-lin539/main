# Finite-state automata (Solutions)

::: exercise
Alternatively, we could use a different definition of labeled edges where we do not have a labeling function $\ell: E \rightarrow L$ from the set of edges to some fixed set $L$ of edge labels, but instead $E$ itself is a subset of $V \times L \times V$.
Explain why this removes the need for sets as edge labels.

::: solution
If $E \subseteq V \times L \times V$, then labeled edges are triples, with the label as second component.
Hence we can have two distinct edges from any given vertex $u$ to some vertex $v$ as long as the labels of these edges are distinct, for example $\tuple{u,l,v}$ and $\tuple{u,m,v}$.
:::
:::

::: exercise
Draw an FSA that recognizes the language $\String{a^* b^+}$, where $a^*$ denotes "0 or more $a$s" and $b^+$ is short for "1 or more $b$s".

::: solution

~~~ {.include-tikz size=mid}
astarbplus.tikz
~~~

:::
:::

::: exercise
Draw an FSA that recognizes the language $\String{a^+ b^+ a^*}$.

::: solution

~~~ {.include-tikz size=mid}
aplusbplusastar.tikz
~~~

:::
:::

::: exercise
Consider once more the following automaton:

~~~ {.include-tikz size=mid}
nondet.tikz
~~~

For each one of the following strings, list all accepting runs with respect to this automaton.
If there is no such run, say so.

1. $\String{aa}$
1. $\String{acbba}$
1. $\String{abba}$
1. $\String{abab}$


::: solution

1.  $\String{aa}$
    - 0-2-3
1.  $\String{acbba}$
    - 0-1-1-2-2-3
1.  $\String{abba}$
    - 0-1-2-2-3
    - 0-2-2-2-3
1.  $\String{abab}$
    - no run

:::

:::

::: exercise
For each one of the following string languages, draw the smallest FSA that recognizes the language.

1. $\setof{\String{aa}}$ (the string $\String{aa}$, and nothing else)
1. the set of all strings except $\String{aa}$
1. $\String{b^+(aa)^+}$ (1 or more $b$s followed by an even number of $a$s, but at least 2 $a$s)
1. $\setof{a,b}^*$ (the set of all strings over $a$ and $b$, including the empty string $\emptystring$)
1. $\String(acdc)^*$ (0 or more iterations of $\String{acdc}$)
1. the set of all strings over $a$, $b$, and $c$ such that the string contains $a$ iff it does not contain $c$
1. $\setof{a,b}^* c \setof{a,b}^*$ (the set of all strings over $a$, $b$, and $c$ that contain exactly one $c$)
1. $c \setof{a,b,c}^* c$ (the set of all strings over $a$, $b$, and $c$ that start with a $c$ and end with another $c$)
1. the set of all strings over $a$, $b$, and $c$ whose first symbol is distinct from their last symbol
1. the set of all strings over $a$ and $b$ such that the number of $a$s within the first 4 symbols must not exceed the number of $b$s among the last 4 symbols
1. the set of all strings over $a$, $b$, and $c$ where $a$ never occurs immediately to the right of $b$ ($\String{ab}$ and $\String{bca}$ are fine, but $\String{ba}$ is not)
1. the set of all strings over $a$, $b$, and $c$ where $a$ never occurs anywhere to the right of $b$ ($\String{ab}$ is fine, but $\String{bca}$ and $\String{ba}$ are not)
1. the set of all strings over $a$, $b$, and $c$ such that the number of $c$s in the string is a multiple of 3 or 5
1. the set of all strings over $a$ and $b$ that are worth at least 10 points, where each $a$ is worth 2 points and each $b$ is worth 3 points
1. the set of all strings over $a$ and $b$ whose point value is at most 10 or a multiple of 3, where each $a$ is worth 2 points and each $b$ is worth 3 points
1. the set of all strings over $a$, $b$, $c$, and $d$ where $a$ may have $b$ somewhere to its left and a $b$ somewhere to its right only if there is no $d$ in the string
1. the set of all strings over $a$, $b$, and $c$ such that whenever a $b$ is immediately followed by at least one $a$, the next $b$ to the right must be immediately followed by at least one $c$ (for example $bbacabcbb$ is well-formed, but $bbacabbcb$ is not because the second $b$ is immediately followed by $a$ but the third $b$ is not immediately followed by $c$)
1. the set of all strings over $a$, $b$, and $c$ such that whenever a $b$ has an $a$ somewhere to its right, then the next $b$ to the right must have at least one $c$ somewhere to its right ($bbacabbcb$ is now well-formed, and so is $bbacabbabbc$, but $bbacabbbb$ and $bbacabbabbb$ are ill-formed)

::: solution
$\setof{\String{aa}}$ (the string $\String{aa}$, and nothing else)

~~~ {.include-tikz size=mid}
aa.tikz
~~~

the set of all strings except $\String{aa}$ (we use $\sigma$ to denote any symbol distinct from $a$)

~~~ {.include-tikz size=mid}
notaa.tikz
~~~

$\String{b^+(aa)^+}$ (1 or more $b$s followed by an even number of $a$s, but at least 2 $a$s)

~~~ {.include-tikz size=mid}
bplusaaplus.tikz
~~~

$\setof{a,b}^*$ (the set of all strings over $a$ and $b$, including the empty string $\emptystring$)

~~~ {.include-tikz size=mid}
sigmastar.tikz
~~~

the set of all strings over $a$, $b$, and $c$ whose first symbol is distinct from their last symbol

~~~ {.include-tikz size=mid}
firstneqlast.tikz
~~~

the set of all strings over $a$ and $b$ that are worth at least 10 points, where each $a$ is worth 2 points and each $b$ is worth 3 points

~~~ {.include-tikz size=mid}
10points.tikz
~~~

:::

:::
