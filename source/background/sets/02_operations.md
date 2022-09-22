**Prerequisites**

- sets (notation)

# Union, intersection, and complement of sets

Sets can be combined with each other in various ways.
Sometimes this is used as yet another way to define sets, and sometimes it is an actual construction process where multiple sets serve as the input to some mechanism that returns a single set as the output.
You'll see many examples of both usages throughout the course.

## Union

Given two sets $A$ and $B$, their **union** $A \cup B$ is the set that contains

- all elements of $A$, and
- all elements of $B$, and
- nothing else.

This means that the union of two sets is the result of taking everything that belongs to at least one set.
So union builds bigger sets from smaller sets.
This makes it something like the set counterpart of addition over numbers.

::: example
The union of $\setof{1}$ and $\setof{2,3,4}$ is $\setof{1,2,3,4}$.
The union of $\setof{1,2}$ and $\setof{3,4}$ is also $\setof{1,2,3,4}$.
:::

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

Union is **associative**, which means that $(A \cup B) \cup C = A \cup (B \cup C)$.
This is just like $(5 + 4) + 3 = 5 + (4 + 3)$.
It is also **commutative**.
That is to say, the order of arguments does not matter: $A \cup B = B \cup A$.
This again mirrors addition, where $5 + 3 = 3 + 5$.
Also note that $A \cup \emptyset = \emptyset$ for any set $A$, just like $n + 0 = n$ for any number $n$.

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

## Intersection

Intersection is the opposite of union in that it builds smaller sets rather than bigger ones.
Given two sets $A$ and $B$, their **intersection** $A \cap B$ is the set that contains only those elements that belong to $A$ as well as $B$.

::: example
The intersection of $\setof{1}$ and $\setof{2,3,4}$ is $\emptyset$, and so is the intersection of $\setof{1,2}$ and $\setof{3,4}$.
But the intersection of $\setof{1,2}$ and $\setof{2,3,4}$ is $\setof{2}$.
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

Note that $A \cap \emptyset = \emptyset$ no matter what the set $A$ looks like.
This is similar to how $n \cdot 0 = 0$ irrespective of the value of $n$.
So intersection is akin to multiplication for sets.
Like multiplication, intersection is associative, so that $(A \cap B) \cap C = A \cap (B \cap C)$.
This mirrors the fact that $(5 \cdot 4) \cdot 2 = 5 \cdot (4 \cdot 2)$.
Intersection is also commutative, again just like multiplication:
$A \cap B = B \cap A$, and $m \cdot n = n \cdot m$.

The one difference between intersection and multiplication seems to be that the former produces something smaller and the latter something bigger.
But as we will learn much later in the semester, this isn't really all that important, and the two operations are indeed very close counterparts in an abstract sense.

## Relative complement

Given the set-counterparts for $+$ and $\cdot$, you probably expect one for subtraction, too.
It exists, indeed, and is called **relative complement**.
Given two sets $A$ and $B$, their relative complement is written $A - B$ (sometimes $A \setminus B$).
It contains all members of $A$ that are not members of $B$.

::: example
The complement of $\setof{2}$ relative to $\setof{1,2,3}$ is $\setof{1,2,3} - \setof{2} = \setof{1,3}$.
The complement of $\setof{3,4,5}$ relative to $\setof{2,3}$ is $\setof{2,3} - \setof{3,4,5} = \setof{2}$.
:::

Relative complement is **not** associative in the general case.
For example, $(\setof{0,1} - \setof{0}) - \setof{1} = \emptyset$, whereas $\setof{0,1} - (\setof{0} - \setof{1}) = \setof{1}$.
Since associativity requires that the order of evaluation may never matter, this one example where it does matter is sufficient to show that associativity does not hold.
That doesn't mean that there are never cases where one can't change the order of evaluation at all.
For instance, $(\setof{0,1} - \setof{0}) - \setof{2} = \setof{1} = \setof{0,1} - (\setof{0} - \setof{2})$ --- but that is merely a coincidence.
That relative complement is not associative mirrors subtraction for numbers, where $(5 - 2) - 3 = 0 \neq 6 = 5 - (2 -3)$.
Commutativity does not hold for relative complement either, as is shown by $\setof{5} - \setof{5,4} = \emptyset \neq \setof{4} = \setof{5,4} - \setof{4}$.

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

## Summary

::: definition
Let $A$ and $B$ be arbitrary sets.

- The **union** of $A$ and $B$ is $A \cup B \is \setof{ x \mid x \in A \text{ or } x \in B}$.
- The **intersection** of $A$ and $B$ is $A \cap B \is \setof{ x \mid x \in A \text{ and } x \in B}$.
- The **relative complement** of $A$ and $B$ is $A - B \is \setof{ x \mid x \in A \text{ and } x \notin B}$.
- If $A$ is clear from context, we just write $\overline{B}$ for $A - B$ and call it the **complement** of $B$.

:::

- Union and intersection are associative (order of evaluation doesn't matter) and commutative (order of arguments doesn't matter).
- Relative complement is neither associative nor commutative.
