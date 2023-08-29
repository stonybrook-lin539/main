# Weak order relations (Solutions)

::: exercise
There is no relation that is reflexive, and irreflexive, and non-reflexive.
Explain why!

::: solution
A relation $R$ is non-reflexive iff there is some $x$ such that $x \mathrel{R} x$ and some $y$ such that $y \not\mathrel{R} y$.
But $x \mathrel{R} x$ rules out that $R$ is irreflexive, and $y \not\mathrel{R} y$ rules out that $R$ is reflexive.
So non-reflexivity is incompatible with reflexivity, and it is also incompatible with irreflexivity.

Note, however, that reflexivity and irreflexivity are not incompatible.
Any relation $R$ over the empty set is both reflexive and irreflexive: since there is no $x \in \emptyset$ such that $x \not\mathrel{R} x$, we have no counterexample to $R$ being reflexive, and since there is no $x \in \emptyset$ such that $x \mathrel{R} x$, we have no counterexample to $R$ being irreflexive.
:::

:::

::: exercise
For each one of the following relations, say whether it is reflexive, irreflexive, or non-reflexive.
Justify your answers!
If you have to make additional assumptions, explain what they are. 

1. the "younger than" relation
1. the "sums to 10" relation ($x \mathrel{R} y$ iff $x + y = 10$)
1. the "at least as rich as" relation
1. the "voted for the same candidate" relation
1. the "parent-of" relation over humans in a world with time travelling
1. the "reverse" relation over words ($x \mathrel{R} y$ iff $x$ is $y$ read backwards; e.g. *deer* and *reed*)

::: solution
1. the "younger than" relation: irreflexive because no individual or object $x$ is younger than themselves.
1. the "sums to 10" relation ($x \mathrel{R} y$ iff $x + y = 10$): non-reflexive; since $3 + 3 \neq 10$, we do not have $3 \mathrel{R} 3$, but we do have $5 \mathrel{R} 5$ as $5 + 5 = 10$
1. the "at least as rich as" relation: reflexive because every individual is at least as rich as themselves
1. the "voted for the same candidate" relation: reflexive; although it is weird to say that Arnold Schwarzenegger voted for the same candidate as Arnold Schwarzenegger, it is certainly true
1. the "parent-of" relation over humans in a world with time travel: non-reflexive or irreflexive.
   In a normal world this would be irreflexive because no human can be their own parent.
   But in a world with time travel some person $x$ could travel back in time, do the nasties with their parent of the opposite sex, and end up fathering/mothering themselves, which would mean the relation is no longer irreflexive but just non-reflexive.
   Then again, human offspring randomly inherits 50% of each parent's DNA, so the odds of this act resulting in exactly the same human $x$ that traveled back in time are basically null, making the relation irreflexive after all.
   Then again, this could be a predestination paradox, in which case the offspring of $x$ must be $x$ because otherwise there would be no $x$ to go back in time to father $x$.
   In that case the relation would be non-reflexive.
   You know what, forget about it, time travel is weird.
1. the "reverse" relation over words ($x \mathrel{R} y$ iff $x$ is $y$ read backwards; e.g. *deer* and *reed*): non-reflexive.
   We have $x \mathrel{R} x$ if $x$ is a palindrome, e.g. *kayak* and *rotator*, but for most words $x \not\mathrel{R} x$, e.g. *relation* or, ironically, *palindrome*.
:::

:::

::: exercise
Say whether the following claim is true or false, and justify your answer: If there are $x$ and $y$ in the domain $D$ of $R$ such that $x \mathrel{R} y$, then it is impossible for $R$ to be reflexive and asymmetric.

::: solution
This statement is true.
Asymmetry states $x \not\mathrel{R} y$ for all $x$ and $y$, which includes the case where $x$ and $y$ are the same element of $D$.
Hence asymmetry entails $x \not\mathrel{R} x$, which implies irreflexivity and hence rules out reflexivity.
:::

:::

::: exercise
Show that every relation that is both irreflexive and antisymmetric is asymmetric.

::: solution
Suppose that our relation $R$ is both antisymmetric and irreflexive.
As $R$ is antisymmetric, $x \mathrel{R} y$ and $y \mathrel{R} x$ jointly entail $x = y$, i.e. $x \mathrel{R} x$.
But since $R$ is irreflexive, there is no $x$ such that $x \mathrel{R} x$ holds.
Hence there can be no $x$ and $y$ such that both $x \mathrel{R} y$ and $y \mathrel{R} x$ are true.
But that is exactly the definition of asymmetry.
:::

:::

::: exercise
Say whether the following claim is true or false, and justify your answer: If there are $x$ and $y$ in the domain $D$ of $R$ such that $x \mathrel{R} y$, then it is impossible for $R$ to be transitive, symmetric, and irreflexive.

::: solution
This statement is true.
By assumption, $x \mathrel{R} y$ holds.
But since $R$ is symmetric, $x \mathrel{R} y$ entails $y \mathrel{R} x$, and by transitivity this entails $x \mathrel{R} x$.
But then $R$ cannot be irreflexive.
:::

:::

::: exercise
For each one of the following relations, say whether it is symmetric, asymmetric, antisymmetric, or non-symmetric.
Be as specific as possible: don't just say "antisymmetric" if the relation is also asymmetric, in that case you should answer "asymmetric".
Take care to justify your answers, and if you have to make additional assumptions, explain what they are. 

1. the "younger than" relation
1. the "sums to 10" relation ($x \mathrel{R} y$ iff $x + y = 10$)
1. the "at least as rich as" relation
1. the "voted for the same candidate" relation
1. the "parent-of" relation over humans in a world with time travelling
1. the "reverse" relation over words ($x \mathrel{R} y$ iff $x$ is $y$ read backwards; e.g. *deer* and *reed*)
1. the lexicographic order of words in a dictionary

::: solution

1. the "younger than" relation: asymmetric.
   If $x$ and $y$ are distinct, it cannot be true that $x$ is younger than $y$ and $y$ is younger than $x$.
   Hence the relation is at least antisymmetric.
   But the relation is also irreflexive, and every antisymmetric, irreflexive relation is asymmetric.
1. the "sums to 10" relation ($x \mathrel{R} y$ iff $x + y = 10$): symmetric.
   Since addition is commutative, $x + y = 10$ iff $y + x = 10$, and hence we have $x \mathrel{R} y$ iff $y \mathrel{R} x$.
1. the "at least as rich as" relation: non-symmetric.
   If $x$ is richer than $y$, then $x$ is at least as rich as $y$ but $y$ is not at least as rich as $x$, which shows that symmetry does not hold.
   If $x$ and $y$ are distinct individuals of equal wealth, then $x$ is at least as rich as $y$, and $y$ is at least as rich as $x$, yet $x$ and $y$ are not the same person.
   This precludes antisymmetry and thus asymmetry.
   Hence this only leaves non-symmetry.
1. the "voted for the same candidate" relation: symmetric.
   If $x$ voted for the same candidate as $y$, then $y$ necessarily voted for the same candidate as $x$.
1. the "parent-of" relation over humans in a world with time travelling: asymmetric or non-symmetric.
   This mirrors our earlier discussion.
   Usually the relation is asymmetric because $x$ being the parent of $y$ precludes $y$ from being the parent of $x$.
   But with time travel we could get such cases.
1. the "reverse" relation over words ($x \mathrel{R} y$ iff $x$ is $y$ read backwards; e.g. *deer* and *reed*): symmetric.
   If $x$ is $y$ read backwards, then $y$ is $x$ read backwards.
1. the lexicographic order of words in a dictionary: asymmetric.
   We cannot order $x$ before $y$ and $y$ before $x$, including cases where $x = y$.
:::

:::

::: exercise
Indicate in the table below which properties hold of the relations.

| **Relation**                  | **transitive** | **reflexive** | **anti-symmetric** | **connex**  |
| :--                           | :--            | :--           | :--                | :--         |
| substring                     |                |               |                    |             |
| $\subsetneq$                  |                |               |                    |             |
| $\subseteq$                   |                |               |                    |             |
| alphabetical order            |                |               |                    |             |
| taller than                   |                |               |                    |             |

::: solution

| **Relation**                  | **transitive** | **reflexive** | **anti-symmetric** | **connex**  |
| :--                           | :--            | :--           | :--                | :--         |
| substring                     | Yes            | Yes           | Yes                | No          |
| proper substring              | Yes            | No            | Yes                | No          |
| $\subsetneq$                  | Yes            | No            | Yes                | No          |
| $\subseteq$                   | Yes            | Yes           | Yes                | No          |
| alphabetical order            | Yes            | No            | Yes                | Yes         |
| taller than                   | Yes            | No            | Yes                | No          |

:::

::: solution_explained

A few remarks should suffice here:

1. The solution gives answers for *substring* as well as *proper substring* because the exercise deliberately leaves open what the intended relation is.
1. All relations are antisymmetric.
   Keep in mind that there are two ways to satisfy antisymmetry.
   Either we have $x \mathrel{R} y$ and $y \mathrel{R} x$ only in those cases where $x = y$, or it simply never happens that we have both $x \mathrel{R} y$ and $y \mathrel{R} x$ (that is to say, the relation is asymmetric).
   The former scenario occurs with the relations above that are reflexive, the latter with the relations that are irreflexive.
1. The *taller than* relation is not connex because we can have distinct $x$ and $y$ of the same height, in which case neither $x \mathrel{R} y$ nor $y \mathrel{R} x$ hold.
:::

:::

::: exercise
Indicate for each relation in the table below what kind of order it represents.
Some relations fit multiple types, and some none.

| **Relation**                  |  **weak partial** | **strict partial** | **weak total** | **strict total** |
| :--                           |  :--              | :--                | :--            | :--              |
| substring                     |                   |                    |                |                  |
| $\subsetneq$                  |                   |                    |                |                  |
| alphabetical order            |                   |                    |                |                  |
| ordering all humans by height |                   |                    |                |                  |
| "sums to 10" relation         |                   |                    |                |                  |
| parent-of relation            |                   |                    |                |                  |
| "voted for same candidate"    |                   |                    |                |                  |

::: solution

| **Relation**                  |  **weak partial** | **strict partial** | **weak total** | **strict total** |
| :--                           |  :--              | :--                | :--            | :--              |
| substring                     |  Yes              | No                 | No             | No               |
| proper substring              |  No               | Yes                | No             | No               |
| $\subsetneq$                  |  No               | Yes                | No             | No               |
| alphabetical order            |  No               | Yes                | No             | Yes              |
| ordering all humans by height |  Yes/No           | Yes/No             | No             | No               |
| "sums to 10" relation         |  No               | No                 | No             | No               |
| parent-of relation            |  No               | No                 | No             | No               |
| "voted for same candidate"    |  No               | No                 | No             | No               |

:::

::: solution_explained

A few clarifying remarks:

1. Keep in mind that every total order is also a partial order.
   If a relation is not a partial order, it cannot be a total order.
1. Whether we take "ordering all humans by height" to be antisymmetric is subject to interpretation.
   If two individuals $x$ and $y$ are exactly the same height, then we could order them as $x \leq y$ and $y \leq x$.
   In that case we don't have antisymmetry and hence no partial order.
   But alternatively, we may say that humans of the same height are unordered with respect to each other, and then antisymmetry holds.
   There's also some leeway whether the relation should be reflexive.
1. The "sums to 10" relation and the parent-of relation are not transitive, so they cannot be partial orders.
1. The "voted for same candidate" relation is not antisymmetric, so it cannot be a partial order.
:::

:::

::: exercise
Give a real-world example of a weak partial order that is not a total order.
:::
