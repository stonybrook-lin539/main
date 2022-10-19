# Tuples: Basics (Solutions)

::: exercise
Fill in the gaps with $=$ and $\neq$ as appropriate, assuming that $a$ and $b$ are distinct elements:

1. $\tuple{a} \_ \tuple{b}$
1. $\tuple{a,b,a} \_ \tuple{a,b,b}$
1. $\tuple{a,b,a,a} \_ \tuple{a,b,a,a}$
1. $\tuple{a,a,b,a} \_ \tuple{a,b,a,a}$
1. $\tuple{a,a,b,a} \_ \tuple{a,a,\setof{b},a}$
1. $\tuple{a,a,b,a} \_ \tuple{a,\tuple{a,b},a}$

::: solution
1. $\tuple{a} \neq \tuple{b}$
1. $\tuple{a,b,a} \neq \tuple{a,b,b}$
1. $\tuple{a,b,a,a} = \tuple{a,b,a,a}$
1. $\tuple{a,a,b,a} \neq \tuple{a,b,a,a}$
1. $\tuple{a,a,b,a} \neq \tuple{a,a,\setof{b},a}$
1. $\tuple{a,a,b,a} \neq \tuple{a,\tuple{a,b},a}$
:::

::: solution_explained
Two $n$-tuples are identical iff it holds for every $i$ between 1 and $n$ that the $i$-th components of the two tuples are the same.

1. $\tuple{a} \neq \tuple{b}$: Since $a \neq b$, the initial components of these 1-tuples are distinct, and thus the tuples are distinct.
1. $\tuple{a,b,a} \neq \tuple{a,b,b}$: Again we have $a \neq b$, but this time this matters for the third component, where the first tuple has $a$ and the second tuple has $b$.
1. $\tuple{a,b,a,a} = \tuple{a,b,a,a}$: These tuples have exactly the same components. Going though the components from left to right, we have $a = a$, $b = b$, $a = a$, and $a = a$.
1. $\tuple{a,a,b,a} \neq \tuple{a,b,a,a}$: Here the tuples disagree on their second component as well as on their third component.
1. $\tuple{a,a,b,a} \neq \tuple{a,a,\setof{b},a}$: Remember that $b \neq \setof{b}$, so these tuples disagree on their third component.
1. $\tuple{a,a,b,a} \neq \tuple{a,\tuple{a,b},a}$: The first tuple is a 4-tuple with the components $a$, $a$, $b$, and $a$. The second tuple is a triple with the components $a$, $\tuple{a,b}$, and $a$.
:::

:::

::: exercise
If $A \is \setof{a}$, then what is $A^5$?

::: solution
$A^5 = \setof{ \tuple{a,a,a,a,a} }$
:::

::: solution_explained
$A^5$ is the set of all $5$-tuples over elements drawn from $A$.
Since $A$ contains only $a$, there is only one such $5$-tuple, which is $\tuple{a,a,a,a,a}$.
:::

:::

::: exercise
If $A \is \setof{\setof{a}}$, then what is $A^1$?

::: solution
$A^1 = \setof{ \tuple{a} }$
:::

::: solution_explained
$A^5$ is the set of all $1$-tuples over elements drawn from $A$.
Since $A$ contains only $a$, there is only one such $1$-tuple, which is $\tuple{a}$.
:::

:::

::: exercise
Calculate the result of the following concatenations:

1. $\tuple{a,b} \tuplecat ((\tuple{c} \tuplecat \tuple{a,b}) \tuplecat \tuple{a,c,e})$
1. $(\tuple{a,b} \tuplecat \tuple{c}) \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e})$

::: solution
1. $\tuple{a,b,c,a,b,a,c,e}$

:::

::: solution_explained
All we have to do is to resolve the concatenations step by step.
$$
\begin{align*}
\tuple{a,b} \tuplecat ((\tuple{c} \tuplecat \tuple{a,b}) \tuplecat \tuple{a,c,e})
&=
\tuple{a,b} \tuplecat (\tuple{c,a,b} \tuplecat \tuple{a,c,e})\\
&=
\tuple{a,b} \tuplecat (\tuple{c,a,b,a,c,e}\\
&=
\tuple{a,b,c,a,b,a,c,e}\\
\end{align*}
$$

$$
\begin{align*}
(\tuple{a,b} \tuplecat \tuple{c}) \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e})
&=
\tuple{a,b,c} \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e})\\
&=
\tuple{a,b,c} \tuplecat (\tuple{a,b,a,c,e})\\
&=
\tuple{a,b,c,a,b,a,c,e}\\ 
\end{align*}
$$
:::

:::

::: exercise
Write down all possible ways of obtaining $\tuple{a,b,c,d}$ via concatenation of tuples whose length is at least $1$.
For instance, one possible way is $\tuple{a,b} \tuplecat \tuple{c, d}$, but there's several more.

::: solution
Since concatenation is associative, we can ignore bracketing.
This leaves us with the following 7 options:

1. $\tuple{a} \tuplecat \tuple{b} \tuplecat \tuple{c} \tuplecat \tuple{d}$
1. $\tuple{a,b} \tuplecat \tuple{c} \tuplecat \tuple{d}$
1. $\tuple{a} \tuplecat \tuple{b,c} \tuplecat \tuple{d}$
1. $\tuple{a} \tuplecat \tuple{b} \tuplecat \tuple{c,d}$
1. $\tuple{a,b} \tuplecat \tuple{c,d}$
1. $\tuple{a} \tuplecat \tuple{b,c,d}$
1. $\tuple{a,b,c} \tuplecat \tuple{d}$
:::

:::

::: exercise
Tuple concatenation is not commutative.
That is to say, for some tuples $a$ and $b$ it is not the case that $a \tuplecat b = b \tuplecat a$.
Illustrate this with an example.

::: solution
The simplest example is $a = \tuple{0}$ and $b = \tuple{1}$.
Then $a \tuplecat b = \tuple{0} \tuplecat \tuple{1} = \tuple{0,1} \neq \tuple{1,0} = \tuple{1} \tuplecat \tuple{0} = b \tuplecat a$.
:::

::: solution_explained
The solutions is fairly self-explanatory, but one additional remark may be helpful here.
With strings we saw that there can be cases where $a \cdot b = b \cdot a$ even though $a \neq b$.
For instance, if $a$ is the string *ba* and the $b$ is the string *baba*, then $a \neq b$ yet $a \cdot b$ and $b \cdot a$ are both *bababa*.
With tuples, the situation is not as clear cut.
If $a \is \tuple{b,a}$ and $b \is \tuple{b,a,b,a}$, then $a \tuplecat b = \tuple{b,a,b,a,b,a} = b \tuplecat a$.
But if $a \is \tuple{ba}$ and $b \is \tuple{baba}$, then $a \tuplecat b = \tuple{ba, baba} \neq \tuple{baba, ba} = b \tuplecat a$.
:::

:::


::: exercise
Compute $\tuple{a} \tuplecat \tuple{}$ and $\tuple{} \tuplecat \tuple{a,a,a}$.

::: solution
1. $\tuple{a} \tuplecat \tuple{} = \tuple{a}$
1. $\tuple{} \tuplecat \tuple{a,a,a} = \tuple{a,a,a}$.
:::

:::


::: exercise
What is the length of the following tuples?

1. $\tuple{a,b,c}$
1. $\tuple{a, \tuple{b,c}}$
1. $\tuple{\tuple{a}, \tuple{b}, \tuple{c}}$
1. $\tuple{\tuple{a,b,c}}$
1. $\tuple{\tuple{}, \tuple{}, \tuple{}}$

::: solution
1. $\tuple{a,b,c}$: 3-tuple (triple)
1. $\tuple{a, \tuple{b,c}}$: 2-tuple (pair)
1. $\tuple{\tuple{a}, \tuple{b}, \tuple{c}}$: 3-tuple (triple)
1. $\tuple{\tuple{a,b,c}}$: 1-tuple
1. $\tuple{\tuple{}, \tuple{}, \tuple{}}$: 3-tuple (triple)
:::

::: solution_explained
This is actually fairly simple once you realize that the only thing that matters for the length of a tuple is how many components it has, not what's going on inside those components.
It is completely irrelevant whether a given component is the number $15$, or the symbol $a$, or the string $abba$, or the set $\setof{a,b,c}$, or the tuple $\tuple{a,\tuple{b,b}}$.

1. $\tuple{a,b,c}$: The components are $a$, $b$, and $c$, hence this is a triple.
1. $\tuple{a, \tuple{b,c}}$: The components are $a$ and $\tuple{b,c}$, hence this is a pair.
1. $\tuple{\tuple{a}, \tuple{b}, \tuple{c}}$: The components are $\tuple{a}$, $\tuple{b}$, and $\tuple{c}$, hence this is a triple.
1. $\tuple{\tuple{a,b,c}}$: The only component is $\tuple{a,b,c}$, hence this is a 1-tuple.
1. $\tuple{\tuple{}, \tuple{}, \tuple{}}$: The three components are $\tuple{}$, and $\tuple{}$ again, and $\tuple{}$ one final time. Since tuples allow duplicates, each one of them counts as its own component, and overall this is a triple.
:::
:::

::: exercise
Does the concatenation of $\tuple{a,b}$ and $\tuple{c}$ yield the same result as the concatenation of $\tuple{a,b}$ and $\tuple{\tuple{c}}$?
Justify your answer!

::: solution
No, it does not.
The former yields $\tuple{a,b,c}$, the latter $\tuple{a,b,\tuple{c}}$.
Two tuples are identical iff all their respective components are identical.
But $c \neq \tuple{c}$, so the two tuples disagree on their third component.
:::
:::
