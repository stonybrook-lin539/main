# Person Case Constraints

::: exercise
Can you think of other clitics in English?
Exemplify their use with specific sentences.

::: solution
There is also *'em* and *'im* as in *I told'em to help each other* or *I told'im to buy himself something nice*.
:::

:::

::: exercise
Add the corresponding table for the M-PCC.

::: solution
**M(e first)-PCC:** If IO is 2 or 3, then DO is not 1.

$\downarrow$IO/DO$\rightarrow$ | 1 | 2 | 3
--: | :-: | :-: | :-:
1   | -   | Y   | Y
2   | N   | -   | Y
3   | N   | Y   | -

:::

:::

::: exercise
Translate between IO/DO notation and pairs.

1. 2IO, 1DO
1. $\tuple{1,2}$
1. $\tuple{3,3}$
1. 2DO, 1IO

::: solution
1. $\tuple{2,1}$
1. 1IO, 2DO
1. 3IO, 3DO
1. $\tuple{1,2}$

:::

:::

::: exercise
Fill each gap with $<$, $>$, or $=$ as appropriate.
If none of the three fit, leave the gap empty.

1. $\tuple{3,3} \_ \tuple{2,2}$
1. $\tuple{2,3} \_ \tuple{2,2}$
1. $\tuple{3,2} \_ \tuple{2,2}$
1. $\tuple{2,2} \_ \tuple{2,2}$
1. $\tuple{1,2} \_ \tuple{3,1}$

::: solution
1. $\tuple{3,3} > \tuple{2,2}$
1. $\tuple{2,3} > \tuple{2,2}$
1. $\tuple{3,2} > \tuple{2,2}$
1. $\tuple{2,2} = \tuple{2,2}$
1. $\tuple{1,2} \_ \tuple{3,1}$
:::

::: solution_explained
In all those cases, we just have to compare the first components and the second components of the two pairs.

1. $3 > 2$ and $3 > 2$; since both components of the first pair are greater than the corresponding components of the second pair, the first pair is greater than the second pair
1. $2 = 2$ and $3 > 2$; the first components are equal, but the second component of the first pair is greater than the second component of the second pair.
1. $3 > 2$ and $2 = 2$; same as the previous case, except that we now see the inequality in the first component
1. $2 = 2$ and $2 = 2$; the first components of both pairs are the same, and so are the second components
1. $1 < 3$ and $2 > 1$; the first component of the first pair is less than the first component of the second pair, but the second component of the first pair is greater than the first component of the second pair, so that we have no order between the pairs
:::

:::

::: exercise
Write down the 6 values of $f$ for the W-PCC.

::: solution
- $\tuple{1,2} \mapsto T$
- $\tuple{1,3} \mapsto T$
- $\tuple{2,1} \mapsto T$
- $\tuple{2,3} \mapsto T$
- $\tuple{3,1} \mapsto F$
- $\tuple{3,2} \mapsto F$
:::

:::

::: exercise
Pick two pairs $x$ and $y$ and use them to show that the U-PCC is not a monotonically increasing map.

*Hint:* What's the main difference between the W-PCC and the U-PCC?

::: solution
We have $\tuple{2,3} \leq \tuple{2,1}$, yet $f(\tuple{2,3}) = T > F = f(\tuple{2,1})$.
:::

:::

::: exercise
Continuing the previous exercise, show that the U-PCC isn't a monotonically decreasing map either.

::: solution
We have $\tuple{3,2} \leq \tuple{1,2}$, yet $f(\tuple{3,2}) = F < T = f(\tuple{1,2})$.
:::

:::

::: exercise
Fill each gap with $\triangleleft$, $\triangleright$, or $=$ as appropriate.
If none of the three fit, leave the gap empty.


1. $\tuple{3,3} \_ \tuple{2,2}$
1. $\tuple{2,3} \triangleleft \tuple{2,2}$
1. $\tuple{3,2} \triangleright \tuple{2,2}$
1. $\tuple{2,2} = \tuple{2,2}$
1. $\tuple{1,2} \triangleleft \tuple{3,1}$

::: solution
Again we only need to compare the respective components against each other.
1. $3 > 2$ and $3 \prec 2$
1. $2 = 2$ and $3 \prec 2$
1. $3 > 2$ and $2 = 2$
1. $2 = 2$ and $2 = 2$
1. $1 < 3$ and $2 \prec 1$.
:::

:::

::: exercise
This exercise is only for those who have already delved deep into the background sections:
Explain why $\triangleleft$ is a weak partial order.

*Hint*: Remember the three properties that each weak partial order must satisfy, and explain for each one why it holds.

::: solution
The relation $\triangleleft$ is a weak partial order because it is transitive, antisymmetric, and reflexive.
In the following, I write $m \prec=n$ as a shorthand for "$m \prec n$ or $m = n$".

1. **Transitivity**:
   Suppose $\tuple{a,x} \triangleleft \tuple{b,y}$ and $\tuple{b,y} \triangleleft \tuple{c,z}$.
   This entails that $a \leq b \leq c$ and $x \prec= y \prec= z$.
   But then, by the definition of $\leq$ and $\prec=$, it holds that $\tuple{a,x} \triangleleft \tuple{b,y}$.

1. **Antisymmetry**:
   Suppose $\tuple{a,x} \triangleleft \tuple{b,y}$ and $\tuple{b,y} \triangleleft \tuple{a,x}$.
   This entails that $a \leq b$, $b \leq a$, $x \prec= y$, and $y \prec= x$.
   But then, by the definition of $\leq$ and $\prec=$, it holds that $a = b$ and $x = y$, so that $\tuple{a,x} = \tuple{b,y}$.

1. **Reflexivity**:
   By definition $\tuple{a,x} \triangleleft \tuple{b,y}$ iff $a \leq b$ or $x \prec= y$.
   This holds if $a = b$ and $x = y$, so that $\tuple{a,x} \triangleleft \tuple{a,x}$ for all choices of $a$ and $x$.
:::

:::

::: exercise
Redraw the figures above with arrows pointing towards T and F as we did earlier on in this unit.
Confirm for yourself that this is indeed a monotonically increasing map.
:::

::: exercise
Draw the corresponding pictures (with boxes instead of arrows) for the S(trong)-PCC and the M(e first)-PCC.

::: solution

~~~ {.include-tikz size=mid}
pcc_hierarchy_right_spcc.tikz
~~~

~~~ {.include-tikz size=mid}
pcc_hierarchy_right_mpcc.tikz
~~~

:::

:::
