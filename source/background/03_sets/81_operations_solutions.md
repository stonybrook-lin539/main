---
pagetitle: >-
    Union, intersection, and complement of sets (Solutions)
---

# Union, intersection, and complement of sets (Solutions)

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
:::

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
   In this case, where the first set contains $0$ and $1$, and the second contains $2$ and $3$, the union hence must contain all of the following, and nothing else: $0$, $1$, $2$, and $3$.
1. The same logic still applies.
   The fact that $1$ appears in both sets does not affect how union works.
1. The union of two identical sets always returns the same set.
1. Since the empty set contains no elements at all, it is always the case that $A \cup \emptyset = A$ (and $\emptyset \cup A = A$), no matter what $A$ looks like.
   And yes, this means that $\emptyset = \emptyset \cup \emptyset$.
1. This is exactly the same as the second exercise because union does not care about the order of the sets: $A \cup B$ is always the same as $B \cup A$, just like $m + n$ is always the same as $n + m$ for addition of numbers.
:::

:::

::: exercise
Compute the union of the following:

1. $\setof{0,\setof{1}} \cup \setof{2,3}$
1. $\setof{0,\setof{1}} \cup \setof{1,2,3}$
1. $\setof{0,\setof{1}} \cup \setof{0,1}$
1. $\setof{0,\setof{1}} \cup \emptyset$
1. $\setof{1,2,3} \cup \setof{0,\setof{1}}$

::: solution

1. $\setof{0,\setof{1}} \cup \setof{2,3} = \setof{0, \setof{1}, 2, 3}$
1. $\setof{0,\setof{1}} \cup \setof{1,2,3} = \setof{0, \setof{1}, 1, 2, 3}$
1. $\setof{0,\setof{1}} \cup \setof{0,1} = \setof{0, \setof{1}, 1}$
1. $\setof{0,\setof{1}} \cup \emptyset = \setof{0, \setof{1}}$
1. $\setof{1,2,3} \cup \setof{0,\setof{1}} = \setof{1,2,3,0,\setof{1}}$

:::

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
Either way you are verifying that it does not matter in what order you carry out the union steps as the result will always be the same.
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
   Commit that to memory: $A \cap \emptyset = \emptyset$ for every set $A$.
1. When we contrast that against the second exercise with $\setof{0,1} \cap \setof{1,2,3}$, we see once again that the order of the sets does not matter for intersection: $\setof{0,1} \cap \setof{1,2,3} = \setof{1} = \setof{1,2,3} \cap \setof{0,1}$.
   Just like union, intersection is commutative.
:::

:::

::: exercise
Compute the intersection of the following:

1. $\setof{0,\setof{1}} \cap \setof{2,3}$
1. $\setof{0,\setof{1}} \cap \setof{1,2,3}$
1. $\setof{0,\setof{1}} \cap \setof{0,1}$
1. $\setof{0,\setof{1}} \cap \emptyset$
1. $\setof{1,2,3} \cap \setof{0,\setof{1}}$

::: solution
1. $\setof{0,\setof{1}} \cap \setof{2,3} = \emptyset$
1. $\setof{0,\setof{1}} \cap \setof{1,2,3} = \emptyset$
1. $\setof{0,\setof{1}} \cap \setof{0,1} = \setof{0}$
1. $\setof{0,\setof{1}} \cap \emptyset = \emptyset$
1. $\setof{1,2,3} \cap \setof{0,\setof{1}} = \emptyset$

:::

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

::: exercise
Assume that the context fixes $A \is \setof{0,1,2,3}$.
Compute all of the following:

1. $\overline{\setof{0}}$
1. $\overline{\setof{0,\setof{1}}}$
1. $\overline{\setof{}}$
1. $\overline{\setof{\setof{0}}}$
1. $\setof{\overline{\setof{0}}}$

::: solution
1. $\overline{\setof{0}} = \setof{1,2,3}$
1. $\overline{\setof{0,\setof{1}}} = \setof{1,2,3}$
1. $\overline{\setof{}} = \setof{0,1,2,3}$
1. $\overline{\setof{\setof{0}}} = \setof{0,1,2,3}$
1. $\setof{\overline{\setof{0}}} = \setof{\setof{1,2,3}}$
:::

::: solution_explained
1. Given the context specified at the beginning of the exercise, we may rewrite $\overline{\setof{0}}$ as $\setof{0,1,2,3} - \setof{0}$.
   This is the set of all elements in $\setof{0,1,2,3}$ that are not elements of $\setof{0}$.
   The only such elements are $1$, $2$, and $3$, and thus the set is $\setof{1,2,3}$.
1. Keep in mind that $1 \neq \setof{1}$.
   So the only element of $\setof{0,1,2,3}$ that isn't a member of $\setof{0,\setof{1}}$ is $0$, and we once again get $\setof{1,2,3}$.
1. Since the empty set contains no elements at all, we do not remove any elements at all from $\setof{0,1,2,3}$.
   Remember: $A - \emptyset = A$ for every set $A$.
1. This formula is just a different way of writing $\setof{0,1,2,3} - \setof{\setof{0}}$.
   But no member of $\setof{0,1,2,3}$ is a member of $\setof{\setof{0}}$ (remember that $0 \neq \setof{0}$).
   Hence we get $\setof{0,1,2,3}$.
1. This is a tricky one.
   You have to look very carefully to notice that this isn't $\overline{\setof{\setof{0}}}$ but rather $\setof{\overline{\setof{0}}}$, which is the set that contains $\overline{\setof{0}}$.
   We already know that the latter is $\setof{1,2,3}$, so $\setof{\overline{\setof{0}}}$ must be $\setof{ \setof{1,2,3} }$.
:::

:::

::: exercise
No matter how one chooses $A$ and $B$, it always holds that the complement of the complement of $B$ is identical to $B$ itself.
In symbols: $B = \overline{\overline{B}}$.
Explain why this holds.

*Hint*: By definition, $\overline{\overline{B}} = A - \overline{B} = A - (A - B)$.

::: solution
At first glance, this seems to be wrong.
For example, if $A \is \setof{1}$ and $B \is \setof{2}$, then $\overline{B} = A - B = \setof{1} - \setof{2} = \setof{1}$, whereas $\overline{\overline{B}} = A - (A - B) = \setof{1} - \setof{1} = \emptyset$.
But there is an additional assumption in place when writing $\overline{B}$ instead of $A - B$.
We said that $\overline{B}$ is a shorthand for $A - B$ if $A$ is clear from context.
But in addition, it must also be the case that $B$ can only contain elements that are also elements of $A$.
In a sense, $A$ serves as a fixed universe that specifies all possible elements, and other sets only get to choose from that universe.

With this additional assumption in place, the claim in the exercise is correct.
Let us use $S$ to denote $A - B$.
That is to say, $S$ is the set of all $x$ such that $x \in A$ and $x \notin B$.
Hence $A - S$ must be the set of all $y$ such that $y \in A$ and it is not the case that $y \notin B$.
This is the same thing as saying that $S$ contains all $y$ such that $y \in A$ and $y \in B$.
But since we just said that the notation $\overline{B}$ implies that every member of $B$ is a member of $A$, the $y \in A$ part is redundant and we can shorten the definition of $S$ to "the set of all $y$ such that $y \in B$".
And that is simply $B$.
:::

:::
