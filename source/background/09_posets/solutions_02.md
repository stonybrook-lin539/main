# (Semi)Lattices (Solutions)

::: exercise
Given the same poset as in the previous examples, compute all of the following:

1. $\mathrm{lub}(\setof{\setof{1,2}, \setof{2,3}})$
1. $\mathrm{glb}(\setof{\setof{1,2}, \setof{2,3}})$
1. $\mathrm{lub}(\setof{\emptyset})$
1. $\mathrm{glb}(\setof{\emptyset, \setof{1,2,3}})$
1. $\mathrm{glb}(\setof{\setof{1}, \setof{2,3}, \setof{1,2,3}})$
1. $\mathrm{lub}(\setof{\setof{1}, \setof{2}, \setof{3}})$

::: solution
1. $\mathrm{lub}(\setof{\setof{1,2}, \setof{2,3}}) = \setof{1,2,3}$
1. $\mathrm{glb}(\setof{\setof{1,2}, \setof{2,3}}) = \setof{2}$
1. $\mathrm{lub}(\setof{\emptyset}) = \emptyset$
1. $\mathrm{glb}(\setof{\emptyset, \setof{1,2,3}}) = \emptyset$
1. $\mathrm{glb}(\setof{\setof{1}, \setof{2,3}, \setof{1,2,3}}) = \emptyset$
1. $\mathrm{lub}(\setof{\setof{1}, \setof{2}, \setof{3}}) = \setof{1,2,3}$
:::

:::


## Uniqueness of lubs and glbs

In the examples so far, there has always been a unique lub and a unique glb.
But this isn't always the case with posets.

::: exercise
Try to explain to yourself why this result holds.

*Hint*: Suppose towards a contradiction that $\mathrm{lub}(T)$ does contain at least two distinct elements $x$ and $y$.
How would $x$ and $y$ have to be ordered by $\leq$?
Is this possible in a poset?

::: solution
Suppose that $\mathrm{lub}(T)$ contains $x$ and $y$.
Then it must hold that $x \leq z$ and $y \leq z$ for all $z \in \mathrm{ub}(T)$.
But if $x$ and $y$ are members of $\mathrm{lub}(T)$, then they are also members of $\mathrm{ub}(T)$.
We may thus substitute $x$ and $y$ for $z$ to get the statements $x \leq y$ and $y \leq x$.
Since $x$ and $y$ are elements of a poset, $x \leq y$ and $y \leq x$ jointly implies $x = y$, which establishes that the least upper bound for $T$ is unique.

The argument for $\mathrm{glb}(T)$ is exactly the same, with $\leq$ replaced by $\geq$.
:::

:::

::: exercise
Writing $\mathrm{glb}(\setof{s_1, \ldots, s_n})$ as $s_1 \wedge s_2 \wedge \cdots \wedge s_n$ is possible because $\wedge$ is an associative operation: $(x \wedge y) \wedge z = x \wedge (y \wedge z)$. 
Explain why $\wedge$ is associative.

*Hint*: You want to show that $\mathrm{glb}(\setof{ \mathrm{glb}(\setof{x, y}), z}) = \mathrm{glb}(\setof{x, \mathrm{glb}(\setof{y, z})})$ if one adopts the convention that the $\mathrm{glb}$ function returns a unique element rather than a set.
:::

::: exercise
For each one of the following depictions of a poset, say whether it is a join semilattice, a meet semilattice, both, or neither.

\begin{forest}
    [True [False]]
\end{forest}

\begin{forest}
    [A
        [D]
        [B
            [C]
        ]
    ]
\end{forest}

\begin{forest}
    [,phantom
        [A
            [D]
            [B
                [C]
            ]
        ]
        [E]
    ]
\end{forest}

\begin{forest}
    [Y
        [A
            [D]
            [B
                [C,name=c]
            ]
        ]
        [E,name=e]
    ]
    %
    \draw (e.south) to (c.north);
\end{forest}

\begin{forest}
    [Y
        [A
            [D,name=d]
            [B
                [C,name=c]
            ]
        ]
        [E,name=e]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
\end{forest}

\begin{forest}
    [,phantom
        [X,name=x]
        [Y
            [A,name=a
                [D,name=d]
                [B
                    [C,name=c]
                ]
            ]
            [E,name=e]
        ]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
\end{forest}

\begin{forest}
    [Z
        [X,name=x]
        [Y
            [A,name=a
                [D,name=d]
                [B
                    [C,name=c]
                ]
            ]
            [E,name=e]
        ]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
\end{forest}

\begin{forest}
    [Z
        [X,name=x]
        [Y
            [A,name=a
                [D,name=d]
                [B
                    [C,name=c]
                ]
            ]
            [E,name=e]
        ]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
    \draw (x.south) to (e.north);
\end{forest}

::: solution

\begin{forest}
    [True [False]]
\end{forest}
both

\begin{forest}
    [A
        [D]
        [B
            [C]
        ]
    ]
\end{forest}
join semilattice ($D \wedge B$ is undefined)

\begin{forest}
    [,phantom
        [A
            [D]
            [B
                [C]
            ]
        ]
        [E]
    ]
\end{forest}
neither ($A \wedge E$ and $A \vee E$ are both undefined)

\begin{forest}
    [Y
        [A
            [D]
            [B
                [C,name=c]
            ]
        ]
        [E,name=e]
    ]
    %
    \draw (e.south) to (c.north);
\end{forest}
join semilattice ($D \wedge C$ is undefined)

\begin{forest}
    [Y
        [A
            [D,name=d]
            [B
                [C,name=c]
            ]
        ]
        [E,name=e]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
\end{forest}
both

\begin{forest}
    [,phantom
        [X,name=x]
        [Y
            [A,name=a
                [D,name=d]
                [B
                    [C,name=c]
                ]
            ]
            [E,name=e]
        ]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
\end{forest}
meet semilattice ($X \vee Y$ is undefined)

\begin{forest}
    [Z
        [X,name=x]
        [Y
            [A,name=a
                [D,name=d]
                [B
                    [C,name=c]
                ]
            ]
            [E,name=e]
        ]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
\end{forest}
both

\begin{forest}
    [Z
        [X,name=x]
        [Y
            [A,name=a
                [D,name=d]
                [B
                    [C,name=c]
                ]
            ]
            [E,name=e]
        ]
    ]
    %
    \draw (e.south) to (c.north);
    \draw (d.south) to (c.north);
    \draw (x.south) to (a.north);
    \draw (x.south) to (e.north);
\end{forest}
neither ($A \vee E$ and $X \wedge Y$ are undefined)
:::

:::

::: exercise
Why don't we need to check $F \wedge T$ (or $F \vee T$)?

::: solution
Because $F \wedge T = T \wedge F$, which we already checked (and similarly, because $F \vee T = T \vee F$).
This holds because $F \wedge T = \mathrm{glb}(\setof{F,T}) = \mathrm{glb}(\setof{T,F}) = T \wedge F$.
:::

:::

::: exercise
Consider the poset depicted below.
Say whether it is a join semilattice, a meet semilattice, or both (and hence a lattice).

~~~ {.include-tikz size=mid}
lattice_pentagon.tikz
~~~

::: solution
This is a lattice.
We can show this in the form of two tables, one for meet and one for join.
Because of commutativity, we only need to fill in the upper diagonal of the table (that is to say, because $a \wedge b = b \wedge a$ it is sufficient to fill the cell in row $a$, column $b$ and leave the cell in row $b$, column $a$ empty).

| $\wedge$ |  a  |  b  |  c  |  d  |  e  |
| --:      | :-: | :-: | :-: | :-: | :-: |
|  a       |  a  |  a  |  a  |  a  |  a  |
|  b       |     |  b  |  a  |  b  |  b  |
|  c       |     |     |  c  |  a  |  c  |
|  d       |     |     |     |  d  |  d  |
|  e       |     |     |     |     |  e  |

| $\vee$   |  a  |  b  |  c  |  d  |  e  |
| --:      | :-: | :-: | :-: | :-: | :-: |
|  a       |  a  |  b  |  c  |  d  |  e  |
|  b       |     |  b  |  e  |  d  |  e  |
|  c       |     |     |  c  |  e  |  e  |
|  d       |     |     |     |  d  |  e  |
|  e       |     |     |     |     |  e  |

:::

:::

::: exercise
Say whether the following statement is true or false.
Justify your answer.

If a poset $\tuple{S, \leq}$ with a finite carrier $S$ does not contain a unique element $x \in S$ such that $x \leq y$ for all $y \in S$, then this poset cannot be a meet semilattice.

::: solution
This statement is false.
Consider the poset $\tuple{\emptyset, \leq}$, which has a finite carrier.
Clearly $\emptyset$ does not contain such a unique element $x$ because it contains no elements at all.
However, $\tuple{\emptyset, \leq}$ is a meet semilattice because the requirement that $x \wedge y$ must exist for all $x, y \in \emptyset$ is vacuously satisfied due to there not being any such $x$ and $y$ to begin with.

However, if we restrict ourselves to posets with finite, non-empty carriers, the statement is true.
Suppose there is no $x$ such that $x \leq y$ for all $y \in S$.
This implies that $S$ contains at least two elements --- if $S$ contained only $x$, then it would hold that $x \leq y$ for all $y \in S$ as $x \leq x$ follows from the reflexivity of the partial order $\leq$.
Then there must be $x$ and $y$ such that there are no $z$ and $z'$ with $z \leq x$ and $z' \leq y$.
But then it follows immediately that $x \wedge y$ does not exist, and thus $\tuple{S, \leq}$ is not a meet semilattice.
:::

:::

::: exercise
Say whether the following statement is true or false.
Justify your answer.

If a poset $\tuple{S, \leq}$ with a finite carrier $S$ contains a unique element $x \in S$ such that $x \leq y$ for all $y \in S$, then this poset is guaranteed to be a meet semilattice.

::: solution
This is false.
Consider the poset $\tuple{\setof{0,a,b,A,B}}$ such that $0 \leq a$, $0 \leq b$, $a \leq A$, $a \leq B$, $b \leq A$, and $b \leq B$.
In this case, $0 \leq y$ for all $y \in \setof{0,a,b,A,B}$, yet $A \wedge B$ does not exist.
:::

:::
