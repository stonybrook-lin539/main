---
pagetitle: >-
    Tuples: The basics (Solutions)
---

# Tuples: The basics (Solutions)

::: exercise
For each one of the following tuples, compute its length.

1. $\tuple{a,b,a}$
1. $\tuple{a,\tuple{b},a}$
1. $\tuple{a,\tuple{b,a}}$
1. $\tuple{\setof{a,b}, \tuple{a}}$
1. $\tuple{\tuple{a, b,\setof{a,a}}}$

::: solution
1. $3$
1. $3$
1. $2$
1. $2$
1. $1$
:::

::: solution_explained
1. This tuple has three components, which are $a$, $b$, and $a$ again.
   Keep in mind that in contrast to set cardinality, duplicates are not ignored when computing the length of a tuple.
1. The second component has changed from $b$ to $\tuple{b}$, but this does not change how many components there are.
1. This tuple has two components, the first being $a$, the second being the tuple $\tuple{b,a}$.
   Note that we do not consider the internal make-up of that tuple when calculating the number of components of the containing tuple.
1. Again we have two components.
   The first one is the set $\setof{a,b}$ (and again we ignore the internal make-up of the set), and other is $\tuple{a}$.
1. This tuple contains only one component, which is $\tuple{a, b, \setof{a,a}}$.
   Again it does not matter that this tuple has multiple components.
:::

:::

::: exercise
For each one of the formulas below, what is its value?

1. $\pi_3(\tuple{a,b,c,d})$
1. $\pi_8(\tuple{a,b,c,d})$
1. $\pi_0(\tuple{a,b,c,d})$
1. $\pi_3(\tuple{a,b,\tuple{c,d}})$
1. $\pi_1(\pi_3(\tuple{a,b,\tuple{c,d}}))$

::: solution
1. $c$
1. undefined
1. undefined
1. $\tuple{c,d}$
1. $c$
:::

::: solution_explained
1. $\pi_3$ returns the third component of its argument $\tuple{a,b,c,d}$, which is $c$.
1. $\pi_8$ is supposed to return the 8th component of its argument, but $\tuple{a,b,c,d}$ only has 4 components.
1. Similarly, there is no such thing as the 0th component of a tuple.
1. Nothing special going on here, we simply determine the third component.
   It does not matter at this point that this component happens to be a tuple.
1. As we just saw, $\pi_3(\tuple{a,b,\tuple{c,d}})$ is $\tuple{c,d}$.
   This becomes the argument of $\pi_1$, which returns its first component, which is $c$.
:::

:::

::: exercise
Explain why $\tuple{a,b} = \tuple{b,a}$ implies $a = b$.

::: solution
The only way two tuples can be identical is if all their respective components are identical.
Hence $\tuple{a,b} = \tuple{b,a}$ holds only if the first components of these tuples are identical and the second components of the tuples are identical.
Hence $\pi_1(\tuple{a,b}) = \pi_1(\tuple{b,a})$, which is the same as saying $a = b$.
We get the same result if we use $\pi_2$ instead of $\pi_1$.
:::
:::

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
Calculate the result of the following concatenations:

1. $\tuple{a,b} \tuplecat ((\tuple{c} \tuplecat \tuple{a,b}) \tuplecat \tuple{a,c,e})$
1. $(\tuple{a,b} \tuplecat \tuple{c}) \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e})$

::: solution
1. $\tuple{a,b,c,a,b,a,c,e}$

:::

::: solution_explained
All we have to do is to resolve the concatenations step by step.
$
\begin{align*}
\tuple{a,b} \tuplecat ((\tuple{c} \tuplecat \tuple{a,b}) \tuplecat \tuple{a,c,e})
&=
\tuple{a,b} \tuplecat (\tuple{c,a,b} \tuplecat \tuple{a,c,e})\\
&=
\tuple{a,b} \tuplecat (\tuple{c,a,b,a,c,e}\\
&=
\tuple{a,b,c,a,b,a,c,e}\\
\end{align*}
$

$
\begin{align*}
(\tuple{a,b} \tuplecat \tuple{c}) \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e})
&=
\tuple{a,b,c} \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e})\\
&=
\tuple{a,b,c} \tuplecat (\tuple{a,b,a,c,e})\\
&=
\tuple{a,b,c,a,b,a,c,e}\\ 
\end{align*}
$
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
For instance, if $a$ is the string *ba* and $b$ is the string *baba*, then $a \neq b$ yet $a \cdot b$ and $b \cdot a$ are both *bababa*.
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
Does the concatenation of $\tuple{a,b}$ and $\tuple{c}$ yield the same result as the concatenation of $\tuple{a,b}$ and $\tuple{\tuple{c}}$?
Justify your answer!

::: solution
No.
We have $\tuple{a,b} \tuplecat \tuple{c} = \tuple{a,b,c}$, whereas $\tuple{a,b} \tuplecat \tuple{\tuple{c}} = \tuple{a,b,\tuple{c}}$.
:::
:::
