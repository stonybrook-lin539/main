---
pagetitle: Formal definition and proof of the normal form theorem
---

# Formal definition and proof of the normal form theorem

:::prereqs
- general (equals VS define)
- sets (basic notation)
- strings (basic notation)
:::

The previous two sections introduced negative $n$-gram grammars at great length and showed a basic normal form theorem: for every grammar with $n$-grams of mixed length, there is an equivalent grammar where all $n$-grams have the same length.
The presentation was deliberately informal to focus on intuitions rather than mathematical rigor.
This unit is very different.
It gives the definitions in a mathematical format, rigorously states the normal form theorem, and states the proof of the theorem in a more standard mathematical style.

I admit that this might be a lot to take in for the newbie, but it is illuminating to see just how much more compactly and precisely things can be stated with mathematical notation.
While it may seem like a nuisance or pointless hurdle to you now, mathematical notation will make things a lot easier in the long run.
I can't deny, though, that there is a learning curve, and you might not be able to take it all in at this point.
Try to get as far as you can, but don't panic, this is just to give you a taste of the power of mathematical notation.
If you can't stomach any more, move on to the next unit.
Once you feel more comfortable with this way of writing and reading, you should come back to this unit and contrast it to the two preceding ones. 
Odds are that this unit will feel very pleasant to you by then, whereas the two preceding ones will strike you as needlessly wordy and drawn out.

But let me reiterate: If you're suffering an acute case of symbol shock, don't worry.
We will continue this chapter at a leisurely pace, with optional formal sections sprinkled in to give a succinct summary of the more informal sections.

## Formal definition of negative grammars

::: definition
Let $\Sigma$ be some alphabet, and $\Sigma_E$ its extension with edge marker symbols ${{{L}}}, {{{R}}} \notin \Sigma$.
A string drawn from $\Sigma_E^n$, where $n \geq 1$, is also called an **$n$-gram**.
Given string $s$ over $\Sigma$, we say that $n$-gram $g$ is a **factor** of $s$ iff there are strings $u, v \in \Sigma_E^*$ such that 
${{{L}}}^{n-1} \stringcat s \stringcat {{{R}}}^{n-1} = u \stringcat g \stringcat v$.
:::

::: definition
A **(strict) negative $n$-gram grammar** $G$ over alphabet $\Sigma$ is a finite set of strings drawn from $\Sigma_E^n$ ($n \geq 1$).
A $\Sigma$-string $s$ is well-formed with respect to $G$ iff no $g \in G$ is a factor of $s$.
The **stringset** or **language of $G$**, denoted $L(G)$, is the set of all strings that are well-formed with respect to $G$, and only those.
:::

::: example
Suppose $\Sigma \is \setof{C, V}$, where C represents consonants and V vowels.
One string over $\Sigma$ is $\mathit{CVCVCV}$, an instance of a very simple CV-syllable template.
Assume $G$ contains $\mathit{CC}$ and $\mathit{VC}$ and let's see if the string $\mathit{CVCVCV}$ is well-formed with respect to $G$.
The bigram $\mathit{CC}$ is not a problem since there are no strings $u$ and $v$ such that ${{{L}}}\mathit{CVCV}{{{R}}} = u \stringcat \mathit{CC} \stringcat v$, which means that $\mathit{CC}$ is not a factor of $\mathit{CVCVCV}$. 
But clearly ${{{L}}}\mathit{CVCV}{{{R}}} = {{{L}}}\mathit{C} \stringcat \mathit{VC} \stringcat \mathit{V}{{{R}}}$.
So $\mathit{VC}$ is a factor of $\mathit{CVCV}$, and as a result the string is ruled out by $G$.
:::

::: definition
A **mixed negative $n$-gram grammar** $G$ is a finite set of strings such that each string is drawn from $\Sigma_E^1$, or $\Sigma_E^2$, or \ldots, or $\Sigma_E^n$.
The well-formedness of string $s$ with respect to $G$ is defined as before, and so is $L(G)$.
:::

::: example
Continuing the previous example, suppose that $G$ contains $\mathit{CC}$ and $\mathit{VVC}$.
Does this grammar deem the string $\mathit{CVCVVCV}$ well-formed?
There are no strings $u$ and $v$ such that $\mathit{{{{L}}}{{{L}}}CVVVCV{{{R}}}{{{R}}}} = u \stringcat \mathit{CC} \stringcat v$, which means that $\mathit{CVCVVCV}$ does not contain any instance of the forbidden bigram $\mathit{CC}$.
However, $\mathit{{{{L}}}{{{L}}}CVCVVCV{{{R}}}{{{R}}}} = \mathit{{{{L}}}{{{L}}}CVC} \stringcat \mathit{VVC} \stringcat \mathit{V{{{R}}}{{{R}}}}$.
In plain English: $\mathit{VVC}$ is a factor of $\mathit{CVCVVCV}$.
As a result, the string is ruled out by $G$.
:::


## Normal form theorem

::: theorem
For every mixed negative $n$-gram grammar $G$, there is a strict negative $n$-gram grammar $G'$ such that $L(G) = L(G')$.
:::

::: proof
If $n = 1$, this is true by definition: as every $n$-gram is at least of length of 1, all $n$-grams of $G$ are members of $\Sigma_E^1$, making $G$ a strict negative $n$-gram grammar.
Suppose, then, that $n \geq 2$.

Let $G'$ be the smallest set containing all strings of the form $u \stringcat g \stringcat v$ such that

1. $g \in G$, and
1. $u \in \Sigma_E^*$, and
1. $v \in \Sigma_E^*$, and
1. $\length{u \stringcat g \stringcat v} = n$.

We show that $L(G) = L(G')$ by showing that $s \notin L(G)$ iff $s \notin L(G')$ (this immediately entails that $s \in L(G) iff s \in L(G')$).

Suppose $s \notin L(G)$.
Then by definition there must be some $k$-gram $g \in G$ with $k \leq n$ and strings $u$ and $v$ over $\Sigma_E$ such that ${{{L}}}^{k-1} s {{{R}}}^{k-1} = u \stringcat g \stringcat v$.
This trivially entails that there are also strings $u'$ and $v'$ over $\Sigma_E$ such that ${{{L}}}^{n-1} s {{{R}}}^{n-1} = u' \stringcat g \stringcat v'$.
But since $\length{{{{L}}}^{n-1} s {{{R}}}^{n-1}} \geq n$, there must also be strings $u_1, u_2, v_1, v_2$ over $\Sigma_E$ such that

1. $u' = u_1 \stringcat u_2$, and
1. $v' = v_1 \stringcat v_2$, and
1. $\length{u_2 \stringcat g \stringcat v_1} = n$.

But then by definition of $G'$ it must hold that $u_2 \stringcat g \stringcat v_2 \in G'$, so that $s \notin L(G')$.

In the other direction, suppose $s \notin L(G')$.
Then there is some $g \in G'$ such that ${{{L}}}^{n-1} \stringcat s \stringcat {{{R}}}^{n-1} = u \stringcat g \stringcat v$.
But then by definition of $G'$ there must be $u'$, $g'$ and $v'$ over $\Sigma$ such that $g = u' \stringcat g' \stringcat v'$ and $g' \in G$.
Hence $g' \in G$ is a factor of $s$, an thus $s \notin L(G)$ by definition.
:::

And there you have it.
All the ground we've covered in dozens of pages so far, condensed into just a few paragraphs.
That's the power of math.

## Linguistics needs more proof enablers

While the proof above may be difficult for you to read or fully grasp, I hope you can see that with enough practice and experience it would be possible for you to make sense of it.
This isn't some opaque blackbox that is impossible to make sense of.
The proof builds on a specific set of assumptions, formalized via the definitions above, and then it shows how these assumptions necessarily lead to the conclusion that is stated in the theorem.
Each step makes sense and provides insights into how the whole system works.
In a sense, the proof doesn't just tell us that the theorem holds, it tells us **why** it holds!
That's very different from experimental models or simulations.
Proofs give us stronger guarantees and deeper insights.
That's powerful stuff!

In light of the unique advantages of proofs, it would be great to see more of them in linguistics.
This does not mean that every linguist suddenly has to start writing proofs.
Nor is it even necessary for all linguists to be able to read and understand existing proofs.
But linguists should strive to state their proposals in sufficiently precise terms that others can study them mathematically and prove things about them.
While writing proofs is a difficult and very specialized skill, it is quite easy to learn enough math to formulate linguistic ideas in mathematical terms.
This book, hopefully, will get you very close to this goal.

## Recap

- Proofs are a powerful tool.
  They give us strong guarantees that specific properties must hold as long as certain conditions are met.
- Proofs are transparent.
  While they may be difficult to read, they are interpretable and tell us why something holds.
- Unless you're already far down the mathematical rabbit hole, odds are you will never write a single proof in your whole life.
  But you should still have an appreciation of why proofs are important.
- It does not take much effort to state a proposal in sufficiently precise terms that enable other researchers to prove deep theorems about it.
