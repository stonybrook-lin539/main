# Comparing sets (Solutions)

::: exercise
Complete the table below.

| A             | B                 | $A \subseteq B$? | $A \supseteq B$? | 
| :--           | :--               | :--              | :--              | 
| $\setof{a,b}$ | $\setof{a,a,b,c}$ |                  |                  | 
| $\setof{a}$   | $\setof{b}$       |                  |                  | 
| $\setof{}$    | $\setof{a}$       |                  |                  | 
| $\setof{a,b}$ | $\setof{a,a,b,b}$ |                  |                  | 

::: solution

| A             | B                 | $A \subseteq B$? | $A \supseteq B$? | 
| :--           | :--               | :--              | :--              | 
| $\setof{a,b}$ | $\setof{a,a,b,c}$ |         Y        |         N        | 
| $\setof{a}$   | $\setof{b}$       |         N        |         N        | 
| $\setof{}$    | $\setof{a}$       |         Y        |         N        | 
| $\setof{a,b}$ | $\setof{a,a,b,b}$ |         Y        |         Y        | 
:::

::: solution_explained

For $A \subseteq B$, we have to check that every member of $A$ is a member of $B$.
For $A \supseteq B$, the opposite has to hold: every membeer of $B$ is a member of $A$.
Keep in mind that the empty set $\setof{}$ contains no elements at all, so it is a subset of every set $A$, no matter what $A$ looks like.
Finally, recall that $\setof{a,a,b,b} = \setof{a,b}$, so the last line is asking whether $\setof{a,b}$ is a subset and/or superset of $\setof{a,b}$, to which the answer is yes in both cases.
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
Fill in $=$, $\subsetneq$, or $\supsetneq$ as appropriate.

1. $\setof{a,b} \_ \setof{a}$
1. $\setof{a,a,b,c} \_ \setof{b,b,a,c}$
1. $\setof{1,2,3} \_ \setof{n + 5 \mid n \in \setof{-4, -3}}$
1. $\emptyset \_ \setof{a}$
1. $\emptyset \_ \setof{\emptyset}$

::: solution
1. $\setof{a,b} \supsetneq \setof{a}$
1. $\setof{a,a,b,c} = \setof{b,b,a,c}$
1. $\setof{1,2,3} \supsetneq \setof{n + 5 \mid n \in \setof{-4, -3}}$
1. $\emptyset \subsetneq \setof{a}$
1. $\emptyset \subsetneq \setof{\emptyset}$

:::

::: solution_explained
1. Every member of $\setof{a}$ is a member of $\setof{a,b}$, but $\setof{a,b}$ contains at least one element that is not a member of $\setof{a}$, hence $\setof{a}$ is a proper subset of $\setof{a,b}$.
1. Just remember that sets cannot contain an element more than once, so $\setof{a,a,b,c} = \setof{a,b,c} = \setof{b,b,a,c}$.
1. The set $\setof{n + 5 \mid n \in \setof{-4,-3} }$ is $\setof{1,2}$, which is a proper subset of $\setof{1,2,3}$.
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
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} - \setof{b,d})$    | A is the proper subset of B |
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
