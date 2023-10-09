---
pagetitle: >-
    Comparing sets (Solutions)
---

# Comparing sets (Solutions)

::: exercise
Complete the table below.

| A                     | B                 | $A \subseteq B$? | $A \supseteq B$? | 
| :--                   | :--               | :--              | :--              | 
| $\setof{a,b}$         | $\setof{a,a,b,c}$ |                  |                  | 
| $\setof{a}$           | $\setof{b}$       |                  |                  | 
| $\setof{}$            | $\setof{a}$       |                  |                  | 
| $\setof{a,b}$         | $\setof{a,a,b,b}$ |                  |                  | 
| $\setof{\setof{a},b}$ | $\setof{a,a,b,b}$ |                  |                  | 

::: solution

| A                     | B                 | $A \subseteq B$? | $A \supseteq B$? | 
| :--                   | :--               | :--              | :--              | 
| $\setof{a,b}$         | $\setof{a,a,b,c}$ |         Y        |         N        | 
| $\setof{a}$           | $\setof{b}$       |         N        |         N        | 
| $\setof{}$            | $\setof{a}$       |         Y        |         N        | 
| $\setof{a,b}$         | $\setof{a,a,b,b}$ |         Y        |         Y        | 
| $\setof{\setof{a},b}$ | $\setof{a,a,b,b}$ |         N        |         N        | 

:::

::: solution_explained

For $A \subseteq B$, we have to check that every member of $A$ is a member of $B$.
For $A \supseteq B$, the opposite has to hold: every member of $B$ is a member of $A$.
Once you are aware of that, you only have to avoid all the ways the exercise is trying to lead you astray:

- The empty set $\setof{}$ contains no elements at all, so it is a subset of every set $A$, no matter what $A$ looks like.
- Recall that $\setof{a,a,b,b} = \setof{a,b}$, so the fourth line is asking whether $\setof{a,b}$ is a subset and/or superset of $\setof{a,b}$, to which the answer is yes in both cases.
- Since $\setof{a} \neq a$, $\setof{\setof{a},b}$ is not a subset of $\setof{a,a,b,b} = \setof{a,b}$, nor is it a superset.
:::

:::

::: exercise
Say whether the following statement is true or false and justify your answer:
for any two sets $A$ and $B$, $A \subseteq B$ iff $A \cap B = A$.

::: solution
This is true.

We have to show that $A \subseteq B$ implies $A \cap B = A$, and that $A \cap B = A$ implies that $A \subseteq B$.
Suppose, then, that $A \subseteq B$.
In this case, every element $A$ is also an element of $B$.
Since $A \cap B$ contains all elements that belong to both $A$ and $B$, and every element of $A$ is also an element of $B$, $A \cap B$ contains at least all elements of $A$.
But by definition, $A \cap B$ cannot contain any elements that do not belong to $A$ itself.
Hence $A \cap B$ contains all elements of $A$, and nothing else, which means that $A \cap B = A$.

Now suppose that $A \cap B = A$.
Since $A \cap B$ contains all elements that are members of $A$ and members of $B$, $A \cap B = A$ entails that every member of $A$ is a member of $B$.
In other words, $A \subseteq B$.
:::

:::

::: exercise
Consider the set $E$ that contains all even natural numbers that are at least 0 and at most 10.
Show that this is the same as the set that contains all $n$ such that $n = 2m$ for $m \in \setof{0,1,2,3,4,5}$.

::: solution
The set of even numbers that are at least 0 and at most 10 is $A \is \setof{0,2,4,6,8,10}$.
Now consider the set that contains all $n$ such that $n = 2m$ for $m \in \setof{0,1,2,3,4,5}$.
This is $\setof{2 \times 0, 2 \times 1, 2 \times 2, 2 \times 3, 2 \times 4, 2 \times 5}$, which is the same as $B \is \setof{0, 2, 4, 6, 8, 10}$.
Clearly $A \subseteq B$ and $B \subseteq A$, so that $A = B$.
:::

:::

::: exercise
Fill in $=$, $\subsetneq$, or $\supsetneq$ as appropriate.

1. $\setof{a,b} \_ \setof{a}$
1. $\setof{a,a,b,c} \_ \setof{b,b,a,c}$
1. $\emptyset \_ \setof{a}$
1. $\emptyset \_ \setof{\emptyset}$

::: solution
1. $\setof{a,b} \supsetneq \setof{a}$
1. $\setof{a,a,b,c} = \setof{b,b,a,c}$
1. $\emptyset \subsetneq \setof{a}$
1. $\emptyset \subsetneq \setof{\emptyset}$

:::

::: solution_explained
1. Every member of $\setof{a}$ is a member of $\setof{a,b}$, but $\setof{a,b}$ contains at least one element that is not a member of $\setof{a}$, hence $\setof{a}$ is a proper subset of $\setof{a,b}$.
1. Just remember that sets cannot contain an element more than once, so $\setof{a,a,b,c} = \setof{a,b,c} = \setof{b,b,a,c}$.
1. Remember that the empty set is a subset of every set, which means that it is a proper subset of every set that is distinct from the empty set.
1. The same reasoning applies here, it is just a bit more confusing because we are comparing the empty set to the set containing the empty set.
   Still, the empty set has to be a subset of $\setof{\emptyset}$, and $\setof{\emptyset}$ contains an element that is not contained in the empty set, namely the empty set itself.
:::

:::

::: exercise
For each line in the table, say whether the sets are disjoint, incomparable, identical, or stand in a proper subset/superset relation.

| A               | B                                                 | 
| :--             | :--                                               | 
| $\setof{2,5,8}$ | the set of all odd numbers                        | 
| $\setof{a,b,c}$ | $\setof{a,b} \cup (\setof{a,c} - \setof{b,d})$    | 
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} - \setof{b,d})$    | 
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} \cap \setof{b,d})$ | 
 
::: solution
| A               | B                                                 |  relation                   |   
| :--             | :--                                               | :--                         |  
| $\setof{2,5,8}$ | the set of all odd numbers                        | incomparable                |
| $\setof{a,b,c}$ | $\setof{a,b} \cup (\setof{a,c} - \setof{b,d})$    | identical                   |
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} - \setof{b,d})$    | A is a proper subset of B   |
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} \cap \setof{b,d})$ | identical                   |
:::

::: solution_explained

1. The set of all odd numbers contains some numbers that occur in $\setof{2,5,8}$, and many that do not.
   In the other direction, $\setof{2,5,8}$ contains $8$, which is not an element of the set of all numbers.
   Overall, the two sets have some overlap, but neither subsumes the other.
   Hence they are incomparable.
1. We have $\setof{a,c} - \setof{b,d} = \setof{a,c}$, and $\setof{a,b} \cup \setof{a,c} = \setof{a,b,c}$.
   That's clearly the same set as $\setof{a,b,c}$.
1. We first have to compute $\setof{a,b} \cap \setof{a,c}$, which is $\setof{a}$.
   Clearly that is distinct from the $\emptyset$, but the $\emptyset$ is a subste of every set, including $\setof{a}$.
   Hence the empty set is a proper subset of $\setof{a}$.
1. Again we perform some computations first: $\setof{a,c} \cap \setof{b,d} = \emptyset$, and $\setof{a,b} \cap \emptyset = \emptyset$.
   Needless to say, $\emptyset = \emptyset$.
:::

:::
