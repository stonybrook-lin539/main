# Crossproduct (Solutions)

::: exercise
Why shouldn't we use a set $\setof{s,c}$ instead of the pair $\tuple{s,c}$?
What might go wrong in this case depending on our choice of $S$ and $C$?

::: solution
Since sets have no order, it is not clear whether in a set $\setof{s,c}$ $s$ specifies the shape or the color, and similarly for $c$.
This isn't a problem for English because there are no words that are ambiguous between describing a shape and describing a color.
But suppose that English undergoes a change such that *magenta* can now also mean rectangular, and *teal* can also mean circular.
Then the set $\setof{ \text{magenta}, \text{teal} }$ could be interpreted as *rectangular and teal*, or as *circular and magenta*.
With pairs, on the other hand, these two are clearly distinguished as $\tuple{ \text{magenta}, \text{teal}}$ and $\tuple{ \text{teal}, \text{magenta} }$.
:::

:::

::: exercise
Suppose $S$ consists of \emph{John}, \emph{Mary}, and \emph{the old man}, whereas $V$ contains only *slept* and *left*.
Compute $S \times V$.

::: solution
$S \times V$ is the set containing all of the following (and nothing else):

1. $\tuple{\text{John}, \text{slept}}$
1. $\tuple{\text{John}, \text{left}}$
1. $\tuple{\text{Mary}, \text{slept}}$
1. $\tuple{\text{Mary}, \text{left}}$
1. $\tuple{\text{the old man}, \text{slept}}$
1. $\tuple{\text{the old man}, \text{left}}$
:::

:::

::: example
Now suppose that we also have a set $A \is \setof{ \text{awesome} }$.
Then $S \times C \times A$ would be a set containing the following triples:


- $\tuple{\text{square}, \text{blue}, \text{awesome}}$
- $\tuple{\text{circle}, \text{blue}, \text{awesome}}$
- $\tuple{\text{square}, \text{red},  \text{awesome}}$
- $\tuple{\text{circle}, \text{red},  \text{awesome}}$

:::

::: exercise
List all 8 members of $A \times C \times S \times A \times C \times A$.

::: solution
1. $\tuple{\text{awesome}, \text{blue}, \text{square}, \text{awesome}, \text{blue}, \text{awesome}}$
1. $\tuple{\text{awesome}, \text{blue}, \text{square}, \text{awesome}, \text{red}, \text{awesome}}$
1. $\tuple{\text{awesome}, \text{blue}, \text{circle}, \text{awesome}, \text{blue}, \text{awesome}}$
1. $\tuple{\text{awesome}, \text{blue}, \text{circle}, \text{awesome}, \text{red}, \text{awesome}}$
1. $\tuple{\text{awesome}, \text{red}, \text{square}, \text{awesome}, \text{blue}, \text{awesome}}$
1. $\tuple{\text{awesome}, \text{red}, \text{square}, \text{awesome}, \text{red}, \text{awesome}}$
1. $\tuple{\text{awesome}, \text{red}, \text{circle}, \text{awesome}, \text{blue}, \text{awesome}}$
1. $\tuple{\text{awesome}, \text{red}, \text{circle}, \text{awesome}, \text{red}, \text{awesome}}$
:::

:::

::: exercise
In a certain sense, the crossproduct is the result of generalizing concatenation from tuples to sets of 1-tuples.
Explain why.

::: solution
By definition, $A \times B$ contains all pairs $\tuple{a,b}$ such that $a \in A$ and $b \in B$.
But that is the same as $\tuple{a} \tuplecat \tuple{b}$ for all $a \in A$ and $b \in B$.
Taking this one step further, we define $A' \is \setof{ \tuple{a} \mid a \in A}$ and $B' \is \setof{ \tuple{b} \mid b \in B}$ --- that is to say, $A'$ and $B'$ are sets of 1-tuples where each 1-tuple contains an element of $A$ or $B$, respectively.
Now let us define a generalized version of concatenation that directly applies to sets like $A'$ and $B'$: $A' \tuplecat B' \is \setof{ a \tuplecat b \mid a \in A', b \in B'}$.
This is exactly the same set as $\setof{ \tuple{a,b} \mid a \in A, b \in B}$, which in turn is the definition of $A \times B$.

This argument can be generalized to $A \times B \times C$, and $A \times B \times C \times D$, and so on.
:::

:::

::: exercise
If $A$ has $m$ members and $B$ has $n$ members, then the number of tuples in $A \times B$ is $m$ multiplied by $n$.
Explain why.

::: solution
The crossproduct $A \times B$ contains all tuples of the form $\tuple{a,b}$ such that $a \in A$ and $b \in B$.
Let us refer to the $m$ members of $A$ as $a_1$, $a_2$, and so on, up to $a_m$.
Since $B$ has $n$ distinct members, there are $n$ distinct tuples of the form $\tuple{a_1, b}$, and $n$ distinct tuples of the form $\tuple{a_2, b}$.
For each member $a_i$ of $A$ there are thus $n$ distinct tuples that start with $a_i$, and since there are $m$ distinct choices for $a_i$ ($a_1$, or $a_2$, and so on, up to and including $a_m$), there are $m \cdot n$ distinct tuples overall.
:::

:::

::: exercise
Continuing the previous example, list all elements of $A \times B \times C$.
Does this set also contain 6 tuples?
Are they also pairs?

::: solution

The elements of $A \times B \times C$ are:

1. $\tuple{a, T, 1}$
1. $\tuple{a, F, 1}$
1. $\tuple{b, T, 1}$
1. $\tuple{b, F, 1}$
1. $\tuple{c, T, 1}$
1. $\tuple{c, F, 1}$

There are again 6 tuples, but they are triples, not pairs.
:::
:::
