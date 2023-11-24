---
pagetitle: >-
    Finite-state transductions as transducers (Solutions)
---

# Finite-state transductions as transducers (Solutions)

::: exercise
Using the FST from the first example of this unit, compute the output strings for all of the following inputs:

1. bba{{{R}}}
1. aaaaa{{{R}}}
1. abbb{{{R}}}

::: solution
1. cccca
1. ababa
1. a
:::

:::

::: exercise
Define an FST that implements the following rewrite process, assuming that input strings may contain the symbols, *a*, *b*, or *c*:

1. If the string starts with *a*, rewrite all subsequent instances of *a* as *aa*.
1. If the string starts with *b*, delete all subsequent instances of *b*.
1. Do not change anything else.

::: solution

|           |           |                          |                              |               |             |           |
| --:       | :-:       | :-:                      | :-:                          | :-:           | :-:         | :-:       |
|           | **0**     | **A**                    | **B**                        | **C**         | **Initial** | **Final** |
| **0**     |           | a:a                      | b:b                          | c:c           | Yes         | Yes       |
| **A**     |           | a:aa, b:b, c:c           |                              |               | No          | Yes       |
| **B**     |           |                          | a:a, b:$\emptystring$        |               | No          | Yes       |
| **C**     |           |                          |                              | a:a, b:b, c:c | No          | Yes       |

:::

::: solution_explained
We have four distinct states:

- *0* is the starting state.
  Depending on the first symbol of the string, we transition into one of the other three states.
- *A*: the first symbol was *a*; from here on out, we rewrite *a* as *aa* but do not change *b* or *c*.
- *B*: the first symbol was *b*; from here on out, we delete *b* but do not change *a* or *c*.
- *C*: the first symbol was *c*; from here on out, we do not change *a* or *b* or *c*.

All states are final.
This includes *0* because this FST should be able to take the empty string as an input, too.
:::
:::

::: exercise
Using the FST from the first example of this unit, compute the output strings for all the inputs below.
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

::: exercise
Write down all the output strings that the FST above can produce from the input *abababb{{{R}}}*.
Keep in mind that the FST must be in a final state when reading {{{R}}}.

::: solution
1. accacca
1. aacca
1. abcca
:::

::: solution_explained
There are multiple paths one can take through the transducer by following the input string *abababb{{{R}}}*.
We can write down these paths as sequences of states, starting with the initial state.
But only two of these paths lead us to a final state:

1. $E \xrightarrow{a} O \xrightarrow{b} E \xrightarrow{a} O \xrightarrow{b} E \xrightarrow{a} O \xrightarrow{b} E \xrightarrow{b} E \xrightarrow{{{{R}}}} \mathrm{stuck}$
1. $E \xrightarrow{a} O \xrightarrow{b} E \xrightarrow{a} O \xrightarrow{b} E \xrightarrow{a} O \xrightarrow{b} O \xrightarrow{b} O \xrightarrow{{{{R}}}} \mathrm{stop}$
1. $E \xrightarrow{a} O \xrightarrow{b} E \xrightarrow{a} O \xrightarrow{b} O \xrightarrow{a} E \xrightarrow{b} E \xrightarrow{b} E \xrightarrow{{{{R}}}} \mathrm{stuck}$
1. $E \xrightarrow{a} O \xrightarrow{b} O \xrightarrow{a} E \xrightarrow{b} E \xrightarrow{a} O \xrightarrow{b} E \xrightarrow{b} E \xrightarrow{{{{R}}}} \mathrm{stuck}$
1. $E \xrightarrow{a} O \xrightarrow{b} O \xrightarrow{a} E \xrightarrow{b} E \xrightarrow{a} O \xrightarrow{b} O \xrightarrow{b} O \xrightarrow{{{{R}}}} \mathrm{stop}$

The two successful paths then have multiple options for rewriting the input string:

1. $E \xrightarrow{a:a} O \xrightarrow{b:cc} E \xrightarrow{a:a} O \xrightarrow{b:cc} E \xrightarrow{a:a} O \xrightarrow{b:\emptystring} O \xrightarrow{b:\emptystring} O \xrightarrow{{{{R}}}:\emptystring} \mathrm{stop}$
1. $E \xrightarrow{a:a} O \xrightarrow{b:\emptystring} O \xrightarrow{a:a} E \xrightarrow{b:cc} E \xrightarrow{a:a} O \xrightarrow{b:\emptystring} O \xrightarrow{b:\emptystring} O \xrightarrow{{{{R}}}:\emptystring} \mathrm{stop}$
1. $E \xrightarrow{a:a} O \xrightarrow{b:\emptystring} O \xrightarrow{a:b} E \xrightarrow{b:cc} E \xrightarrow{a:a} O \xrightarrow{b:\emptystring} O \xrightarrow{b:\emptystring} O \xrightarrow{{{{R}}}:\emptystring} \mathrm{stop}$

Reading just the output symbols along these paths, we get:

1. accacca
1. aacca
1. abcca
:::

:::
