# Morphological paradigms (Solutions)

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
Define
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
if one assumes the hierarchy $\text{positive} < \text{comparative} < \text{superlative}$.
Explain why this is an intuitively plausible hierarchy.

::: solution
The paradigm *good*-*better*-*goodest* represents a case where the positive and superlative use an A form, while the comparative uses a B form.
No monotnic function $f$ can produce this pattern from the adjectival gradation hierarchy $\text{positive} < \text{comparative} < \text{superlative}$.
Note that it holds for the *good*-*better*-*goodest* pattern that $f(\text{positive}) = A = f(\text{superlative})$.
If $f$ is monotonic increasing or monotonic decreasing, then it must be the case that $f(x) = A$ for every $x$ such that $\text{positive} \leq x$ and $x \leq \text{superlative}$.
The comparative satisfies this condition ($\text{positive} \leq \text{comparative}$ and $\text{comparative} \leq \text{superlative}$), yet $f(\text{comparative}) \neq A$.
Hence $f$ is not monotonic, which confirms the initial claim.

The hierarchy is intuitively plausible because it orders the three forms by their meaning.
For example, a *tall* man is not as tall as a *taller* man, and nobody is taller than the *tallest* man.
:::

:::

::: exercise
As was briefly mentioned earlier, no language seems to allow AAB as an adjectival gradation pattern.
Is this predicted by monotonicity?
If not, is this an undergeneration or an overgeneration problem?

::: solution
This is not predicted because the AAB pattern is monotonically increasing: $f(\text{positive}) = f(\text{comparative}) = A$, $f(\text{superlative}) = B$, and $A < B$.
This is an overgeneration problem because our formalism predicts that AAB should exist in some language, yet we do not find it in any language.
:::

:::
