---
pagetitle: >-
    Operations: Union, intersection, and complement of sets
---

# Operations: Union, intersection, and complement of sets

:::prereqs
- sets (basic notation)
:::

Sets can be combined with each other in various ways.
Sometimes this is used as a different way of defining sets, and sometimes it is an actual construction process where multiple sets serve as the input to some mechanism that returns a single set as the output.
You'll see many examples of both usages throughout the course.
Before we discuss these operations, though, we have to introduce one special set that will help us illustrate how these operations work.


## The empty set

As mentioned before, you can think of sets as a kind of strange container without internal order and without duplicates.
Since containers can be empty, it isn't too surprising that there is something called the **empty set**.
The empty set is written $\setof{}$, or more commonly $\emptyset$.

The empty set contains nothing.
There is no $a$ such that $a \in \emptyset$.
At the same time, the empty set is not simply nothing because it is still a set.
A set is not nothing, just like an empty container is not nothing.

The empty set may seem rather useless to you, but it actually has a very important role to play.
Just like the introduction of $0$ was a tremendous breakthrough that made arithmetic a lot more elegant and internally consistent, operations on sets would not be as well-behaved without the empty set.
You will see some examples of that right away.

::: exercise
For each one of the statements below, say whether it is true or false.

- $\emptyset = \setof{}$
- $\emptyset = \setof{\emptyset}$
- $\emptyset \in \setof{a}$
- $\setof{a,b} \neq \emptyset$

::: solution
- True
- False
- False
- True

::: solution_explained
- By definition, $\emptyset$ and $\setof{}$ are just different ways of denoting the empty set.
- The empty set is not the same thing as the set containing the empty set.
  The former has no elements, whereas the latter has exactly one element (which happens to be the empty set, but this is irrelevant).
- The set $\setof{a}$ has exactly one member, which is $a$.
  When using symbols like $a$ or $b$ in exercises, we usually assume that they are distinct from other symbols.
  So we may assume that $a \neq \emptyset$, which means that $\emptyset \notin \setof{a}$.
- The set $\setof{a,b}$ has two members (again we assume that $a \neq b$), whereas the empty set has no members at all.
  Clearly, then, these must be distinct sets.
:::
:::
:::


## Union

Given two sets $A$ and $B$, their **union** $A \cup B$ is the set that contains

- all elements of $A$, and
- all elements of $B$, and
- nothing else.

This means that the union of two sets is the result of taking everything that belongs to at least one set.
Union builds bigger sets from smaller sets.
This makes it something like the set counterpart of addition over numbers.

::: definition
Given two sets $A$ and $B$, $x$ is a member of the **union** $A \cup B$ iff $x$ is a member of at least one of $A$ and $B$.
:::

::: example
The union of $\setof{1}$ and $\setof{2,3,4}$ is $\setof{1,2,3,4}$.
The union of $\setof{1,2}$ and $\setof{3,4}$ is also $\setof{1,2,3,4}$.
And the union of $\setof{1,2}$ and $\setof{1,2,3,4}$ is just $\setof{1,2,3,4}$ itself.
:::

::: exercise
Compute the union of the following:

- $\setof{0,1} \cup \setof{2,3}$
- $\setof{0,1} \cup \setof{1,2,3}$
- $\setof{0,1} \cup \setof{0,1}$
- $\setof{0,1} \cup \emptyset$
- $\setof{1,2,3} \cup \setof{0,1}$

::: solution
1. $\setof{0,1} \cup \setof{2,3} = \setof{0,1,2,3}$
1. $\setof{0,1} \cup \setof{1,2,3} = \setof{0,1,2,3}$
1. $\setof{0,1} \cup \setof{0,1} = \setof{0,1}$
1. $\setof{0,1} \cup \emptyset = \setof{0,1}$
1. $\setof{1,2,3} \cup \setof{0,1} = \setof{0,1,2,3}$

::: solution_explained
1. The union must contain all elements of the first set, all elements of the second set, and nothing else.
   In this case, where the first set contains $0$ and $1$, and the second contains $2$ and $3$, the union hence must contain all of the following, and nothing else: $0$, $1$, $2$, and $3$.
1. The same logic still applies.
   The fact that $1$ appears in both sets does not affect how union works.
1. The union of two identical sets always returns the same set.
1. Since the empty set contains no elements at all, it is always the case that $A \cup \emptyset = A$ (and $\emptyset \cup A = A$), no matter what $A$ looks like.
   And yes, this means that $\emptyset = \emptyset \cup \emptyset$.
1. This is exactly the same as the second exercise because union does not care about the order of the sets: $A \cup B$ is always the same as $B \cup A$, just like $m + n$ is always the same as $n + m$ for addition of numbers.
:::
:::
:::

::: exercise
Compute the union of the following:

- $\setof{0,\setof{1}} \cup \setof{2,3}$
- $\setof{0,\setof{1}} \cup \setof{1,2,3}$
- $\setof{0,\setof{1}} \cup \setof{0,1}$
- $\setof{0,\setof{1}} \cup \emptyset$
- $\setof{1,2,3} \cup \setof{0,\setof{1}}$

::: solution

1. $\setof{0,\setof{1}} \cup \setof{2,3} = \setof{0, \setof{1}, 2, 3}$
1. $\setof{0,\setof{1}} \cup \setof{1,2,3} = \setof{0, \setof{1}, 1, 2, 3}$
1. $\setof{0,\setof{1}} \cup \setof{0,1} = \setof{0, \setof{1}, 1}$
1. $\setof{0,\setof{1}} \cup \emptyset = \setof{0, \setof{1}}$
1. $\setof{1,2,3} \cup \setof{0,\setof{1}} = \setof{1,2,3,0,\setof{1}}$

::: solution_explained

1. Again we keep all elements from both sets.
   The only wrinkle is that one of those elements is itself a set, but that's irrelevant for union.
   We do not care what exactly the elements are, if it is an element of at least one of $A$ and $B$ then it must be in $A \cup B$.
1. The important thing to keep in mind here is that $1 \neq \setof{1}$, so the union must contain both $1$ and $\setof{1}$.
1. For the same reason as above, the union must contain both $1$ and $\setof{1}$.
   If the exercise had asked for the union of $\setof{0, \setof{1}} \cup \setof{0, \setof{1}}$, then the union would have been $\setof{0, \setof{1}}$ because $A \cup A = A$ for every set $A$.
   Note again that it is completely immaterial for all of this that $\setof{1}$ is a set, the only thing that matters is that it is an element of at least one set and is distinct from $0$ and $1$.
1. As always, $A \cup \emptyset = A$ no matter what $A$ looks like.
1. This is again the same $\setof{0,\setof{1}} \cup \setof{1,2,3} = \setof{0, \setof{1}, 1, 2, 3}$.
   Note that the solution given here has a different order from that set, but since sets have no internal order this is just an artefact of our writing system.
:::
:::
:::

Union is **associative**, which means that $(A \cup B) \cup C = A \cup (B \cup C)$.
This is just like $(5 + 4) + 3 = 5 + (4 + 3)$.

::: example
Is is easy to show that
$(\setof{a} \cup \setof{b}) \cup \setof{c} = \setof{a} \cup (\setof{b} \cup \setof{c})$:

$$
(\setof{a} \cup \setof{b}) \cup \setof{c} =
\setof{a,b} \cup \setof{c} =
\setof{a,b,c} =
\setof{a} \cup \setof{b,c} =
\setof{a} \cup (\setof{b} \cup \setof{c})
$$

:::

Union is also **commutative**.
That is to say, the order of arguments does not matter: $A \cup B = B \cup A$.
This again mirrors addition, where $5 + 3 = 3 + 5$.
Also note that $A \cup \emptyset = A$ for any set $A$, just like $n + 0 = n$ for any number $n$.

::: example
It is easy to see that $\setof{a} \cup \setof{b} = \setof{a,b} = \setof{b} \cup \setof{a}$.
And just as obviously $\setof{a,b} \cup \emptyset = \emptyset \cup \setof{a,b} = \setof{a,b}$.
:::

::: exercise
Compute the union of the following in a step-wise fashion:

- $\setof{0,1} \cup \setof{2,3} \cup \emptyset$
- $\setof{0,1} \cup \emptyset \cup \setof{2,3}$

::: solution
1. $\setof{0,1} \cup \setof{2,3} \cup \emptyset = (\setof{0,1} \cup \setof{2,3}) \cup \emptyset = \setof{0,1,2,3} \cup \emptyset = \setof{0,1,2,3}$
1. $\setof{0,1} \cup \emptyset \cup \setof{2,3} = (\setof{0,1} \cup \emptyset) \cup \setof{2,3} = \setof {0,1} \cup \setof{2,3} = \setof{0,1,2,3}$

::: solution_explained
Another way to phrase the exercise would be to ask you to verify that $(\setof{0,1} \cup \setof{2,3}) \cup \emptyset = \setof{0,1} \cup (\setof{2,3} \cup \emptyset)$.
Either way you are verifying that it does not matter in what order you carry out the union steps as the result will always be the same.
:::
:::
:::


## Intersection

Intersection is the opposite of union in that it builds smaller sets rather than bigger ones.

::: definition
Given two sets $A$ and $B$, $x$ is a member of the **intersection** $A \cap B$ iff $x$ is a member of both $A$ and $B$.
:::

::: example
The intersection of $\setof{1}$ and $\setof{2,3,4}$ is $\emptyset$, and so is the intersection of $\setof{1,2}$ and $\setof{3,4}$.
But the intersection of $\setof{1,2,3}$ and $\setof{2,3,4}$ is $\setof{2,3}$.
:::

::: exercise
Compute the intersection of the following:

- $\setof{0,1} \cap \setof{2,3}$
- $\setof{0,1} \cap \setof{1,2,3}$
- $\setof{0,1} \cap \setof{0,1}$
- $\setof{0,1} \cap \emptyset$
- $\setof{1,2,3} \cap \setof{0,1}$

::: solution
1. $\setof{0,1} \cap \setof{2,3} = \emptyset$
1. $\setof{0,1} \cap \setof{1,2,3} = \setof{1}$
1. $\setof{0,1} \cap \setof{0,1} = \setof{0,1}$
1. $\setof{0,1} \cap \emptyset = \emptyset$
1. $\setof{1,2,3} \cap \setof{0,1} = \setof{1}$

::: solution_explained

1. As neither set contains any elements that occur in the other set, their intersection is empty.
1. The only element shared by both sets is $1$, hence the intersection is $\setof{1}$.
   Note that the intersection of two sets is always a set, even if that set has only one member.
   It is incorrect to say that the intersection of $\setof{0,1} \cap \setof{1,2,3}$ is $1$, it is the set $\setof{1}$.
1. Just like $A \cup A = A$ is universally true no matter what this set $A$ looks like, it is always the case that $A \cap A = A$.
1. Since the empty set contains no elements at all, the result of intersecting a set $A$ with the empty set will always be the empty set, no matter what $A$ looks like.
   Commit that to memory: $A \cap \emptyset = \emptyset$ for every set $A$.
1. When we contrast that against the second exercise with $\setof{0,1} \cap \setof{1,2,3}$, we see once again that the order of the sets does not matter for intersection: $\setof{0,1} \cap \setof{1,2,3} = \setof{1} = \setof{1,2,3} \cap \setof{0,1}$.
   Just like union, intersection is commutative.
:::
:::
:::

::: exercise
Compute the intersection of the following:

- $\setof{0,\setof{1}} \cap \setof{2,3}$
- $\setof{0,\setof{1}} \cap \setof{1,2,3}$
- $\setof{0,\setof{1}} \cap \setof{0,1}$
- $\setof{0,\setof{1}} \cap \emptyset$
- $\setof{1,2,3} \cap \setof{0,\setof{1}}$

::: solution
1. $\setof{0,\setof{1}} \cap \setof{2,3} = \emptyset$
1. $\setof{0,\setof{1}} \cap \setof{1,2,3} = \emptyset$
1. $\setof{0,\setof{1}} \cap \setof{0,1} = \setof{0}$
1. $\setof{0,\setof{1}} \cap \emptyset = \emptyset$
1. $\setof{1,2,3} \cap \setof{0,\setof{1}} = \emptyset$

::: solution_explained
1. As the two sets have no elements in common, their intersection is empty.
1. Again it is crucial to keep in mind that $\setof{1} \neq 1$.
   Hence the two sets have no overlap and their intersection is the empty set.
1. Since $\setof{1} \neq 1$, only $0$ is a member of both sets, and the intersection is $\setof{0}$.
   Remember that the intersection is not just $0$, but $\setof{0}$.
   Intersection of two sets always yields a set.
1. This must be the empty set because $A \cap \emptyset = \emptyset$ for every set $A$.
1. Since $A \cap B = B \cap A$, we can just reuse the result from the second line of this exercise.
:::
:::
:::

Note that $A \cap \emptyset = \emptyset$ no matter what the set $A$ looks like.
This is similar to how $n \cdot 0 = 0$ irrespective of the value of $n$.
<!-- fixme: multiplication symbol -->
So intersection is akin to multiplication for sets.
Like multiplication, intersection is **associative**, so that $(A \cap B) \cap C = A \cap (B \cap C)$.
This mirrors the fact that $(5 \cdot 4) \cdot 2 = 5 \cdot (4 \cdot 2)$.

::: example
Is is easy to show that
$(\setof{a,b,c} \cap \setof{b,c,d}) \cap \setof{c,d,e} = \setof{a,b,c} \cap (\setof{b,c,d} \cap \setof{c,d,e})$:

$$
(\setof{a,b,c} \cap \setof{b,c,d}) \cap \setof{c,d,e} =
\setof{b,c} \cap \setof{c,d,e} =
\setof{c} =
\setof{a,b,c} \cap \setof{b,c,d} =
\setof{a,b,c} \cap (\setof{b,c,d} \cap \setof{c,d,e})
$$

:::

Intersection is also **commutative**, again just like multiplication:
$A \cap B = B \cap A$, and $m \cdot n = n \cdot m$.

::: example
It is easy to see that $\setof{a,b} \cap \setof{b,c} = \setof{b} = \setof{b,c} \cap \setof{a,b}$.
And just as obviously $\setof{a,b} \cap \emptyset = \emptyset = \emptyset \cap \setof{a,b}$.
:::

The one difference between intersection and multiplication seems to be that the former produces something smaller and the latter something bigger.
But as we will learn later, this isn't really all that important, and the two operations are indeed very close counterparts in an abstract sense.
<!-- fixme: vague reference to abstract algebra, not in lecture notes yet -->

## (Relative) complement

Given the set-counterparts for $+$ and $\cdot$, you probably expect one for subtraction, too.
It exists, indeed, and is called **relative complement**.

::: definition
Given two sets $A$ and $B$, $x$ is a member of the **complement of $B$ relative to $A$** iff $x$ is a member of $A$ but not $B$.
The set of all such $x$ is denoted $A - B$ (sometimes $A \setminus B$).
:::

Given two sets $A$ and $B$, their relative complement is written $A - B$ (sometimes $A \setminus B$).
The *complement of $B$ relative to $A$* contains all members of $A$ that are not members of $B$.

::: example
The complement of $\setof{2}$ relative to $\setof{1,2,3}$ is $\setof{1,2,3} - \setof{2} = \setof{1,3}$.
The complement of $\setof{3,4,5}$ relative to $\setof{2,3}$ is $\setof{2,3} - \setof{3,4,5} = \setof{2}$.
:::

Relative complement is **not associative** in the general case.

::: example
Consider $(\setof{0,1} - \setof{0}) - \setof{1} = \emptyset$, whereas $\setof{0,1} - (\setof{0} - \setof{1}) = \setof{1}$.
Since associativity requires that the order of evaluation may never matter, this one example where it does matter is sufficient to show that associativity does not hold.
:::

That doesn't mean that there are never cases where one can't change the order of evaluation at all.
For instance, $(\setof{0,1} - \setof{0}) - \setof{2} = \setof{1} = \setof{0,1} - (\setof{0} - \setof{2})$.
But that is merely a coincidence.
That relative complement is not associative mirrors subtraction for numbers, where $(5 - 2) - 3 = 0 \neq 6 = 5 - (2 -3)$.

Commutativity does not hold for relative complement either, as is shown by $\setof{5} - \setof{5,4} = \emptyset \neq \setof{4} = \setof{5,4} - \setof{5}$.

::: exercise
Give a concrete example where $A - B = B - A$.
Then make a single change to $A$ such that $A - B \neq B - A$.

::: solution
Let $A = B = \setof{1}$.
Then $A - B = \setof{1} - \setof{1} = B - A$.
Now remove $1$ from $B$ such that $B = \emptyset$.
Then $A - B = \setof{1} - \emptyset = \setof{1}$, which is distinct from $B - A = \emptyset - \setof{1} = \emptyset$.

::: solution_explained
In general, $A - B \neq B - A$ whenever $A$ and $B$ are distinct sets, but if $A = B$ then $A - B$ is always the same as $B - A$.
Hence we can always pick $A$ and $B$ to be identical sets and then make a single change to render them distinct.
:::
:::
:::

Sometimes we may fix a specific set $U$ such that every set we are interested in can only contain elements of $U$.
In this case, we call $U$ our **universe**.
Given a universe $U$, we just $\overline{B}$ for $A - B$ and call it the **complement of $B$**.

::: example
There are four sets that can be built from the elements of the universe $U \is \setof{0,1}$:

1. $\emptyset$
1. $\setof{0}$
1. $\setof{1}$
1. $\setof{0,1}$

Their complements are shown below.

1. $\overline{\emptyset}   = \setof{0,1} - \emptyset = \setof{0,1}$
1. $\overline{\setof{0}}   = \setof{0,1} - \setof{0} = \setof{1}$
1. $\overline{\setof{1}}   = \setof{0,1} - \setof{1} = \setof{0}$
1. $\overline{\setof{0,1}} = \setof{0,1} - \setof{0,1} = \emptyset$

If we change the universe to $\setof{0,1,2}$, instead, the complements also change.

1. $\overline{\emptyset}   = \setof{0,1,2,3} - \emptyset = \setof{0,1,2}$
1. $\overline{\setof{0}}   = \setof{0,1,2,3} - \setof{0} = \setof{1,2}$
1. $\overline{\setof{1}}   = \setof{0,1,2,3} - \setof{1} = \setof{0,2}$
1. $\overline{\setof{0,1}} = \setof{0,1,2,3} - \setof{0,1} = \setof{2}$
:::

::: exercise
Assume that the context fixes $U \is \setof{0,1,2,3}$.
Compute all of the following:

- $\overline{\setof{0}}$
- $\overline{\setof{0,\setof{1}}}$
- $\overline{\setof{}}$
- $\overline{\setof{\setof{0}}}$
- $\setof{\overline{\setof{0}}}$

::: solution
1. $\overline{\setof{0}} = \setof{1,2,3}$
1. $\overline{\setof{0,\setof{1}}} = \setof{1,2,3}$
1. $\overline{\setof{}} = \setof{0,1,2,3}$
1. $\overline{\setof{\setof{0}}} = \setof{0,1,2,3}$
1. $\setof{\overline{\setof{0}}} = \setof{\setof{1,2,3}}$

::: solution_explained
1. Given the context specified at the beginning of the exercise, we may rewrite $\overline{\setof{0}}$ as $\setof{0,1,2,3} - \setof{0}$.
   This is the set of all elements in $\setof{0,1,2,3}$ that are not elements of $\setof{0}$.
   The only such elements are $1$, $2$, and $3$, and thus the set is $\setof{1,2,3}$.
1. Keep in mind that $1 \neq \setof{1}$.
   So the only element of $\setof{0,1,2,3}$ that isn't a member of $\setof{0,\setof{1}}$ is $0$, and we once again get $\setof{1,2,3}$.
1. Since the empty set contains no elements at all, we do not remove any elements at all from $\setof{0,1,2,3}$.
   Remember: $U - \emptyset = U$ for every set $U$.
1. This formula is just a different way of writing $\setof{0,1,2,3} - \setof{\setof{0}}$.
   But no member of $\setof{0,1,2,3}$ is a member of $\setof{\setof{0}}$ (remember that $0 \neq \setof{0}$).
   Hence we get $\setof{0,1,2,3}$.
1. This is a tricky one.
   You have to look very carefully to notice that this isn't $\overline{\setof{\setof{0}}}$ but rather $\setof{\overline{\setof{0}}}$, which is the set that contains $\overline{\setof{0}}$.
   We already know that the latter is $\setof{1,2,3}$, so $\setof{\overline{\setof{0}}}$ must be $\setof{ \setof{1,2,3} }$.
:::
:::
:::


::: exercise
Explain why the complement of the complement of $A$ is $A$ itself.
In symbols: $A = \overline{\overline{A}}$.

*Hint*: By definition, $\overline{\overline{A}} = U - \overline{A} = U - (U - A)$.

::: solution
Let us use $S$ to denote $U - A$.
That is to say, $S$ is the set of all $x$ such that $x \in U$ and $x \notin A$.
Hence $U - S$ must be the set of all $y$ such that $y \in U$ and it is not the case that $y \notin A$.
This is the same thing as saying that $U - S$ contains all $y$ such that $y \in U$ and $y \in A$.
But since $U$ is our universe, every member of $A$ is necessarily an element of $U$, and thus the set of objects that are in both $U$ and $A$ is the same as the set of objects that are in $A$.
And that set is simply $A$ itself.
:::
:::

## Pictures for set operations

If we represent the sets $A$ and $B$ as overlapping circles, then we can use shading to indicate what parts of $A$ and or $B$ are picked out by the respective operations.

~~~ {.include-tikz size=mid}
set_intersection.tikz
~~~

~~~ {.include-tikz size=mid}
set_union.tikz
~~~

~~~ {.include-tikz size=mid}
set_complement.tikz
~~~

## Mnemonics for notation

Beginners tend to confuse $\cap$ and $\cup$.
Here is a mnemonic:
The term *union* starts with *u*, and $\cup$ looks like a stylized U.
By contrast, $\cap$ looks like a bit like a stylized, minimalist A, and $A \cap B$ contains all $x$ that are members of $A$ **a**nd $B$.

## Recap

- The **union** of $A$ and $B$ is the smallest set that contains every $x$ such that $x \in A$ or $x \in B$ (or both).
- The **intersection** of $A$ and $B$ is the smallest set that contains every $x$ such that $x \in A$ and $x \in B$.
- The **relative complement** of $A$ and $B$ (or equivalently, *the complement of $B$ relative to $A$*) is the smallest set that contains every $x$ such that $x \in A$ and $x \notin B$.
- Union and intersection are associative (order of evaluation doesn't matter) and commutative (order of arguments doesn't matter).
- Relative complement is neither associative nor commutative.
- The complement of $B$, denoted $\overline{B}$, is a shorthand for $A - B$ when $A$ is clear from context.

\includecollection{solutions}
