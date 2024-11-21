---
pagetitle: >-
    Finite-state transductions as transducers
---

# Finite-state transductions as transducers

Our little game may have struck you as a bit silly, but it really captures the essence of finite-state transducers (FSTs).
If you understand how the game is played and what a valid rule sheet may look like, you understand FSTs.
Let us take a closer look.

## From game to transducer

The differences between our game and FSTs are mostly a matter of terminology:

- Instead of finitely many players, we have finitely many **states**.
- Instead of a player getting the next turn, we **transition** from one state to another.

One conceptual difference to our game is that most discussions of FSTs assume that the input is fixed in advance rather than built up as part of the transduction.
But this is immaterial because an FST only gets to look at the input string one symbol at a time, without the ability to make decisions based on what the remainder of the input string looks like.
So the FST behaves pretty much as if the input string were built up incrementally during the transduction process.

Putting these conceptual issues aside, the FST is still playing the game of building an output string based on the shape of the input string.
We also say that the FST **rewrites** the input string as (or into) the output string.
Let us be fully explicit about how this works in the special case where the FST does not have to make any choices and is always able to process the whole input.
Later in this unit, we will discuss the more general case without these simplifying assumptions.

1. The FST starts in a state that is designated as an **initial** state or **start** state.
   (If there are multiple initial states, one is chosen at random.)
1. The FST moves through the **input string** from left to right, reading in one input symbol at a time.
   The current state of the transducer and the current input symbol jointly determine which transition the FST chooses. 
   The transition causes the FST to produce a specific output symbol and switch into a new state.
1. The FST keeps repeating the previous step until it reaches {{{R}}} in the input.
   It takes the transition jointly picked out by {{{R}}} and its current state, and then it stops.
1. The string that the FST has built along the way is the **output string**.

As with games, we can represent FSTs as tables or graphs.
In the table format, rows indicate the current state and columns the state we can switch to when reading a specific input $i$ and producing a corresponding output $o$ (which we write $i:o$).
We also have two special columns that indicate for each state whether it is initial and what its **final** output is (i.e. the output when reading in {{{R}}}).
In the graph format, states are circled **nodes** and transitions are arrows, which we also call **edges**.
Again these edges have labels of the form $i:o$, where $i$ is the input symbol being read and $o$ a string of output symbols.

One brief remark on notation: instead of writing *nothing* as in the previous unit, we will henceforth use the empty string $\emptystring$ to indicate that a transducer outputs nothing.

::: example
Let us look at a mathematical example.
Below is a transducer with two states, $O$ and $E$.

|           |                                    |                              |             |                         |
| --:       | :-:                                | :-:                          | :-:         | :-:                     |
|           | **E**                              | **O**                        | **Initial** | **Final**               |
| **E**     | b:cc                               | a:a                          | Yes         | {{{R}}}:$\emptystring$  |
| **O**     | a:b                                | b:$\emptystring$             | No          | {{{R}}}:$\emptystring$  |


~~~ {.include-tikz size=mid}
oddeven_total.tikz
~~~

Suppose our input string is *abababb{{{R}}}*.
The transducer will read this string from left to right, one symbol at a time, and produce a corresponding output string.
What output symbol is produced depends on the current state and the input symbol (just like in our game, where the output token was determined by the input symbol and the rules of the current player).
We can display this process as a table.

| Current State | Input   | Output          | New State | Remaining input string | Output string built so far |
| :-:           | :-:     | :-:             | :-:       | :--                    | :--                        |
| -             | Start   | -               | E         | abababb{{{R}}}         | -                          |
| E             | a       | a               | O         | bababb{{{R}}}          | a                          |
| O             | b       | $\emptystring$  | O         | ababb{{{R}}}           | a                          |
| O             | a       | b               | E         | babb{{{R}}}            | ab                         |
| E             | b       | cc              | E         | abb{{{R}}}             | abcc                       |
| E             | a       | a               | O         | bb{{{R}}}              | abcca                      |
| O             | b       | $\emptystring$  | O         | b{{{R}}}               | abcca                      |
| O             | b       | $\emptystring$  | O         | {{{R}}}                | abcca                      |
| O             | {{{R}}} | $\emptystring$  | Stop      | -                      | abcca                      |

Alternatively, we can construct the output string by putting our finger on an initial state and then following the path through the FST that is described by the input string.
For example, we start in the initial state $E$, see that the first input symbol is *a*, and hence follow the arrow with input symbol *a* to go to $O$, outputting *a* along the way.
Once in $O$, we see that the next input symbol is *b* and follow the arrow from $O$ that has *b* as an input symbol, which leads us back to $O$.
But since the arrow is labeled $b: \emptystring$, we do not produce any output when doing this.
We keep tracing our path through the FST, and after having read in {{{R}}}, we stop. 

Either way, you can see that the FST produces the output string *abcca* from the input string *abababb*.
:::

::: exercise
Using the FST from the example above, compute the output strings for all of the following inputs:

1. bba{{{R}}}
1. aaaaa{{{R}}}
1. abbb{{{R}}}

::: solution
1. cccca
1. ababa
1. a
:::
:::

Upon closer inspection of the example above, we can deduce what kind of rewrite process its FST is implementing:

1. The states $E$ and $O$ keep track of whether, so far, we have seen an even or an odd number of *a*s in the input.
1. Every other *a* (i.e. every *a* after an odd number of *a*s) is rewritten as *b*.
1. If a *b* occurs after we have seen an odd number of *a*s, we delete it.
   If it occurs after we have seen an even number of *a*s, we replace it with *cc*.
1. We do not change anything else.

::: exercise
Define an FST that implements the following rewrite process, assuming that input strings may contain the symbols, *a*, *b*, or *c*:

1. If the string starts with *a*, rewrite all subsequent instances of *a* as *aa*.
1. If the string starts with *b*, delete all subsequent instances of *b*.
1. Do not change anything else.

::: solution

The FST looks as follows

|           |           |                          |                              |               |             |                              |
| --:       | :-:       | :-:                      | :-:                          | :-:           | :-:         | :-:                          |
|           | **0**     | **A**                    | **B**                        | **C**         | **Initial** | **Final**                    |
| **0**     |           | a:a                      | b:b                          | c:c           | Yes         | {{{R}}}:$\emptystring$       |
| **A**     |           | a:aa, b:b, c:c           |                              |               | No          | {{{R}}}:$\emptystring$       |
| **B**     |           |                          | a:a, b:$\emptystring$        |               | No          | {{{R}}}:$\emptystring$       |
| **C**     |           |                          |                              | a:a, b:b, c:c | No          | {{{R}}}:$\emptystring$       |

::: solution_explained
We have four distinct states:

- *0* is the starting state.
  Depending on the first symbol of the string, we transition into one of the other three states.
- *A*: the first symbol was *a*; from here on out, we rewrite *a* as *aa* but do not change *b* or *c*.
- *B*: the first symbol was *b*; from here on out, we delete *b* but do not change *a* or *c*.
- *C*: the first symbol was *c*; from here on out, we do not change *a* or *b* or *c*.

The FST can stop in any state.
This includes *0* because this FST should be able to take the empty string as an input, too.
:::
:::
:::

## When the transduction fails

As hinted at above, our description of FSTs is more restricted than usual.
We assume that the FST is **total** and **deterministic**.
Let us look at total first, leaving determinism for the next section.

An FST is **total** iff there is a suitable transition for every combination of a state and an input symbol.
This means that the FST can never find itself in a situation where it cannot take any transitions.
To put it bluntly: total transducers cannot get stuck.

::: example
Consider the minimally different FST where $E$ lacks a transition for input symbol {{{R}}}.

|           |                                    |                              |             |                         |
| --:       | :-:                                | :-:                          | :-:         | :-:                     |
|           | **E**                              | **O**                        | **Initial** | **Final**               |
| **E**     | b:cc                               | a:a                          | Yes         | -                       |
| **O**     | a:b                                | b:$\emptystring$             | No          | {{{R}}}:$\emptystring$  |

~~~ {.include-tikz size=mid}
oddeven.tikz
~~~

This transducer is not total because it can get stuck.

Consider what happens when this FST has to process the input string *abababba{{{R}}}*.
This is almost exactly the same as the input *abababb{{{R}}}* from the previous example, but with an extra *a* at the end.
Mirroring the previous example, the transducer will be in state $O$ after it processes the last *b* of *abababba{{{R}}}*.
But now it has to read in one more *a* before it reaches {{{R}}}.
We do have a transition out of $O$ with *a* as the input symbol, so the FST is not stuck.
This transition causes the FST to output *b* and switch to state $E$.
But this is where things go wrong.
Next we read in {{{R}}}, and since $E$ is not a final state, it does not have an outgoing edge with {{{R}}} as the input symbol.
The FST gets stuck and fails to process the whole input.
<!-- The FST gets stuck, right before the finish line, and our beautiful output string *abccab* is simply flushed down the drain. -->
:::

::: exercise
Removing the {{{R}}}:$\emptystring$ transition from $E$ as in the example above imposes a specific requirement on input strings.
What is this requirement that an input string must satisfy so that the FST produces an output for it?

::: solution
The input string must contain an odd number of *a*s.
:::
:::

::: example
Now suppose that the FST from the previous example receives the input string *acbababb{{{R}}}*, with a *c* after the first *a*.
At first things are fine.
We start in the initial state $E$ and transition to state $O$ by reading in *a* and outputting *a*.
But then we are stuck.
The next symbol in the input is *c*, but there is no transition out of our current state $O$ that has *c* as its input symbol.
Without a valid transition, the transducer cannot continue processing the input string
<!-- and we have to discard the output string built so far. -->
<!-- The input string is not mapped to any output whatsoever, not even a partial output. -->
:::

If an FST gets stuck when processing some input string $i$, then it does not produce any output for $i$ at all.
This is very important.
It does not produce a partial output, nor does it give a warning that no output was produced, nor does it output the empty string.
A stuck FST simply produces no output at all.
So if an FST isn't total, there will be input strings that have no output at all.

::: exercise
Using the FST from the previous example, compute the output strings for all the inputs below.
If no output is produced, say so.

1. a{{{R}}}
1. bb{{{R}}}
1. {{{R}}}

::: solution
1. a
1. no output
1. no output
:::
:::

When a transducer isn't total, one often uses the term **final state** to refer to a state with a transition of the form ${{{R}}}:o$.
But even if all states of an FST are final, that still does not mean that the FST is total.

::: exercise
Explain why this holds.

::: solution
An FST can get stuck even if all states are final.
If the current input symbol is $i$ and the FST has no transition $i:o$ from its current state, then the FST gets stuck and won't produce any output for the input. 
:::
:::

## Non-determinism

You might remember that our game sometimes gave players a choice as to what they want to do.
This is also possible with FSTs, and such an FST with choice points is called **non-deterministic**.
This is in contrast to an FST without such choice points, which is **deterministic**.
There are two ways non-determinism can arise.
Either an FST has more than one initial state, or there is at least one state with two outgoing transitions that are both compatible with the current input.

::: example
Consider once more the transducer from the previous example, where $E$ is not a final state, but suppose that both E and O are now initial states.

|           |                                    |                              |             |                         |
| --:       | :-:                                | :-:                          | :-:         | :-:                     |
|           | **E**                              | **O**                        | **Initial** | **Final**               |
| **E**     | b:cc                               | a:a                          | Yes         | -                       |
| **O**     | a:b                                | b:$\emptystring$             | Yes         | {{{R}}}:$\emptystring$  |

~~~ {.include-tikz size=mid}
oddeven_fullyinitial.tikz
~~~

Then there are two distinct paths we could take through the FST in an effort to rewrite the input string *abababb{{{R}}}*.
If we start in *E*, things work out as in the first example, yielding *abcca*.
If we start with *O*, things go differently.

| Current State | Input   | Output          | New State | Remaining input string | Output string built so far |
| :-:           | :-:     | :-:             | :-:       | :--                    | :--                        |
| -             | Start   | -               | O         | abababb{{{R}}}         | -                          |
| O             | a       | b               | E         | bababb{{{R}}}          | b                          |
| E             | b       | cc              | E         | ababb{{{R}}}           | bcc                        |
| E             | a       | a               | O         | babb{{{R}}}            | bcca                       |
| O             | b       | $\emptystring$  | O         | abb{{{R}}}             | bcca                       |
| O             | a       | b               | E         | bb{{{R}}}              | bccab                      |
| E             | b       | cc              | E         | b{{{R}}}               | bccabcc                    |
| E             | b       | cc              | E         | {{{R}}}                | bccabcccc                  |
| E             | {{{R}}} |                 | STUCK!!!  | -                      | -                          |

Starting with *O* instead of *E* made it impossible to reach a final state and the output was aborted.
Hence this is a case where we have a choice point in the FST, but only one of the choices works out eventually.

If we tweaked the FST so that both *O* and *E* are final states, then starting with *O* would also be a valid option.
In this case, the FST can produce two distinct outputs for *abababb{{{R}}}*, one being *abcca* (when we start in *E*) and the other being *bccabcccc* (when we start in *O*).
:::

::: example
Consider yet another variant of the transducer from the first example of this unit.
Now $E$ is the only initial state and $O$ is the only final state, but there are also two more transitions from *O* to *E* --- one with *a:a*, the other with *b:cc*.

|           |                                    |                              |             |           |
| --:       | :-:                                | :-:                          | :-:         | :-:       |
|           | **E**                              | **O**                        | **Initial** | **Final** |
| **E**     | b:cc                               | a:a                          | Yes         | -         |
| **O**     | a:a, a:b, b:cc                     | b:$\emptystring$             | No          | {{{R}}}:$\emptystring$   |

~~~ {.include-tikz size=mid}
oddeven_extended.tikz
~~~

Now when we are in state *O*, we have multiple choice points.
When we are in *O* and get *a* in the input, we still can only move to *E*, but this *a* may be rewritten as *a* or as *b*.
And if we are in *O* and see a *b* in the input, we may either rewrite is as *cc* and go to *E*, or we may delete is as before and stay in *O*.
For example, it now is possible to rewrite *abababb{{{R}}}* as
*accacca*.
:::

::: exercise
Write down all the output strings that the FST above can produce from the input *abababb{{{R}}}*.
Keep in mind that the FST is not total and thus may get stuck.

::: solution
1. aacca
1. abcca
1. accacca

::: solution_explained
The easiest way to keep track of all options is via a graph that tracks each run of the non-deterministic FST.
This graph will have the shape of a tree, where nodes correspond to states and branches represent specific transitions taken by the FST.

~~~ {.include-tikz size=mid}
nfst_treeunfolding.forest
~~~

In order to get all the outputs, one simply has to follow all the branches that lead from the top of the tree to the final transition ${{{R}}}:\emptystring$.
For each branch, we read the output symbols from top to bottom to get the output string produced by the FST when it takes the sequence of transitions described by that branch.
:::
:::
:::

The examples above show that non-determinism can lead to multiple outputs for a single input string, but that does not always happen because some of the available choices may cause the transducer to get stuck.
Either way you might be wondering how the FST decides which routes to pursue.
The short answer is that it doesn't really matter for us because almost all our transducers will be deterministic (more on that in a second).

If you're still curious about non-determinism, read on.
Mathematically, it is convenient to assume that the transducer doesn't make any choices at all and instead explores all options in parallel.
Whenever there is a choice point, all possible continuations will be explored.
For practical implementations, this requires a bit of ingenuity because the number of possible outputs can grow exponentially.
Still, one can think of such non-deterministic FSTs as producing not a single string but rather a **prefix tree** that encodes all possible outputs.
We will encounter **prefix trees** in a later unit when we discuss phonological parsing.

<!-- ::: example -->
<!-- Consider once more the FST from the previous example, repeated here. -->
<!--  -->
<!-- |           |                                    |                              |             |           | -->
<!-- | --:       | :-:                                | :-:                          | :-:         | :-:       | -->
<!-- |           | **E**                              | **O**                        | **Initial** | **Final** | -->
<!-- | **E**     | b:cc                               | a:a                          | Yes         | -         | -->
<!-- | **O**     | a:a, a:b, b:cc                     | b:$\emptystring$             | No          | {{{R}}}:$\emptystring$   | -->
<!--  -->
<!-- ~~~ {.include-tikz size=mid} -->
<!-- oddeven_extended.tikz -->
<!-- ~~~ -->
<!--  -->
<!-- Below is a prefix tree that encodes all the possible outputs of fixme -->
<!-- ::: -->

## Subclasses of finite-state transducers

In contrast to the description at the beginning of this unit, the default definition of FSTs does not require them to be total or deterministic.
But in the next unit, we will try to use FSTs to capture a variety of phonological phenomena, and we will see that these FSTs are total and deterministic.
It is only when we push FSTs beyond the immediate task of handling phonological mappings that determinism and totality become too restrictive.
This is a surprising state of affairs, but it once again points towards language being remarkably simple.

So unless stated otherwise, we will henceforth assume that our FSTs are both total and deterministic.
This means that there is exactly one initial state and every state has exactly one outgoing edge for every input symbol (including {{{R}}}).

## Recap

- **Finite-state transducers** (FSTs) are a formal model of how input strings can be mapped to output strings.
  We also say that an FST **rewrites** the input string.
- We assume that every input string ends with the distinguished symbol {{{R}}}.
- Every FST consists of finitely many states.
  The states are connected by **transitions** of the form $i:o$, where $i$ is an input symbol (or the empty string) and $o$ is a string of 0 or more output symbols.
- States may be initial and/or final.
    - **initial**: the FST can start in this state when processing a string
    - **final**: the state has a transition of the form ${{{R}}}:o$
- The FST processes an input string symbol by symbol, moving from left to right.
  When the FST is in state $q$ and the current input symbol is $i$, the FST follows a transition $i:o$ from $q$ and $o$ is added to the output string built so far.
- If there is no suitable transition, the FST is stuck and no output is produced.
- An FST is **non-deterministic** if there are choice points (multiple initial states and/or multiple applicable transitions).
  Otherwise it is **deterministic**.
- An FST is **total** iff it produces at least one output string for every possible input string.
- A **total deterministic FST** has exactly one initial state and every state of the FST must have a transition $i:o$ for every input symbol $i$ (including {{{R}}}).

\includecollection{solutions}
