---
pagetitle: >-
    Phonological processes as transductions (Solutions)
---

# Phonological processes as transductions (Solutions)

::: exercise
Many language do not like consonant clusters of three or more consonants in a row.
Using the strategy illustrated above, construct an FST that deletes all consonants in a cluster except the first two.
For the sake of simplicity, assume that the input alphabet only consists of C for consonants and V for vowels.
For example, you may have the input string CCVCCCCV, and it should be rewritten as CCVCCV.

::: solution

|           |                   |               |                   |             |           |
| --:       | :-:               | :-:           | :-:               | :-:         | :-:       |
|           | **0**             | **1**         | **2**             | **Initial** | **Final** |
| **0**     | V:V               | C:C           |                   | Yes         | Yes       |
| **1**     | V:V               |               | C:C               | Yes         | Yes       |
| **2**     | V:V               |               | C:$\emptystring$  | Yes         | Yes       |

:::

::: solution_explained
We have three states, called *0*, *1*, and *2*, which keep track of the number of consecutive consonants seen so far.
Since seeing a V disrupts a consonant cluster, V transitions always move us back to *0*.
Cs increase the length of the cluster, which is why C transitions move us from 0 to 1 and from 1 to 2.
Once we are in two, all subsequent Cs must be the $n$-th C of a cluster, where $n > 2$.
Hence we delete all those Cs.
:::

:::

::: exercise
Explain in your own words how this non-deterministic FST ensures that *t* is rewritten as *p* iff it occurs immediately before *b*.

::: solution
Whenever the FST ecounters a *t*, it has two options: keep *t* as is and move to state *T*, or rewrite *t* as *p* and move to state *P*.
But *P* is not a final state, and the only way out of it is to rewrite *b* as *b*.
This ensures that *t* is rewritten as *p* only if it is followed by *b* --- otherwise, the FST gets stuck in state T.
At the same time, there is no *b:b* transition out of state *T*.
If the FST is in state *T* and encounters *b*, it gets stuck.
This ensures that the FST cannot rewrite *t* as *t* if *t* is followed by *b*.
:::

:::

::: exercise
For each one of the following input strings, compute the output produced by the FST above.

1. xxptbx
1. txptbx
1. txptttbx

::: solution
1. xxppbx
1. txppbx
1. txpttpbx
:::
:::

::: exercise
What is the role of the transition *t:t* from state *T* to *T*?

::: solution
When we encounter multiples instances of *t* in a row, only the last one should be rewritten as *p* if followed by *b*.
But we have already delayed output of the first *t* in that sequence.
If we have delayed *t* and encounter another *t*, we need to reinsert the former.
At the same time, we have to delay output of the latter *t* because it might be rewritten as *p*.
This combination of reinserting one *t* while delaying the other means that we are writing exactly one *t*.
But this whole process was triggered by reading in a *t*, so the whole transition is *t:t*.

We can make all of this more intuitive by using **origin semantics** to indicate how the parts of a given output string are produced from specific pieces of the input string.

|
| --:               | :--   | :--            | :-- | :-- | :-- |
| **Input string**  | x     | t              | t   | t   | x   |
| **Output string** | x     | $\emptystring$ | t   | t   | tx  |

Notice how both the input and the output contain three instances of *t*, but the first *t* in the output actually corresponds to the second *t* in the input.
The last *t* in the output does not correspond to any *t* in the input, it is part of the output obtained from the final *x*.
This isn't very intuitive, but it is an unavoidable artefact of the delayed output strategy.
:::
:::

::: exercise
In a previous chapter, we encountered the process of word-final devoicing in German.
Inspired by this phenomenon, define an FST that uses the delayed output strategy and the final emission trick in order to replace word-final *z* with *s* and word-final *v* with *f*.
You may write a table or draw a graph.

::: solution

|            |                   |                  |                  |             |                     |
| --:        | :-:               | :-:              | :-:              | :-:         | :-:                 |
|            | **0**             | **z**            | **v**            | **Initial** | **Final**           |
| **0**      | x:x               | z:$\emptystring$ | v:$\emptystring$ | Yes         | Yes($\emptystring$) |
| **z**      | x:zx              | z:z              | v:z              | No          | Yes(s)              |
| **v**      | x:vx              | z:v              | v:v              | No          | Yes(f)              |

:::
:::

::: exercise
The process of intervocalic voicing is also familiar from an earlier chapter.
Suppose that *s* is subject to intervocalic voicing::
$\mathrm{s} \rightarrow \mathrm{z} \mid \mathrm{V} \_ \mathrm{V}$.
You may assume that the only input symbols are *s*, *z*, *x*, and *V* (and of course {{{R}}}).
Define an FST for intervocalic voicing.
You may write a table or draw a graph.

Does your FST use the delayed output strategy?
What about the final emission trick?

::: solution

The FST uses the delayed output strategy to postpone the output of *s* after *V*.
It also uses the final emission track to handle *Vs* sequences at the end of the string.

|            |                   |                  |                   |             |                     |
| --:        | :-:               | :-:              | :-:               | :-:         | :-:                 |
|            | **0**             | **V**            | **Vs**            | **Initial** | **Final**           |
| **0**      | s:s, z:z, x:x     | V:V              |                   | Yes         | Yes($\emptystring$) |
| **V**      | z:z, x:x          | V:V              | s:$\emptystring$  | No          | Yes($\emptystring$) |            
| **Vs**     | s:ss, z:sz, x:sx  | V:zV             |                   | No          | Yes(s)              |

:::

:::

::: exercise
The delayed output strategy does not work if the conditioning context can be arbitrarily far to the right of the target.
Suppose, for instance, that *t* would become *p* if there is a *b* somewhere to the right of *t*, no matter how far apart the two are.
This cannot be captured with the delayed output strategy.
Explain why!

::: solution
If we delay the output of *t*, then we also have to delay the output all the symbols that follow *t* until we have made a decision about how to rewrite *t*.
But if the trigger for rewriting *t* can be arbitrarily far away, we have to be able to delay an unbounded number of symbols.
FSTs cannot do that.
We need a separate state for every separate sequence of symbols whose output we have delayed so that we can correctly insert the output of all those symbols once the trigger has been encountered.
But FSTs can only have a finite number of states, which means that we can only memorize a finite number of distinct sequences.
This is a problem because with no fixed upper bound on how far the trigger can be from the target, there are infinitely many sequences of such delayed outputs.
:::

:::

::: exercise
Continuing the previous exercise, can you imagine a way to handle such regressive long-distance phenomena with an FST?

::: solution
We could allow the FST to process the input string from right-to-left.
Then this becomes a case of progressive assimilation, which is very easy to handle.

However, this strategy does not work for phenomena where the target must be surrounded by two elements, one arbitrarily far to its left, one arbitrarily far to its right.
An example of that would be unbounded tone plateauing.
:::

:::


::: exercise
For each one of the URs below, compute the corresponding surface form.
Don't forget to add {{{R}}} at the end of the input string.

1. xBxxM
1. MxxBxxBxxM
1. MxxxxxxxxB

::: solution
1. xBxxB
1. MxxMxxMxxM
1. MxxxxxxxxM
:::

:::

::: exercise
The high dark vowels (H) are neutral vowels.
They can occur together with B or M, and they do not undergo vowel harmony.
That is to say, H stays H.
Revise the FST above so that it also handles H correctly.

::: solution

|           |          |                    |                     |             |                     |
| --:       | :-:      | :-:                | :-:                 | :-:         | :-:                 |
|           | **0**    | **B**              | **M**               | **Initial** | **Final**           |
| **0**     | x:x, H:H | B:B                | M:M                 | Yes         | Yes($\emptystring$) |
| **B**     |          | B:B, M:B, H,H x:x  |                     | No          | Yes($\emptystring$) |
| **M**     |          |                    | B:M, M:M, H:H, x:x  | No          | Yes($\emptystring$) |

:::

:::

::: exercise
Suppose that vowel harmony were not iterative.
That is to say, the first vowel only controls the harmony for the second vowel, after that the third vowel controls the harmony for the fourth vowel, and so on.
For instance, *xBxMxMxB* would come out as *xBxBxMxM*.
Modify the FST above so that it captures this pattern.

::: solution

There are two solutions depending on how one interprets the exercise.
If it really should be such that vowel harmony applies in pairs, then we get the FST below.

|           |          |                    |                     |             |                     |
| --:       | :-:      | :-:                | :-:                 | :-:         | :-:                 |
|           | **0**    | **B**              | **M**               | **Initial** | **Final**           |
| **0**     | x:x      | B:B                | M:M                 | Yes         | Yes($\emptystring$) |
| **B**     | B:B, M:B | x:x                |                     | No          | Yes($\emptystring$) |
| **M**     | B:M, M:M |                    | x:x                 | No          | Yes($\emptystring$) |

If instead we take the exercise to say that vowel harmony cannot alter more than one vowel in a row, then we get the FST below.

|           |          |                    |                     |             |                     |
| --:       | :-:      | :-:                | :-:                 | :-:         | :-:                 |
|           | **0**    | **B**              | **M**               | **Initial** | **Final**           |
| **0**     | x:x      | B:B                | M:M                 | Yes         | Yes($\emptystring$) |
| **B**     | M:B      | B:B, x:x           |                     | No          | Yes($\emptystring$) |
| **M**     | B:M      |                    | M:M, x:x            | No          | Yes($\emptystring$) |

:::

:::

::: exercise
Now suppose that vowel harmony is even more restricted so that harmony never involves more than the first two vowels in the word.
For example, *xBxMxMxB* would now come out as *xBxBxMxB*.
Modify the FST above so that it captures this pattern.

::: solution

|           |          |                    |                     |             |             |                     |
| --:       | :-:      | :-:                | :-:                 | :-:         | :-:         | :-:                 |
|           | **0**    | **B**              | **M**               | **1**       | **Initial** | **Final**           |
| **0**     | x:x      | B:B                | M:M                 |             | Yes         | Yes($\emptystring$) |
| **B**     |          | x:x                |                     | B:B, M:B    | No          | Yes($\emptystring$) |
| **M**     |          |                    | x:x                 | B:M, M:M    | No          | Yes($\emptystring$) |

:::

:::

::: exercise
Slovenian has a version of sibilant harmony that is similar to Samala, except that harmony is blocked by an intervening *t*.
That is to say, the first sibilant after a *t* does not need to be harmonic with any of the sibilants to its left, but the sibilants to its right must be harmonic with that sibilant (unless another *t* intervenes).
Hence we get the following mappings between URs and surface forms:

- *xxsxxʃ* becomes *xxsxxs*
- *xxstxʃ* becomes *xxstxʃ*
- *xxstxʃxs* becomes *xxstxʃxʃ*
- *xxstxʃts* becomes *xxstxʃts*

Modify the FST above so that it incorporates blocking by *t*.

::: solution

|           |           |                |                |             |                     |
| --:       | :-:       | :-:            | :-:            | :-:         | :-:                 |
|           | **0**     | **ESS**        | **ESH**        | **Initial** | **Final**           |
| **0**     | t:t, x:x  | s:s            | ʃ:ʃ            | Yes         | Yes($\emptystring$) |
| **ESS**   | t:t       | s:s, ʃ:s, x:x  |                | No          | Yes($\emptystring$) |
| **ESH**   | t:t       |                | s:ʃ, ʃ:ʃ, x:x  | No          | Yes($\emptystring$) |

:::

:::
