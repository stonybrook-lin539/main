# Lower bounds and upper bounds (Solutions)

::: exercise
Draw corresponding diagrams indicating the upper and lower bounds of


- $\setof{1,3}$
- $\emptyset$

::: solution

~~~ {.include-tikz size=mid}
lattice_123_bounds_13.tikz
~~~

~~~ {.include-tikz size=mid}
lattice_123_bounds_empty.tikz
~~~

:::

:::

::: exercise
Say whether the following is true or false, and justify your answer:
if $\tuple{S, \leq}$ is a poset, then it holds for all $x, y \in S$ that $y$ is both an upper and a lower bound for $x$ iff $x = y$.

::: solution
This statement is true.

If $y$ is both an upper bound and a lower bound for $x$, then we have $y \leq x$ and $x \leq y$.
Since $\leq$ is a partial order and hence antisymmetric, this entails that $x = y$.

The other direction is trivial.
Since $\leq$ is reflexive, we have $x \leq x$, which means that $x$ is both an upper bound of itself and a lower bound of itself.
:::

:::

::: exercise
Given some arbitrary poset $\tuple{S, \leq}$, what are $\mathrm{lb}(\emptyset)$ and $\mathrm{ub}(\emptyset)$?
Justify your answer.

::: solution
In this case, $\mathrm{ub}(\emptyset) = \mathrm{lb}(\emptyset) = S$.
This follows immediately from the definitions.
First, $\mathrm{ub}(\emptyset)$ is the set of all $y \in S$ such that $x \leq y$ for all $x \in \emptyset$.
Since there are no such $x$, this condition is vacuously true for ever $y$ in $S$.
Similarly, $\mathrm{lb}(\emptyset)$ is the set of all $y \in S$ such that $y \leq x$ for all $x \in \emptyset$.
But again there are no such $x$ and consequently every $y \in S$ satisfies this condition.
:::

:::

::: exercise
Explain why the set of upper bounds of some element $x$ of a poset is identical to $\mathrm{ub}(\setof{x})$.

::: solution
By definition, $\mathrm{ub}(\setof{x})$ contains all $y$ such that $z \leq y$ for all $z \in \setof{x}$.
But since $\setof{x}$ contains only $x$, this reduces to the set of all $y$ such that $x \leq y$, which by definition are all the upper bounds of $x$.
:::

:::

::: exercise
Given the poset in the previous example, compute all of the following:

1. $\mathrm{ub}(\setof{\setof{1,2}, \setof{2,3}})$
1. $\mathrm{lb}(\setof{\setof{1,2}, \setof{2,3}})$
1. $\mathrm{ub}(\setof{\emptyset})$
1. $\mathrm{ub}(\emptyset)$
1. $\mathrm{lb}(\setof{\emptyset, \setof{1,2,3}})$
1. $\mathrm{lb}(\setof{\setof{1}, \setof{2,3}, \setof{1,2,3}})$
1. $\mathrm{ub}(\setof{\setof{1}, \setof{2}, \setof{3}})$

::: solution
1. $\mathrm{ub}(\setof{\setof{1,2}, \setof{2,3}}) = \setof{1,2,3}$
1. $\mathrm{lb}(\setof{\setof{1,2}, \setof{2,3}}) = \setof{\emptyset, \setof{2}}$
1. $\mathrm{ub}(\setof{\emptyset})$ contains all elements of the poset
1. $\mathrm{ub}(\emptyset)$ contains all elements of the poset
1. $\mathrm{lb}(\setof{\emptyset, \setof{1,2,3}}) = \setof{\emptyset}$
1. $\mathrm{lb}(\setof{\setof{1}, \setof{2,3}, \setof{1,2,3}}) = \setof{\emptyset}$
1. $\mathrm{ub}(\setof{\setof{1}, \setof{2}, \setof{3}}) = \setof{ \setof{1,2,3} }$
:::

:::

::: exercise
Consider $\tuple{\setof{0,1,2,3,4}, \leq}$, the set of the first five natural numbers ordered in the usual fashion via $\leq$.
Using the pictorial format described above, indicate the lower and upper bounds for the following subsets:


- $\setof{2}$
- $\setof{1,4}$
- $\setof{2,3}$
- $\setof{0,3}$

:::

::: exercise
Since $\mathrm{lb}$ and $\mathrm{ub}$ are functions from sets to sets, the output of one can be the input for the other.
Compute $\mathrm{lb}(\mathrm{ub}({\setof{0,3}}))$ over $\setof{0,1,2,3,4}$ ordered by $\leq$.
By comparison, what is $\mathrm{ub}(\mathrm{lb}(\setof{0,3}))$?

::: solution
1. $\mathrm{lb}(\mathrm{ub}(\setof{0,3})) = \mathrm{lb}(\setof{3,4}) = \setof{0,1,2,3}$
1. $\mathrm{ub}(\mathrm{lb}(\setof{0,3})) = \mathrm{ub}(\setof{0}) = \setof{0,1,2,3,4}$
:::

:::

::: exercise
Now consider $\tuple{\mathbb{N}, \leq}$ instead, the set of all natural numbers ordered via $\leq$.
For each one of the following statements, say whether it is true or false and justify your answer.

1. Any two natural numbers $x$ and $y$ have infinitely many upper bounds.
1. Any two natural numbers $x$ and $y$ have infinitely many lower bounds.

::: solution
1. This is true.
   Suppose without loss of generality that $x \leq y$.
   Then $\mathrm{ub}(\setof{x,y})$ contains every natural number $z$ such that $y \leq z$.
   There are infinitely many such $z$.
1. This is false.
   Suppose without loss of generality that $x \leq y$.
   Then $\mathrm{lb}(\setof{x,y}$ contains every natural number $z$ such that $z \leq x$.
   There are exactly $x + 1$ such $z$, which is a finite number.
:::

:::

::: exercise
You might think that the poset in the previous example is somehow defective or pathological because no element is related to any element except itself.
But that's not really the issue, as is witnessed by the structure below.

~~~ {.include-tikz size=mid}
poset_nobounds.tikz
~~~

Find the smallest subset $S$ such that $\mathrm{ub}(S) = \emptyset$ and $\mathrm{lb}(S) = \emptyset$.

::: solution
$S = \setof{a,b,d,e}$
:::

::: solution_explained
It is the case that $\mathrm{ub}(S)$ is empty because there is no $z$ such that $d \leq z$ and $e \leq z$.
Similarly, $\mathrm{ub}(S)$ is empty because there is no $z$ such that $z \leq a$ and $z \leq b$.
In order to show that $S$ is the smallest subset for which this holds, suppose we remove $e$ from $S$.
In this case, we have $\mathrm{ub}(\setof{a,b,d}) = \setof{d} \neq \emptyset$.
The same happens if we remove $d$ instead of $e$.
If we remove $a$, then $\mathrm{lb}(\setof{b,d,e}) = \setof{b} \neq \emptyset$, and similarly if we remove $b$ instead of $a$.
Hence $S$ is indeed the smallest subset for which it holds that $\mathrm{ub}(S) = \mathrm{lb}(S) = \emptyset$.
:::

:::

::: exercise
Say whether the following is true or false, and justify your answer:

Given some poset $\tuple{S, \leq}$, it holds for every finite subset $\setof{s_1, \ldots, s_n}$ of $S$ that
$$\mathrm{ub}(\setof{s_1, \ldots, s_n}) = \mathrm{ub}(\setof{s_1}) \cap \mathrm{ub}(\setof{s_2} \cap \cdots \cap \mathrm{ub}(\setof{s_n})$$

::: solution
This is true.

By definition, $\mathrm{ub}(\setof{s_1, \ldots, s_n})$ is the set of all $y$ such that $x \leq y$ for all $x \in \setof{s_1, \ldots, s_n}$.
In other words, it is the set of all $y$ such that $s_1 \leq y$, and $s_2 \leq y$, and $s_3 \leq y$, and so on.

Now consider the intersection $\mathrm{ub}(\setof{s_1}) \cap \mathrm{ub}(\setof{s_2} \cap \cdots \cap \mathrm{ub}(\setof{s_n})$.
It is the set of all $y$ that are members of $\mathrm{ub}(\setof{s_1})$, and members of $\mathrm{ub}(\setof{s_2})$, and members of $\mathrm{ub}(\setof{s_3})$, and so on.
In other words, it is the set of all $y$ such that $s_1 \leq y$, and $s_2 \leq y$, and $s_3 \leq y$, and so on.
As we already saw, this is the set $\mathrm{ub}(\setof{s_1, \ldots, s_n})$.
:::

:::

::: exercise
Say whether the following is true or false, and justify your answer:

Given some poset $\tuple{S, \leq}$, it holds for every finite subset $\setof{s_1, \ldots, s_n}$ of $S$ that
$$\mathrm{lb}(\setof{s_1, \ldots, s_n}) = \mathrm{lb}(\setof{s_1}) \cup \mathrm{lb}(\setof{s_2} \cup \cdots \cup \mathrm{lb}(\setof{s_n})$$

::: solution
This is false.
As a concrete counterexample, suppose we have a poset $\tuple{\setof{1,a}, \leq}$ with $1 \leq 1$ and $a \leq a$ and no other orderings.
Then $\mathrm{lb}(\setof{1,a}) = \emptyset$ whereas $\mathrm{lb}(\setof{1}) \cup \mathrm{lb}(\setof{a}) = \setof{1} \cup \setof{a} = \setof{1,a}$.
:::

:::
