---
pagetitle: >-
    Rule ordering via cascades and composition
---

# Rule ordering via cascades and composition

::: prereqs
- tuples(crossproduct)
- relations(composition, closure)
:::

During our discussion of mapping n-grams, we saw that problems can arise if a context is compatible with multiple ways of rewriting the string: which rewrite step should we carry out first?
Phonologists resolve this problem by assuming that the set of phonological rules is totally ordered. 
If two rules are both applicable, the total order tells us which one to apply first.
This practice is known as **rule ordering** in phonology.
While rule ordering certainly solves this problem, it poses profound questions: Why should grammars allow for rule ordering? Does rule ordering increase the power of the grammar?
The surprising answer offered by finite-state transducers is that rule ordering does not increase power because every grammar with rule ordering corresponds to one without rule ordering.
And that is because every grammar with rewrite rules can be flattened into a grammar with just a single rewrite rule.
Let's see how one arrives at this surprising conclusion.

## Ordering effects with FSTs

We should first confirm that the issue of rule ordering is a real one in FST-land.
That is to say, if we have two FSTs, can we apply them in sequence, and does it matter in what order we apply them?
The answer to both is a resounding Yes.

First, applying two FSTs *X* and *Y* in sequence to some underlying representation *u* can be understood as feeding *u* into *X* to obtain some intermediate form *i*, which is then used as the input for *Y* to produce the surface form *s*.
This sounds abstract but is actually pretty trivial when dealing with concrete examples of *X* and *Y*, e.g. nasal deletion and nasalization.

::: example
Suppose that we have a phonological grammar with two rewrite rules.
One deletes nasals that occur immediately before voiceless plosives.
For simplicity, let us assume that the only voiceless plosive is *p* and the only nasal is *n*.

$$\mathrm{n} \rightarrow \emptystring \mid \_ \mathrm{p}$$

The other rewrite rule enforces that a non-nasalized vowel becomes nasalized before a nasal.
Again let us simplify this by assuming that there is only one nasal *n*, one non-nasalized vowel *a*, and its nasalized counterpart *ã*.

$$\mathrm{a} \rightarrow \mathrm{\tilde{a}} \mid \_ \mathrm{n}$$

Each one of these rules can be represented as a transducer that uses the delayed output strategy we encountered in an earlier unit.
These FSTs are shown below, both in the tabular format and as graphs.
For ease of exposition, the transducers only contain transitions for *n*, *p*, *a*, and *ã*, but additional transitions would be easy to add. 

(((**Note by TG**: to make things easier later on in this unit, the behavior of final states is changed so that {{{R}}} is always rewritten as some string with {{{R}}} at the end.
This is different from previous units, where {{{R}}} would be rewritten as a string without {{{R}}}.
I will update these earlier units accordingly at a later point.)))

|           |                   |                  |             |                     |
| --:       | :-:               | :-:              | :-:         | :-:                 |
|           | **X**             | **Del?**         | **Initial** | **Final**           |
| **X**     | p:p, a:a, ã:ã     | n:$\emptystring$ | Yes         | Yes({{{R}}})        |
| **Del?**  | p:p, a:na, ã:nã   | n:n              | No          | Yes(n{{{R}}})       |

~~~ {.include-tikz size=mid}
nasaldeletion.tikz
~~~

|           |                   |                  |             |                     |
| --:       | :-:               | :-:              | :-:         | :-:                 |
|           | **Y**             | **Nas?**         | **Initial** | **Final**           |
| **Y**     | n:n, p:p, ã:ã     | a:$\emptystring$ | Yes         | Yes({{{R}}})        |
| **Nas?**  | n:ãn, p:ap, ã:aã  | a:a              | No          | Yes(a{{{R}}})       |

~~~ {.include-tikz size=mid}
nasalization.tikz
~~~

Notice how the nasal deletion transducer is almost exactly the same as the nasalization transducer, except that their transitions have slightly different labels and their initial states have different names (which doesn't matter mathematically because the names of states are immaterial for the transduction).
All of this will hopefully make the next few examples easier to follow.
:::

::: exercise
For each one of the two transducers, write down the surface form that it maps the following URs to:

1. an
1. anpa
1. ãpaannap
1. ãpaannpan

:::

Now suppose that we have a UR like *anp*.
What should be the surface form of that?
If nasal deletion applies before nasalization, we should get *ap*.
If nasalization applies before nasal deletion, it should be *ãp*.
This corresponds exactly to the order in which we apply the two FSTs.

::: example
Suppose that we feed the UR *anp* into the FST for nasal deletion.
This produces the output *ap* as the UR contains *n* followed by *p*, triggering deletion of *n*.

| Current State | Input   | Output          | New State | Remaining input string | Output string built so far |
| :-:           | :-:     | :-:             | :-:       | :--                    | :--                        |
| -             | Start   | -               | X         | anp                    | -                          |
| X             | a       | a               | X         | np                     | a                          |
| X             | n       | $\emptystring$  | Del?      | p                      | a                          |
| Del?          | p       | p               | X         | {{{R}}}                | ap                         |
| X             | {{{R}}} | {{{R}}}         | Stop      | -                      | ap{{{R}}}                  |

If we now take this output *ap* and use it as the input for the FST for nasalization, we again get the output *ap* because there is no nasal that could trigger nasalization *a*.

| Current State | Input   | Output          | New State | Remaining input string | Output string built so far |
| :-:           | :-:     | :-:             | :-:       | :--                    | :--                        |
| -             | Start   | -               | Y         | ap                     | -                          |
| Y             | a       | a               | Y         | p                      | a                          |
| Y             | p       | p               | Y         | {{{R}}}                | ap                         |
| Y             | {{{R}}} | {{{R}}}         | Stop      | -                      | ap{{{R}}}                  |

Applying the nasal deletion FST before the nasalization FST thus maps the UR *anp* to the surface form *ap*.

Now suppose that we use the opposite order.
We take the UR *anp* and feed it into the nasalization FST.
This will yield *ãnp* as the *n* after *a* causes the latter to be nasalized.

| Current State | Input   | Output          | New State | Remaining input string | Output string built so far |
| :-:           | :-:     | :-:             | :-:       | :--                    | :--                        |
| -             | Start   | -               | Y         | anp                    | -                          |
| Y             | a       | $\emptystring$  | Nas?      | np                     | $\emptystring$             |
| Nas?          | n       | ãn              | Y         | p                      | ãn                         |
| Y             | p       | p               | Y         | {{{R}}}                | ãnp                        |
| Y             | {{{R}}} | {{{R}}}         | Stop      | -                      | ãnp{{{R}}}                 |

And when we take the output *ãnp* and use it as the input for the nasal deletion FST, it produces the output string *ãp* as the *n* before *p* is deleted.

| Current State | Input   | Output          | New State | Remaining input string | Output string built so far |
| :-:           | :-:     | :-:             | :-:       | :--                    | :--                        |
| -             | Start   | -               | X         | ãnp                    | -                          |
| X             | ã       | ã               | X         | np                     | ã                          |
| X             | n       | $\emptystring$  | Del?      | p                      | ã                          |
| Del?          | p       | p               | X         | {{{R}}}                | ãp                         |
| X             | {{{R}}} | {{{R}}}         | Stop      | -                      | ãp{{{R}}}                  |

We see, then, that the order in which we run FSTs can change the final output.
:::

::: exercise
For each one of the two ways of ordering the nasal deletion FST and the nasalization FST, indicate the final output form obtained from the URs listed below:

1. an
1. anpa
1. ãpaannap
1. ãpaannpan

:::

When we take multiple FSTs and run them in sequence, using the output of one as the input to the next, we are building a **cascade** of transducers.
The example above is a cascade of two transducers, but any finite number of FSTs can be arranged to form a cascade.

::: exercise
Suppose that the example grammar contains a third rewrite rule that inserts *p* at the end of the word.
Write down an FST that implements this rewrite rule (you may give a table or a graph).
With three FSTs, there are six possible cascades:

1. nasal deletion, nasalization, p-insertion
1. nasal deletion, p-insertion, nasalization
1. nasalization, nasal deletion, p-insertion
1. nasalization, p-insertion, nasal deletion
1. p-insertion, nasal deletion, nasalization
1. p-insertion, nasalization, nasal deletion

For each one of those cascades, write down the final output obtained from the UR *ãpaannpan*.
:::

Just as with rewrite rules in phonology, changing the order of transducers in the cascade can greatly affect the final output produced by this cascade.
This is one more instance, then, where FSTs make it easy to capture a common aspect of phonology.

However, things do not stop here.
The truly amazing thing about FSTs are that they can give rise to such ordering effects without any cascades.
That is because every cascade can be replaced with just a single FST!

## Incremental cascades: the intuition

When we built the transducer cascade above, we ran the FSTs in series.
That is to say, we took the whole input, fed it into the first FST, took the output from that, and fed it into the second FST to obtain the final output.
But with FSTs, we could have done this in an incremental fashion instead where we run each input symbol through the whole cascade before moving on to the next input symbol.

::: example
Consider once more the cascade of nasal deletion followed by nasalization, applied to the UR *anp*.
Let us see what happens if we use this cascade to rewrite the UR one symbol at a time.

1. Since the UR is *anp*, the input string is *anp{{{R}}}*.
1. The first input symbol is *a*.
   The nasal deletion FST starts in state *X*, rewrites *a* as *a*, and stays in state *X*.
   The nasalization FST starts in state *X*, takes the output *a* as its input, rewrites it as the empty string, and changes to state *Nas?*.
   At this point, we have rewritten *a* as the empty string, the nasal deletion FST is in state *X*, and the nasalization FST is in state *Nas?*.
1. The next input symbol is *n*.
   This causes the nasal deletion FST to from state *X* to state *Del?*, rewriting *n* as the empty string.
   Since we have no non-empty output from the nasal deletion FST, we have nothing to feed into the nasalization FST and have to skip it.
   Hence the nasalization FST does nothing and remains in state *Nas?*.
   At this point, we have rewritten *n* as the empty string, the nasal deletion FST is in state *Del?*, and the nasalization FST is in state *Nas?*.
1. Now the magic happens.
   We feed *p* into the nasal deletion FST, which outputs *p* and moves from *Del?* to *X*.
   We then feed the output *p* into the nasalization FST, which is currently in state *Nas?*.
   It outputs *ap* and moves to state *Y*.
1. We feed in the last symbol, which is {{{R}}}.
   The nasal deletion FST, which is in state *X*, rewrites this as {{{R}}} and stops.
   We then feed {{{R}}} into the nasalization FST (which is in state *Y*).
   It also rewrites {{{R}}} as {{{R}}} and stops.

We have finished processing the input string, and in doing so we produced the output string *ap{{{R}}}*, which corresponds to the surface form *ap*.

:::

Plain English isn't a good way of keeping track of such incremental applications of transducer cascades.
Instead, a tabular format is more succinct and easier to follow.
The table has five columns:

- **Input symbol**: the symbol of the input string that we are currently feeding into the transducer cascade
- **New state of FST1**: what state the first FST is in **after** rewriting the input symbol
- **Intermediate**: the output produced by the first FST from the input symbol; this output serves as the input to the second FST
- **New state of FST2**: what state the first FST is in **after** rewriting the input symbol
- **Final output**: the output produced from the input symbol; reading this column from top to bottom yields the output string

::: example

The lengthy English description above can be condensed to the table below.

| Input symbol | New state of FST1 | Intermediate   | New state of FST2 | Output         |
| :-:          | :-:               | :-:            | :-:               | :-:            |
| Start        | X                 | -              | Y                 | -              |
| a            | X                 | a              | Nas?              | $\emptystring$ |
| n            | Del?              | $\emptystring$ | Nas?              | $\emptystring$ |
| p            | X                 | p              | Y                 | ap             |
| {{{R}}}      | Stop              | {{{R}}}        | Stop              | {{{R}}}        |

:::

::: example
Now consider the cascade where nasalization applies before nasal deletion.
This will rewrite *anp{{{R}}}* as *ãp{{{R}}}*.
If you don't believe me (and you shouldn't), check the table below.

| Input symbol | New state of FST1 | Intermediate   | New state of FST2 | Output         |
| :-:          | :-:               | :-:            | :-:               | :-:            |
| Start        | Y                 | -              | X                 | -              |
| a            | Nas?              | $\emptystring$ | X                 | $\emptystring$ |
| n            | Y                 | ãn             | Del?              | ã              |
| p            | Y                 | p              | Y                 | p              |
| {{{R}}}      | Stop              | {{{R}}}        | Stop              | {{{R}}}        |

The only complication here is that the nasalization transducer, when rewriting *n*, doesn't just output a single symbol but the string *ãn*.
However, this does not change the overall procedure: we feed *ãn* into the nasal deletion transducer, which is in state X, and check what it produces from that input and what state it ends up in. 
:::

::: exercise
For each one of the two ways of ordering the nasal deletion FST and the nasalization FST, write down a table like the one above that indicates how *ãpaannpan* is rewritten in an incremental fashion (keep in mind that we add {{{R}}} at the end of the UR).
:::

You may be wondering what we gain from using this clunky incremental way of running the cascade.
It seems much more intuitive to run the cascade in serial mode, with the first FST processing the whole input, then second FST processing the whole output of the first FST, and so on.
Well, the difference is that --- hard as it may be to see --- the incremental way of running the cascade is a single finite-state transduction!

::: example
Consider once more the table for nasal deletion followed by nasalization, applied to *anp*.
It is repeated here for your convenience.

| Input symbol | New state of FST1 | Intermediate   | New state of FST2 | Output         |
| :-:          | :-:               | :-:            | :-:               | :-:            |
| Start        | X                 | -              | Y                 | -              |
| a            | X                 | a              | Nas?              | $\emptystring$ |
| n            | Del?              | $\emptystring$ | Nas?              | $\emptystring$ |
| p            | X                 | p              | Y                 | ap             |
| {{{R}}}      | Stop              | {{{R}}}        | Stop              | {{{R}}}        |

Suppose that we remove the third column from this table and fuse the second and fourth column into one, giving us the table below.

| Input symbol | New state | Output         |
| :-:          | :-:       | :-:            |
| Start        | X-Y       | -              |
| a            | X-Nas?    | $\emptystring$ |
| n            | Del-Nas?  | $\emptystring$ |
| p            | X-Y       | ap             |
| {{{R}}}      | Stop      | {{{R}}}        |

What does this table say if we read it literally?
It says that we start in state *X-Y* and change into state *X-Nas?* after rewriting *a* as the empty string.
We then rewrite *n* as the empty string and change into state *Del-Nas?*.
After that, *p* is rewritten as *ap* and we change into state *X-Y*, before we finally read in {{{R}}}, output {{{R}}}, and stop.
That's not a cascade of transductions, that's just a transduction!
:::

::: exercise
Construct the corresponding table for the cascade where nasalization precedes nasal deletion.
:::

## From an FST cascade to a cascade FST

What the intuitive discussion above is getting at is that every cascade of FSTs can be replaced by a single FST that immediately rewrites an input string into the output string produced by the cascade.
We may call this a **cascade FST**, even though that is not a common term in the literature.
It is more common to call such an FST the **composition** of the cascade.

The cascade FST can be constructed automatically using the incremental processing metaphor above.
The states of the cascade FST are tuples where each component corresponds to the state of one of the transducers in the cascade: the first component records the state of the first transducers, the second component records the state of the second transducer, and so on, for all of the finitely many FSTs that make up the cascade.
In formal terms, the set of states of the FST that computes the cascade of FSTs *U* and *V* is the crossproduct of $Q_U$ and $Q_V$, where $Q_U$ is the set of states of $U$ and $Q_V$ is the set of states of $V$, respectively.

::: example
For the cascade of nasal deletion followed by nasalization, the cascade FST has four states:

1. $\tuple{\mathrm{X},\mathrm{Y}}$
1. $\tuple{\mathrm{X},\mathrm{Nas?}}$
1. $\tuple{\mathrm{Del?},\mathrm{Y}}$
1. $\tuple{\mathrm{Del?},\mathrm{Nas?}}$
:::

We then have to determine how the cascade FST moves between these tuple states.
But that is just the process of incremental rewriting that we used in the preceding section.
For each input symbol *x*, we test whether the cascade FST can move from one state to the other, and what output the FST would produce if we do so.
More precisely:

- In order to construct an FST $Q$ that computes the cascade of FSTs $U$ and $V$, do the following:
    - For every state $u_1$ of $U$ and transition $x:y$ from $u_1$ to $u_2$, do the following:
        - if $y:z$ is transition in $V$ from $v_1$ to $v_2$, add to $Q$ a transition $x:z$ from $\tuple{u_1,v_1}$ to $\tuple{u_2,v_2}$.
    - A state $\tuple{u_1, v_1}$ of $Q$ is initial iff $u_1$ is an initial state of $U$ and $v_1$ is an initial state of $V$.

::: example
As we saw in the previous example, the FST $Q$ that computes the cascade of nasal deletion followed by nasalization has four states.
Let us start with a blank transition table for $Q$ and mark all initial states.
To reduce visual clutter, we write the states in the form *u-v* instead of $\tuple{u,v}$.

|                    |                   |                  |                |                   |             |                     |
| --:                | :-:               | :-:              | :-:            | :-:               | :-:         | :-:                 |
|                    | **X-Y**           | **X-Nas?**       | **Del-Y**      | **Del?-Nas?**     | **Initial** | **Final**           |
| **X-Y**            |                   |                  |                |                   | Yes         |                     |
| **X-Nas?**         |                   |                  |                |                   | No          |                     |
| **Del?-Y**         |                   |                  |                |                   | No          |                     |
| **Del?-Nas?**      |                   |                  |                |                   | No          |                     |

We now follow the procedure above to fill in this transition table one cell after the other.

1. We consider all transitions out of state *X* of the nasal deletion FST:
    - *p:p* goes to *X*:
        - there is a transition *p:p* from *Y* to *Y*; we add *p:p* as a transition from *X-Y* to *X-Y*
        - there is a transition *p:ap* from *Nas?* to *Y*; we add *p:ap* as a transition from *X-Nas?* to *X-Y*
    - similarly for *ã:ã*
    - *a:a* goes to *X*:
        - there is a transition *a:$\emptystring$ from *Y* to *Nas?*; we add *a:$\emptystring$* as a transition from *X-Y* to *X-Nas?*
        - there is a transition *a:a* from *Nas?* to *Nas?*; we add *a:a* as a transition from *X-Nas?* to *X-Nas?*
    - *n:$\emptystring$* goes to *Del?*:
        - there is a (trivial) transition *$\emptystring$:$\emptystring$* from *Y* to *Y*; we add *n:$\emptystring$* from *X-Y* to *Del?-Y*
        - there is a (trivial) transition *$\emptystring$:$\emptystring$* from *Nas?* to *Nas?*; we add *n:$\emptystring$* from *X-Nas?* to *Del?-Nas?*
    - the final transition *{{{R}}}:{{{R}}}*:
        - there is a final transition *{{{R}}}:{{{R}}}* from *Y*; we add final *{{{R}}}:{{{R}}}* from *X-Y*
        - there is a final transition *{{{R}}}:a{{{R}}}* from *Nas?*; we add final *{{{R}}}:a{{{R}}}* from *X-Nas?*
1. We consider all transitions out of state *Del?* of the nasal deletion FST:
    - *p:p* goes to *X*:
        - there is a transition *p:p* from *Y* to *Y*; we add *p:p* as a transition from *Del?-Y* to *X-Y*
        - there is a transition *p:ap* from *Nas?* to *Y*; we add *p:ap* as a transition from *Del?-Nas?* to *X-Y*
    - *ã:nã* goes to *X*:
        - there is a transition *n:n* from *Y* to *Y* and *ã:ã* from *Y* to *Y*; we add *ã:nã* as a transition from *Del?-Y* to *X-Y*
        - there is a transition *n:ãn* from *Nas?* to *Y* and *ã:ã* from *Y* to *Y*: we add *ã:ãnã* as a transition from *Del?-Nas?* to *X-Y*
    - *a:na* goes to *X*:
        - there is a transition *n:n* from *Y* to *Y* and a transition *a:$\emptystring$* from *Y* to *Nas?*; we add *a:n* as a transition from *Del?-Y* to *X-Nas?*
        - there is a transition *n:ãn* from *Nas?* to *Y* and transition *a:$\emptystring$* from *Y* to *Nas?*; we add *a:ãn* as a transition from *Del?-Nas?* to *X-Y*
    - *n:n* goes to *Del?*:
        - there is a transition *n:n* from *Y* to *Y*; we add *n:n* as a transition from *Del?-Y* to *Del?-Y*
        - there is a transition *n:ãn* from *Nas?* to *Y*; we add *n:ãn* as a transition from *Del?-Nas?* to *Del?-Y*
    - the final transition *{{{R}}}:n{{{R}}}*:
        - there is a transition *n:n* from *Y* to *Y* and final transition *{{{R}}}:{{{R}}}* from *Y*; we add final transition *{{{R}}}:n{{{R}}}* from *Del?-Y*
        - there is a transition *n:ãn* from *Nas?* to *Y* and final transition *{{{R}}}:{{{R}}}* from *Y*; we add final transition *{{{R}}}:ãn{{{R}}}* from *Del?-Nas?*

|                    |                   |                  |                  |                   |             |                     |
| --:                | :-:               | :-:              | :-:              | :-:               | :-:         | :-:                 |
|                    | **X-Y**           | **X-Nas?**       | **Del-Y**        | **Del?-Nas?**     | **Initial** | **Final**           |
| **X-Y**            | p:p, ã:ã          | a:$\emptystring$ | n:$\emptystring$ |                   | Yes         | Yes({{{R}}})        |
| **X-Nas?**         | p:ap, ã:aã        | a:a              |                  | n:$\emptystring$  | No          | Yes(a{{{R}}})       |
| **Del?-Y**         | p:p, ã:nã         | a:n              | n:n              |                   | No          | Yes(n{{{R}}})       |
| **Del?-Nas?**      | p:ap, ã:ãnã       | a:ãn             | n:ãn             |                   | No          | Yes(ãn{{{R}}})      |

~~~ {.include-tikz size=mid}
nasaldeletion_nasalization.tikz
~~~

When we apply the cascade FST above to the UR *anp* (i.e. the input string *anp{{{R}}}*), it correctly rewrites it as the surface form *ap* (i.e. the output string *ap{{{R}}}*).
:::

::: exercise
Compute the surface forms that the cascade transducer in the example above produces from the URs listed below:

1. an
1. anpa
1. ãpaannap
1. ãpaannpan
:::

The cascade FST implements a specific rule ordering without using any explicit rule ordering mechanism.
It is the details of the transitions that make this an FST that applies nasal deletion before nasalization rather than the other way round.

::: exercise
Construct the cascade FST for nasalization followed by nasal deletion (hint: the states are *Y-X*, *Nas?-X*, *Y-Del?*, and *Nas?-Del?*).
What are the differences to the cascade FST from the example above?
If both FSTs had meaningless state names like 0, 1, 2, 3, would it be easy to tell which FST represents which rule ordering?
:::

::: exercise
Compute the surface forms the cascade FST that implements nasalization followed by nasal deletion produces from the following URs:

1. an
1. anpa
1. ãpaannap
1. ãpaannpan
:::

::: exercise
The cascade FST construction above only specifies the case when the cascade involves exactly two transducers.
Explain why this is sufficient to also reduce cascades with more than two FSTs to a single FST.
:::

Cascade FSTs are certainly convoluted and often contain parts that make no sense in isolation.
For example, the cascade FST in the example above contains a transition that rewrites *a* as *n*, which would be a bizarre phonological process and seems to have nothing to do with nasal deletion or nasalization.
This transition is vital to make the whole FST work correctly, but this means that it cannot be understood without understanding the FST as a whole.
That's not nice from a scientific perspective, we want our models to be transparent and easily interpretable.
But that's not an argument against FSTs.
FSTs tell us that we can safely factorize our model by positing small, easily understood rewrite rules that we apply in a specific order.
It is safe to do so because it is just a different way of specifying FSTs --- if we want a single FST, we can always take this sequence of rules and flatten it to a single FST that directly rewrites URs as surface forms.

This isn't just a nice engineering trick, it has linguistic ramifications.
If all of phonology can be described with FSTs, then it is not immediately clear what it means to say that phonology has rule ordering.
We can replace the rule ordering with a single rewrite rule corresponding to the cascade FST.
And we could take any single rewrite rule (i.e. FST) and decompose it into multiple ordered rewrite rules (i.e. a cascade of FSTs).
None of that would affect the mapping form URs to surface forms.
To the extent that there are empirical arguments for rule ordering, they would have to link rule ordering to some additional property: processing claims, acquisition claims, typological claims.
But then it might still be possible to recast those claims in a way that they work with cascade FSTs, too.
This is yet another instance where the mathematical perspective urges us to practice *ontological modesty*: 
if there are many different ways to say a thing, we should not get too attached to one of them as more cognitively real than the others.

## Recap

- A **cascade** is a sequence of finitely many transductions run in sequence, with the output of one transduction serving as the input for the next one.
- Cascades can be run in an incremental, symbol-by-symbol fashion rather than reading in the whole input string at once.
- If the cascade consists entirely of FSTs, it can be flattened to a single FST, the cascade FST, that computes the same transduction as the whole cascade.
- The set of states of the cascade FST is the crossproduct of the sets of states of the FSTs making up the cascade.
- In order to construct an FST $Q$ that computes the cascade of FSTs $U$ and $V$, do the following:
    - For every state $u_1$ of $U$ and transition $x:y$ from $u_1$ to $u_2$, do the following:
        - if $y:z$ is transition in $V$ from $v_1$ to $v_2$, add to $Q$ a transition $x:z$ from $\tuple{u_1,v_1}$ to $\tuple{u_2,v_2}$.
    - A state $\tuple{u_1, v_1}$ of $Q$ is initial iff $u_1$ is an initial state of $U$ and $v_1$ is an initial state of $V$.
