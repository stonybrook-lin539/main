---
pagetitle: >-
    Partial orders
---

# Partial orders

::: prereqs
- relations (basic notation)
- sets (basic notation)
:::

There are numerous types of order relations, but arguably the most common one is **partial orders**.
Intuitively, a partial order is a linear order (also called total order) where we have removed some orderings between elements.
Formally, though, things are defined exactly the other way round: linear orders are a special case of partial orders.
Hence we will first define partial orders before turning to linear orders in the next unit.

## Definition of partial orders

Partial orders can be defined very succinctly, but doing so requires specialized vocabulary.

::: definition
A **partial order** is a binary relation $R$ that is

- **transitive**: for all $x, y, z$, $x \mathrel{R} y$ and $y \mathrel{R} z$ jointly imply $x \mathrel{R} z$, and
- **antisymmetric**: for all $x$ and $y$, if $x \mathrel{R} y$, and $y \mathrel{R} x$ then $x = y$, and
- either **reflexive** or **irreflexive**:
    - **reflexive**: for all $x$, it holds that $x \mathrel{R} x$,
    - **irreflexive**: there is no $x$ such that $x \mathrel{R} x$.

If the partial order is reflexive, it is a **weak partial order**.
If it is irreflexive, it is a **strict partial order**.

:::

This is a very abstract definition.
In order to truly understand it, you have to develop an intuitive grasp of what each property means.

## Transitivity

In a nutshell, transitivity says "Whatever you can reach in two steps, you can reach in one step".

Suppose you have some set $D$ of objects with a binary relation $R$ defined over them.
For example, we may have the set of natural numbers (0, 1, 2, \ldots) with the *strictly less than* relation $<$, where we have $3 < 5$ and $4 < 5$, but not $5 < 5$ (although $5 \leq 5$).
We can think of these as structures where the set specifies the collection of building blocks and the relation connects these building blocks, putting them into a particular structural configuration.
We can move through $D$ along $R$: if we are at $x \in D$, we can move to any $y$ such that $x \mathrel{R} y$.
And from $y$, we can move on to any $z$ such that $y \mathrel{R} z$, and so on.

::: example
From the natural number $5$, we can move to $17$ via $<$, and from there to $329$.
:::

This movement metaphor is useful for understanding transitivity and other properties of relations.
Some relations are such that whatever can be reached in two steps can also be reached in one step.
So $x \mathrel{R} y$ and $y \mathrel{R} z$ entail that we also have $x \mathrel{R} z$ --- the ability to move from $x$ to $z$ via $y$ implies that we can move directly from $x$ to $z$ without a stop at $y$.
This is what it means for a relation to be **transitive**.

::: definition
A binary relation $R$ over $D$ is **transitive** iff for all $x,y,z \in D$ it holds that $x \mathrel{R} y$ and $y \mathrel{R} z$ jointly imply $x \mathrel{R} z$.
:::

::: example
The human ancestor relation $A$ is transitive.
Your mother is one of your ancestors, and every ancestor of your mother is an ancestor of yourself.
So $x \mathrel{A} y$ and $y \mathrel{A} z$ imply $x \mathrel{A} z$.
:::

::: example
The human parent-of relation is not transitive.
There can be $x$, $y$, and $z$ such that $x$ is the parent of $y$, $y$ is the parent of $z$, but $x$ is not the parent of $z$.
In fact, that is how things are supposed to go in the real world and every deviation from this case is very problematic.
:::

Crucially, for a relation to be transitive it is not enough to have some case where $x \mathrel{R} y$ and $y \mathrel{R} z$ jointly imply $x \mathrel{R} z$.
This has to hold in all cases, including those where $x$, $y$, and $z$ are not necessarily all distinct.

::: example
Consider the sibling relation $S$.
There certainly are instances of transitivity.
If John is a sibling of Mary and Mary is a sibling of Sue, then John is a sibling of Sue.
However, even though John is a sibling of Mary and Mary is a sibling of John, John is not his own sibling.
In formal terms, we have $\text{John} \mathrel{S} \text{Mary}$ and $\text{Mary} \mathrel{S} \text{John}$, yet $\text{John} \not\mathrel{S} \text{John}$.
:::

::: example
Let's consider one more example of a relation that may look transitive but is not.
You may love your parents, your parents love their parents, and you love your grandparents.
So this is a case where we have $x \mathrel{R} y$, $y \mathrel{R} z$, and $x \mathrel{R} z$.
But this does not make love a transitive relation --- it is perfectly possible for a person you love to love somebody that you do not love at all.
:::

The examples above show that a relation is transitive only if there isn't even a single counterexample to transitivity.
If there is even one choice of $x$, $y$, and $z$ such that $x \mathrel{R} y$, $y \mathrel{R} z$, but $x \not\mathrel{R} z$, then $R$ is not transitive.

Intuitively, transitivity tells us that whatever can be reached in two steps can be reached in one step.
But this actually implies that anything that can be reached in a finite number of steps can be reached in one step.
This follows by iterated invocation of transitivity.
Suppose that $a \mathrel{R} b$, $b \mathrel{R} c$, and $c \mathrel{R} d$.
This is shown pictorially below.

~~~ {.include-tikz size=mid}
transitivity1.tikz
~~~

Then by transitivity, we also have $a \mathrel{R} c$.

~~~ {.include-tikz size=mid}
transitivity2.tikz
~~~

But then, again by transitivity, we must also have $a \mathrel{R} d$ because of $a \mathrel{R} c$ and $c \mathrel{R} d$.

~~~ {.include-tikz size=mid}
transitivity3.tikz
~~~

Since we can apply the same argument over and over again, anything that can be reached with a finite number of steps can also be reached in a single step.

It is also important to keep in mind that some relations can be trivially transitive.
Transitivity can be violated only if there are $x$, $y$, and $z$ such that both $x \mathrel{R} y$ and $y \mathrel{R} z$ hold.
If that is not the case, the relation is trivially transitive because there is no configuration where it violates transitivity.

::: example
Consider the relation with
$a_1 \mathrel{R} a_2$,
$b_1 \mathrel{R} b_2$,
$c_1 \mathrel{R} c_2$, and
$d_1 \mathrel{R} d_2$.
It is also depicted below.

~~~ {.include-tikz size=large}
transitivity_trivial.tikz
~~~

Here there is no way of choosing $x$, $y$, and $z$ such that we have both $x \mathrel{R} y$ and $y \mathrel{R} z$.
Consequently, transitivity holds because we cannot produce any counterexample to the claim that the relation is transitive.
:::

Transitivity also does not imply that every element is reachable from any other element in a single step.
Nodes may still be unreachable from certain positions.

::: example
In the example above, there is no way at all to move from $a_2$ to any other element.
:::

::: example
The relation $<$ over natural numbers is transitive.
Yet it does not follow that $5$ can be reached from $8$, only the opposite holds: $8$ can be reached from $5$.
:::

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
Consider the relation $\not\sim$ over natural number such that $x \mathrel{\not\sim} y$ iff one of the following holds: $x$ is odd while $y$ is even, or $x$ is even while $y$ is odd.
In other words, $x \mathrel{\not\sim} y$ iff exactly one of $x$ and $y$ is odd and exactly one of $x$ and $y$ is even.
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


## Antisymmetry

Antisymmetry can be thought of in two different ways that build on the metaphor of relations as adding arrows to the elements of a set:

- "If the order relation has any loops at all, those must be self-loops."
- "If $x$ and $y$ are distinct, then they cannot be mutually related."

Here a loop is a sequence of arrows that leads from an element back to itself.
A self-loop is the special case of a loop where there is a single arrow that directly goes from the element back to itself.
And "mutually related" means that there are arrows from one element to the other and the other way round.

These are intuitive interpretations of two equivalents definition of antisymmetry.

::: definition
A binary relation $R$ over $D$ is **antisymmetric** iff $x \mathrel{R} y$ and $y \mathrel{R} x$ jointly imply $x = y$ for all $x, y \in D$.
:::

::: definition
A binary relation $R$ over $D$ is **antisymmetric** iff it holds for all $x, y \in D$ that $x \neq y$ implies $x \not\mathrel{R} y$ or $y \not\mathrel{R} x$ (or both).
:::

::: example
Consider again the set of natural numbers with the relation $<$, which is antisymmetric.
Let us see how this follows from the first definition.

There are no natural numbers $x$ and $y$ such that $x < y$ and $y < x$ both hold.
But then $<$ is trivially antisymmetric.
This is because the only way a relation $R$ can fail to be antisymmetric is if there is a counterexample to antisymmetry.
A counterexample would require $x$ and $y$ such that

1. $x \mathrel{R} y$, and
1. $y \mathrel{R} x$, and
1. $x \neq y$.

But if we cannot even find any $x$ and $y$ such that $x \mathrel{R} y$ and $y \mathrel{R} x$, then clearly there is no such counterexample.
:::

::: example
Let us look one more time at the natural numbers with $<$, but this time we will use the second definition.
It requires that $x \neq y$ entails $x \not\mathrel{R} y$ or $y \not\mathrel{R} x$ (or both).
But this is obviously the case for $<$.
For instance, $3 \neq 5$ and we have $3 < 5$ but $5 \not< 3$.
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

::: solution_explained
Antisymmetry trivially holds of any relation $R$ for which one cannot find any $x$ and $y$ such that both $x \mathrel{R} y$ and $y \mathrel{R} x$ hold.
This is the case of the human ancestor relation in the real world.
If $x$ is an ancestor of $y$, then $y$ cannot be an ancestor of $x$.
Antisymmetry holds because we cannot even find any scenario where it could be possibly violated.
Or the other way round: if $x$ and $y$ are distinct individuals, then it is impossible for $x$ to be an ancestor of $y$ and for $y$ to be an ancestor of $x$.

But now consider the case of Futurama's Philip J. Fry, who (spoilers!) travels back in time, does the nasties with his grandma, and ends up fathering his own father.
This means that Fry is an ancestor of his father, and of course Fry's father is an ancestor of Fry.
Yet Fry and his father are not the same person.
Antisymmetry is violated.
:::
:::
:::

::: exercise
Given an example to show that the human sibling relation is not antisymmetric.

::: solution
Cersei Lannister is a sibling of Jaime Lannister, and Jaime Lannister is a sibling of Cersei Lannister, yet the two are not the same person.
:::
:::

::: exercise
Recall from a previous exercise that $x \sim y$ iff one of the following holds: $x$ and $y$ are both even, or $x$ and $y$ are both odd.
Give an example to show that $\sim$ is not antisymmetric.
Justify your answer.

::: solution
Let $x \is 1$ and $y \is 3$.
Then $x \sim y$ and $y \sim x$, yet $x \neq y$.
:::
:::

::: exercise
Recall from a previous exercise that $x \not\sim y$ iff one of the following holds: $x$ is odd while $y$ is even, or $x$ is even while $y$ is odd.
Is $\not\sim$ antisymmetric?
Justify your answer.

::: solution
No, it is not antisymmetric.
Suppose $x \is 1$ and $y \is 2$.
Then $x \not\sim y$ and $y \not\sim x$ yet $x \neq y$.
:::
:::


## (Ir)Reflexivity

Reflexivity and irreflexivity are much easier to understand than transitivity and, in particular, antisymmetry.
Intuitively, they are statements about the presence of self-loops.

1. *Reflexivity*: "Every element must have a self-loop."
1. *Irreflexivity*: "No element may have a self-loop."

::: definition
Let $R$ be a binary relation over $D$.
Then $R$ is **reflexive** iff $x \mathrel{R} x$ holds for every $x \in D$.
:::

::: definition
Let $R$ be a binary relation over $D$.
Then $R$ is **irreflexive** iff there is no $x \in D$ such that $x \mathrel{R} x$.
:::

If there is at least one element that is not related to itself, then the relation is not reflexive.
If there is at least one element that is related to itself, then the relation is not irreflexive.
If it is neither reflexive nor irreflexive, it is **non-reflexive**.

::: example
The human parent-of relation is irreflexive because nobody can be their own parent.
:::

::: example
Similarly, $<$ over natural numbers is irreflexive because no number can be strictly less than itself.
However, $\leq$ is reflexive because $x \leq x$ for every number $x$.
:::

::: example
Another reflexive relation is the relation induced by the identity function $\mathrm{id}$, which maps every element to itself.
This is shown below for the set $\setof{1,2,3,4}$ with the identity relation: 

~~~ {.include-tikz size=large}
1234.tikz
~~~

:::

::: example
Suppose that John voted for Mary, and Mary voted for herself.
We can represent this as a relation $V$ such that
$\text{John} \mathrel{V} \text{Mary}$
and
$\text{Mary} \mathrel{V} \text{Mary}$.
This relation is not reflexive because $\text{John} \not\mathrel{V} \text{John}$.
But it isn't irreflexive either because $\text{Mary} \mathrel{V} \text{Mary}$.
Hence it is non-reflexive.
:::

::: example
Here's a surprising one: there is a relation that is both reflexive and irreflexive.
It's the **empty relation** $R$, whose domain is the empty set $\emptyset$.
In this case, there is no $x \in D$ such that $x \mathrel{R} x$, which means that $R$ is irreflexive.
But there's also no $x \in D$ such that $x \not\mathrel{R} x$, which is the same as saying that $x \mathrel{R} x$ holds for every $x \in D$ (there simply happens to be no $x$ at all in $D$).
Consequently, $R$ is also reflexive.
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
Hence $R$ is both reflexive and irreflexive.
Any relation $R$ over a non-empty set, however, cannot be both reflexive and irreflexive.
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
1. the "younger than" relation: irreflexive; no individual or object $x$ is younger than themselves.
1. the "sums to 10" relation ($x \mathrel{R} y$ iff $x + y = 10$): non-reflexive; since $3 + 3 \neq 10$, we do not have $3 \mathrel{R} 3$, but we do have $5 \mathrel{R} 5$ as $5 + 5 = 10$
1. the "at least as rich as" relation: reflexive; every individual is at least as rich as themselves
1. the "voted for the same candidate" relation: reflexive; although it is weird to say that Arnold Schwarzenegger voted for the same candidate as Arnold Schwarzenegger, it is certainly true
1. the "parent-of" relation over humans in a world with time travel: non-reflexive or irreflexive.
   In a normal world this would be irreflexive because no human can be their own parent.
   But in a world with time travel some person $x$ could travel back in time, do the nasties with their parent of the opposite sex, and end up fathering/mothering themselves, which would mean the relation is no longer irreflexive but just non-reflexive.
   Then again, human offspring randomly inherits 50% of each parent's DNA, so the odds of this act resulting in exactly the same human $x$ that traveled back in time are basically null, making the relation irreflexive after all.
   Then again, this could be a predestination paradox, in which case the offspring of $x$ must be $x$ because otherwise there would be no $x$ to go back in time to father $x$.
   In that case the relation would be non-reflexive.
   You know what, forget about it, time travel is weird.
1. the "reverse" relation over words ($x \mathrel{R} y$ iff $x$ is $y$ read backwards; e.g. *deer* and *reed*): non-reflexive;
   we have $x \mathrel{R} x$ if $x$ is a palindrome, e.g. *kayak* and *rotator*, but for most words $x \not\mathrel{R} x$, e.g. *relation* or, ironically, *palindrome*.
:::
:::

:::

Note that pictures can sometimes be misleading when it comes to (ir)reflexivity.
Consider the figure below.

~~~ {.include-tikz size=large}
irreflexivity_violated.tikz
~~~

Here we have two elements $a$ and $b$ with an arrow from $a$ to $b$ and another from $b$ to $a$.
It looks like this relation is irreflexive because no element has a self-loop.
But it is common style for such figures to omit all connections that can be inferred via transitivity.
So if this figure actually depicts a transitivity relation, then $a \mathrel{R} b$ and $b \mathrel{R} a$ implies $a \mathrel{R} a$ because of transitivity.
A clear violation of irreflexivity.
In fact, transitivity would also entail $b \mathrel{R} b$, rendering $R$ reflexive.

## A note on asymmetry and strict partial orders

Sometimes strict partial orders are given a definition that looks different but is actually equivalent to the one we used above.
Instead of antisymmetry, this definition uses **asymmetry**.

::: definition
A **strict partial order** is a binary relation $R$ that is

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



## Recap

- Partial orders allow some elements to be unordered with respect to each other, but it is not a case of anything goes.
  Very specific properties must be met in order for a binary relation to be a partial order.

::: definition
A **partial order** is a binary relation $R$ that is transitive, antisymmetric, and either reflexive or irreflexive.
If the partial order is reflexive, it is a **weak partial order**.
If it is irreflexive, it is a **strict partial order**.
:::

- Strict partial orders are sometimes defined as binary relations that are transitive and asymmetric.
  This definition is equivalent to the one above.

::: definition
A binary relation $R$ over $D$ is

- **transitive** iff for all $x,y,z \in D$ it holds that $x \mathrel{R} y$ and $y \mathrel{R} z$ jointly imply $x \mathrel{R} z$.
- **antisymmetric** iff $x \mathrel{R} y$ and $y \mathrel{R} x$ jointly imply $x = y$ for all $x, y \in D$ (or equivalently, if $x \neq y$ implies $x \not\mathrel{R} y$ or $y \not\mathrel{R} x$ or both).
- **asymmetric** iff $x \mathrel{R} y$ implies $y \not\mathrel{R} x$ for all $x,y \in D$.
- **reflexive** iff $x \mathrel{R} x$ holds for every $x \in D$.
- **irreflexive** iff there is no $x \in D$ such that $x \mathrel{R} x$.
- **non-reflexive** if it is neither reflexive nor irreflexive.
:::

\includecollection{solutions}
