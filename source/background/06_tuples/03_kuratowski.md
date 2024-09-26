---
pagetitle: >-
    The Kuratowski definition of pairs
---

# The Kuratowski definition of pairs

::: prereqs
- sets (basic notation, cardinality)
- tuples (pairs)
:::

Disclaimer: This unit is different from other background units in that it is quite opinionated.
I will talk about the Kuratowski definition of pairs and how linguists' attempts to leverage it for the study of sentence structure have serious problems.
A lot of them stem from a misunderstanding of the status of mathematical definitions and their intended usage.
After reading this unit, you will hopefully have a deeper appreciation of these issues and stay away from such misapplications of math.

## Pairs as sets

As you have seen several times by now, mathematics provides many different ways of talking about the same thing.
This includes the option to look at pairs as specific kinds of sets.
In fact, there are many different ways of defining pairs as sets.
Below is a far-from-comprehensive selection of such definitions.

::: definition
We define the **pair** $\tuple{a,b}$ as the set

Wiener

: $\setof{ \setof{ \setof{a}, \emptyset }, \setof{ \setof{b}} }$

Hausdorff

: $\setof{ \setof{a, 1}, \setof{b, 2}}$

Kuratowski (long)

: $\setof{ \setof{a}, \setof{a,b}}$

Kuratowski (short)

: $\setof{ a, \setof{a,b}}$

:::

Note that since these are definitions, they cannot be true or false.
The only question is whether these are useful definitions of pairs.
What exactly this means depends on why one would want to use sets instead of pairs.
At the very least, though, a useful definition of pairs has to preserve the most fundamental property of pairs:
$\tuple{a,b} = \tuple{c,d}$ iff $a = c$ and $b = d$.
Let us take a closer look at whether that holds for the two Kuratowski definitions.

## The logic behind the long Kuratowski definition

According to the long Kuratowski definition, the pair $\tuple{a,b}$ is equivalent to the set $\setof{ \setof{a}, \setof{a,b} }$.
The two are equivalent because they satisfy the same identity condition: $\tuple{a,b} = \tuple{c,d}$ iff $a = c$ and $a = d$, and $\setof{ \setof{a}, \setof{a,b}} = \setof{ \setof{c}, \setof{c, d}}$ iff $a = c$ and $b = d$.
Let us verify that this indeed holds.

::: proof
The right to left direction is trivial: if $a = c$ and $b = d$, then
$\setof{ \setof{a}, \setof{a,b} } = \setof{ \setof{c}, \setof{c,d}}$.
In the other direction, we have to consider two separate cases depending on whether $a = b$ or $a \neq b$.
In each case, we need to show that $a = c$ and $b = d$.

**Case 1.**
Suppose $a = b$.
Then $\{ \{a\}, \{a,b\} \} = \{ \{a\}, \{a, a\} \} = \{ \{a\}, \{a\} \} = \{ \{a\} \}$.
But then $\{ \{a\}, \{a,b\} \} = \{ \{c\}, \{c,d\} \}$ is the same as $\{ \{a\} \} = \{ \{c\}, \{c,d\} \}$.
This is possible only if $\{ c \} = \{c ,d\}$, which implies $c = d$.
Hence $\{ \{c\}, \{c,d\} \} = \{ \{c\}, \{c,c\} \} = \{ \{c\}, \{c\} \} = \{\{c\}\} = \{\{a\}\}$, which entails $a = c$.
As we already know that $a = b$ and $c = d$, we also conclude from $a = c$ that $b = d$.

**Case 2.**
Now suppose that $a \neq b$.
Then either $\setof{a} = \setof{c,d}$ or $\setof{a} = \setof{c}$.
We consider each subcase.

**Subcase 2.1.**
Suppose towards a contradiction that $\setof{a} = \setof{c,d}$.
Since two sets with distinct cardinality cannot be identical, the equality $\{a\} = \{c,d\}$ holds only if $c = d$.
Then $\{ \{a\}, \{a,b\} \} = \{ \{c\}, \{c,d\} \} = \{ \{c\}, \{c\} \}$.
But then we have both $\setof{a} = \setof{c}$ and $\setof{a,b} = \setof{c}$.
This is impossible unless $a = b$, but by our initial assumption for Case 2, $a \neq b$.
This is a contradiction, disproving the assumption of Subcase 2.1 that $\setof{a} = \setof{c,d}$.
We conclude that $\setof{a} \neq \setof{c,d}$ after all.

**Subcase 2.2.**
Assume, then, that $\setof{a} = \setof{c} \neq \setof{c,d}$.
This implies that $a = c$, so it only remains for us to show that $b = d$.
Note that $c \neq d$ because we assume $\setof{c} \neq \setof{c,d}$.
Given all these (in)equalities, $\setof{ \setof{a}, \setof{a,b} } = \setof{ \setof{c}, \setof{c,d} }$ necessarily entails that $\setof{a,b} = \setof{c,d}$, which in turn implies $b = d$ because we already know that $a = c$ and $a \neq b$.
:::

::: exercise
Show that the Wiener definition of pairs preserves identity.
That is to say, prove that
$\setof{ \setof{ \setof{a}, \emptyset }, \setof{ \setof{b} } } = \setof{ \setof{ \setof{c}, \emptyset }, \setof{ \setof{d} } }$ iff $a = c$ and $b = d$.

::: solution
Again the right-to-left direction is trivial.
In the other direction, observe that $\setof{ \setof{a}, \emptyset}$ must have cardinality 2 because $\setof{a} \neq \emptyset$ for every choice of $a$.
But $\setof{\setof{d}}$ has cardinality 1.
Hence it must be the case that $\setof{\setof{d}} \neq \setof{ \setof{a}, \emptyset } = \setof{ \setof{c}, \emptyset}$, which in turn entails that $\setof{\setof{d}} = \setof{\setof{b}}$ and thus $b = d$.
Since we already know that $\setof{a} \neq \emptyset$, it also follows that $\setof{a} = \setof{c}$ and thus $a = c$.
:::
:::

::: exercise
It is tempting to generalize the long Kuratowski definition from pairs to tuples.
For instance, the triple $\tuple{a,b,c}$ would correspond to the set $\setof{ \setof{a}, \setof{a,b}, \setof{a,b,c}}$.
However, this definition does not preserve the identity requirement of tuples.
Show that there are cases where $\tuple{a,b,c} \neq \tuple{d,e,f}$ yet $\setof{ \setof{a}, \setof{a,b}, \setof{a,b,c}} = \setof{ \setof{d}, \setof{d,e}, \setof{d,e,f}}$.

::: solution
Suppose that $a \neq b$ and consider the triple $\tuple{a,a,b}$:

\begin{align*}
\tuple{a,a,b}
    &= \setof{ \setof{a}, \setof{a,a}, \setof{a,a,b} }
        \tag{Generalized Kuratowski definition}\\
    &= \setof{ \setof{a}, \setof{a}, \setof{a,b} }
        \tag{Idempotency of sets}\\
    &= \setof{ \setof{a}, \setof{a,b} }
        \tag{Idempotency of sets}\\
    &= \setof{ \setof{a}, \setof{a,b}, \setof{a,b} }
        \tag{Idempotency of sets}\\
    &= \setof{ \setof{a}, \setof{a,b}, \setof{a,b,b} }
        \tag{Idempotency of sets}\\
    &= \tuple{ a, b, b }
        \tag{Generalized Kuratowski definition}\\
\end{align*}

But since $a \neq b$, it cannot be the case that $\tuple{a,a,b} = \tuple{a,b,b}$.
Contradiction.

The generalized Kuratowski definition gives the desired behavior only in the special case of $\tuple{a,b,c}$ with $a \neq b$, $a \neq c$, and $b \neq c$.
:::
:::

## When does the Kuratowski definition work?

The proof above is mathematically sound, but it relies on specific assumptions of set theory.
For example, we assumed that it is impossible for both $c \neq d$ and $\{a\} = \{c,d\}$ to be true at the same time because a set with one member can never be identical to a set with two members.
While this is intuitive enough, it means that the proof is tied to a notion of sets that satisfies this property.
Change how sets work, and the long Kuratowski definition will no longer be useful as an alternative view of pairs.

While the troubles with the long Kuratowski definition stop there, the short Kuratowski definition requires even more specialized assumptions.
This definition defines $\tuple{a,b}$ as $\setof{ a, \setof{a,b}}$ instead of $\setof{ \setof{a}, \setof{a,b}}$.
It is this definition in particular that seems to be a good fit for linguistics because of recent proposals that sentence structure involves sets of the shape $\setof{a, \setof{a,b}}$.

::: example
Consider the sentence *My cat snored*.
It is built from the verb *snored* and the noun phrase **my cat**.
One common proposal is that this noun phrase is built by an operation called **Merge**.
Given a **head** *H* and **argument** *A*, Merge combines them into the set $\setof{\mathit{H}, \setof{\mathit{H}, \mathit{A}}}$.
In the case at hand, Merge takes the head *my* and argument *cat* and combines them into $\setof{\mathit{my}, \setof{\mathit{my}, \mathit{cat}}}$ (there are linguistic reasons for assuming *my* is the head rather than *cat*).

Applying the short Kuratowski definition to the set $\setof{\mathit{my}, \setof{\mathit{my}, \mathit{cat}}}$ yields the pair $\tuple{\mathit{my}, \mathit{cat}}$, which is conceptually pleasing because it corresponds to the string *my cat* that we actually see in the sentence *my cat snored*.
:::

::: exercise
What would be the set produced by merging $\setof{\mathit{my}, \setof{\mathit{my}, \mathit{cat}}}$ with *snored*, assuming that *snored* is the head?
Does this still produce the correct linear order?
That is to say, does the order of words in the resulting pair correspond to the order of words in the sentence *my cat snored*?

::: solution
Merge produces the set $\setof{ \mathit{snored}, \setof{ \mathit{snored}, \setof{ \mathit{my}, \setof{ \mathit{my}, \mathit{cat} }}}}$.
The corresponding pair is $\tuple{ \mathit{snored}, \tuple{ \mathit{my}, \mathit{cat} }}$.
This is the wrong order as it yields *snored my cat* instead of *my cat snored*.

::: solution_explained
The set is constructed as usual using the rule that Merge of $H$ and $A$ results in $\setof{ H, \setof{H ,A}}$.
Here $H$ is *snored* and $A$ is the set $\setof{ \mathit{my}, \setof{ \mathit{my}, \mathit{cat} }}$.
:::
:::
:::

::: exercise
Many linguists would argue that *snored* is itself built up from smaller parts which correspond to the verb *snore* and the past tense marker *ed*.
Assuming that the past tense marker acts as the head and the verb as the argument, *snored* corresponds to the set $\setof{ \mathit{ed}, \setof{ \mathit{snore}, \mathit{ed} }}$.
What, then, would be the result of merging this set with $\setof{ \mathit{my}, \setof{ \mathit{my}, \mathit{cat} }}$ as in the previous exercise?
What pair does this correspond to?

::: solution
Merge produces the set $\setof{ \setof{\mathit{ed}, \setof{ \mathit{snore}, \mathit{ed} }}, \setof{ \setof{ \setof{\mathit{ed}, \setof{ \mathit{snore}, \mathit{ed} }}, \setof{\mathit{my}, \setof{ \mathit{my}, \mathit{cat} }}}}}$.
The corresponding pair is $\tuple{ \tuple{\mathit{ed}, \mathit{snore}}, \tuple{\mathit{my}, \mathit{cat} }}$.

::: solution_explained
Again we are just applying the definition of Merge.
The only complication is that $H$ is now itself a set built by Merge.
:::
:::
:::

::: exercise
Consider the sentence *The dog hates my cat*.
Treating *hates* as a single element, and assuming that it is a head that first combines with *my cat*, we get the set $H \is \setof{ \mathit{hates}, \setof{ \mathit{hates}, \setof{ \mathit{my}, \setof{ \mathit{my}, \mathit{cat} }}}}$.
Similarly, *the dog* corresponds to the set $A \is \setof{ \mathit{the}, \setof{ \mathit{the}, \mathit{dog}}}$.
What is the result of combining the two if $H$ is the head and $A$ the argument?
Can this set be interpreted as a pair via the short Kuratowski definition?
If so, what is the corresponding pair?

::: solution
As usual, Merge produces the set $\setof{ H, \setof{H, A}}$.
Substituting for $H$ and $A$, we get:

$$
\{
    \{ \mathit{hates}, \setof{ \mathit{hates}, \setof{ \mathit{my}, \setof{ \mathit{my}, \mathit{cat} }}}\},
    \{
        \{ \mathit{hates}, \setof{ \mathit{hates}, \setof{ \mathit{my}, \setof{ \mathit{my}, \mathit{cat} }}}\},
        \{ \mathit{the}, \setof{ \mathit{the}, \mathit{dog}}\}
    \}
\}
$$

The corresponding pair is

$$
    \tuple{
        \tuple{ \mathit{hates},
            \tuple{ \mathit{my}, \mathit{cat}}
        },
        \tuple{ \mathit{the}, \mathit{dog}}
    }
$$

Again the pairs do not track the linear order of words in the sentence but rather the order in which heads are merged with their arguments.
:::
:::

At first glance it seems that the proof for the long Kuratowski definition also works for its short counterpart.
But this is truly at first glance only.
Consider the counterpart to Subcase 2.1 above.
That is to say, we assume $\setof{ a, \setof{a,b} } = \setof{ c, \setof{c,d} }$ and furthermore assume towards a contradiction that $a = \{c, d\}$.
The problem is that this does not result in a contradiction.
We have two cases to consider: $\setof{a,b} = c$ and $\setof{a,b} = \setof{c,d}$.
If $\setof{a,b} = c$, then we have

\begin{align*}
a
    &= \setof{c, d}
        \tag{Initial assumption that $a = \setof{c,d}$}\\
    &= \setof{ \setof{a,b}, d}
        \tag{Substitute $\setof{a,b}$ for $c$}\\
    &= \setof{ \setof{ \setof{c,d} ,b}, d}
        \tag{Initial assumption that $a = \setof{c,d}$}\\
    &= \setof{ \setof{ \setof{\setof{a,b} ,d} ,b}, d}
        \tag{Substitute $\setof{a,b}$ for $c$}\\
    &\vdots\\
\end{align*}

And if $\setof{a,b} = \setof{c, d}$, then by our previous assumption that $a = \setof{c,d}$ we have

\begin{align*}
a
    &= \setof{c, d}
        \tag{Initial assumption that $a = \setof{c,d}$}\\
    &= \setof{a, b}
        \tag{Substitute\ $\setof{a,b}$ for $\setof{c,b}$}\\
    &= \setof{ \setof{a,b}, b}
        \tag{Substitute $\setof{a,b}$ for $a$}\\
    &= \setof{ \setof{\setof{a, b}, b}, b}
        \tag{Substitute $\setof{a,b}$ for $a$}\\
    &\vdots\\
\end{align*}

Either way we end up with what looks like an infinite sequence of substitutions, building an infinitely deep set where we never reach the bottom.
This may strike you as highly unintuitive and quite distinct from how we have used sets so far.
But remember what we said about sets: a set can contain arbitrarily complex objects, including other sets.
This does not rule out a set that contains a set that contains a set that contains a set, and so on, *ad infinitum*.
We can rule it out, of course, but we don't have to.
Mathematicians have produced many different definitions of sets, which are called **axiomatizations** of sets.
Some axiomatizations allow this kind of infinite nesting, and some do not.

::: example
The most commonly used axiomatization of sets is **ZFC**, which is short for **Zermelo-Fraenkel with the axiom of choice**.
ZFC is very different from the naive notion of sets we have been using as it makes no explicit distinction between objects and collections of objects.
In ZFC, everything is a set.

ZFC consists of multiple axioms.
One of them, the **axiom of regularity**, does indeed rule out infinitely nested sets like the ones we are building above.
However, this axiom isn't very important for ZFC.
One can remove it from the axioms and almost all the interesting theorems that have been established for sets in ZFC still hold.
:::

## Do we want infinitely nested sets?

There are over 100 years of mathematical research on sets that allow such infinite nesting.
This branch of mathematics is known as **non-well-founded set theory**, and these infinite sets are sometimes referred to as **hypersets**.
Hypersets aren't just a mathematical curiosity, they have been used in linguistics as the mathematical foundation of situation semantics, which models how humans reason over situations.
This is a very natural task that billions of humans perform effortlessly each day.
It does not look like human cognition struggles with the concept of hypersets.
On what grounds, then, should we ban hypersets for sentence structure?

::: exercise
Let $S$ be defined as $\setof{a, S}$.
This is a hyperset.
Explain why!

::: solution
By substituting for $S$, we obtain $\setof{a, S} = \setof{a, \setof{a, S}}$.
But then we can again substitute for $S$ to obtain $\setof{a, \setof{a, \setof{a, S}}}$.
We can keep doing so indefinitely, creating a set with infinite nesting.
This is a hyperset.
:::
:::

::: exercise
Can you think of an argument that sentences might be hypersets?

::: solution
English allows us to form sentences of the form *I know* but also *I know that I know*, which can be shortened to *I know I know*.
This can then be continued to produce, say, *I know I know I know I know*.
We can imagine forming a sentence *I know I know I know I know I know I know...*, continuing indefinitely.
Using the set-based representation of sentences, this would be the hyperset

$$
S \is 
    \setof{
        \setof{
            \mathit{know},
            \setof{
                \mathit{know},
                S
            }
        },
        \setof{
            \setof{
                \mathit{know},
                \setof{
                    \mathit{know},
                    S
                }
            },
                \mathit{I}
        }
    }
$$
:::
:::

We can do it, of course, we can rule out hypersets with the stroke of a pen.
But it would be a stipulation whose only motivation is to save the short Kuratowski definition as a convenient way of serializing the sets we see in sentence structure.
It would be tantamount to claiming that human cognition does not involve hypersets when it comes to sentence structure, but at the same time it is so deeply rooted in mathematical sets that it even employs the short Kuratowski definition of pairs.
That is a peculiar claim to make.

Moreover, making this claim does not tell us anything deep or profound about sentences.
We are simply putting in place mathematical assumptions to get the result we want.
These mathematical assumptions aren't forced onto us by the empirical lay of the land.
Whether we allow hypersets or not has no empirical consequences, it is a purely theory-internal decision.
This does not constitute scientific progress, it is a mathematical mirage.

To the extent that this proposal is supposed to capture a real property, the math is at best orthogonal to it and at worst actively obscures it.
The exercises earlier in this unit reveal that the short Kuratowski definition does not map the sets built by Merge to pairs with an obvious linguistic interpretation.
Invoking the short Kuratowski definition has nothing to say on the problem of how the sets built by Merge are mapped to the linear sequences that we call sentences, and it is unclear what other property of language it could possibly be capturing in an insightful manner.
In the absence of a clear empirical payoff, we should not open the can of worms that is hypersets, ZFC, the axiom of regularity, and correspondences between sets and pairs.
And if a linguistic proposal lacks empirical substance, then it is worthless as a claim about language no matter how elegantly it was derived from mathematical set theory.

## Recap

\includecollection{solutions}
