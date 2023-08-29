# Union, intersection, and complement of sets (Solutions)

::: exercise
Compute the union of the following:

1. $\setof{0,1} \cup \setof{2,3}$
1. $\setof{0,1} \cup \setof{1,2,3}$
1. $\setof{0,1} \cup \setof{0,1}$
1. $\setof{0,1} \cup \emptyset$
1. $\setof{1,2,3} \cup \setof{0,1}$

::: solution
1. $\setof{0,1} \cup \setof{2,3} = \setof{0,1,2,3}$
1. $\setof{0,1} \cup \setof{1,2,3} = \setof{0,1,2,3}$
1. $\setof{0,1} \cup \setof{0,1} = \setof{0,1}$
1. $\setof{0,1} \cup \emptyset = \setof{0,1}$
1. $\setof{1,2,3} \cup \setof{0,1} = \setof{0,1,2,3}$
:::

::: solution_explained
1. The union must contain all elements of the first set, all elements of the second set, and nothing else.
   In this case, where the first set contains $0$ and $1$, and the second contains $2$ and $3$, the union hence must contain all of the following, and nothing else:$0$, $1$, $2$, and $3$.
1. The same logic still applies.
   The fact that $1$ appears in both sets does not affect how union works.
1. The union of two identical sets always returns the same set.
1. Since the empty set contains no elements at all, it is always the case $A \cup \emptyset = A$ (and $\emptyset \cup A = A$), no matter what $A$ looks like.
   And yes, this means that $\emptyset = \emptyset \cup \emptyset$.
1. This is exactly the same as the second exercise because union does not care about the order of the sets: $A \cup B$ is always the same as $B \cup A$, just like $m + n$ is always the same as $n + m$ for addition of numbers.
:::

:::

::: exercise
Compute the union of the following in a step-wise fashion:

1. $\setof{0,1} \cup \setof{2,3} \cup \emptyset$
1. $\setof{0,1} \cup \emptyset \cup \setof{2,3}$

::: solution
1. $\setof{0,1} \cup \setof{2,3} \cup \emptyset = (\setof{0,1} \cup \setof{2,3}) \cup \emptyset = \setof{0,1,2,3} \cup \emptyset = \setof{0,1,2,3}$
1. $\setof{0,1} \cup \emptyset \cup \setof{2,3} = (\setof{0,1} \cup \emptyset) \cup \setof{2,3} = \setof {0,1} \cup \setof{2,3} = \setof{0,1,2,3}$
:::

::: solution_explained
Another way to phrase the exercise would be to ask you to verify that $(\setof{0,1} \cup \setof{2,3}) \cup \emptyset = \setof{0,1} \cup (\setof{2,3} \cup \emptyset)$.
Either way you are verifying that it does not matter in what order you carry out the union steps, the result will always be the same.
:::

:::

::: exercise
Compute the intersection of the following:

1. $\setof{0,1} \cap \setof{2,3}$
1. $\setof{0,1} \cap \setof{1,2,3}$
1. $\setof{0,1} \cap \setof{0,1}$
1. $\setof{0,1} \cap \emptyset$
1. $\setof{1,2,3} \cap \setof{0,1}$

::: solution
1. $\setof{0,1} \cap \setof{2,3} = \emptyset$
1. $\setof{0,1} \cap \setof{1,2,3} = \setof{1}$
1. $\setof{0,1} \cap \setof{0,1} = \setof{0,1}$
1. $\setof{0,1} \cap \emptyset = \emptyset$
1. $\setof{1,2,3} \cap \setof{0,1} = \setof{1}$
:::

::: solution_explained

1. As neither set contains any elements that occur in the other set, their intersection is empty.
1. The only element shared by both sets is $1$, hence the intersection is $\setof{1}$.
   Note that the intersection of two sets is always a set, even if that set has only one member.
   It is incorrect to say that the intersection of $\setof{0,1} \cap \setof{1,2,3}$ is $1$, it is the set $\setof{1}$.
1. Just like $A \cup A = A$ is universally true no matter what this set $A$ looks like, it is always the case that $A \cap A = A$.
1. Since the empty set contains no elements at all, the result of intersecting a set $A$ with the empty set will always be the empty set, no matter what $A$ looks like.
1. When we contrast that against the second exercise with $\setof{0,1} \cap \setof{1,2,3}$, we see once again that the order of the sets does not matter for intersection: $\setof{0,1} \cap \setof{1,2,3} = \setof{1} = \setof{1,2,3} \cap \setof{0,1}$.
   Just like union, intersection is commutative.
:::

:::

::: exercise
Give a concrete example where $A - B = B - A$.
Then make a single change to $A$ such that $A - B \neq B - A$.

::: solution
Let $A = B = \setof{1}$.
Then $A - B = \setof{1} - \setof{1} = B - A$.
Now remove $1$ from $B$ such that $B = \emptyset$.
Then $A - B = \setof{1} - \emptyset = \setof{1}$, which is distinct from $B - A = \emptyset - \setof{1} = \emptyset$.
:::

::: solution_explained
In general, $A - B \neq B - A$ whenever $A$ and $B$ are distinct sets, but if $A = B$ then $A - B$ is always the same as $B - A$.
Hence we can always pick $A$ and $B$ to be identical sets and then make a single change to render them distinct.
:::

:::
