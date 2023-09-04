---
title: Skill Survey (Not Graded)
---

This survey is part of a *pre-post assessment* to determine your mathematical linguistics skills before and after taking the class.
Answer the questions to the best of your abilities, but do not guess.
If you do not know an answer, just skip the question.
Even skipping all questions is perfectly fine, this is **not** a test of your ability to pass the class.

1.  Are natural languages infinite? Justify your answer.

1.  Are natural languages countably infinite? Justify your answer.

1.  For each of the following relations, say whether it is a weak partial order.

    1. set containment
    1. proper subset relation
    1. sister-of (kinship)
    1. sister-of (syntax tree)
    1. proper dominance (syntax tree)
    1. c-command (syntax tree)
    1. $x R y$ iff word $x$ is derivable from word $y$ by substituting 0 or more characters
    1. $x R y$ iff word $x$ is derivable from word $y$ by deleting 0 or more characters

1.  Compute the power set of the power set of the empty set (i.e. $\wp(\wp(\emptyset))$).

1.  Give a picture-based proof of De Morgan's law.

1.  Explain why the following formula is (or is not) a tautology: $((a \rightarrow a) \rightarrow a) \rightarrow b$

1.  Explain how English *or* differs from the propositional operator $\vee$.

1.  Are there cases where English *and* differs from the propositional operator $\wedge$? Justify your answer.

1.  Consider the sentence *If Bill is hungry, there's leftovers in the fridge.*
    How does this differ in meaning from the formula $\exists x [\mathrm{Bill}(x) \wedge (\mathrm{hungry}(x) \rightarrow \exists y, z [\mathrm{fridge}(y) \wedge \mathrm{leftovers}(z) \wedge \mathrm{contains}(y, z)])]$.

1.  Write a formula of first-order logic with successor that enforces the first and fourth sound of a word (if they exist) to be $a$, $i$, or $u$ unless the word already contains two or more instances of $p$ or $k$.

1.  Resolve the (untyped) lambda-term to its simplest form: $[\lambda x. \lambda f. f(x)]([\lambda f. \lambda g. g(f)](\lambda x. x \neq x)(\lambda x. x))$

1.  Write down the denotion of the English verb *introduce* as a typed lambda expression.

1.  Calculate the result of the matrix multiplication below (if this isn't possible, say so):

    $$
    \begin{bmatrix}
    1 & 2 & 3\\
    3 & 2 & 1\\
    \end{bmatrix}
    \times
    \begin{bmatrix}
    3 & 1 & 2\\
    1 & 3 & 2\\
    \end{bmatrix}
    $$

1.  Calculate the result of the matrix multiplication below (if this isn't possible, say so):

    $$
    \begin{bmatrix}
    1 & 2 & 3\\
    3 & 2 & 1\\
    \end{bmatrix}
    \times
    \begin{bmatrix}
    3 & 1\\
    1 & 3\\
    2 & 2\\
    \end{bmatrix}
    $$

1.  Calculate the meaning vector of *when* based on the sentence *When buffalo buffalo buffalo, then buffalo buffalo buffalo, obviously.*

1.  Draw the smallest strongly connected digraph with 3 vertices (where smallest means the digraph with the fewest number of edges).

1.  Syntactic trees are weakly connected digraphs. True or false?

1.  Give a finite-state transducer that maps every $1^n$ to $a^n b^*$.
    Give a second transducer that maps every $1^n$ to $a^* b^n$.
    Is the intersection of the corresponding transductions a finite-state transduction?

1.  Explain why total reduplication is not finite-state.

1.  Let $G$ be a PCFG with the following rules:

    - 1.0: S $\rightarrow$ NP VP
    - 0.8: NP $\rightarrow$ A N
    - 0.2: NP $\rightarrow$ V ing N
    - 0.4: VP $\rightarrow$ can VP
    - 0.4: VP $\rightarrow$ V NP
    - 0.2: VP $\rightarrow$ V A
    - A $\rightarrow$ flying
    - A $\rightarrow$ dangerous
    - N $\rightarrow$ planes
    - V $\rightarrow$ fly
    - V $\rightarrow$ be

    Ignoring lexical frequency, calculate the probability for each one of the two readings of *flying planes can be dangerous* (i.e. *planes that fly can be dangerous* and *it can be dangerous to fly planes*).

1.  Give an example of a monoid.

1.  Is $\langle \wp(\Sigma^n), \cup, -, \emptyset, \Sigma^n \rangle$ a semiring? Why (not)?
