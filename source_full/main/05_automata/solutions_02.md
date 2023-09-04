# Automaton constructions (Solutions)

## Intersection

::: exercise
Using the same "finger pushing" procedure, say for each one of the following strings whether it is a member of $L(A) \cap L(B)$.

1. $\String{aba}$
1. $\String{abaabaabaabaabaa}$
1. $\String{abb}$

You do not need to write down each individual move of your finger, "Yes" and "No" are sufficient answers.

::: solution
1. No (rejected by $A$ and $B$)
1. Yes
1. No (rejected by $A$ and $B$)
:::
:::

::: exercise
In an earlier exercise you had to construct FSAs for $\String{a^* b^+}$ and $\String{a^+ b^+ a^*}$.
Construct their intersection automaton and verify that it recognizes the language $\String{a^+ b^+}$.

::: solution
We start with the two automata below:

~~~ {.include-tikz size=mid}
astarbplus.tikz
~~~

~~~ {.include-tikz size=mid}
aplusbplusastar.tikz
~~~

The corresponding intersection automaton is shown below:

~~~ {.include-tikz size=mid}
astarbplus_cap_aplusbplusastar.tikz
~~~

This automaton generates strings that start with $a$, followed by 0 or more $a$s, then a $b$, followed by 0 or more $b$s.
More succinctly, it generates $a a^* b b^*$, which is the same as $a^+ b^+$.
:::
:::

::: exercise
This exercise is optional!

The theorem above still requires a proof.
We have to show that the intersection automaton $C \is A \cap B$ does indeed recognize $L(A) \cap L(B)$.
This breaks down into two separate claims:

- $L(C) \subseteq L(A) \cap L(B)$
- $L(C) \supseteq L(A) \cap L(B)$

Try to prove each statement.

::: solution
Consider first $L(C) \subseteq L(A) \cap L(B)$.
Suppose $s \in L(C)$.
Then $s$ must have some run $\tuple{a_1, b_1}, \tuple{a_2, b_2}, \ldots, \tuple{a_n, b_n}$ ($n \geq 1$) such that $\tuple{a_1, b_1}$ is an initial state of $C$ and $\tuple{a_n, b_n}$.
But based on the construction of $C$ from $A$ and $B$, this means that $a_1, a_2, \ldots, a_n$ is a run of $A$ over $s$ with $a_1$ an initial state of $A$ and $a_n$ a final state of $A$.
Hence $s \in L(A)$.
The same argument entails that $s \in L(B)$.
But if $s \in L(A)$ and $s \in L(B)$, then $s \in L(A) \cap L(B)$.

Now suppose $s \in L(A) \cap L(B)$.
By assumption, there must be a valid run $a_1, a_2, \ldots, a_n$ of $A$ over $s$ and a valid run $b_1, b_2, \ldots, b_n$ of $B$ over $s$.
But then $\tuple{a_1, b_1}, \tuple{a_2, b_2}, \ldots, \tuple{a_n, b_n}$ must be a valid run of $C$, and thus $s \in L(C)$.
This entails that $L(A) \cap L(B) \subseteq L(C)$.
:::
:::

::: exercise
Construct a non-deterministic automaton that recognizes the language $ac^*b \cup acb^*$.
Careful, the automaton should recognize all strings of this language, but no more than that.
For instance, $\String{accbb}$ is not a string of this language.

::: solution

~~~ {.include-tikz size=mid}
acstarb_cup_acbstar.tikz
~~~

:::
:::

::: exercise
In the previous two examples, determinization does not increase the size of the automaton.
in general, though, determinization can cause an exponential blow-up: determinizing a non-deterministic FSA with $n$ states may yield a deterministic FSA with $2^n$ states.
That's huge.
For instance, a 10-state automaton might have 1024 states after determinization.
A 20-state automaton over a million!


In practice, the blow-up is not as bad, but it isn't uncommon for automata size to double, triple, or quadruple.
As a concrete example of this, determinize the automaton below.

~~~ {.include-tikz size=mid}
nondet_blowup.tikz
~~~

::: solution

~~~ {.include-tikz size=mid}
nondet_blowup_determinized.tikz
~~~

:::

:::

::: exercise
Only for the brave!

The automaton above doubles its size after determinization.
What about the automaton below?

~~~ {.include-tikz size=mid}
nondet_blowup2.tikz
~~~

::: solution

The determinized automaton is too large to draw.
Instead, we can represent its transitions in a tabular format with a row for each state and a column for each symbol.
For example, the cell in the row for state $0$ and the column for symbol $a$ contains $01$, telling us that $a$ moves us from $0$ to $01$ in this automaton (for the sake of succinctness, we drop set brackets and commas from state names).

| **State** | **a**   | **b**  |
| :--       | :-:     | :-:    |
| 0         | 01      | 0      |
| 01        | 012     | 02     |
| 012       | 0123    | 023    |
| 0123      | 01234   | 0234   |
| 01234     | 012345  | 0234   |
| 01235     | 01234   | 0234   |
| 012345    | 012345  | 0234   |
| 0124      | 01235   | 023    |
| 01245     | 01235   | 023    |
| 0125      | 0123    | 023    |
| 013       | 0124    | 024    |
| 0134      | 01245   | 024    |
| 01345     | 01245   | 024    |
| 0135      | 0124    | 024    |
| 014       | 0125    | 02     |
| 0145      | 0125    | 02     |
| 015       | 012     | 02     |
| 02        | 013     | 03     |
| 023       | 0134    | 034    |
| 0234      | 01345   | 034    |
| 024       | 0135    | 03     |
| 03        | 014     | 04     |
| 034       | 0145    | 04     |
| 04        | 015     | 0      |

The only initial state is 0, and all states containing 3, 4, or 5 are final.
Overall, the automaton has 24 states, whereas the original automaton had 6 states.
Determinizing has quadrupled the size of the automaton (but that is still much better than the worst-case scenario of an automaton with $2^6 = 64$ states).
:::

:::

::: exercise
Determinization does not necessarily increase the size of an automaton.
If the original automaton contains some redundancies, determinization can eliminate those.

The automaton below is a slightly redundant machine for accepting all strings over $a$ and $b$ that contain at least three symbols.

~~~ {.include-tikz size=mid}
nondet_shrinking.tikz
~~~

What does it look like after determinization?

::: solution

~~~ {.include-tikz size=mid}
nondet_shrinking_determinized.tikz
~~~

:::
:::

::: exercise
For each one of the following strings, give its run according to the automaton above with a sink state.

1. $\String{a}$
1. $\String{ab}$
1. $\String{abaa}$
1. $\String{abba}$
1. $\String{abaabaa}$
1. $\String{abbabaa}$

::: solution

1. $\String{a} =$ 0-1
1. $\String{ab} =$ 0-1-2
1. $\String{abaa} =$ 0-1-2-0-1
1. $\String{abba} =$ 0-1-2-S-S
1. $\String{abaabaa} =$ 0-1-2-0-1-2-0-1
1. $\String{abbabaa} =$ 0-1-2-S-S-S-S-S

:::
:::
