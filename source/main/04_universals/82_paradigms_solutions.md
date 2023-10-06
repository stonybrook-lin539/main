---
pagetitle: >-
    Morphological paradigms (Solutions)
---

# Morphological paradigms (Solutions)

::: exercise
Can you think of an example of an English adjective that does not have a comparative and/or superlative form?

::: solution
Your answer depends on how one interprets the requirement "does not have a comparative and/or superlative form".
Prescriptivists (a polite term for grammar nazis) claims that there is no such thing as *more pregnant* and *most pregnant* since you are either pregnant or you are not.
But people do say things like "this is the most pregnant I have ever been" and nobody bats an eye.
Lots of adjectives that seem not to be gradable can be made to be gradable.
Pregnancy can be construed as a sliding scale, with week 1 barely pregnant and week 30 really, really pregnant.
And once something is on a scale, it can usually be graded.

However, there seem to be cases where an adjective is scalar and thus should be gradable, yet it resists gradation nonetheless.
Consider *alleged*.
This seems like it should be gradable: depending on how many people, say, allege that the current president is a crook, the current president may be a more alleged crook than previous presidents.
Yet "a more alleged crook" sounds really clunky.
And if you do a online search for the phrase "a more alleged", all you find is other uses like "a more alleged than genuine consistency", sentences that are full of grammar mistakes, or example sentences from linguistics papers.
There is something about *alleged* that seems to make gradation more difficult.
:::

:::

::: exercise
What patterns do the two pictures below represent?

~~~ {.include-tikz size=mid}
123_AAB.tikz
~~~

~~~ {.include-tikz size=mid}
123_ABB.tikz
~~~

::: solution
AAB and ABB, respectively.
:::

:::

::: exercise
Using $\mapsto$ as above, define
$f_{AAA}$,
$f_{ABB}$,
$f_{ABC}$,
and
$f_{ABA}$.

::: solution
1. $f_{AAA}$: $1 \mapsto A$, $2 \mapsto A$, $3 \mapsto A$; or equivalently: $x \mapsto A$ for every $x \in \setof{1,2,3}$
1. $f_{ABB}$: $1 \mapsto A$, $2 \mapsto B$, $3 \mapsto B$
1. $f_{ABC}$: $1 \mapsto A$, $2 \mapsto B$, $3 \mapsto C$
1. $f_{ABA}$: $1 \mapsto A$, $2 \mapsto B$, $3 \mapsto A$
:::

:::

::: exercise
Show that $f_{ABA}$ is not monotonically decreasing.

::: solution
We have to show that there are $x$ and $y$ such that $x \leq_S y$ holds but $f(x) \geq_T f(y)$ does not hold.
This is the case for $x = 1$ and $y = 2$:
$1 \leq_S 2$, yet $f(1) = A \leq_T B = f(2)$.
:::

:::

::: exercise
Show that monotonicity also explains the absence of adjectival gradation paradigms like
*good*-*better*-*goodest*
if one assumes the hierarchy $\mathrm{positive} < \mathrm{comparative} < \mathrm{superlative}$.
Explain why this is an intuitively plausible hierarchy.

::: solution
The paradigm *good*-*better*-*goodest* represents a case where the positive and superlative use an A form, while the comparative uses a B form.
No monotonic function $f$ can produce this pattern from the adjectival gradation hierarchy $\mathrm{positive} < \mathrm{comparative} < \mathrm{superlative}$.
Note that it holds for the *good*-*better*-*goodest* pattern that $f(\mathrm{positive}) = A = f(\mathrm{superlative})$.
If $f$ is monotonic increasing or monotonic decreasing, then it must be the case that $f(x) = A$ for every $x$ such that $\mathrm{positive} \leq x$ and $x \leq \mathrm{superlative}$.
The comparative satisfies this condition ($\mathrm{positive} \leq \mathrm{comparative}$ and $\mathrm{comparative} \leq \mathrm{superlative}$), yet $f(\mathrm{comparative}) \neq A$.
Hence $f$ is not monotonic, which confirms the initial claim.

The hierarchy is intuitively plausible because it orders the three forms by their meaning.
For example, a *tall* man is not as tall as a *taller* man, and nobody is taller than the *tallest* man.
:::

:::

::: exercise
Earlier I mentioned briefly that no language seems to allow AAB as an adjectival gradation pattern.
Is this predicted by monotonicity?
If not, is this an undergeneration or an overgeneration problem?

::: solution
This is not predicted because the AAB pattern is monotonically increasing: $f(\text{positive}) = f(\text{comparative}) = A$, $f(\text{superlative}) = B$, and $A < B$.
This is an overgeneration problem because our formalism predicts that AAB should exist in some language, yet we do not find it in any language.
:::

:::
