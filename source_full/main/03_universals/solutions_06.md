# The lattice space of $n$-gram grammars (Solutions)

::: exercise
As a reminder for yourself, write down an SL grammar for an attested linguistic phenomenon.
A simple option is word-final devoicing or intervocalic voicing, but feel free to mix it up a bit.
:::

::: exercise
Suppose that you have the SL-$3$ language $(\String{aba})^+$, which contains $\String{aba}$, $\String{abaaba}$, $\String{abaabaaba}$, and so on.
Write down the positive trigram grammar for this language.
Then write down a single example from which one can immediately infer the whole grammar.

::: solution
The positive trigram grammar $G$ contains all of the following, and nothing else:

1. $\String{{{{L}}}{{{L}}}a}$
1. $\String{{{{L}}}ab}$
1. $\String{aba}$
1. $\String{baa}$
1. $\String{ba{{{R}}}}$
1. $\String{a{{{R}}}{{{R}}}}$

The shortest example from which one can infer the entire grammar is $\String{abaaba}$.
:::

:::

::: exercise
Suppose $G_1 \is \setof{{{{L}}}{{{R}}}, {{{L}}}a, aa}$ and $G_2 \is \setof{a{{{R}}}}$.
Compute $G_{1 \wedge 2}$ and $G_{1 \vee 2}$.

::: solution
1. $G_{1 \wedge 2} = \emptyset$
1. $G_{1 \vee 2} = \setof{ {{{L}}}{{{R}}}, {{{L}}}a, aa, a{{{R}}} }$
:::

:::

::: exercise
Suppose that the lattice of grammars is as depicted above.
Assume furthermore that the currently conjectured grammar is $\setof{{{{L}}}{{{R}}}}$.
The next example contains the bigrams ${{{L}}}a$ and $a{{{R}}}$.
Verify via calculation that
$\setof{{{{L}}}{{{R}}}} \cup \setof{{{{L}}}a, a{{{R}}}} = \setof{{{{L}}}{{{R}}}} \vee \setof{{{{L}}}a, a{{{R}}}}$.

::: solution
1. $\setof{{{{L}}}{{{R}}}} \cup \setof{{{{L}}}a, a{{{R}}}} = \setof{{{{L}}}{{{R}}}, {{{L}}}a, a{{{R}}}}$
1. $\setof{{{{L}}}{{{R}}}} \vee \setof{{{{L}}}a, a{{{R}}}}$ is the least upper bound of $\setof{ {{{L}}}{{{R}}} }$ and $\setof{ {{{L}}}a, a{{{R}}} }$.
The following grammars are upper bounds for both of them:
$\setof{ {{{L}}}{{{R}}}, {{{L}}}a, a{{{R}}} }$
and
$\setof{ {{{L}}}{{{R}}}, {{{L}}}a, a{{{R}}}, aa }$.
As
$\setof{ {{{L}}}{{{R}}}, {{{L}}}a, a{{{R}}} }$
is less than
$\setof{ {{{L}}}{{{R}}}, {{{L}}}a, a{{{R}}}, aa }$,
it follows that 
$\setof{ {{{L}}}{{{R}}}, {{{L}}}a, a{{{R}}} }$
is the least upper bound of the two grammars.
But as we already showed, this is exactly the union of the two grammars.
:::

:::

::: exercise
Suppose that all members of $\mathcal{G}$ are negative grammars.
Draw the corresponding lattice of languages, and connect each grammar to its language with a colored line.
:::

::: exercise
What is the relation between negative grammars and their languages?
Is it still monotonic?
If so, is it the same kind of monotonicity?

::: solution
The function mapping negative grammars to their languages is monotonic decreasing.
:::

:::
