---
pagetitle: >-
    Partial orders (Solutions)
---

# Partial orders (Solutions)

::: exercise
Consider the relation $\sim$ over natural numbers such that $x \mathrel{\sim} y$ iff $x$ and $y$ are both odd or $x$ and $y$ are both even.
Is this relation transitive?
Justify your answer.

::: solution
Yes, this relation is transitive.
Suppose $x \mathrel{\sim} y$ and $y \mathrel{\sim} z$ are both true.
Then either $x$ and $y$ are both odd, or they are both even.
We assume w.l.o.g. that $x$ and $y$ are both odd.
If $y$ is odd, then $y \mathrel{\sim} z$ implies that $z$ is odd.
But then it follows from the definition of $\mathrel{\sim}$ that $x \mathrel{\sim} z$ holds because $x$ and $z$ are both odd.
:::

:::

::: exercise
Consider the relation $\not\sim$ over natural number such that $x \mathrel{\not\sim} y$ iff either $x$ is odd and $y$ is even or $x$ is even and $y$ is odd.
Is this relation transitive?
Justify your answer.

::: solution
No, this relation is not transitive.
Suppose that $x \mathrel{\not\sim} y$ and $y \mathrel{\not\sim} z$ are both true.
Then either $x$ is odd and $y$ is even, or $x$ is even and $y$ is odd.
We assume w.l.o.g. that $x$ is odd and $y$ is even.
If $y$ is even, then $y \mathrel{\not\sim} z$ implies that $z$ is odd.
But then it follows from the definition of $\mathrel{\not\sim}$ that $x \mathrel{\not\sim} z$ does not hold because $x$ and $z$ are both odd.
:::

:::

::: exercise
Give two arguments modeled after the ones above to show that $\leq$ over the set of natural numbers is antisymmetric.

::: solution
1. Let $x$ and $y$ be natural numbers such that $x \leq y$ and $y \leq x$.
   This can only be the case if $x = y$.
   Since this holds for every possible choice of $x$ and $y$, we see that $\leq$ obeys antisymmetry.
1. Let $x$ and $y$ be natural numbers such that $x \neq y$.
   Then at least one of the following must not hold: $x \leq y$ or $y \leq x$.
   But this is of course true.
   For example, if $x = 7$ and $y = 5$, then it does not hold that $x \leq y$.
:::
:::

::: exercise
Earlier on we encountered the human ancestor relation.
Is this relation antisymmetric?

::: solution
In a world without time travel, it is antisymmetric.
In a world with time travel, it might not be antisymmetric.
:::

::: solution_explained
Antisymmetry trivially holds of any relation $R$ for which one cannot find any $x$ and $y$ such that both $x \mathrel{R} y$ and $y \mathrel{R} x$ hold.
This is the case of the human ancestor relation in the real world.
If $x$ is an ancestor of $y$, then $y$ cannot be an ancestor of $x$.
Antisymmetry holds because we cannot even find any scenario where it could be possibly violated.

But now consider the case of Futurama's Philip J. Fry, who (spoilers!) travels back in time, does the nasties with his grandma, and ends up fathering his own father.
This means that Fry is an ancestor of his father, and of course Fry's father is an ancestor of Fry.
Yet Fry and his father are not the same person.
Antisymmetry is violated.
:::
:::

::: exercise
Given an example to show that the human sibling relation is not antisymmetric.

::: solution
Cersei Lannister is a sibling of Jaime Lannister, and Jaime Lannister is a sibling of Cersei Lannister, yet the two are not the same person.
:::
:::

::: exercise
Give an example to show that $\sim$ as defined in a previous example is not antisymmetric.

::: solution
Let $x \is 1$ and $y \is 3$.
Then $x \sim y$ and $y \sim x$, yet $x \neq y$.
:::
:::

::: exercise
Is $\not\sim$ as defined in a previous example antisymmetric?
Justify your answer.

::: solution
No, it is not antisymmetric, for the very same reason as in the previous exercise.
Suppose $x \is 1$ and $y \is 2$.
Then $x \not\sim y$ and $y \not\sim x$ yet $x \neq y$.
:::

:::


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
1. the "sums to 10" relation over natural numbers ($x \mathrel{R} y$ iff $x + y = 10$)
1. the "at least as rich as" relation
1. the "voted for the same candidate" relation
1. the "parent-of" relation over humans in a world with time travel
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

- **transitive**: for all $x, y, z$, $x \mathrel{R} y$ and $y \mathrel{R} z$ jointly imply $x \mathrel{R} z$, and
- **asymmetric**: for all $x$ and $y$, if $x \mathrel{R} y$ then $y \not\mathrel{R} x$.
:::

::: exercise
Explain in intuitive terms why the two definitions of strict partial orders are equivalent.

*Hint:* You have to explain why asymmetry is essentially the combination of antisymmetry and irreflexivity.

::: solution
We have to show that a relation is asymmetric iff it is both antisymmetric and irreflexive.
Intuitively, this clearly holds.
The definition of asymmetry says that the relation must not contain any loops, whereas antisymmetry says that the only permitted loops are self-loops, which in turn are ruled out by irreflexivity.

More formally, suppose that $R$ is asymmetric.
Then for all $x$ and $y$, $x \mathrel{R} y$ entails $y \not\mathrel{R} x$.
But then antisymmetry trivially holds because there are no $x$ and $y$ such that both $x \mathrel{R} y$ and $y \mathrel{R} x$.
In addition, asymmetry enforces that $x \mathrel{R} x$ entails $x \not\mathrel{R} x$.
Since this is a contradiction, the only way asymmetry can hold is if there is no $x$ such that $x \mathrel{R} x$.
In other words, $R$ is irreflexive.

In the other direction, suppose that $R$ is antisymmetric and irreflexive.
Then $x \mathrel{R} y$ and $y \mathrel{R} x$ imply $x = y$.
But if $x = y$, then $x \mathrel{R} y$ is actually $x \mathrel{R} x$, which violates irreflexivity.
Hence there must not be any $x$ and $y$ such that $x \mathrel{R} y$ and $y \mathrel{R} x$ are both true.
In other words, $x \mathrel{R} y$ implies $y \not\mathrel{R} x$, which is exactly the definition of asymmetry.
:::
:::
