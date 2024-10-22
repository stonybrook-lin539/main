---
pagetitle: >-
    Monotonicity in case syncretism
---

# Monotonicity in case syncretism

:::prereqs
- relations (basic notation, intuition behind order relations)
:::

Monotonicity also seems to play a role in a phenomenon called **case syncretism**.
As you probably know, some languages have specific endings that go on nouns to indicate their case.
A subject might usually be nominative case, whereas an object could be accusative or dative, and a possessor might have genitive case.
Case syncretism refers to the phenomenon that a word ends up using identical forms for distinct cases.
Once again not every logically conceivable system is actually attested.
Languages seem to be very finicky in what kinds of case syncretism they allow, and we would like to know why that is so.


## A primer on case syncretism

We still see small reflexes of case syncretism in English, where the personal pronouns have different forms:

| **Word**                      | **Subject** | **Object** | **Possessor** |
| :--                           | :-:         | :-:        | :-:           |
| 3rd person singular masculine | he          | him        | his           |
| 3rd person singular feminine  | she         | her        | her           |
| 3rd person singular neuter    | it          | it         | its           |

The table above is called a **morphological paradigm**, where **morphology** means that we are talking about the form of words, and a **paradigm** is a collection of cells that specify the relation between the forms of a word and their function.
In the case at hand, those functions are subject, object, and possessor.
As you can see, *her* is the form for both the object and the possessor, and *it* is the form for both the subject and the object.
Such cases where multiple cells of a paradigm look the same are called **syncretism**.

The case system of English is so impoverished by now that it isn't very interesting to look at.
But many languages have a much richer case morphology, and case syncretism is a common occurrence in those languages.
This is shown below for Latin *rex* 'king', where nominative and accusative are syncretic in the plural, as are dative and ablative.

| **Case** | **Singular** | **Plural** |
| --:      | :--          | :--        |
| Nom      | rex          | reg-es     |
| Gen      | reg-is       | reg-um     |
| Dat      | reg-i        | reg-ibus   |
| Acc      | reg-em       | reg-es     |
| Abl      | reg-e        | reg-ibus   |

And Icelandic has paradigms like the one for *mamma* 'mum' below, where almost every form is syncretic with some other form.

| **Case** | **Singular** | **Plural** |
| --:      | :--          | :--        |
| Nom      | mamma        | mömm-ur    |
| Gen      | mömm-u       | mamm-a     |
| Dat      | mömm-u       | mömm-um    |
| Acc      | mömm-u       | mömm-ur    |

As with person pronoun paradigms and adjectival gradation, some conceivable case syncretisms never show up in any language. 
For instance, there is no language with the following variant of the plural case paradigm for 'rex':

| **Case** | **Plural** |
| --:      | :--        |
| Nom      | reg-ibus   |
| Gen      | reg-um     |
| Dat      | reg-ibus   |
| Acc      | reg-es     |
| Abl      | reg-ibus   |

Why is this impossible?
It can't be just because three cases are syncretic, because we've seen that this is fine in Icelandic.
So why does no language like to have a case paradigm of this form?
Again we are forced to explain some typological gaps, and again monotonicity provides an answer.

::: exercise
Pick one of the languages below and write down a case paradigm for a specific word of that language.
Highlight the cells that are syncretic (if any).

- Ancient Greek
- Basque
- Finnish
- German
- Hungarian
- Icelandic
- Japanese
- Korean
- Old English
- Old Norse
- Russian
- Sanskrit
- Tamil

Unless you're a native speaker of one of those languages, you will have to do some research to find out how their case system works.
Try your local library, or an online resource like Wikipedia.

::: solution
I will give a boring example from German.
German *Haus* 'house' inflects as follows:

1. Nominative: *Haus*
1. Accusative: *Haus*
1. Genitive: *Hauses*
1. Dative: *Haus*

Nominative, accusative, and dative are syncretic to the exclusion of genitive.
Note that the dative can also take the form *Hause*, but this is very archaic.
:::
:::


## Genitive, dative and accusative

Case systems can be very complex and convoluted, so we will only focus on a few simple problems here.
First of all, we will only consider syncretism within a single column of the case paradigm.
That is to say, we do not worry how singular forms can be syncretic with plural forms, we're only interested in syncretism among case forms in the singular and syncretism among case forms in the plural.
Second, we won't consider each individual case that has been proposed for some language, because there's tons of them: ablative, locative, elative, instrumental, benefactive, and much more.
Instead, we will subsume them all under *other* and use **Blake's case hierarchy** (named after Australian linguist Barry Blake) as our starting point.

Slightly truncated, Blake's case hierarchy postulates that
$$\mathrm{Nom} <
\mathrm{Acc} <
\mathrm{Gen} <
\mathrm{Dat} <
\mathrm{others}$$
The \*ABA generalization, which we encountered with adjectival gradation and person pronoun paradigms, can be extended to this hierarchy, and linguists have indeed done so.
But now that the generalization applies to paradigms with more than three cells, it receives a slightly more general interpretation: two cases $x$ and $z$ cannot have the same form in a paradigm unless every case $y$ that occurs between them in the hierarchy also has this form in the paradigm.

::: example
The paradigm for Latin *rex* displays syncretism of nominative and accusative to the exclusion of genitive, dative, and ablative.
But since these cases do not occur between nominative and accusative in Blake's case hierarchy, this obeys the \*ABA generalization.
:::

::: exercise
The paradigm for *rex* also has syncretism of dative and ablative in the plural.
Can a monotonic function produce this pattern from Blake's case hierarchy?
Justify your answer.

::: solution
Ablative falls under the *others* category.
There is no other case between *Dat* and *others*.
A monotonic function may always map two cases to the same form as long as there is no other case between the two that gets mapped to a different form.
Hence syncretism of dative and ablative is not problematic.
:::
:::

::: exercise
Barry Blake did not actually intend his case hierarchy to be used in this manner.
Instead, it was supposed to capture a particular typological generalization: if a language has some case $y$, then it also has every case such that $x < y$ in Blake's hierarchy.
Show that this, too, can be understood as an instance of monotonicity.

::: solution
We can conceptualize every language as a function $f$ from Blake's hierarchy to the values $0$ and $1$, where $f(x) = 1$ means that the language has case $x$ and $f(x) = 0$ means that it does not.
Let us assume $0 < 1$ as usual.
Then Blake's generalization can be restated as follows: if $x < y$ and $f(y) = 1$, then it must also hold that $f(x) = 1$.
Let us generalize this statement even more.
Since the only two possible values are $0$ and $1$, $f(x) = 1$ is equivalent to $f(x) \geq 1 = f(y)$, i.e. $f(x) \geq f(y)$.
And if we do not explicitly assume that $x \neq y$, then $x < y$ should be rewritten as $x \leq y$.
This leaves us with the following claim: if $x \leq y$, then $f(x) \geq f(y)$.
But that's exactly the definition of a monotonic decreasing function.
:::
:::

There is a problem with the \*ABA generalization, though.
In many Germanic languages, dative and accusative are syncretic to the exclusion of genitive.
But given Blake's case hierarchy, that would be an instance of an ABA pattern.

::: example
In German, it is very common for nominative, dative and accusative to take the base form, whereas genitive receives a special affix.
So *Papa* 'dad' could be nominative, dative, or accusative, whereas the genitive must be *Papas*.
:::

German is not an ideal example because the genitive is becoming increasingly unproductive.
Moreover, the dative allows for a special suffix *-e* for nouns that end in a consonant, so that *Mann* can be either *Mann* or *Manne* (although the latter sounds very archaic).
it is conceivable, then, that the dative of *Papa* is underlyingly *Papae*, with the final vowel subsequently deleted by some phonological process.

::: exercise
Show that the German case pattern for *Papa* obeys the \*ABA generalization if one makes at least one of the following assumptions:

1. German has no genitive case and uses a truncated version of Blake's case hierarchy without genitive.
1. German has a genitive form *Papas*, but the dative is underlyingly *Papae* rather than *Papa*.

::: solution
Consider the first option, without genitive.
Then Blake's case hierarchy for German reduces to
$$\mathrm{Nom} <
\mathrm{Acc} <
\mathrm{Dat}$$,
and we have the forms *Papa - Papa - Papa*.
That is an A-A-A pattern, which does not violate the \*ABA generalization.

Alternative, suppose that the dative is underlyingly *Papae*, mirroring the archaic dative *Hause* 'house' we encountered earlier on.
Then the four forms for *Papa* (in the order nominative - accusative - genitive - dative) are *Papa - Papa - Papas - Papae*.
This pattern corresponds to AABC, which does not violate the \*ABA generalization either.
:::
:::

::: example
A better example comes from the Icelandic word for *father*.
The nominative is *faðir*, its dative and accusative are *föður*, yet the genitive is *föðurs*.
And in contrast to German, there's no wiggle room here: these are the endings, and there aren't any colloquial variations.
So accusative and dative are indeed the only syncretic cases, and crucially the genitive case does not participate in this syncretism.
:::

If we combine the \*ABA generalization with Blake's hierarchy in its current form, then we cannot produce these attested syncretism patterns.
Since genitive occurs between accusative and dative, syncretism of the latter two the exclusion of the former necessarily generates an ABA pattern.
Either the \*ABA generalization is too restrictive, or Blake's hierarchy is wrong.
We could of course try to change the hierarchy, but the easy options do not work.

::: exercise
Explain why the following hierarchy is empirically inadequate:
$\mathrm{Nom} <
\mathrm{Gen} <
\mathrm{Acc} <
\mathrm{Dat} <
\mathrm{others}$.

::: solution
We can conceptualize every language as a function $f$ from Blake's hierarchy to the values $0$ and $1$, where $f(x) = 1$ means that the language has case $x$ and $f(x) = 0$ means that it does not.
Let us assume $0 < 1$ as usual.
Then Blake's generalization can be restated as follows: if $x < y$ and $f(y) = 1$, then it must also hold that $f(x) = 1$.
Let us generalize this statement even more.
Since the only two possible values are $0$ and $1$, $f(x) = 1$ is equivalent to $f(x) \geq 1 = f(y)$, i.e. $f(x) \geq f(y)$.
And if we do not explicitly assume that $x \neq y$, then $x < y$ should be rewritten as $x \leq y$.
This leaves us with the following claim: if $x \leq y$, then $f(x) \geq f(y)$.
But that's exactly the definition of a monotonic decreasing function.
:::
:::

::: exercise
Icelandic also has some nouns where nominative and genitive are syncretic to the exclusion of dative and accusative.
Which variants of Blake's hierarchy does this rule out?

::: solution
This argues against any variant of the hierarchy where accusative or dative occur between nominative and genitive.
:::
:::


## Partial orders to the rescue

It seems that no matter how we order the cases, at least one attested syncretism will violate the \*ABA generalization.
But perhaps we are accidentally limiting ourselves.
First of all, remember that the \*ABA generalization is just a linguistic counterpart to the mathematical notion of monotonicity.
Perhaps monotonicity provides a way out?

::: exercise
Pick one of the problematic syncretisms pointed out above and explain why it is also problematic if we replace the \*ABA generalization with the requirement that the mapping from the Blake hierarchy to surface forms must be a monotonic function.

::: solution
Consider the Icelandic case of syncretism of accusative and dative.
We have $f(\mathrm{Acc}) = f(\mathrm{Dat}) = A \neq B = f(\mathrm{Gen})$.
Suppose w.l.o.g. that $A < B$.
Then $f$ is not monotonically increasing because $\mathrm{Gen} \leq \text{Dat}$ yet $f(\text{Gen}) > f(\text{Dat})$.
But $f$ is not monotonically decreasing either because $\mathrm{Acc} \leq \text{Gen}$ yet $f(\text{Acc}) < f(\text{Gen})$.
:::
:::

Well, monotonicity by itself doesn't really help.
But it opens up a path toward a new solution.
So far, we have implicitly assumed that linguistic hierarchies must be **trichotomous**: for any given $x$ and $y$, it holds that $x < y$, or $y < x$, or $x = y$.

::: example
If we order the natural numbers by $<$, the result is a trichotomous order.
No matter which two numbers $m$ and $n$ we pick, we either have $m < n$, $n < m$, or $m = n$.

Now suppose that we take the set of all humans that have ever lived and order them by the ancestor relation $A$ such that $x \mathrel{A} y$ iff $x$ is an ancestor of $y$.
The resulting order is not trichotomous because there are at least two distinct human beings such that neither one is the other's ancestor.
:::

Trichotomy is a natural starting point for linguistic hierarchies, but it isn't a necessary one.
In contrast to the \*ABA generalization, monotonicity is also a meaningful concept if we consider **partial orders**.
In a partial order, some elements may be unordered with respect to some other elements.
This allows us to make a small but important modification to Blake's hierarchy: allow accusative and genitive to be unordered with respect to each other.
We can depict this new hierarchy in the form of a graph

~~~ {.include-tikz size=mid}
blake_partialorder.tikz
~~~

In this graph, the vertical axis corresponds to the order induced by $<$.
The graph is, essentially, the result of rotating Blake' case hierarchy 90 degrees clockwise and then rearranging accusative and genitive so that they are still between nominative and dative but unordered with respect to each other.
More precisely, the graph encodes the following orderings of cases:

1. $\mathrm{Nom} < \mathrm{Acc}$,
1. $\mathrm{Nom} < \mathrm{Gen}$,
1. $\mathrm{Acc} < \mathrm{Dat}$,
1. $\mathrm{Gen} < \mathrm{Dat}$,
1. $\mathrm{Dat} < \mathrm{others}$,
1. all the orders that follow from the orders above:
    - $\mathrm{Nom} < \mathrm{Dat}$,
    - $\mathrm{Nom} < \mathrm{others}$,
    - $\mathrm{Acc} < \mathrm{others}$,
    - $\mathrm{Gen} < \mathrm{others}$.

Crucially, since genitive and accusative are now unordered with respect to each other, monotonicity no longer applies to them.
Monotonicity is a restriction on what a function may map $x$ and $y$ to if $x$ and $y$ are ordered with respect to each other.
Monotonicity has nothing to say for cases where no such ordering holds.
If there is no order between $x$ and $y$, then it does not matter whether $f(x) \leq f(y)$ or the other way round.
Without an ordering between accusative and genitive, it becomes possible for accusative and dative to be syncretic to the exclusion of genitive.

::: example
Suppose that accusative and dative are both mapped to the same exponent, which is different from the realization of genitive: $f(\mathrm{Acc}) = f(\mathrm{Dat}) \neq f(\mathrm{Gen})$.
We will show that this is compatible with the assumption of a monotonically increasing (or decreasing) function.

First, the revised case hierarchy above establishes that $\mathrm{Acc} < \mathrm{Dat}$.
If $f$ is monotonically increasing, then $\mathrm{Acc} < \mathrm{Dat}$ entails $f(\mathrm{Acc}) \leq f(\mathrm{Dat})$.
By our initial assumption, $f(\mathrm{Acc}) = f(\mathrm{Dat})$, which confirms $f(\mathrm{Acc}) \leq f(\mathrm{Dat})$.
Our revised case hierarchy also postulates that $\mathrm{Gen} < \mathrm{Dat}$, so it must be the case that $f(\mathrm{Gen}) \leq f(\mathrm{Dat})$.
Whether this holds depends on how one orders the surface forms, but it is always possible to pick an ordering that satisfies $f(\mathrm{Gen}) \leq f(\mathrm{Dat})$.
Finally, $\mathrm{Acc}$ and $\mathrm{Gen}$ are unordered with respect to each other, and consequently the relative order of $f(\mathrm{Acc})$ and $f(\mathrm{Gen})$ is irrelevant for monotonicity.
:::

::: exercise
For each one of the following syncretisms, state whether it can be realized by a monotonic mapping assuming the modified Blake hierarchy (if necessary, you may assume a different linear order of output forms for each syncretism).
Justify your answer.

- Syncretism of nominative and genitive to the exclusion of accusative
- Syncretism of nominative and dative to the exclusion of accusative
- Syncretism of nominative, accusative, and dative to the exclusion of genitive
- Syncretism of nominative, accusative, and genitive to the exclusion of dative
- Syncretism of accusative and genitive to the exclusion of nominative and dative

::: solution
1. Yes, because accusative does not occur between nominative and genitive.
1. No, because accusative occurs between nominative and dative.
1. No, because genitive occurs between nominative and dative (this might suggest that German dative does indeed always have an *e* which is removed for phonological reasons, so we don't have true syncretism of all three cases there).
1. Yes, because nominative, accusative, and genitive are all less than dative.
1. Yes. Suppose $f(\text{Nom}) = A$, $f(\text{Acc}) = f(\text{Gen}) = B$, and $f(\text{Dat}) = C$. This is a monotonic map if $A < B < C$.

::: solution_explained
The important thing to keep in mind here is the following fact: if $x \leq y \leq z$, then $f$ cannot be monotonic if $f(x) = f(z) \neq f(y)$.
Because $x \leq y \leq z$ implies that both $f(x) \leq f(y)$ and $f(y) \leq f(z)$ hold, and the only way to satisfy this if $f(x) = f(z)$ is for $y$ to be mapped to the same output as $x$ and $z$.
Hence we cannot have syncretism of two cases $x$ and $z$ to the exclusion of some other case $y$ between the two.
:::
:::
:::

It seems, then, that monotonicity does a lot of work even in the richer domain of case syncretisms.
The crucial step is to move from a total order to a partial order.

::: exercise
Actually, this insight was already implicit in the unit on NPIs, where we looked at the distribution of *ever*.
What was the partial order that we used in this case?

::: solution
It was the subset relation between sets.
This is not a linear order.
For instance, $\setof{a}$ and $\setof{b}$ are both subsets of $\setof{a,b}$, but (assuming $a \neq b$) $\setof{a}$ is not a subset of $\setof{b}$, nor the other way round.
:::
:::

## Recap

- Linguists often assume that hierarchies are **trichotomous**: all elements of the hierarchy must be ordered with respect to each other.
- If we drop the trichotomy requirement, linguistic hierarchies can be **partial orders**.
- In contrast to linguistic proposals like the No-Crossing-Branches constraint or the \*ABA generalization, monotonicity isn't limited to trichotomous orders.
  It works just as well for partial orders.
- This makes it possible to explain highly distinct linguistic phenomena as the result of two interacting factors: the formal universal of monotonicity that holds across many domains of language, and domain-specific substantive universals, each one of which takes the form of a linear order (e.g. $1 < 2 < 3$ for pronouns or $\mathrm{positive} < \mathrm{comparative} < \mathrm{superlative}$ in adjectival gradation) or a partial order (Blake's case hierarchy).

\includecollection{solutions}
