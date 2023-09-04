---
title: Skill Survey (Not Graded)
---

This survey is part of a *pre-post assessment* to determine your mathematical linguistics skills before and after taking the class.
Some questions can be answered with prior training in mathematics, some with prior training in linguistics, some require both.

Answer the questions to the best of your abilities, but do not guess.
If you do not know an answer, just say so and move on to the next question.
It is perfectly fine to do this for every question, this is **not** a test of your ability to pass the class.
Ideally, once the semester is over, you will come back to all these questions and they will strike you as really easy (assuming, of course, that we got to the unit that gives the answer to the question).

## Sets

1.  Suppose $A := \{0, 1\}$, $B := \{1, 2, 3\}$ and $C = A - B$.
    What is $C - (A \cap B)$?

1.  Compute the power set of the empty set (i.e. $\wp(\emptyset)$).

1.  Are natural languages countably infinite? Justify your answer.

1.  What is the smallest positive bigram grammar $G$ over $a$, $b$, and the left and right edge markers such that $G$ generates an infinite string language?
    If there are multiple options that are equally small, list all of them.

1.  What is the smallest negative trigram grammar $G$ over $a$, $b$, and the left and right edge marker such that $G$ generates an infinite string language?
    If there are multiple options that are equally small, list all of them.

1.  Suppose a language allowed words of the form $V\{C,V\}^*V$ or $C\{C,V\}^*C$, where $C$ is any random consonant and $V$ is any random vowel.
    That is to say, words that start with vowels must end with vowels, and words that start with consonants must end with consonants.
    No language works like that.
    This makes sense as this constraint on words is not tier-based strictly local.
    Explain what that means, and how this makes sense of the typological gap.

## Functions and relations

1.  Adjectives in English can be graded, like, *strong* (positive), *stronger* (comparative), and *strongest* (superlative).
    Here all three forms are built from the same stem *strong*, an AAA pattern.
    Some adjectives have a stem change, like *good-better-best* (ABB).
    Curiously, no known language has adjectival gradation patterns like *good-better-goodest* (ABA).
    Explain how this can be derived from the requirement that the mapping from the hierarchy *positive-comparative-superlative* to stems must be monotonic.

1.  For each of the following relations, say whether it is a weak partial order.

    1. set containment
    1. proper subset relation
    1. sister-of (kinship)
    1. sister-of (syntax tree)
    1. proper dominance (syntax tree)
    1. c-command (syntax tree)
    1. $x R y$ iff word $x$ is derivable from word $y$ by substituting 0 or more characters
    1. $x R y$ iff word $x$ is derivable from word $y$ by deleting 0 or more characters

## Logic

1.  Explain why the following formula is (or is not) a tautology: $((a \rightarrow a) \rightarrow a) \rightarrow b$

1.  Explain how English *or* differs from the propositional operator $\vee$.

1.  Are there cases where English *and* differs from the propositional operator $\wedge$? Justify your answer.

1.  Consider the sentence *If Bill is hungry, there's leftovers in the fridge.*
    How does this differ in meaning from the formula $\exists x [\mathrm{Bill}(x) \wedge (\mathrm{hungry}(x) \rightarrow \exists y, z [\mathrm{fridge}(y) \wedge \mathrm{leftovers}(z) \wedge \mathrm{contains}(y, z)])]$.

1.  Write a formula of first-order logic with successor that forces the first and fourth sound of a word (if they exist) to be $a$, $i$, or $u$ unless the word already contains two or more instances of $p$ or $k$.

1.  Resolve the (untyped) lambda-term to its simplest form: $[\lambda x. \lambda f. f(x)]([\lambda f. \lambda g. g(f)](\lambda x. x \neq x)(\lambda x. x))$

1.  Write down the denotion of the English verb *introduce* as a typed lambda expression.


## Automata

1.  Give an example of a non-deterministic finite-state automaton.

1.  Explain why total reduplication is not finite-state.

1.  **Grad students only**:
    Give a finite-state transducer that maps every $1^n$ to $a^n b^*$.
    Give a second transducer that maps every $1^n$ to $a^* b^n$.
    Is the intersection of the corresponding transductions a finite-state transduction?


## Vectors and matrices

1.  Calculate the meaning vector of *when* based on the sentence *When buffalo buffalo buffalo, then buffalo buffalo buffalo, obviously.*

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

1.  Suppose you have a neural network that implements logistic regression.
    It has three input neurons, one output neuron, and the weights connecting the input neurons to the output neuron are as follows:
    
    - first input neuron to output neuron: .25
    - second input neuron to output neuron: .5
    - third input neuron to output neuron: 1

    The neural network uses the sigmoid function as its activation function: $\sigma(x) = \frac{1}{1 + e^{-x}}$.
    What is the output of the neural network for the input vector $(2,1,3)$?

## Graphs (only for grad students)

1.  Define the smallest strongly connected digraph with 3 vertices (where smallest means the digraph with the fewest number of edges).
    You may draw a picture or write down a formal definition.

1.  Syntactic trees are weakly connected digraphs. True or false?
