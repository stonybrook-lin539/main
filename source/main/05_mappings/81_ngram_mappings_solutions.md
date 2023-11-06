---
pagetitle: >-
    Generalizing n-grams to mappings: a failed attempt (Solutions)
---

# Generalizing n-grams to mappings: a failed attempt (Solutions)

::: exercise
The English plural marker has multiple forms that are phonologically conditioned.
Roughly speaking, we get

1. *es* after *s*, *z*, *ʃ*, and *tʃ*,
2. *s* after any other voiceless consonants (e.g. *t*, *k*),
3. *z* everywhere else (that is to say, after vowels and voiced consonants).

Assume that a form like *gases* is underlyingly *gasP*, where P is a single abstract symbol indicating plural.
Provide a list of n-grams that rewrite P as the correct surface form.
For simplicity, you may assume that the alphabet only consists of *g*, *s*, *t*, *a*, and *e*.

::: solution
1. sP[es]
1. tP[s]
1. gP[z], aP[z], eP[z]
:::

::: solution_explained
Since the realization of the plural is conditioned by the preceding segment, we only need bigrams to capture its distribution.
The stipulated alphabet contains only *s*, which matches the first condition above, *t*, which matches the second condition above, and *g*, *a*, *e*, which match the third condition above.
:::

:::

::: exercise
Specify the mapping n-grams for intervocalic voicing.
You may assume that the alphabet only consists of *a*, *o*, *s*, *z*, and *l*.

::: solution
- as[z]a
- as[z]o
- os[z]a
- os[z]o
:::

::: solution_explained
Intervocalic voicing only targets voiceless segments, and *s* is the only voiceless segment in the stipulated alphabet.
A segment is voiced only if both the preceding and the following segment is a vowel, and thus we have to use trigrams instead of bigrams.
:::

:::

::: exercise
Matching n-grams also run into issues with unbounded processes like sibilant harmony.
Suppose that *s* becomes *ʃ* after *ʃ*, no matter how far the two are apart.
For instance,
*ʃtojowonowas*
would become
*ʃtojowonowaʃ*.
Explain why this cannot be handled with matching n-grams if the number of intervening segments is truly unbounded.

::: solution
The problem is pretty much the same we encountered with the phonotactics of unbounded sibilant harmony: n-grams only allow us to capture dependencies that span up to *n* segments.
If there truly is no upper bound on how far the sibilants can be apart, then no value *n* is ever sufficient to cover all cases.
If, on the other hand, we assume that there is an upper bound but it's simply very large, then we run into the problem of having a very, very large grammar that fails to capture the phenomenon succinctly.
:::

:::

::: exercise
Continuing the previous exercise, suggest a way matching n-grams could be amended to handle such unbounded dependencies.

::: solution
Just as in the case of phonotactics, we could project a tier and use the matching n-grams over this sibilant tier instead of the whole string.
Then sibilant harmony would be captured by the bigrams ʃs[ʃ] and sʃ[s].
In contrast to what we saw with phonotactics, though, this would still fail to handle cases with multiple sibilants.
For instance, if the sibilant tier is *ʃss*, then the first *s* would be correctly rewritten as *ʃ*, but the second *s* would not change because it is preceded by *s* --- the rewriting of *s* as *ʃ* does not trigger the same rewriting step on subsequent segments.
This is another case where we would have to define the match over the surface form of the UR.
Hence we would need tiers over surface forms for this phenomenon, rather than tiers over URs.
:::

:::

::: exercise
Suppose you are given the following mapping n-grams.

1. n[m]p
1. mp[$\emptystring$]
1. a[a:]mp
1. a:[a]{{{R}}}

Which of the following are URs from which one can obtain the surface form *a:mpa*?
Assume that the mapping n-grams must match the UR, not the surface form or something else.

1. ampa:
1. ampa
1. a:mpa:
1. a:mpa
1. anpa:
1. anpa
1. a:npa:
1. a:npa

::: solution
The surface form *a:mpa* can be obtained from the following two URs in the list, and only those:

- a:npa:
- a:npa
:::

::: solution_explained
1. ampa: becomes a:ma because of mp[$\emptystring$], a[a:]mp, and a:[a]{{{R}}} (keep in mind that each one of them only considers the UR, not the forms obtained by applications of matching n-grams)
1. ampa becomes a:ma because of mp[$\emptystring$] and a[a:]mp
1. a:mpa: become a:ma because of mp[$\emptystring$] and a:[a]{{{R}}}
1. a:mpa becomes a:ma because of mp[$\emptystring$]
1. anpa: becomes ampa because of n[m]p and a:[a]{{{R}}}
1. anpa becomes ampa because of n[m]p
1. a:npa: becomes a:mpa because of n[m]p and a:[a]{{{R}}}
1. a:npa becomes a:mpa because of n[m]p
:::

:::
