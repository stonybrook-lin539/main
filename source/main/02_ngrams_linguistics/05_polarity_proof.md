---
pagetitle: >-
    Proof: Equivalence of positive and negative grammars
---

# Proof: Equivalence of positive and negative grammars

:::prereqs
- general (abbreviations[w.l.o.g.])
- sets (basic notation, operations)
- strings (basic notation)
:::

This section defines both negative and positive versions of $n$-gram grammars and shows that they are expressively equivalent.
Like in the section on the equivalence of strict and mixed $n$-gram grammars, this is accomplished by a **constructive** proof.
A proof is constructive if it doesn't just derive the existence of some object, but gives a concrete procedure for constructing this object.
In the case at hand, the proof shows how to construct a positive grammar from a negative one, and the other way around.

::: definition
A **(strict) $n$-gram grammar** $G$ over alphabet $\Sigma$ is a finite set of strings drawn from $\Sigma^E_n$ ($n \geq 1$).
A $\Sigma$-string $s$ is well-formed with respect to

- the **negative** interpretation of $G$ iff no $n$-gram that is a factor of $s$ is a member of $G$,
- the **positive** interpretation of $G$ iff every $n$-gram that is a factor of $s$ is a member of $G$.

The **negative stringset** or **negative language of $G$**, denoted $N(G)$, is the set of all strings that are well-formed with respect to $G$ under its negative interpretation.
Similarly, $P(G)$ is the **positive stringset/language of $G$**.
:::

Note that the definition above does not treat positive and negative as a fundamental split between types of grammars but rather as different ways of interpreting the same grammar.
This is mostly for mathematical convenience, but it goes to show that there are many ways of formalizing the same basic idea.

::: theorem
For every $n$-gram grammar $G$ there exists a grammar $G'$ such that $P(G) = N(G')$ and $N(G) = P(G')$.
:::

::: proof
Let $G' \is \Sigma_E^n - G$.
We show w.l.o.g. that $P(G) = N(G')$.

First, every $s \in P(G)$ is necessarily a member of $N(G')$.
Assume towards a contradiction that $s \notin N(G')$.
Then there must be some $g \in G'$ that is a factor of $s$.
But since $G' \is \Sigma_E^n - G$, $g \in G'$ implies $g \notin G$, wherefore $s \notin P(G)$.
As this contradicts our initial assumption that $s \in P(G)$, it cannot be the case that $s \notin N(G')$.
So $s \in N(G')$ after all.

In the other direction, suppose that $s \notin P(G)$.
Then by definition there must be some $\Sigma_E^n \ni g \notin G$ that is a factor of $s$.
But then $g \in G'$, which entails $s \notin N(G')$.

This shows that $s \in P(G)$ iff $s \in N(G')$.
As $s$ was arbitrary, this holds for all strings and establishes $P(G)=N(G')$, which concludes our proof.
:::

::: exercise
Explain why we do not need to show that $N(G) = P(G')$.

::: solution
The proof already shows that $P(G) = N(G')$.
Hence there must be some grammar $G''$ for $G'$ such that $P(G') = N(G'')$.
By our construction, $G'' \is \Sigma^n_E - G'$.
But since $G' \is \Sigma^n_E - G$, we have $G'' = \Sigma^n_E - (\Sigma^n_E - G) = G$.
Obviously $G'' = G$ implies $N(G'') = N(G)$, and thus $P(G') = N(G)$.
:::
:::

Again you should not feel discouraged if you can't make sense of the proof yet.
Take a deep breath, don't panic, and try to translate the symbol salad into English in your head.
Try to break the proof down into individual chunks that you can make sense of, and then reassemble those chunks into the overall argument of the proof.
And if you run out of energy, put this unit down, move on to the next one, and come back a few weeks later when you have built up more math endurance.

\includecollection{solutions}
