---
pagetitle: >-
    N-gram models of grammaticality (Solutions)
---

# N-gram models of grammaticality (Solutions)

::: exercise
Consider the word
*supercalifragilisticexpialidocious*.
For each one of the following, say whether it is a bigram of the word.

- fr
- z
- doci
- pail
- sit
- co
- super

::: solution

- fr: yes
- z: no
- doci: no
- pail: no
- sit: no
- co: no
- super: no

**Explanation**  
We assume for this exercise that the relevant symbols are the characters of the English alphabet that are used to spell *supercalifragilisticexpialidocious*, rather than the sounds that are uttered when pronouncing the word.

Bigrams consist of exactly two symbols.
Consequently, none of the following are bigrams:

- z (only 1 symbol)
- doci (4 symbols)
- pail (4 symbols)
- sit (3 symbols)
- super (5 symbols)

As these are not bigrams, they cannot be bigrams of *supercalifragilisticexpialidocious*.
That leaves us with only two contenders:

- fr
- co

The bigrams of the word *supercalifragilisticexpialidocious* are *ag, al, ca, ce, ci, do, er, ex, fr, gi, ia, ic, id, if, il, io, is, li, oc, ou, pe, pi, ra, rc, st, su, ti, up, us, xp*.
As you can see, *fr* is in this list, but *co* is not.
Among all the items listed in the exercise, then, only *fr* is a bigram.
:::

:::

::: exercise
Consider once more the word
*supercalifragilisticexpialidocious*.
Which one of the following is among its bigrams (with edge markers):


- fr
- z
- {{{L}}}{{{R}}}
- {{{L}}}s
- s{{{R}}}{{{R}}}

::: solution

- fr: yes
- z: no
- {{{L}}}{{{R}}}: no
- {{{L}}}s: yes
- s{{{R}}}{{{R}}}: no

**Explanation**  
Once we consider edge markers, the long list of bigrams from the previous solution gains two new members: *{{{L}}}s* and *s{{{R}}}*.
Bigrams that were already on the original list without edge markers are still bigrams, so *fr* is still a bigram of *supercalifragilisticexpialidocious*.
Similarly *n*-grams that do not consist of exactly two symbols are still not possible bigrams, which rules out *z* (only 1 symbol) and *s{{{R}}}{{{R}}}* (3 symbols).
This leaves us with {{{L}}}{{{R}}} and {{{L}}}s.
The latter is one of the two new members, but the former is not.
In fact, {{{L}}}{{{R}}} can never be a bigram of any string that consists of one or more symbols.
:::

:::

::: exercise
For each one of the following strings with the appropriate number of edge markers, say whether it has been padded for use with a bigram grammar, a trigram grammar, or a 4-gram grammar.

- {{{L}}}{{{L}}}kbin{{{R}}}{{{R}}}
- {{{L}}}{{{L}}}{{{L}}}workbench{{{R}}}{{{R}}}{{{R}}}
- {{{L}}}akbar{{{R}}}

::: solution

- trigram grammar
- 4-gram grammar
- bigram grammar

**Explanation**  
As all the strings have the same number of left edge and right edge markers, they are correctly padded for some kind of $n$-gram grammar.
All we have to do, then, is to count the number of left edge markers (or alternatively, the number of right edge markers) and add $1$ to that in order to obtain the value of $n$ for the $n$-gram grammar.

:::

:::


::: exercise
Consider once more the word
*supercalifragilisticexpialidocious*.
For each one of the following, say whether it is a bigram of the word (with edge markers), a trigram, a 4-gram, or none of those choices.

- {{{L}}}fr
- z
- do{{{R}}}c
- s{{{R}}}{{{R}}}{{{R}}}
- sit
- cious
- {{{L}}}sup

::: solution

- {{{L}}}fr: none of those choices
- z: none of those choices
- do{{{R}}}c: none of those choices
- s{{{R}}}{{{R}}}{{{R}}}: 4-gram
- sit: none of those choices
- cious: none of those choices
- {{{L}}}sup: 4-gram

**Explanation**

- {{{L}}}fr: the word starts with *su*, not *fr*, so *{{{L}}}fr* does not occur in the word
- z: this is a unigram, but we are only considering bigrams, trigrams, and 4-grams; and even if we did consider unigrams, the word does not contain *z* at all
- do{{{R}}}c: this is a 4-gram but it can never occur in any string because it is impossible to have any symbol after {{{R}}}
- s{{{R}}}{{{R}}}{{{R}}}: this is a 4-gram; for 4-grams, we have to assume at least three edge markers on each side of the string, and since the word ends in *s*, the string with edge markers must indeed contain s{{{R}}}{{{R}}}{{{R}}}
- sit: this is a trigram, but it does not occur in the word
- cious: this is a 5-gram that occurs in the word, but we are only considering bigrams, trigrams, and 4-grams
- {{{L}}}sup: this is a 4-gram and since the word starts with *sup*, *{{{L}}}sup* is indeed a 4-gram of the string once we include edge markers
:::

:::

::: exercise
Italian has intervocalic voicing, which means that it is impossible for a voiceless consonant like *s* or *f* to occur between two vowels.
For instance, it is impossible to have a form like *asola*, it must be *azola* with the voiced *z* instead of a voiceless *s*.
For the sake of simplicity, let us assume that Italian only has the vowels *a* and *o*, and the consonants *s*, *z*, and *l*.
Only the voiceless *s* is subject to intervocalic voicing.
Write a negative trigram grammar that captures intervocalic voicing in this simplified version of Italian.

::: solution
The grammar consists of the following forbidden trigrams:

- asa
- aso
- osa
- oso

**Explanation**  
Intervocalic voicing only occurs if *s* is surrounded by two vowels.
So the forbidden trigrams must be of the form *VsV*, where *V* is a vowel.
We have to replace each *V* in *VsV* with every possible vowel.
Since our toy Italian only has the vowels *a* and *o*, this leaves us with $2 \times 2 = 4$ possible substitutions, yielding the four trigrams above.

:::

:::

::: exercise
Intervocalic voicing cannot be captured with a negative bigram grammar.
That is because no negative bigram grammar can rule out the illicit *asola* without also ruling out the well-formed *alsola* and *aslola* (while non-existant, these words satisfy the phonotatic laws of Italian).
Explain in detail why this is the case.

::: solution
A bigram grammar that deems *asola* illicit must deem at least one of its bigrams illicit.
The list of bigrams of *asola* is as follows:

- {{{L}}}a
- as
- so
- ol
- la
- a{{{R}}}

But each one of these bigrams is also a bigram of *alsola* or *aslola* (or both).
Hence, if one of these bigrams is deemed illicit by the grammar, then at least one of *alsola* or *aslola* is also deemed illicit.

:::

:::

::: exercise
Intervocalic voicing in Italian does not always apply.
The word *asociale*, comparable to English *anti-social*, has a voiceless *s* between *a* and *o*.
However, linguists would argue that this word is more complex because it is built from two separate parts *a* and *sociale* that are fused together into a single word.
In technical terms, *a* and *sociale* are two separate *morphemes*, and we should represent *asociale* more accurately as *a+sociale* with the morpheme boundary *+* between *a* and *s*.
Explain why, given this assumption, your negative trigram grammar for intervocalic voicing correctly predicts *a+sociale* to be well-formed.

::: solution
As a reminder, the negative trigram grammar for intervocalic voicing consists of the following trigrams:

- asa
- aso
- osa
- oso

Padding *a+sociale* with the appropriate number of edge markers yields *{{{L}}}{{{L}}}a+sociale{{{R}}}{{{R}}}*, the trigrams of which are as follows:

- {{{L}}}{{{L}}}a
- {{{L}}}a+
- a+s
- +so
- soc
- oci
- cia
- ale
- le{{{R}}}
- e{{{R}}}{{{R}}}

Crucially, none of those trigrams are forbidden by the negative trigram grammar.
Intuitively speaking, that is because the morpheme boundary now intervenes between *a* and *s* so that *s* no longer appears between two vowels.

:::

:::

::: exercise
Consider the formal language where all strings are sequences of *a*, *b*, and *c* such that

- every string starts with *a*
- no string ends with *c*
- *a* and *c* are always separated by at least two symbols.

Write a negative 4-gram grammar for this language.
Then write an equivalent negative grammar that mixes bigrams and 4-grams.
Which one strikes you as a more direct description of the constraints above?

::: solution
The negative 4-gram grammar contains numerous 4-grams.
For the sake of readability, the list is split up based on what constraint the 4-grams capture.
As a result, some 4-grams may be listed multiple times.

- **every string starts with a**
    - {{{L}}}{{{L}}}{{{L}}}b
    - {{{L}}}{{{L}}}{{{L}}}c
- **no string ends with c**
    - c{{{R}}}{{{R}}}{{{R}}}
- **a and c are always separated by at least two symbols**
    - *a must not be immediately before c*
        - ac{{{R}}}{{{R}}}
        - aca{{{R}}}
        - acb{{{R}}}
        - acc{{{R}}}
        - acaa
        - acab
        - acac
        - acba
        - acbb
        - acbc
        - acca
        - accb
        - accc
        - {{{L}}}ac{{{R}}}
        - {{{L}}}aca
        - {{{L}}}acb
        - {{{L}}}acc
        - bac{{{R}}}
        - baca
        - bacb
        - bacc
        - cac{{{R}}}
        - caca
        - cacb
        - cacc
        - {{{L}}}{{{L}}}ac
        - {{{L}}}aac
        - {{{L}}}bac
        - {{{L}}}cac
        - aaac
        - abac
        - acac
        - baac
        - bbac
        - bcac
        - caac
        - cbac
        - ccac
    - *c must not be immediately before a*
        - ca{{{R}}}{{{R}}}
        - caa{{{R}}}
        - cab{{{R}}}
        - cac{{{R}}}
        - caaa
        - caab
        - caac
        - caba
        - cabb
        - cabc
        - caca
        - cacb
        - cacc
        - {{{L}}}ca{{{R}}}
        - {{{L}}}caa
        - {{{L}}}cab
        - {{{L}}}cac
        - bca{{{R}}}
        - bcaa
        - bcab
        - bcac
        - cca{{{R}}}
        - ccaa
        - ccab
        - ccac
        - {{{L}}}{{{L}}}ca
        - {{{L}}}aca
        - {{{L}}}bca
        - {{{L}}}cca
        - aaca
        - abca
        - acca
        - baca
        - bbca
        - bcca
        - caca
        - cbca
        - ccca
    - *a must not be one symbol before c*
        - aac{{{R}}}
        - abc{{{R}}}
        - acc{{{R}}}
        - {{{L}}}aac
        - {{{L}}}abc
        - {{{L}}}acc
        - aaac
        - aabc
        - aacc
        - baac
        - babc
        - bacc
        - caac
        - cabc
        - cacc
    - *c must not be one symbol before a*
        - caa{{{R}}}
        - cba{{{R}}}
        - cca{{{R}}}
        - {{{L}}}caa
        - {{{L}}}cba
        - {{{L}}}cca
        - acaa
        - acba
        - acca
        - bcaa
        - bcba
        - bcca
        - ccaa
        - ccba
        - ccca

Note that we do not need to list 4-grams like *{{{L}}}{{{L}}}ba* because every string with edge markers that contains *{{{L}}}{{{L}}}ba* also contains *{{{L}}}{{{L}}}{{{L}}}b*, which we already list as illicit.

Hence the switch to bigrams does not buy us much for the first two constraints.

- **every string starts with a**
    - {{{L}}}b
    - {{{L}}}c
- **no string ends with c**
    - c{{{R}}}

But bigrams allow us to express much more succinctly that *a must not be immediately before c* and that *c must not be immediately before a*.

- *a must not be immediately before c*
    - ac
- *c must not be immediately before a*
    - ca

This eliminates dozens of 4-grams from the grammar.
If the exercise had allowed us to use trigrams, then we could also express more succinctly that *a must not be one symbol before c* and *c must not be one symbol before a*.

- *a must not be one symbol before c*
    - abc
- *c must not be one symbol before a*
    - cba

We do not need to explicitly block *aac*, *acc*, *caa* or *cca* as these configurations are already ruled out by the bigrams *ac* and *ca*.
So if we had been allowed to use bigrams and trigrams, instead of using 4-grams for everything, the giant grammar above could have been much smaller and could have stated the generalizations much more succinctly:

- {{{L}}}b
- {{{L}}}c
- c{{{R}}}
- ac
- ca
- abc
- cba

:::

:::
