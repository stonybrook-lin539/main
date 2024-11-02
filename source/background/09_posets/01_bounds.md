---
pagetitle: >-
    Lower bounds and upper bounds
---

# Lower bounds and upper bounds

Suppose that we have some poset $\tuple{S, \leq}$, where $\leq$ is an arbitrary partial order.
Given a set $x \in S$, we can ask which elements are less than $x$ and which elements are greater than $x$.
These are the **lower bounds** and **upper bounds** of $x$.
This is an important notion, and it can be generalized from a single member of $S$ to whole subsets of $S$.

## Bounds for single elements

The definition for lower and upper bounds of a single element in a poset is straightforward.

::: definition
Let $\tuple{S, \leq}$ be an arbitrary poset and $x$ an arbitrary member of $S$.
Then $y \in S$ is a **lower bound** for $x$ iff $y \leq x$. 
We call $y$ an **upper bound** iff $x \leq y$.
:::

::: example
Consider the poset below, which consists of all subsets of $\setof{1,2,3}$ ordered by the subset relation $\subseteq$.

~~~ {.include-tikz size=mid}
lattice_123.tikz
~~~

The upper bounds of $\setof{1}$ are $\setof{1}$, $\setof{1,2}$, $\setof{1,3}$, and $\setof{1,2,3}$.
Its lower bounds are $\setof{1}$ and $\emptyset$.
:::

::: example
Thinking of upper and lower bounds in pictorial terms may strengthen your intuitions.
In the figure below, upper bounds are in dashed boxes, and lower bounds in dashed circles.
We underline $\setof{1}$ to indicate that this is the element for which we are computing upper and lower bounds.

~~~ {.include-tikz size=mid}
lattice_123_bounds1.tikz
~~~
:::

::: exercise
Draw corresponding diagrams indicating the upper and lower bounds of


- $\setof{1,3}$
- $\emptyset$

::: solution
The upper bounds of $\setof{1,3}$ are as follows:

~~~ {.include-tikz size=mid}
lattice_123_bounds_13.tikz
~~~

And the upper bounds of $\emptyset$ are as follows: 

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
If $y$ is an upper bound for $x$, then $x \leq y$, and if $y$ is a lower bound for $x$, then $y \leq x$.
Since $\leq$ is a partial order, and thus antisymmetric, $x \leq y$ and $y \leq x$ jointly imply $x = y$.
:::
:::

## Generalizing bounds to subsets

While it can be interesting to know the lower and upper bounds for a given element, very often we want to know the bounds for multiple elements.
For instance, which elements are such that they are greater than both $x$ and $y$?
To this end, we generalize bounds from elements of a poset to subsets of the poset.
We say that $y$ is an upper (or lower) bound for subset $T$ iff $y$ is an upper (or lower) bound for every member of $T$.

::: definition
Let $\tuple{S, \leq}$ be a poset and $T$ and arbitrary subset of $S$.
Then the set of **upper bounds** of $T$ is
$$\mathrm{ub}(T) \is \setof{ y \in S \mid x \leq y \text{ for all } x \in T}.$$
Similarly, the set of **lower bounds** of $T$ is
$$\mathrm{lb}(T) \is \setof{ y \in S \mid y \leq x \text{ for all } x \in T}.$$
:::

::: example
Consider the poset $\tuple{\setof{0,1,2,3,4}, \leq}$, the set of the first five natural numbers ordered in the usual fashion via $\leq$.
The lower bounds of $2$ and $4$ are $0$, $1$, and $2$ as these are the only elements that are less than $2$ and less than $4$.
More succinctly, $\mathrm{lb}(\setof{2,4}) = \setof{0,1,2}$.

The only upper bound of $2$ and $4$ is $4$ as no other member of the carrier $\setof{0,1,2,3,4}$ is greater than both of those numbers.
Hence we write $\mathrm{ub}(\setof{2,4}) = \setof{4}$.
:::

::: exercise
Given some arbitrary poset $\tuple{S, \leq}$, what are $\mathrm{lb}(\emptyset)$ and $\mathrm{ub}(\emptyset)$?
Justify your answer.

::: solution
By definition, $\mathrm{lb}(A)$ contains every $x$ such that $x \leq y$ is true for all $y \in A$.
But if $A$ is empty, then this condition is trivially satisfied --- for any arbitrary $x$, there is no $y \in A$ such that $x \leq y$ is false.
Hence $\mathrm{lb}(\emptyset) = S$.
For the same reason, it is also the case that $\mathrm{ub}(\emptyset) = S$.
:::
:::

::: example
Consider once more the poset of all subsets of $\setof{1,2,3}$ ordered by the subset relation $\subseteq$.

~~~ {.include-tikz size=mid}
lattice_123.tikz
~~~

The upper bounds of $\setof{1}$ and $\setof{2}$ are $\setof{1,2}$ and $\setof{1,2,3}$.
Their only lower bound is $\emptyset$.
In mathematical notation, this is
$$\mathrm{lb}(\setof{ \setof{1}, \setof{2} }) = \setof{ \setof{1,2}, \setof{1,2,3} }$$
and
$$\mathrm{ub}(\setof{ \setof{1}, \setof{2} }) = \setof{ \emptyset }.$$

Yes, those are sets of sets.
You have to keep in mind that $\mathrm{lb}$ and $\mathrm{ub}$ always apply to the set of things whose lower and upper bounds we want to compute.
In the case at hand, these things themselves are sets, so $\mathrm{lb}$ and $\mathrm{ub}$ take a set of sets as their argument.
And since they return a set of things that are lower/upper bounds, we get back a set of sets.

We can also depict this in the graphical format that we used for the lower and upper bounds of individual elements.

~~~ {.include-tikz size=mid}
lattice_123_bounds1-2.tikz
~~~
:::

::: example
Given the same poset, the upper bounds of $\setof{1}$ are $\setof{1}$, $\setof{1,2}$, $\setof{1,3}$, and $\setof{1,2,3}$, while the lower bounds are $\setof{1}$ and $\emptyset$.
Hence we have
$\mathrm{ub}(\setof{\setof{1}}) = \setof{\setof{1}, \setof{1,2}, \setof{1,3}, \setof{1,2,3}}$ and 
$\mathrm{lb}(\setof{\setof{1}}) = \setof{\emptyset, \setof{1}}$.
Again the notation is slightly confusing as we are looking at sets of elements of the poset, and these elements just so happen to be sets themselves.
Relying once more on our graphical format, we see that $\mathrm{ub}(\setof{\setof{1}})$ and $\mathrm{lb}(\setof{\setof{1}})$ yield the same upper and lower bounds that we computed for $\setof{1}$ at the beginning of this unit.

~~~ {.include-tikz size=mid}
lattice_123_bounds1.tikz
~~~
:::

::: exercise
Explain why the set of upper bounds of some element $x$ of a poset is identical to $\mathrm{ub}(\setof{x})$.

::: solution
Given some element $x$ of some poset $\tuple{S, \leq}$, its set of upper bounds is defined as $\setof{y \in S \mid x \leq y}$.
And for every subset $A$ of $S$,
$\mathrm{ub}(A) \is \setof{ y \in S \mid z \leq y \text{ for all } z \in A}$.
If $A \is \setof{x}$, then this definition reduces to
$\mathrm{ub}(A) \is \setof{ y \in S \mid z \leq y \text{ for all } z \in \setof{x}}$,
which is equivalent to
$\mathrm{ub}(A) \is \setof{ y \in S \mid x \leq y}$.
But as we saw before, this is the set of upper bounds of $x$.
:::
:::

::: example
One more example with the same poset.
The upper bounds of $\setof{2}$, $\setof{3}$, and $\setof{2,3}$ are $\setof{2,3}$ and $\setof{1,2,3}$, whereas their only lower bound is $\emptyset$.
We write this more succinctly as
$\mathrm{ub}(\setof{\setof{2}, \setof{3}, \setof{2,3}}) = \setof{\setof{2,3} \setof{1,2,3}}$ and 
$\mathrm{lb}(\setof{\setof{2}, \setof{3}, \setof{2,3}}) = \setof{\emptyset}$.
Once again we can also depict this in the graphical format: 

~~~ {.include-tikz size=mid}
lattice_123_bounds2-3-23.tikz
~~~
:::

::: exercise
Given the poset in the previous example, compute all of the following:


- $\mathrm{ub}(\setof{\setof{1,2}, \setof{2,3}})$
- $\mathrm{lb}(\setof{\setof{1,2}, \setof{2,3}})$
- $\mathrm{ub}(\setof{\emptyset})$
- $\mathrm{ub}(\emptyset)$
- $\mathrm{lb}(\setof{\emptyset, \setof{1,2,3}})$
- $\mathrm{lb}(\setof{\setof{1}, \setof{2,3}, \setof{1,2,3}})$
- $\mathrm{ub}(\setof{\setof{1}, \setof{2}, \setof{3}})$

::: solution
- $\mathrm{ub}(\setof{\setof{1,2}, \setof{2,3}}) = \setof{ \setof{ 1,2,3 } }$
- $\mathrm{lb}(\setof{\setof{1,2}, \setof{2,3}}) = \setof{ \setof{2}, \emptyset }$
- $\mathrm{ub}(\setof{\emptyset}) = \setof{ \emptyset, \setof{1}, \setof{2}, \setof{3}, \setof{1,2}, \setof{1,3}, \setof{2,3}, \setof{1,2,3} }$
- $\mathrm{ub}(\emptyset) = \setof{ \emptyset, \setof{1}, \setof{2}, \setof{3}, \setof{1,2}, \setof{1,3}, \setof{2,3}, \setof{1,2,3} }$
- $\mathrm{lb}(\setof{\emptyset, \setof{1,2,3}}) = \setof{ \emptyset }$
- $\mathrm{lb}(\setof{\setof{1}, \setof{2,3}, \setof{1,2,3}}) = \setof{ \emptyset }$
- $\mathrm{ub}(\setof{\setof{1}, \setof{2}, \setof{3}}) = \setof{ \setof{1,2,3} }$
:::
:::

::: exercise
Consider $\tuple{\setof{0,1,2,3,4}, \leq}$, the set of the first five natural numbers ordered in the usual fashion via $\leq$.
Using the pictorial format described above, indicate the lower and upper bounds for the following subsets:


- $\setof{2}$
- $\setof{1,4}$
- $\setof{2,3}$
- $\setof{0,3}$

::: solution
- The set of upper bounds of $\setof{2}$ is $\setof{2,3,4}$, while the set of lower bounds is $\setof{0,1,2}$.

~~~ {.include-tikz size=mid}
natnum_bounds_2.tikz
~~~

- The set of upper bounds of $\setof{1,4}$ is $\setof{4}$, while the set of lower bounds is $\setof{0,1}$.

~~~ {.include-tikz size=mid}
natnum_bounds_14.tikz
~~~

- The set of upper bounds of $\setof{2,3}$ is $\setof{3,4}$, while the set of lower bounds is $\setof{0,1,2}$.

~~~ {.include-tikz size=mid}
natnum_bounds_23.tikz
~~~

- The set of upper bounds of $\setof{0,3}$ is $\setof{3,4}$, while the set of lower bounds is $\setof{0}$.

~~~ {.include-tikz size=mid}
natnum_bounds_03.tikz
~~~
:::
:::

::: exercise
Since $\mathrm{lb}$ and $\mathrm{ub}$ are functions from sets to sets, the output of one can be the input for the other.
Compute $\mathrm{lb}(\mathrm{ub}({\setof{0,3}}))$ over $\setof{0,1,2,3,4}$ ordered by $\leq$.
By comparison, what is $\mathrm{ub}(\mathrm{lb}(\setof{0,3}))$?

::: solution
- $\mathrm{lb}(\mathrm{ub}(\setof{0,3})) = \mathrm{lb}(\setof{3}) = \setof{3}$
- $\mathrm{ub}(\mathrm{lb}(\setof{0,3})) = \mathrm{ub}(\setof{0}) = \setof{0}$
:::
:::

::: exercise
Now consider $\tuple{\mathbb{N}, \leq}$ instead, the set of all natural numbers ordered via $\leq$.
For each one of the following statements, say whether it is true or false and justify your answer.


- Any two natural numbers $x$ and $y$ have infinitely many upper bounds.
- Any two natural numbers $x$ and $y$ have infinitely many lower bounds.

::: solution
The first statement is true, the second one is false.

For any two natural numbers $x$ and $y$ such that $x \leq y$, $\mathrm{ub}(\setof{x,y}) = \setof{ z \in \mathbb{N} \mid y \leq z}$.
But irrespective of how we choose $y$, there are infinitely many $z \in \mathbb{N}$ such that $z \geq y$.

With $x$ and $y$ as before, it also holds that $\mathrm{lb}(\setof{x,y}) = \setof{ z \in \mathbb{N} \mid z \leq x}$.
But for any $x \in \mathbb{N}$, there are exactly $x+1$ elements $z \in \mathbb{N}$ such that $z \leq x$.
Hence $\mathrm{lb}(\setof{x,y})$ is finite for any choice of $x$ and $y$.
:::
:::


::: example
Note that the existence of upper and lower bounds isn't guaranteed once we move from individual elements of the posets to subsets.
Take for instance the poset $\tuple{\setof{1,2}, R}$ where $x \mathrel{R} y$ iff $x = y$.
<!-- You should convince yourself that this is a poset (i.e. that $R$ transitive, antisymmetric, and reflexive). -->
Yes, this is still a poset (there is an order, and it is partial).
In this case, $\mathrm{lb}(\setof{1,2}) = \emptyset$ because there simply is no $y$ such that $y \mathrel{R} 1$ and $y \mathrel{R} 2$.
In other words, $1$ and $2$ don't have any lower bounds.
For the same reason, they don't have any upper bounds either.
:::

::: exercise
You might think that the poset in the previous example is somehow defective or pathological because no element is related to any element except itself.
But that's not really the issue, as is witnessed by the structure below.

~~~ {.include-tikz size=mid}
poset_nobounds.tikz
~~~

Find the smallest subset $S$ such that $\mathrm{ub}(S) = \emptyset$ and $\mathrm{lb}(S) = \emptyset$.

::: solution
The smallest subset is $\setof{a,b,d,e}$.
This is because $\mathrm{lb}(\setof{a,b}) = \emptyset$, and if $\mathrm{lb}(A) = \emptyset$ for some subset $A$, then $\mathrm{lb}(B) = \emptyset$ for every $B \supseteq A$.
Similarly, $\mathrm{ub}(\setof{d,e}) = \emptyset$, and if $\mathrm{ub}(A) = \emptyset$ for some subset $A$, then $\mathrm{ub}(B) = \emptyset$ for every $B \supseteq A$.

Every proper subset of $\setof{a,b,d,e}$ has a non-empty set of upper bonds, a non-empty set of lower bounds, or both.
:::
:::

::: exercise
Say whether the following is true or false, and justify your answer:

Given some poset $\tuple{S, \leq}$, it holds for every finite subset $\setof{s_1, \ldots, s_n}$ of $S$ that
$$\mathrm{ub}(\setof{s_1, \ldots, s_n}) = \mathrm{ub}(\setof{s_1}) \cap \mathrm{ub}(\setof{s_2} \cap \cdots \cap \mathrm{ub}(\setof{s_n})$$

::: solution
The smallest subset is $\setof{a,b,d,e}$.
This is because $\mathrm{lb}(\setof{a,b}) = \emptyset$, and if $\mathrm{lb}(A) = \emptyset$ for some subset $A$, then $\mathrm{lb}(B) = \emptyset$ for every $B \supseteq A$.
Similarly, $\mathrm{ub}(\setof{d,e}) = \emptyset$, and if $\mathrm{ub}(A) = \emptyset$ for some subset $A$, then $\mathrm{ub}(B) = \emptyset$ for every $B \supseteq A$.

Every proper subset of $\setof{a,b,d,e}$ has a non-empty set of upper bonds, a non-empty set of lower bounds, or both.
:::
:::

::: exercise
Say whether the following is true or false, and justify your answer:

Given some poset $\tuple{S, \leq}$, it holds for every finite subset $\setof{s_1, \ldots, s_n}$ of $S$ that
$$\mathrm{lb}(\setof{s_1, \ldots, s_n}) = \mathrm{lb}(\setof{s_1}) \cup \mathrm{lb}(\setof{s_2} \cup \cdots \cup \mathrm{lb}(\setof{s_n})$$

::: solution
This statement is false, as can be shown with a single counterexample.
Consider the poset **2** of truth values, with carrier $S \is \setof{T, F}$ and $F \leq T$.
Then $\mathrm{lb}(\setof{T}) \cup \mathrm{lb}(\setof{F}) = \setof{T,F} \cup \setof{F} = \setof{T,F} \neq \setof{F} = \mathrm{lb}(\setof{T,F})$.
:::
:::

\includecollection{solutions}
