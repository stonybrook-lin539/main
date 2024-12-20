---
pagetitle: >-
    Linear orders (aka total orders)
---

# Linear orders (aka total orders)

::: prereqs
- relations (basic notation, partial orders)
:::
A **linear order** (also called a **total order**) is the special case of a partial order where all elements are ordered with respect to each other.
The formal definition only requires us to add one simple property to the definition of partial orders.
But which property that is depends on whether the order is a weak partial order or a strict partial order.

## Strict linear orders

A strict linear order is the special case of a relation that is both a strict partial order and trichotomous.

::: definition
A binary relation $R$ over set $D$ is **trichotomous** (or **semi-connex**) iff for all $x$ and $y$ in $D$ at least one of the following holds:

1. $x \mathrel{R} y$,
1. $y \mathrel{R} x$,
1. $x = y$.

:::

::: definition
A **strict linear order** (or **strict total order**) is a strict partial order that is trichotomous.
:::

::: example
The relation $<$ over the set of natural numbers is trichotomous because no matter what numbers $x$ and $y$ we pick, it must be the case $x < y$, $y < x$, or $x = y$.
:::

::: example
The human ancestor relation is not trichotomous.
For instance, if John and Mary have the same parents, then John is not an ancestor of Mary, Mary is not an ancestor of John, and Mary and John are not the same individual.
:::

::: exercise
For each one of the following relations, say whether it is trichotomous.

- the "strictly taller than" relation over humans
- the "exactly as tall" relation over humans
- the "strictly taller than and at least as heavy" relation over humans

::: solution
- The "strictly taller than" relation over humans is not trichotomous. 
  We say that $x$ is strictly taller than $y$ if the height of $x$ exceeds the height of $y$.
  But there are distinct humans that have exactly the same height.
  In this case, we have $x \neq y$, $x \not\mathrel{R} y$, and $y \not\mathrel{R} x$.
- The "exactly as tall" relation is not trichotomous either.
  This time, there are distinct humans $x$ and $y$ that differ in their height and hence are not related.
  Again we have $x \neq y$, $x \not\mathrel{R} y$, and $y \not\mathrel{R} x$.
- The "strictly taller than and at least as heavy" relation over humans is not trichotomous.
  The "strictly taller than and at least as heavy" relation is necessarily a subset of the "strictly taller than" relation, which we already saw is not trichotomous.

::: solution_explained
You might be wondering why none of the relations in the exercise are strict linear orders.
It's actually fairly difficult to think of a strict linear order over humans.
If the world still had phone books, and if somebody compiled a universal phone book of all humans, then we could define a relation "follows in the universal phone book".
Like the order of words in a dictionary, this would be a strict total order.
Similarly, sorting all US citizens by their social security number would yield a strict linear order (assuming that SSNs are never reused).
:::
:::
:::

::: exercise
Give another real-world example of a strict partial order that is not trichotomous and hence not a strict linear order.

::: solution
There are many options, for example:

- "is (strictly) heavier than"
- "contains (strictly) more atoms than"
- "has (strictly) bluer eyes than"
- "has a (strictly) more sausage-like nose than"
- "has published (strictly) more papers than"
- "has watched (strictly) more episodes of *Garth Marengi's Darkplace*"

All of those give you some ordering statements of the form $x \mathrel{R} y$, don't allow $x \mathrel{R} x$, but also have many $x$ and $y$ that are unordered with respect to each other. 
:::
:::

::: remark
Some mathematicians use **trichotomous** only for the special case where exactly one of $x = y$, $x \mathrel{R} y$, and $y \mathrel{R} x$ holds.
If there is an $x$ and a $y$ such that at least two of those cases are met, these mathematicians would consider the relation semi-connex but not trichotomous.
In this usage, trichotomy is a special case of semi-connexity.

I like to use *trichotomous* as a synonym for *semi-connex* rather than a special case.
There are three reasons for this.
First, I have never come across a relation in linguistics where it would have been crucial to make a distinction between semi-connex and trichotomous.
Second, the term *semi-connex* could mean just about anything when you first encounter it, whereas *trichotomous* already tells you that this is going to be about satisfaction of three different scenarios.
Third, I always confuse the terms *semi-connex* and *connex* --- which is a nice segue to the next section.
:::


## Weak linear orders

Trichotomy is not a meaningful restriction on weak partial orders because every weak partial order is already trichotomous by virtue of being reflexive.

::: exercise
Explain in intuitive terms why reflexivity implies trichotomy/semiconnexity.

::: solution
Now that I think about it, this doesn't hold and I'll have to rewrite this unit quite a bit.
Trichotomy works just fine with weak and strict orders.
:::
:::

Instead, the step from a weak partial order to a weak linear order requires the stronger property of **connexity**.
This is simply trichotomy without the case of $x = y$.

::: definition
A binary relation $R$ over set $D$ is **connex** iff for all $x$ and $y$ in $D$ at least one of the following holds:

1. $x \mathrel{R} y$,
1. $y \mathrel{R} x$.

:::

::: definition
A **weak linear order** (or **weak total order**) is a weak partial order that is connex.
:::

::: example
The relation $\leq$ over the set of natural numbers is connex.
Either $x = y$, in which case we trivially have $x \leq y$ because that is the same as $x \leq x$ and $\leq$ is reflexive.
Or, if $x \neq y$, then it must be the case that $x < y$, which implies $x \leq y$, or $y < x$, which implies $y \leq x$.
:::

::: example
The "at least as tall" relation over humans is connex.
If $x$ and $y$ are the same human being, then trivially $x$ is at least as tall as $y$ because everybody is at least as tall as themselves.
If $x$ and $y$ are distinct, then $x$ may be shorter than $y$, taller than $y$, or exactly as tall as $y$.
But this means that either $x$ is at least as tall as $y$, or $y$ is at least as tall as $x$.
:::

::: exercise
Indicate in the table below which properties hold of the respective relations.

*Remarks*:

- Assume suitable sets that the relations are defined over. For instance, the substring relation is defined over the set of all possible strings, and the subset relation should be defined over all possible sets.
- The substring relation $\sqsubseteq$ is defined as follows: $x \sqsubseteq y$ iff there are strings $u$ and $v$ in $\Sigma^*$ such that $y = u \stringcat x \stringcat v$.
- The lexicographic order $\prec_l$ refers to how words would be ordered in a dictionary, e.g. $\text{aardvark} \prec_l \text{apple} \prec_l \text{be} \prec_l \text{bet} \prec_l \text{zoom}$.
  You should assume that no word can be ordered before itself.
- For some relations, you might want to justify why you think they (do not) satisfy a certain property.

| **Properties**       | $\sqsubseteq$ | $\subsetneq$ | $\subseteq$ | $\prec_l$           | at least as tall as |
| :--                  | :-:           | :-:          | :-:         | :-:                 | :-:                 |
| transitive           |               |              |             |                     |                     |
| reflexive            |               |              |             |                     |                     |
| irreflexive          |               |              |             |                     |                     |
| antisymmetric        |               |              |             |                     |                     |
| trichotomous         |               |              |             |                     |                     |
| connex               |               |              |             |                     |                     |

::: solution
The completed table is shown below.

| **Properties**       | $\sqsubseteq$ | $\subsetneq$ | $\subseteq$ | $\prec_l$           | at least as tall as |
| :--                  | :-:           | :-:          | :-:         | :-:                 | :-:                 |
| transitive           | Y             | Y            | Y           | Y                   | Y                   |
| reflexive            | Y             | N            | Y           | N                   | Y                   |
| irreflexive          | N             | Y            | N           | Y                   | N                   |
| antisymmetric        | Y             | Y            | Y           | Y                   | N                   |
| trichotomous         | N             | N            | N           | Y                   | Y                   |
| connex               | N             | N            | N           | Y                   | Y                   |

:::

:::

::: exercise
Continuing the previous exercise, say for each relation whether it is a weak partial order, a weak linear order, a strict partial order, or a strict linear order.

::: solution
1. $\sqsubseteq$ is a weak partial order
1. $\subsetneq$ is a strict partial order
1. $\subseteq$ is a weak partial order
1. $\prec_l$ is a strict total order
1. "at least as tall as" is not an order at all because it isn't antisymmetric
:::
:::

## Recap

::: definition
A **strict linear order** (or **strict total order**) is a strict partial order that is trichotomous.
A **weak linear order** (or **weak total order**) is a weak partial order that is connex.
:::

::: definition
A binary relation $R$ over set $D$ is

- **connex** iff for all $x$ and $y$ in $D$ at least one of the following holds: $x \mathrel{R} y$ or $y \mathrel{R} x$.
- **trichotomous** iff for all $x$ and $y$ in $D$ at least one of the following holds: $x \mathrel{R} y$ or $y \mathrel{R} x$ or $x = y$.
:::

\includecollection{solutions}
