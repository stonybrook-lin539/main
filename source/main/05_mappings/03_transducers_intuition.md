---
pagetitle: >-
    Finite-state transductions as transducers
---

# Finite-state transductions as transducers

Our little game may have struck you as a bit silly, but it really captures the essence of finite-state transducers (FSTs).
If you understand how the game is played and what a valid rule sheet may look, you understand FSTs.
Let us take a closer look.

## From game to transducer

The differences between our game and FSTs are mostly a matter of terminology:

- Instead of finitely many players, we have finitely many **states**.
- Instead of a player getting the next turn, we **transition** from one state to another.

One conceptual difference is that most discussions of FSTs assume that the input is fixed in advance rather than built up as part of the transduction.
But this is immaterial because an FST only gets to look at the input string one symbol at a time, without the ability to make decisions based on what the remainder of the input string looks like.
So the FST behaves pretty much as if the input string were built up incrementally during the transduction process.

Putting these conceptual issues aside, the FST is still playing the game of building an output string based on the shape of the input string.
We also say that the FST **rewrites** the input string as (or into) the output string.
It moves through the input string left to right and stops immediately after reading in {{{R}}}.

::: example
Let us look at a mathematical example.
Below is a transducer with two states, $O$ and $E$.
Again we use the table format with rows representing the current state and columns the state we can switch to when reading a specific input and producing a corresponding output.
Instead of writing *nothing*, we use the empty string $\emptystring$ to indicate that a transducer outputs nothing.
And we once again indicate whether a state is initial, final, neither, or both.

|           |                                    |                              |             |           |
| --:       | :-:                                | :-:                          | :-:         | :-:       |
|           | **E**                              | **O**                        | **Initial** | **Final** |
| **E**     | b:cc                               | a:a                          | Yes         | No        |
| **O**     | a:b                                | b:$\emptystring$             | No          | Yes       |

Once again we can also represent this as a graph.
Since we use $\emptystring$ instead of *nothing*, final states have an outgoing edge labeled ${{{R}}}:\emptystring$.

~~~ {.include-tikz size=mid}
oddeven.tikz
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
For example, we start in the initial state, see that the first input symbol is *a*, and hence follow the arrow with input symbol *a* to go to $O$, outputting *a* along the way.
Once in $O$, we see that the next input symbol is *b* and follow the arrow from $O$ that has *b* as an input symbol, which leads us back to $O$.
But since the arrow is labeled $b: \emptystring$, we do not produce any output when doing this.
We keep tracing our path through the FST, and after having read in {{{R}}}, we stop. 

Either way, you can see that the FST produces the output string *abcca* from the input string *abababb*.
:::

::: exercise
Using the FST from the first example of this unit, compute the output strings for all of the following inputs:

1. bba{{{R}}}
1. aaaaa{{{R}}}
1. abbb{{{R}}}
:::

Upon closer inspection of the FST, we can deduce what kind of rewrite process it is implementing:

1. The states $E$ and $O$ keep track of whether, so far, we have seen an even or an odd number of *a*s in the input.
1. Every other *a* (i.e. every *a* after an odd number of *a*s) is rewritten as *b*.
1. If a *b* has an odd number of *a*s, we delete it, and otherwise we replace it with *bb*.
1. Do not change anything else.

::: exercise
Define an FST that implements the following rewrite process, assuming that input strings may contain the symbols, *a*, *b*, or *c*:

1. If the string starts with *a*, rewrite all subsequent instances of *a* as *aa*.
1. If the string starts with *b*, delete all subsequent instances of *b*.
1. Do not change anything else.
:::

## When the transduction fails

The FST also enforces two secret rules that have escaped our attention so far.

4. The input string must only contain *a* or *b*.
5. The input must contain an odd number of *a*s.

Both secret rules follow from the fact that the transducer would get stuck in the input otherwise.
And if a transducer cannot process the entire input, it does not produce any output at all.

::: example
Suppose that the input string in the example above weren't *abababb{{{R}}}* but rather *acbababb{{{R}}}*.
At first things are fine.
We start in the initial state $E$ transition to state $O$ by reading in *a* and outputting *a*.
But then we are stuck.
The next symbol is *c*, but there is no transition out of our current state $O$ that has *c* as its input symbol.
Since the transducer cannot make its way through the whole input string, we discard the output string built so far.
The input string is not given any output whatsoever, not even a partial output.
:::

The second secret rule is a consequence of the same issue.
If the transducer is in some non-final state while reading in {{{R}}}, it gets stuck because there is no suitable edge out of that state.
Once again the whole output string built so far is discarded.

::: example
Suppose that the input string in the example above weren't *abababb{{{R}}}* but rather *abababba{{{R}}}*.
Rather than ending in state $O$ after the last *b*, we now have to read in one more *a*.
We do have a transition out of $O$ with *a* as the input symbol, so the FST is not stuck.
This transition causes the FST to output *b* and switch to state $E$.
But this is where things go wrong.
Next we read in {{{R}}}, and since $E$ is not a final state, it does not have an outgoing edge with {{{R}}} as the input symbol.
The FST gets stuck, right before the finish line, and our beautiful output string *abccab* is simply flushed down the drain.
:::

::: exercise
Using the FST from the first example of this unit, compute the output strings for all the inputs below.
If no output is produced, say so.

1. a{{{R}}}
1. bb{{{R}}}
1. {{{R}}}
:::

Given an FST and input string, then, it is not enough to trace the path that this input describes through the transducer, we also have to check that we do not get stuck.
The FST produces an output string if and only if it can make it all the way through the input string without getting stuck.

## Non-determinism

You might remember that our game sometimes gave players a choice as to what they want to do.
This is also possible with FSTs, and such an FST with choice points is called **non-deterministic**.
This is in contrast to an FST without such choice points, which is **deterministic**.
There are two ways non-determinism can arise.
Either an FST has more than one initial state, or there is at least one state with two outgoing transitions that are both compatible with the current input.

::: example
Consider once more the transducer from the first example of this unit, but suppose that both E and O are initial states.
Then there are two distinct paths we could take through the FST in an effort to rewrite the input string *abababb{{{R}}}*.
If we start in *E*, things pass out as in the first example, yielding *abcca*.
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
Consider once more the transducer from the first example of this unit, but suppose that we add two more transitions from *O* to *E* --- one with *a:a*, the other with *b:cc*.

|           |                                    |                              |             |           |
| --:       | :-:                                | :-:                          | :-:         | :-:       |
|           | **E**                              | **O**                        | **Initial** | **Final** |
| **E**     | b:cc                               | a:a                          | Yes         | No        |
| **O**     | a:a, a:b, b:cc                     | b:$\emptystring$             | No          | Yes       |

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
Keep in mind that the FST must be in a final state when reading {{{R}}}.
:::

The examples above show that non-determinism can lead to multiple outputs for a single input string, but does not need to as some of the available choices may cause the transducer to get stuck.
Either way you might be wondering how the FST decides which routes to pursue.
The short answer is that it simply doesn't.
When there are multiple choices, we assume that the FST tries each one of them.
This is a simplification, but it is an acceptable one because we aren't really interested in practical implementations of FSTs, we want to use FSTs as a model of how underlying representation can be mapped to one or more surface forms.
We want to know the relation between underlying representations and surface forms, not so much how one actually makes this work in practice.

If you find that unsatisfying, feel free to assume the following:
when the FST reaches a point with, say, three choices, we temporarily halt the FST, make two copies of it, and then have each one of those three FSTs try a different one of those three choices.
When one of them reaches another choice point, we do the same thing, and so on.
If we keep doing this, we are guaranteed for each possible output to discover it eventually.

## Subclasses of finite-state transducers

This unit presented FSTs in full generality.
In the next unit, we will see how FSTs allow us to capture a variety of phonological phenomena, and curiously, we won't need the full power of FSTs for that.
In general, we will be able to work with FSTs that meet all of the following conditions:

1. They are deterministic.
   Hence there is only one initial state, and no state has two or more outgoing edges that can simultaneously match the input.
1. They are **total**, which means that we don't have to worry about getting stuck.
   Every state has an outgoing edge for every possible input symbol, including {{{R}}} (which means that every state is final).
  
It is only when we push FSTs beyond the immediate task of handling phonological mappings that non-determinism and non-final states become essential.
This is a surprising state of affairs that once again points towards language being remarkable simple.

## Recap

- A **finite-state transducer** (FST) consists of finitely many states.
  The states are connected by **transitions** of the form $i:o$, where $i$ is an input symbol (or the empty string) and $o$ is a string of 0 or more output symbols.
- States may be initial and/or final.
- The FST moves through an input string from left to right.
  When the FST is in state $q$ and the current input symbol is $i$, the FST follows a transition $i:o$ from $q$ and $o$ is added to the output string built so far.
- If there is no suitable transition, the FST is stuck and no output is produced.
- We assume that every input string ends with the distinguished symbol {{{R}}}.
- An FST is **non-deterministic** if there are choice points (multiple initial states and/or multiple applicable transitions).
  Otherwise it is **deterministic**.
