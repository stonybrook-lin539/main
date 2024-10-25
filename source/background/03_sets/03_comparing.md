---
pagetitle: >-
    Comparing sets
---

# Comparing sets

:::prereqs
- sets (basic notation, operations, cardinality)
:::

Two sets can stand in several distinct relations to each other:

1. subset
1. superset
1. identity
1. proper subset
1. proper superset
1. disjoint
1. incomparable


## Subset and superset

Given two sets $A$ and $B$, $A$ is a **subset** of $B$ iff every element of $A$ is also an element of $B$.
In this case, one writes $A \subseteq B$.
For example, $\setof{a,b} \subseteq \setof{a,b,c,d}$.
Alternatively, one also says in this case that $B$ is a **superset** of $A$ (written $B \supseteq A$).

::: example
A transitive verb is a verb that occurs with a subject and one object: *devour*, *contradict*, *wager*, *flummox*, and many more.
Not all verbs are transitive, e.g. *sleep* or *give*. 
Suppose $V_T$ is the set of all English transitive verbs, whereas $V$ is the set of all English verbs.
Since every transitive verb is a verb, but no the other way round, we have $V_T \subseteq V$.
:::

By the definition of subset, every set $S$ is a subset of itself.
The reasoning is simple.
If $S \subseteq S$, then every member of $S$ must be a member of $S$, which is obviously true (how could it be otherwise?).

In addition, the empty set is a subset of every set, including itself.
This is because the empty set contains no elements at all, so it trivially holds that every member of the empty set is a member of every set.

::: exercise
Complete the table below.

| A                      | B                 | $A \subseteq B$? | $A \supseteq B$? | 
| :--                    | :--               | :--              | :--              | 
| $\setof{a,b}$          | $\setof{a,a,b,c}$ |                  |                  | 
| $\setof{a}$            | $\setof{b}$       |                  |                  | 
| $\setof{}$             | $\setof{a}$       |                  |                  | 
| $\setof{a,b}$          | $\setof{a,a,b,b}$ |                  |                  | 
| $\setof{\setof{a}, b}$ | $\setof{a,a,b,b}$ |                  |                  |

::: solution

The table looks as follows:

| A                      | B                 | $A \subseteq B$? | $A \supseteq B$? | 
| :--                    | :--               | :--              | :--              | 
| $\setof{a,b}$          | $\setof{a,a,b,c}$ | Y                | N                | 
| $\setof{a}$            | $\setof{b}$       | N                | N                | 
| $\setof{}$             | $\setof{a}$       | Y                | N                | 
| $\setof{a,b}$          | $\setof{a,a,b,b}$ | Y                | Y                | 
| $\setof{\setof{a}, b}$ | $\setof{a,a,b,b}$ | N                | N                | 

::: solution_explained
1. Every element of $\setof{a,b}$ is an element of $\setof{a,a,b,c} = \setof{a,b,c}$: $a \in \setof{a,b,c}$ and $b in \setof{a,b,c}$.
   But $c \notin \setof{a,b,}$, so $\setof{a,b,c}$ isn't a subset of $\setof{a,b}$.
   (As usual, we assume that distinct symbols refer to distinct elements, e.g. that $a \neq b$.)
1. Under our default assumption that $a \neq b$, these two sets share no elements at all, which entails that neither is a subset of the other.
1. The empty set is a subset of every set, but no non-empty set is a subset of the empty set.
1. Keep in mind that $\setof{a,b} = \setof{a,a,b,b}$.
   This is the same thing as saying that $\setof{a,b} \subseteq \setof{a,a,b,b}$ and $\setof{a,a,b,b} \subseteq \setof{a,b}$.
1. For this one, you have to remember that $\setof{a} \neq a$ (and that $\setof{a,a,b,b} = \setof{a,b}$).
   Hence we have $\setof{a} \in \setof{\setof{a}, b}$ but $\setof{a} \notin \setof{a,b}$, and thus it cannot be the case that $\setof{ a, b } \subseteq \setof{ \setof{a},b }$.
   Similarly, $a \in \setof{a,b}$ but $a \notin \setof{ \setof{a}, b }$ and thus it cannot be the case $\setof{ \setof{a}, b } \subseteq \setof{a,b}$.
:::
:::
:::

``` jupyterpython
def set_print(some_set):
    return '{' + ', '.join(sorted(list(some_set))) + '}'

# adapt the sets as necessary
set1 = set(['a', 'b'])
set2 = set(['a', 'a', 'b', 'c'])

if set1.issubset(set2):
    print(set_print(set1), "is a subset of", set_print(set2))
else:
    print(set_print(set1), "is not a subset of", set_print(set2))
```

::: exercise
Say whether the following statement is true or false and justify your answer:
for any two sets $A$ and $B$, $A \subseteq B$ iff $A \cap B = A$.

::: solution
This statement is correct.
We first show the right-to-left direction, then left-to-right.

If $A \cap B = A$, then every element of $A$ must also be an element of $B$, i.e. $A \subseteq B$.

In the other direction, if $A \subseteq B$, then every element of $A$ is an element of $B$.
Hence $A \cap B$ is a superset of $A$.
But as it is impossible for $A \cap B$ to a proper superset of $A$, it must be the case that $A \cap B = A$.
:::
:::

## Identity

Two sets are *identical* iff each one is a subset of the other.
In formal terms, $A = B$ iff both $A \subseteq B$ and $B \subseteq A$ hold.
The reason for this is again simple:

1.  If two sets $A$ and $B$ are identical, then they must contain exactly the same elements.
    But then every member of $A$ is a member of $B$, which implies $A \subseteq B$.
    And it's also the case that every member of $B$ is a member of $A$, so that we have $B \subseteq A$, too.

1.  In the other direction, if $A \subseteq B$ and $B \subseteq A$, then every member of $A$ is a member of $B$, and every member of $B$ is a member of $A$.
    But that can only happen if the sets are identical.

::: exercise
Consider the set $E$ that contains all even natural numbers that are at least 0 and at most 10.
Show that this is the same as the set that contains all $n$ such that $n = 2m$ for $m \in \setof{0,1,2,3,4,5}$.

::: solution
Let $2$ be the set of all $n$ such that $n = 2m$ for $m \in \setof{0,1,2,3,4,5}$.
That is to say, $2 \is \setof{0, 2, 4, 6, 8, 10}$.
It is easy to see that $2 \subseteq E$, and it also holds that $E \subseteq 2$.
Hence $2 = E$.
:::
:::


## Proper subset and superset

We call $A$ a **proper subset** of $B$ ($A \subsetneq B$) iff $A$ is a subset of $B$ but $A$ and $B$ are not identical.
In other words, every element of $A$ is a member of $B$, but not every element of $B$ is a member of $A$.
We also say that $B$ is a **proper superset** of $A$ ($B \supsetneq A$).

::: example
Given our previous discussion, the set $V_T$ of transitive verbs is proper subset of the set $V$ of verbs because it is a subset but not every verb is a transitive verb.
In other words, $V_T \subseteq V$ yet $V_T \neq V$.
Hence $V_T \subsetneq V$.
:::

Remember that it is possible for both $A \subseteq B$ and $B \subseteq A$ to be true --- in this case, $A = B$.
But there can be no $A$ and $B$ such that $A \subsetneq B$ and $B \subsetneq A$.

::: exercise
Fill in $=$, $\subsetneq$, or $\supsetneq$ as appropriate.
If none of them work, put in $\neq$.

- $\setof{a,b} \_ \setof{a}$
- $\setof{a,b} \_ \setof{\setof{a}}$
- $\setof{a,a,b,c} \_ \setof{b,b,a,c}$
- $\emptyset \_ \setof{a}$
- $\emptyset \_ \setof{\emptyset}$

::: solution
- $\setof{a,b} \supsetneq \setof{a}$
- $\setof{a,b}  \neq \setof{\setof{a}}$
- $\setof{a,a,b,c} = \setof{b,b,a,c}$
- $\emptyset \subsetneq \setof{a}$
- $\emptyset \subsetneq \setof{\emptyset}$

::: solution_explained
- We have $a \in \setof{a}$ and $a \in \setof{a,b}$, so all elements of $\setof{a}$ are elements of $\setof{a,b}$.
  At the very least, then, we have $\setof{a} \subseteq \setof{a,b}$.
  But since we always assume that $a \neq b$ in these exercises, $\setof{a} \neq \setof{a,b}$.
  And thus we have $\setof{a} \subsetneq \setof{a,b}$.
- Remember that $a \neq \setof{a}$.
  Thus $\setof{a,b}$ and $\setof{ \setof{a} }$ do not share any elements.
  That is to say, none of the following is true:
  $\setof{a,b} = \setof{ \setof{a} }$,
  $\setof{a,b} \subsetneq \setof{ \setof{a} }$,
  $\setof{a,b} \supsetneq \setof{ \setof{a} }$.
  But it is true that $\setof{a,b} \neq \setof{ \setof{a} }$.
- Since order and numerosity do not matter for sets, we have $\setof{a,a,b,c} = \setof{a,b,c} = \setof{b,b,a,c}$.
- The empty set is a subset of every set, so at the very least we have $\emptyset \subsetneq \setof{a}$.
  But since $\setof{a}$ contains an element, it is necessarily distinct from the empty set, i.e. $\emptyset \neq \setof{a}$.
  Taken together, this tells us that $\emptyset \subsetneq \setof{a}$.
- The logic is exactly the same as before.
  Simply assume that $a = \emptyset$.
:::
:::
:::

## Disjoint and incomparable sets

If there are two sets $A$ and $B$ such that neither $A \subseteq B$ nor $B \subseteq A$, then there can be only two scenarios.
One option is that $A$ and $B$ are **disjoint**, which means that there is no $x$ such that both $x \in A$ and $x \in B$ --- the two sets have absolutely no overlap.
In mathematical terms, $A \cap B = \emptyset$.
Alternatively, $A$ and $B$ might be **incomparable**.
In this case the two sets have a limited overlap such that there is at least one $x$ with both $x \in A$ and $x \in B$, but there are also $a \in A$ and $b \in B$ such that $a \notin B$ and $b \notin A$.

::: example
The set of English prepositions (*on*, *to*, *at*, ...) and the set of English determiners (*a*, *the*, *this*, ...) have not a single word in common and thus are disjoint.
The set of English verbs and the set of English nouns, on the other hand, are incomparable.
Many words like *water*, *cut*, *fall*, *love*, *try*, *judge*, *beat*, or *cross* can be used as nouns or verbs, but many other words are used only as nouns (*tree*, *waterfall*, *idea*, *Ferrari*) or only as verbs (*write*, *convince*, *admonish*).
:::

While the concept of two disjoint sets is simple enough, it becomes slightly counterintuitive when we consider the empty set.
By definition, the empty set is a subset of every set, including itself.
But by the definition of intersection, it also holds that $A \cap \emptyset = \emptyset$ for any set $A$.
So this means that the empty set is a subset of every set $A$ but also disjoint from it.
In fact, $A$ could even be the empty set itself, and thus the empty set is disjoint from itself!
This is admittedly very unintuitive, and one could amend the definition of disjoint sets above to avoid all of this.
But this edge case is harmless enough that it doesn't really merit moving to a more complicated definition.

::: exercise
For each line in the table, say whether the sets are disjoint, incomparable, identical, or stand in a proper subset/superset relation.

| A               | B                                                 | 
| :--             | :--                                               | 
| $\setof{2,5,8}$ | the set $O$ of all odd numbers                    | 
| $\setof{a,b,c}$ | $\setof{a,b} \cup (\setof{a,c} - \setof{b,d})$    | 
| $\setof{a,b,c}$ | $(\setof{a,b} \cup \setof{a,c}) - \setof{b,d}$    | 
| $\setof{a,b,c}$ | $(\setof{a,b} - \setof{a,c}) \cup \setof{b,d}$    | 
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} - \setof{b,d})$    | 
| $\emptyset$     | $\setof{a,b} \cap (\setof{a,c} \cap \setof{b,d})$ | 
   
::: solution

1. $A$ and $B$ are incomparable
1. $A = B$
1. $A \supsetneq B$
1. $A$ and $B$ are incomparaable
1. $A \subsetneq B$, and $A$ and $B$ are also disjoint
1. $A = B$, and $A$ and $B$ are also disjoint

::: solution_explained
1. As the set $\setof{2,5,8}$ contains some numbers that are odd, it cannot be asubset of $O$.
   Nor does it contain all odd numbers, so it cannot be a superset of $O$ either.
   The question, then, is whether the two sets are disjoint or incomparable.
   But since $\setof{2,5,8} \ni 5 \in O$, it must be the latter.
1. This is easy once you resolve the formula for $B$:
   $\setof{a,b} \cup (\setof{a,c} - \setof{b,d}) = \setof{a,b} \cup \setof{a,c} = \setof{a,b,c}$.
   Obviously $\setof{a,b,c} = \setof{a,b,c}$.
1. Again we have to compute $B$ first:
   $(\setof{a,b} \cup \setof{a,c}) - \setof{b,d} = \setof{a,b,c} - \setof{b,d} = \setof{a,c}$, which is a proper subset of $\setof{a,b,c}$.
1. Here we have
   $(\setof{a,b} - \setof{a,c}) \cup \setof{b,d} = \setof{b} \cup \setof{b,d} = \setof{b,d}$.
   Since $\setof{a,b,c} \ni a \notin \setof{b,d}$ and $\setof{b,d} \ni d \notin \setof{a,b,c}$ and $\setof{a,b,c} \ni b \in \setof{b,d}$, the two are incomparable.
1. The empty set is disjoint from every set, including itself, so we can always say that $A$ and $B$ are disjoint.
   But since the empty set is also a subset of every set, we also have to check whether it is a proper subset of $B$ or identical to $B$.
   Here $B$ is $\setof{a,b} \cap (\setof{a,c} - \setof{b,d}) = \setof{a,b} \cap \setof{a,c} = \setof{a}$, which is distinct from $\emptyset$.
1. Here $B$ is $\setof{a,b} \cap (\setof{a,c} \cap \setof{b,d}) = \setof{a,b} \cap \emptyset = \emptyset$, and thus $A = B$ (but they are also disjoint because the empty set is disjoint from every set, even itself).
:::
:::
:::

## Remarks on notation

### Similarity to $\leq$ and $\geq$

Students sometimes confuse the symbols $\subseteq$ and $\supseteq$.
To avoid that, just keep in mind that these symbols are modeled after $\leq$ and $\geq$ for numbers.
Just like $x \leq y$ means that $x$ is at most as large as $y$, $x \subseteq y$ tells us that $x$ contains at most all the elements of $y$, and nothing else.

### A note on $\subset$

You may occasionally come across the symbol $\subset$ in other math texts.
Some authors use $\subset$ instead of $\subseteq$, while others use it for $\subsetneq$.
As you might imagine, this is a frequent source of confusion.
It is best to avoid $\subset$ and use $\subseteq$ and $\subsetneq$ instead.

### And then there's $\not\subseteq$

Sometimes we might just want to say that $A$ is not a subset of $B$.
We could paraphrase this, as in "it is not the case that $A \subseteq B$".
But mathematicians like to use symbols for common phrases, so there's a dedicated symbol for this: $\not\subseteq$.
Careful, do not confuse $\not\subseteq$ with $\subsetneq$.

Here's an overview of all the relevant notation:

| **Formula**         | **means...**                                                                 |
| :-:                 | :--                                                                          |
| $A \subseteq B$     | $A$ is a subset of $B$ (holds even if $A = B$)                               |
| $A \subsetneq B$    | $A$ is a proper subset of $B$ ($A \subseteq B$ and $A \neq B$)               |
| $A \not\subseteq B$ | $A$ is not a subset of $B$ ($A \ni a \notin B$ for some $a$) |

As you might have expected, there's corresponding counterparts for superset: $\supseteq$, $\supsetneq$, $\not\supseteq$.
There is no standardized symbol for sets being incomparable, although some authors like to use $\sim$ for this purpose.

## Recap

::: definition
Let $A$ and $B$ be arbitrary sets.
Then $A$ is a **subset** of $B$ ($A \subseteq B$) iff every member of $A$ is a member of $B$.
In this case, $B$ is a **superset** of $A$ ($B \supseteq A$).
:::

::: definition
For $A$ and $B$ arbitrary sets, $A$ is a **proper subset** of $B$ ($A \subsetneq B$) iff $A \subseteq B$ and there is a $b \in B$ such that $b \notin A$.
Similarly, $B$ is a **proper superset** of $A$ ($B \supsetneq A$).
:::

::: definition
Let $A$ and $B$ be arbitrary sets.
Then $A$ and $B$ are:

- **identical** iff $A \subseteq B$ and $B \subseteq A$ both hold,
- **disjoint** iff $A \cap B = \emptyset$,
- **incomparable** iff $A \not\subseteq B$ and $B \not\subseteq A$ and $A \cap B \neq \emptyset$.
:::

\includecollection{solutions}
