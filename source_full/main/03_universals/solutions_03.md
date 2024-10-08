# Monotonicity in case syncretism (Solutions)

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
German *Haus* 'house' inflects s follows:

1. Nominative: *Haus*
1. Accusative: *Haus*
1. Genitive: *Hauses*
1. Dative: *Haus*

Nominative, accusative, and dative are syncretic to the exclusion of genitive.
:::
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
Explain why the following hierarchy is empirically inadequate:
$\text{Nom} <
\text{Gen} <
\text{Acc} <
\text{Dat} <
\text{others}$.

::: solution
This hierarchy predicts that nominative and accusative can never be syncretic to the exclusion of genitive, but we find tons of languages that do that, including the German example of *Haus*.
:::
:::

::: exercise
Icelandic also has some nouns where nominative and genitive are syncretic to the exclusion of dative and accusative.
Which variants of Blake's hierarchy does this rule out?

::: solution
This argues against any variant of the hierarchy where accusative or dative occur between nominative and genitive.
:::
:::

::: exercise
Pick one of the problematic syncretisms pointed out above and explain why it is also problematic if we replace the $^*$ABA generalization with the requirement that the mapping from the Blake hierarchy to surface forms must be a monotonic function.


::: solution
Consider the Icelandic case of syncretism of Accusative and Dative.
We have $f(\text{Acc}) = f(\text{Dat}) = A \neq B = f(\text{Gen})$.
Suppose w.l.o.g. that $A < B$.
Then $f$ is not monotonically increasing because $\text{Gen} \leq \text{Dat}$ yet $f(\text{Gen}) > f(\text{Dat})$.
But $f$ is not monotonically decreasing either because $\text{Acc} \leq \text{Gen}$ yet $f(\text{Acc}) < f(\text{Gen})$.
:::
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
:::

::: solution_explained
The important thing to keep in mind here is the following fact: if $x \leq y \leq z$, then $f$ cannot be monotonic if $f(x) = f(z) \neq f(y)$.
Because $x \leq y \leq z$ implies that both $f(x) \leq f(y)$ and $f(y) \leq f(z)$ hold, and the only way to satisfy this if $f(x) = f(z)$ is for $y$ to be mapped to the same output as $x$ and $z$.
Hence we cannot have syncretism of two cases $x$ and $z$ to the exclusion of some other case $y$ between the two.
:::

:::
