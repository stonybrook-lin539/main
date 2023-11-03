---
pagetitle: >-
    Phonological processes as transductions
---

# Phonological processes as transductions

We have spent a fair amount of time on FSTs by now, but we still haven't seen a truly compelling reason for using them as a formal model of phonology.
So far, our only observation has been that FSTs allow us to rewrite one string into another, which would allow us to do relate underlying representations (URs) in phonology to their corresponding surface forms.
But this is really underselling FSTs as a model of phonology.
What is impressive about FSTs is that they use a single core mechanic --- connecting finitely many states via transitions that have input:output labels --- yet get tremendous phonological mileage out of it.
FSTs can handle local processes like assimilation and word-final devoicing, iterated local processes like vowel harmony, unbounded dependencies and tiers, blocking, rule ordering, and much more.
They truly are a phonological swiss army knife, except that it is a swiss army knife that does everything with just one blade.

## Progressive assimilation

Let us start with a very simple example.
In colloquial speech, *n* often is pronounced *m* immediately after *p*.
For example, somebody might say *cap'm* instead of *cap'n* as the short form of *captain*.
This is an instance of **progressive assimilation**.
Phonologists would describe this with a **rewrite rule** of the form

$$\mathrm{n} \rightarrow \mathrm{m} \mid \mathrm{p} \_$$

which is read as "*n* becomes *m* in any context where *n* immediately appears to the right of *p*".

We can also express this progressive assimilation very easily in the form of an FST.
Again we may use the tabular format or the graph-based one in order to specify the FST.
For the sake of succinctness, we assume that the only input symbols are *m*, *n*, *p*, and *x*.
A realistic FST would have many more input symbols, but they would all be treated exactly the same as *x* here.

|           |                                    |                              |             |           |
| --:       | :-:                                | :-:                          | :-:         | :-:       |
|           | **0**                              | **P**                        | **Initial** | **Final** |
| **0**     | m:m, n:n, x:x                      | p:p                          | Yes         | Yes       |
| **P**     | m:m, n:m, x:x                      | p:p                          | No          | Yes       |

~~~ {.include-tikz size=mid}
progressiveassimilation.tikz
~~~

This transducer leaves almost all input symbols unchanged.
If it sees a *p*, it moves into the state *P*, and only at this point, if the next symbol it sees is *n*, does it do some rewriting and output *m* instead.
The key strategy is to switch from the default state *0* to the special state *P* when the conditions for rewriting *n* as *m* are met.
Once we are in the state, we go back to *0* the moment the conditions for assimilation are no longer met, either because we have already carried out the assimilation step, or because we have encountered other input symbols that have disrupted the conditions for assimilation.

::: exercise
Many language do not like consonant clusters of three or more consonants in a row.
Using the strategy illustrated above, construct an FST that deletes all consonants in a cluster except the first two.
For the sake of simplicity, assume that the input alphabet only consists of C for consonants and V for vowels.
For example, you may have the input string CCVCCCCV, and it should be rewritten as CCVCCV.
:::

## Regressive assimilation, the delayed output strategy, and the final emission trick

Whereas progressive assimilation proceeds from left-to-right, **regressive assimilation** proceeds from right-to-left.
For example, the word *white board* is commonly pronounced like *wipe board* because the *b* in *board* causes the preceding *t* in *white* to become a *p*.
The rewrite rule for that would be

$$\mathrm{t} \rightarrow \mathrm{p} \mid \_ \mathrm{b}$$

Notice how the conditioning environment now occurs after the sound that undergoes assimilation.
At first sight it may seem that our FST cannot handle regressive assimilation patterns.
Since the FST moves through the input from left-to-right and does not get to look ahead, it does not know what to do when it encounters a *t*.
Maybe it will be followed by a *b*, in which case it should be rewritten as *p*, or maybe *t* won't be followed by *b*, in which case it should stay a *t*.
How could the FST figure out which one is the right option?

One solution is to use a non-deterministic FST like the one below.

|           |                   |               |               |             |           |
| --:       | :-:               | :-:           | :-:           | :-:         | :-:       |
|           | **0**             | **P**         | **T**         | **Initial** | **Final** |
| **0**     | b:b, p:p, x:x     | t:p           | t:t           | Yes         | Yes       |
| **P**     | b:b               |               |               | No          | No        |
| **T**     | p:p, t:t, x:x     | t:p           |               | No          | Yes       |

~~~ {.include-tikz size=mid}
regressiveassimilation.tikz
~~~

::: exercise
Explain in your own words how this non-deterministic FST ensures that *t* is rewritten as *p* iff it occurs immediately before *b*.
:::

Ideally, though, we avoid non-determinism unless it is absolutely necessary, and it is not necessary at all for regressive assimilation.
Rather than having the FST make a guess about whether the current *t* should be rewritten as *t* or *p*, we can make it hold off on the rewriting until more of the input string has been seen.
This is the **delayed output strategy**, and it exploits the fact that the output of a transition can also be the empty string $\emptystring$ or a sequence of output symbols.

|           |                         |                               |             |           |
| --:       | :-:                     | :-:                           | :-:         | :-:       |
|           | **0**                   | **T**                         | **Initial** | **Final** |
| **0**     | b:b, p:p, x:x           | t:$\emptystring$              | Yes         | Yes       |
| **T**     | b:pb, p:tp, x:tx        | t:t                           | No          | No        |

~~~ {.include-tikz size=mid}
regressiveassimilation_delayedoutput.tikz
~~~

This deterministic FST deletes *t* upon encountering it, but it switches to a different state *T* to keep track of the fact that a *t* has been deleted.
When it encounters a *b*, a *p*, or an *x*, the transducer transitions from *T* back to the default state *0*.
However, in doing so it also reinserts the deleted *t*, or rather, *t* or *p* depending on the symbol: with *p* and *x*, the deleted *t* is reinserted, whereas with *b*, a *p* is reinserted instead.
Hence a *t* followed by a *b* undergoes assimilation via a two-step procedure: deletion of *t* and rewriting of *b* as *pb*.
And this two-step procedure is exactly what the delayed output strategy is about.

::: exercise
For each one of the following input strings, compute the output produced by the FST above.

1. xxptbx
1. txptbx
1. txptttbx
:::

::: exercise
What is the role of the transition *t:t* from state *T* to *T*?
:::

Unfortunately, though, there is a significant problem with the FST above.
As currently defined, it cannot process any input strings that end in *t*.

::: example
Consider the UR *xt*, which corresponds to the input string *xt{{{R}}}*.
The transducer starts in state *0*, rewrites *x* as *x*, and transitions to state *0*.
After that, it sees *t* in the input and transitions from *0* to *T* while outputting nothing.
It then reads in *{{{R}}}*, but since *T* is not a final state, the FST gets stuck and no output is produced at all.
We could fix this by making *T* final, but then we run into a different problem: the word-final *t* is deleted and never reinserted, and thus we end up with the incorrect output *x* instead of *xt*.
:::

The solution to this is rather simple: the special outgoing edge of final states does not have to be labeled *{{{R}}}:$\emptystring$*, it can be any label with *{{{R}}}* as the input symbol.
In other words, we can use {{{R}}} to add the final piece of the output string.
This is the **final emission trick**.

The revised FST is shown below.
Note that the column **Final** of the table no specifies the symbols added to the output when the FST stops in this state.

|           |                         |                               |             |                     |
| --:       | :-:                     | :-:                           | :-:         | :-:                 |
|           | **0**                   | **T**                         | **Initial** | **Final**           |
| **0**     | b:b, p:p, x:x           | t:$\emptystring$              | Yes         | Yes($\emptystring$) |
| **T**     | b:pb, p:tp, x:tx        | t:t                           | No          | Yes(t)              |

~~~ {.include-tikz size=mid}
regressiveassimilation_delayedoutput_finalemission.tikz
~~~

::: example
Consider once more the UR *xt* and its corresponding input string *xt{{{R}}}*.
After rewriting *x* as *x*, the FST is in state *T*.
It next reads in *t* and outputs the empty string so that the output string is still just *x*.
But now, when it encounters {{{R}}}, it adds *t* to the output string, correctly yielding *xt* as the surface form of the UR *xt*.
:::

::: exercise
In a previous chapter, we encountered the process of word-final devoicing in German.
Inspired by this phenomenon, define an FST that uses the delayed output strategy and the final emission trick in order to replace word-final *z* with *s* and word-final *v* with *f*.
You may write a table or draw a graph.
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
:::

::: exercise
The delayed output strategy does not work if the conditioning context can be arbitrarily far to the right of the target.
Suppose, for instance, that *t* would become *p* if there is a *b* somewhere to the right of *t*, no matter how far apart the two are.
This cannot be captured with the delayed output strategy.
Explain why!
:::

::: exercise
Continuing the previous exercise, can you imagine a way to handle such regressive long-distance phenomena with an FST?
:::


## Iterativity/spreading for vowel harmony

Another process we are familiar with by now is vowel harmony.
We described Korean vowel harmony as a ban against mixing bright vowels (B) and mid-dark vowels (M) in the same word.
But vowel harmony is actually a process that changes non-harmonic vowels in the UR to harmonic vowels in the surface form.
Suppose, then, that if the first vowel is B, all other vowels in the word become B, and if the first vowel is M, all other vowels in the word become M.
Can we do this with an FST?
Why yes, of course we can, just see below (assuming that our only input symbols are *B*, *M*, and *x* for anything else).

|           |         |                |                |             |                     |
| --:       | :-:     | :-:            | :-:            | :-:         | :-:                 |
|           | **0**   | **B**          | **M**          | **Initial** | **Final**           |
| **0**     | x:x     | B:B            | M:M            | Yes         | Yes($\emptystring$) |
| **B**     |         | B:B, M:B, x:x  |                | No          | Yes($\emptystring$) |
| **M**     |         |                | B:M, M:M, x:x  | No          | Yes($\emptystring$) |

~~~ {.include-tikz size=mid}
vowelharmony.tikz
~~~

This FST starts out in the default state *0*, but the very first time it encounters *B* or *M*, it switches into the corresponding state.
Once it is in one of those states, it rewrites all vowels into harmonic vowels.

::: exercise
For each one of the URs below, compute the corresponding surface form.
Don't forget to add {{{R}}} at the end of the input string.

1. xBxxM
1. MxxBxxBxxM
1. MxxxxxxxxB

:::

::: exercise
The high dark vowels (H) are neutral vowels.
They can occur together with B or M, and they do not undergo vowel harmony.
That is to say, H stays H.
Revise the FST above so that it also handles H correctly.
:::

::: exercise
Suppose that vowel harmony were not iterative.
That is to say, the first vowel only controls the harmony for the second vowel, after that the third vowel controls the harmony for the fourth vowel, and so on.
For instance, *xBxMxMxB* would come out as *xBxBxMxM*.
Modify the FST above so that it captures this pattern.
:::

::: exercise
Now suppose that vowel harmony is even more restricted so that harmony never involves more than the first two vowels in the word.
For example, *xBxMxMxB* would now come out as *xBxBxMxB*.
Modify the FST above so that it captures this pattern.
:::

## Unboundedness, tiers, and blocking

Another harmony process we have encountered before is sibilant harmony in Samala, which was noteworthy because it seems to be able to span arbitrary distances.
All sibilants in the word must be harmonic with the very first sibilant.
If the first sibilant is *s*, then any subsequent instances of *ʃ* become *s*.
And if the first sibilant is *ʃ*, then any subsequent instances of *s* become *ʃ*
When we first encountered this phenomenon, we modeled it with tiers, but no such addition is needed for FSTs to capture the unbounded nature of sibilant harmony.
In fact, the can pretty much recycle our FST for vowel harmony.

|           |         |                |                |             |                     |
| --:       | :-:     | :-:            | :-:            | :-:         | :-:                 |
|           | **0**   | **ESS**        | **ESH**        | **Initial** | **Final**           |
| **0**     | x:x     | s:s            | ʃ:ʃ            | Yes         | Yes($\emptystring$) |
| **ESS**   |         | s:s, ʃ:s, x:x  |                | No          | Yes($\emptystring$) |
| **ESH**   |         |                | s:ʃ, ʃ:ʃ, x:x  | No          | Yes($\emptystring$) |

~~~ {.include-tikz size=mid}
sibilantharmony.tikz
~~~

::: exercise
Slovenian has a version of sibilant harmony that is similar to Samala, except that harmony is blocked by an intervening *t*.
That is to say, the first sibilant after a *t* does not need to be harmonic with any of the sibilants to its left, but the sibilants to its right must be harmonic with that sibilant (unless another *t* intervenes).
Hence we get the following mappings between URs and surface forms:

- *xxsxxʃ* becomes *xsxxs*
- *xxstxʃ* becomes *xstxʃ*
- *xxstxʃxs* becomes *xstxʃxʃ*
- *xxstxʃts* becomes *xstxʃts*

Modify the FST above so that it incorporates blocking by *t*.
:::

We could look at many other phenomena, but the central point should be clear by now: the simple and elegant mechanism of connecting states via transitions allows us to capture wide range of phonological phenomena.
No extra tweaks or extensions are required to capture locality, unboundedness, iterativity, tiers, blocking, and much more.
They are all particular instantiations of the same basic machinery.

## Recap

- FSTs allow us model a variety of phonological phenomena as the rewriting of URs into surface forms.
- Without any extra machinery, FSTs can express
    - locally bounded phenomena (progressive and regressive), and
    - unbounded phenomena/tier-based phenomena, and
    - iterative phenomena and spreading, and
    - phenomena that involve blocking.
- Rewriting steps that are conditioned by subsequent material require the **delayed output strategy**: delete the symbol, then reinsert it later on when the conditioning context has been fully read in.
- The **final emission trick** allows us to rewrite {{{R}}} as a sequence of 0 or more input symbols.
