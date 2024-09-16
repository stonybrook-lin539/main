---
pagetitle: Positive n-gram grammars
---

# Positive $n$-gram grammars

:::prereqs
- basic math (factorial)
:::

We now have a simple model of phonotactics, i.e. what sequences of sounds may occur in the words of a natural language.
According to this model, the phonotactic well-formedness of a word can be determined from the chunks that said word is built from.
In a trigram model, for instance, a word is ill-formed iff it contains one or more illicit trigrams.
We formalize this in terms of a negative $n$-gram grammar, which is a finite set of illicit $n$-grams.

::: example
Suppose our alphabet, i.e. the set of available symbols, is $\setof{a,b,c}$.
Then the negative trigram grammar $\setof{\mathit{aac}, \mathit{abc}, \mathit{acc}}$ only permits strings where no symbol is directly sandwiched between $a$ and $c$.
:::

The model looks rather promising as it can handle a variety of phenomena that have been studied extensively by linguists:
word-final devoicing, intervocalic voicing, local assimilation, and various stress rules.

::: exercise
For each one of the following phenomena, write a negative $n$-gram grammar that handles it correctly.
For some of them, you have to rephrase the phenomenon as a phonotactic constraint first.

- **intervocalic voicing**: voiceless fricatives (assume *s* and *f*) may not occur between vowels (assume *a*, *i*, *u*)
- **local assimilation**: *n* must be *m* before *b* or *p*
- **local dissimilation**: *rVr* becomes *lVr*, where *V* is *a*, *i*, or *u*
- **penultimate stress**: in words with at least two syllables, stress falls on the last but one syllable (assume that words are strings of stressed syllables ($\acute{\sigma}$) and unstressed syllables ($\sigma$))

::: solution
1. **intervocalic voicing**: asa, asi, asu, afa, afi, afu, isa, isi, isu, ifi, ifa, ifu, usa, usi, usu, ufa, ufu, ufi
1. **local assimilation**: nb, np
1. **local dissimilation**: rar, rir, rur
1. **penultimate stress** ${{{L}}}\sigma{{{R}}}, \sigma \acute{\sigma}{{{R}}}, \sigma \sigma {{{R}}}, \acute{\sigma} \sigma \sigma$

::: solution_explained
1. We have to forbid trigrams of the form $xyz$ where $x$ and $z$ are vowels and $y$ is a voiceless fricative.
   The exercise tells us that $x$ and $z$ can be *a*, *i*, or *u*, and $y$ can be *s* or *f*.
   After carrying out all possible substitutions of $x$, $y$, and $z$, we get the list of forbidden trigrams above.
1. If *n* must be *m* before *b* or *p*, this means that we can never have an *n* followed by *b* or *p* (because then we would have a case where *n* failed to turn into *m*).
   Hence we forbid the bigrams *nb* and *np*.
1. The exercise describes local dissimilation as a process where *r* changes to *l* if it is followed by *Vr*.
   In terms of phonotactics, this means that we cannot have *r* followed by *Vr*.
   Replacing *V* with all possible choices for a vowel, we get the forbidden trigrams *rar*, *rir*, and *rur*.
1. This one is tricky because we have to consider multiple cases.
   If a word has just one syllable, then it is not subject to the penultimate stress rule (which only applies to words with at least two syllables), and hence stress falls on the last syllable in this case.
   In other words, monosyllabic words must be of the form $\acute{\sigma}$, whereas $\sigma$ is not allowed.
   If a word has exactly two syllables, then it must be of the form $\acute{\sigma} \sigma$ because the other option $\sigma \acute{\sigma}$ would violate the penultimate stress rule.
   And if a word has three or more syllables, then it must be of the form $\sigma^+ \acute{\sigma} \sigma$.
   Based on this, we can deduce what must be forbidden:
   First, we do not want to allow words like $\sigma$, so our grammar must contain the forbidden trigram ${{{L}}} \sigma {{{R}}}$.
   We also do not want to allow any word with at least two syllables where stress falls on the last syllable, and thus we add the forbidden trigram $\sigma \acute{\sigma} {{{R}}}$.
   We do not want to allow any word that ends with two unstressed syllables, which we capture with the forbidden trigram $\sigma \sigma {{{R}}}$.
   The combination of $\sigma \acute{\sigma} {{{R}}}$ and $\sigma \sigma{{{R}}}$ guarantees that if a word has at least two syllables, the last but one is stressed.
   But that's not quite enough, we also have to ensure that this is the only syllable that is stressed.
   That is the same as saying that we do not to allow any word where the stressed syllable is followed by at least two unstressed syllables, and thus we also forbid the trigram $\acute{\sigma} \sigma \sigma$.
   And that's it, nothing else is required.
:::

:::

:::

Since the model seems to work well for phonotactics, it is tempting to expand it to other domains of language.
But as we will see next, this reveals certain shortcomings of the negative grammar format.


## Morphotactics

Just like phonotactics regulates the linear order of sounds in a word, **morphotactics** regulates the linear order of **morphemes**.
Morphemes consist of multiple sounds and are the building blocks of words (linguists, please keep in mind that once again we won't distinguish between morphemes, morphs, and allomorphs).
For example, *denaturalization* is built from the morphemes *de-*, *nature*, *-al*, *-ize*, and *-ation*.
Morphemes cannot be combined willy-nilly, they have to follow a specific order.
In the case of *denaturalization*, no other order is possible.
Even though the word is built up from 5 elements, which could be arranged in $5! = 5 \mult 4 \mult 3 \mult 2 \mult 1 = 120$ distinct ways, only one of them is actually allowed by English.
So morphotactics defines a very tight rule system for how elements may be ordered in a word, much tighter than phonotactics, where individual sounds have more leeway as to where they occur in a word.

Let's see if we can write a negative $n$-gram grammar that allows for *denaturalization* but forbids all illicit orders, e.g. *naturedeationizal*.
First, we have to pick the basic building blocks for the $n$-grams.
For phonotactics, we used $n$-grams where each symbol is a sound, but this is too fine-grained for morphotactics.
Instead, we will use $n$-grams where each symbol is a morpheme.
If we used sounds, then *-ize -ation* would be an 11-gram that consists of 8 letters, 2 hyphens, and 1 space.
But since we use morphemes as our basic building blocks, *-ize -ation* is a bigram.

``` jupyterpython
chunk = "-ize -ation"
print("{} with characters as symbols: {}-gram".format(chunk, len(chunk)))
print("{} with sounds as symbols: {}-gram".format(chunk, len("izaSon")))
print("{} with morphemes as symbols: {}-gram".format(chunk, len(("-ize", "-ation"))))
```

::: exercise
For each one of the following $n$-grams, say how large it is depending on what one chooses as the basic symbols that $n$-grams are built from.
Possible choices for building blocks are typed characters, morphemes, or words.
Not all choice may be appropriate in each case.

- *de-*
- *mpi*
- *John likes Mary*

::: solution
1. *de-*: It could be a unigram consisting just of the morpheme *de-*, or a trigram that consists of the characters *d*, *e*, and a hyphen. 
1. *mpi*: The only reasonable treatment here is as a trigram consisting of the characters *m*, *p*, and *i*.
1. *John likes Mary*: This could be a trigram that consists of the words *John*, *likes*, and *Mary*, or a 4-gram that consists of the morphemes *John*, *like*, *s*, and *Mary*, or a 15-gram that consists of a long sequence of letters and spaces.
:::

:::

With each morpheme as a separate symbol, it should be straight-forward to design a negative grammar to generate *de-nature-al-ize-ation* but none of the other orders.
Let's first write down the conditions in plain English:

1. start with *de-*,
1. *de-* is followed by *nature*,
1. *nature* is followed by *-al*,
1. *-al* is followed by *-ize*,
1. *-ize* is followed by *-ation*,
1. end with *-ation*.

Easy peasy, so let's write it down as a negative grammar.
Here's the list of the forbidden $n$-grams that correspond to each one of the conditions.

1. start with *de-*
    1. *{{{L}}} {{{R}}}*
    1. *{{{L}}} nature*
    1. *{{{L}}} -al*
    1. *{{{L}}} -ize*
    1. *{{{L}}} -ation*
1. *de-* is followed by *nature*
    1. *de- {{{R}}}*
    1. *de- de-*
    1. *de- -al*
    1. *de- ize*
    1. *de -ation*
1. *nature* is followed by *-al*
    1. *nature {{{R}}}*
    1. *nature de-*
    1. *nature nature*
    1. *nature -ize*
    1. *nature -ation*
1. *-al* is followed by *-ize*
    1. *-al {{{R}}}*
    1. *-al de-*
    1. *-al nature*
    1. *-al -al*
    1. *-al -ation*
1. *-ize* is followed by *-ation*
    1. *-ize {{{R}}}*
    1. *-ize de-*
    1. *-ize nature*
    1. *-ize -al*
    1. *-ize -ize*
1. end with *-ation*
    1. *-ation de-*
    1. *-ation nature*
    1. *-ation -al*
    1. *-ation ize*
    1. *-ation -ation*

Hmm, that didn't turn out as succinctly as one might have hoped.

## From negative to positive grammars...

The negative bigram grammar above is much larger than one would expect.
Perhaps even more problematically, it does not clearly express the relevant generalizations.
Intuitively, it would be much more appealing to list what combinations are allowed, rather than forbidden:

1. start with *de-*
    1. *{{{L}}} de-*
1. *de-* is followed by *nature*
    1. *de- nature*
1. *nature* is followed by *-al*
    1. *nature -al*
1. *-al* is followed by *-ize*
    1. *-al -ize*
1. *-ize* is followed by *-ation*
    1. *-ize -ation*
1. end with *-ation*
    1. *-ation {{{R}}}*

This is a **positive $n$-gram grammar**, where the $n$-grams list what sequences are allowed, rather than forbidden.

::: example
The list of bigrams above is *{{{L}}} de-*, *de- nature*, *nature -al*, *-al -ize*, *-ize -ation*, *-ation {{{R}}}*.
If this is interpreted as a positive bigram grammar, then only *denaturalization* is well-formed.
A string like *nature -al -ize -ation -de* is illicit because it contains the bigram *-ation de-*, which is not part of the positive grammar and thus forbidden.
If one adds *nature {{{R}}}* to the grammar, then *nature* can also be generated.
:::

In positive $n$-gram grammars, all $n$-grams must be of the same length to avoid inconsistencies.
That's because with a positive $n$-gram grammar, a word is well-formed iff each one of its $n$-grams is part of the grammar.

::: example
Suppose we want to allow both *natural* and *denaturalization*, but not *denatural*.
In order to allow the former, the grammar has to contain the bigrams *{{{L}}} nature*, *nature -al*, and *-al {{{R}}}*.
But in combination with the bigrams from the previous example, this would also allow for *denatural*.
Instead, then, one might try replacing *{{{L}}} de-* with the 5-gram *{{{L}}} de- nature -al -ize*, so that the grammar looks as follows:

- *{{{L}}} de- nature -al -ize*
- *de- nature*
- *nature -al*
- *-al -ize*
- *-ize -ation*

But then it is unclear how the grammar should be evaluated.
If we look at all the 5-grams of *{{{L}}} de- nature -al -ize -ation*, then only *{{{L}}} de -nature -al -ize* is part of the grammar and the string is incorrectly ruled out.
If we instead look at all the bigrams, then the word is ruled out because *{{{L}}} de-* is no longer part of the grammar.
Either way the mixing of bigrams and 5-grams causes inconsistencies.
:::

Despite the requirement to stick with one fixed length of $n$-grams, positive grammars can be much smaller than negative ones.
But the opposite is also true, in particular for mixed negative grammars.
It depends on the specific phenomenon.

::: exercise
Many languages only allow syllables of the form *CV*, where C is some consonant and V is a vowel.
In these languages, words are of the from *CV*, *CVCV*, *CVCVCV*, and so on.
Write both a positive and a negative grammar that only allows strings of this form.
Is one grammar significantly smaller than the other?

::: solution
The positive grammar contains

- {{{L}}}C
- CV
- VC
- V{{{R}}}

The negative grammar is of the form

- {{{L}}}V
- CC
- VV
- C{{{R}}}
- {{{L}}}{{{R}}} (which is needed to rule out the empty string)

The two grammars are of comparable size.
:::

:::

::: exercise
Continuing the previous exercise, suppose that we use actual consonants and vowels instead of the abstract symbols C and V.
Assume that the language has 5 consonants (*p*, *t*, *k*, *s*, *f*) and only one vowel (*a*).
So this language allows strings like *papa* or *tasa*, but not *tas*, *psafa*, or *saaka*.
Write both a positive and a negative grammar that only allows strings of this form.
Is one grammar significantly smaller than the other?

::: solution
We have to replace each bigram with a list of bigrams based on the available substitutions for C and V.

The positive grammar now contains

- instead of {{{L}}}C: {{{L}}}p, {{{L}}}t, {{{L}}}k, {{{L}}}s, {{{L}}}f
- instead of CV: pa, ta, ka, sa, fa
- instead of VC: ap, at, ak, as, af
- instead of V{{{R}}}: a{{{R}}}

The negative grammar now contains

- instead of {{{L}}}V: {{{L}}}a
- instead of CC: pp, pt, pk, ps, pf, tp, tt, tk, ts, tf, kp, kt, kk, ks, kf, sp, st, sk, ss, sf, fp, ft, fk, fs, ff
- instead of VV: aa
- instead of C{{{R}}}: p{{{R}}}, t{{{R}}}, k{{{R}}}, s{{{R}}}, f{{{R}}}
- still {{{L}}}{{{R}}} (which is needed to rule out the empty string)

The positive grammar with 16 bigrams is now only half the size of the negative grammar with 33 bigrams.
If we increased the number of vowels, that would bring the positive grammar closer to the negative one.
Quite generally, if the number of vowels and consonants is the same, then the negative grammar will be larger than the positive one by one bigram (which is {{{L}}}{{{R}}}).
The larger the difference between the number of vowels and the number of consonants, the more the size of the negative grammar will exceed that of the positive grammar.
:::
:::

::: exercise
For each one of the following phenomena, write a positive $n$-gram grammar that handles it correctly.
For some of them, you have to rephrase the phenomenon as a phonotactic constraint first.
You will also have to make assumptions about the sound inventory of the language.

- **intervocalic voicing**: voiceless fricatives (assume *s* and *f*) may not occur between vowels (assume *a*, *i*, *u*)
- **local assimilation**: *n* must be *m* before *b* or *p*
- **local disimilation**: *rVr* becomes *lVr*, where *V* is *a*, *i*, or *u*
- **penultimate stress**: in words with at least two syllables, stress falls on the last but one syllable (assume that words are strings of stress syllables ($\acute{\sigma}$) and unstressed syllables ($\sigma$))

Once you're done, contrast the positive grammars against the negative ones from an earlier exercise.
Can you identify some general guidelines for when a positive grammar is preferable to a negative one?

::: solution
This exercise requires a lot more assumptions than the one for negative grammars.
The problem is that it is not enough to know how intervocalic voicing works, we also have to know what the rest of the language looks like.
Consider the case of intervocalic voicing.
With the negative grammar, it was enough to say that *s* and *f* may not occur between the vowels *a*, *i*, and *u*.
With the positive grammar, we instead have to allow for every possible trigram except the ones where *s* or *f* occurs between *a*, *i* and *u*.
But we do not actually know what the set of all possible trigrams is because the exercise does not specify the alphabet.
If the alphabet contains only *a*, *i*, *u*, *s*, *f*, and *k*, then the set of possible trigrams is much smaller compared to an alphabet that also contains all the other consonants of English.

For this reason, each answer must always specify the assumed alphabet.
And ideally, this alphabet will be small to reduce the number of *n*-grams that need to be written down.
Even then, though, these grammars will be very large.
They contain all possible $n$-grams except the ones that were listed in the negative grammar.
:::

:::

## ...and back: Translating between positive and negative grammars

We now have two different kinds of $n$-gram grammars: positive grammars, and negative grammars.
The latter actually span two subtypes, strict negative grammars and mixed negative grammars, but as we have already proved those two are equivalent in the sense that one can freely translate between them.
The same is in fact true for positive and negative grammars.

The idea is very simple.
Suppose that your alphabet (i.e. the set of symbols from which strings are built) contains only *a* and *b*.
Then consider the language $(\mathit{aba})^+$, which contains *aba*, *ababa*, *abababa*, and so on.
The negative grammar generating this language consists of

1. *{{{L}}}{{{R}}}* (no string without any symbols),
1. *{{{L}}}b* (don't start with *b*),
1. *aa* (don't have *a* followed by *a*),
1. *bb* (don't have *b* followed by *b*),
1. *b{{{R}}}* (don't end with *b*).

The positive grammar, on the other hand, contains

1. *{{{L}}}a* (you may start with *a*),
1. *ab* (*a* may be followed by *b*),
1. *ba* (*b* may be followed by *a*),
1. *a{{{R}}}* (you may end with *a*).

Now compare this to the list of all possible bigrams over *a*, *b*, and the edge markers {{{L}}} and {{{R}}}.
Useless bigrams such as {{{R}}}{{{L}}}, which can never occur in a string, are listed in parenthesis.

|                  |            |              |                  |
| :-:              | :-:        | :-:          | :-:              |
| ({{{L}}}{{{L}}}) | {{{L}}}a   | {{{L}}}b     | {{{L}}}{{{R}}}  |
| (a{{{L}}})       | aa         | ab           | a{{{R}}}         |
| (b{{{L}}})       | ba         | bb           | b{{{R}}}         |
| ({{{R}}}{{{L}}}) | ({{{R}}}a) | ({{{R}}}b)   | ({{{R}}}{{{R}}}) |

Notice anything?
With the exception of the useless bigrams, each bigram in this table is either in the negative grammar or in the positive one, but never in both.
Here, let me highlight it for you, with the $n$-grams of the negative grammar in *italics* and those of the positive grammar in **boldface**.

|                  |                |              |                  |
| :-:              | :-:            | :-:          | :-:              |
| ({{{L}}}{{{L}}}) | **{{{L}}}a**   | *{{{L}}}b*   | *{{{L}}}{{{R}}}* |
| (a{{{L}}})       | *aa*           | **ab**       | **a{{{R}}}**     |
| (b{{{L}}})       | **ba**         | *bb*         | *b{{{R}}}*       |
| ({{{R}}}{{{L}}}) | ({{{R}}}a)     | ({{{R}}}b)   | ({{{R}}}{{{R}}}) |

So in order to convert a positive grammar to a negative one, or the other way round, it suffices to first compute all possible $n$-grams and then remove all those that are in the original grammar.
The remainder (*modulo* useless $n$-grams) is the corresponding grammar of the opposite polarity.


::: example
Suppose our alphabet contains only *a* and that the only well-formed string is *aa*.
This would be the case if we have a positive trigram grammar containing:

- *{{{L}}}{{{L}}}a*
- *{{{L}}}aa*
- *aa{{{R}}}*
- *a{{{R}}}{{{R}}}*

The set of all possible (and useful) trigrams over the alphabet is as follows:

- *{{{L}}}{{{L}}}a*
- *{{{L}}}{{{L}}}{{{R}}}*
- *{{{L}}}aa*
- *{{{L}}}a{{{R}}}*
- *{{{L}}}{{{R}}}{{{R}}}*
- *aaa*
- *aa{{{R}}}*
- *a{{{R}}}{{{R}}}*

Removing all trigrams of the positive trigram grammar leaves us with the following list:

- *{{{L}}}{{{L}}}{{{R}}}*
- *{{{L}}}{{{R}}}{{{R}}}*
- *{{{L}}}a{{{R}}}*
- *aaa*

You can verify for yourself that a negative trigram grammar that contains those four trigrams (and no other $n$-grams) can only generate *aa* over the alphabet $\setof{a}$.
:::

``` jupyterpython
from itertools import product

def all_ngrams(alphabet, n):
    """Build all n-grams over alphabet."""
    # for n = 0, we want the empty set rather than {''}
    if n == 0:
        return set()
    else:
        return set(''.join(ngram)
                   for ngram in product(alphabet, repeat=n))

def posneg_conversion(grammar, alphabet, n):
    """Convert between positive and negative n-gram grammars.
    
    Arguments
    ---------
    grammar: set
        grammar that is to be converted
    alphabet: set
        alphabet for the grammar
    n: int
        length of n-grams
    """
    return all_ngrams(alphabet, n) - grammar

neg_gram = set(['aa', 'ba'])
alphabet = set(['a', 'b', '$'])
pos_gram = posneg_conversion(neg_gram, alphabet, 2)

print("The original grammar is:")
print(neg_gram)
print("The opposite polarity version is:")
print(pos_gram)
```

::: exercise
English allows for *nature*, *natural*, *naturalize*, *denature*, *denaturalize*, *naturalization*, and *denaturalization*, but not *denatural* or any of misordered forms like *naturizalation*.
Write a grammar that generates all the well-formed forms but none of the ill-formed ones.
It is up to you whether you want to use a positive or a negative grammar.
If you use a negative grammar, it can be in the mixed format, with $n$-grams of varying lengths.

::: solution
A mixed negative grammar is the easiest option here.
As our alphabet, we assume the morphemes *de-*, *nature*, *-al*, *-ize*, and *-ation*.
The negative grammar then contains the following $n$-grams:

1. You must start with *de-* or *nature*: {{{L}}} -al, {{{L}}} -ize, {{{L}}} -ation
1. *de-* can only be followed by *nature*: de- de-, de- -al, de -ize, de -ation, de {{{R}}}
1. *nature* can only be followed by *-al* or the end of the word: nature de-, nature nature, nature -ize, nature -ation
1. *-al* can only be followed by *-ize* or the end of the word: -al de-, -al nature, -al -al, -al -ation
1. *-ize* can only be followed by *-ation* or the end of the word: -ize -de, -ize nature, -ize -al,  -ize -ize
1. *-ation* can only be followed by the end of the word: -ation -de, -ation nature, -ation -al, -ation -ize, -ation -ation
1. Do not end in *denature* or *denatural*: de- nature {{{R}}}, de- nature -al {{{R}}}
:::

:::

## The moral of more is more

The next section will give a formal proof that the simple conversion strategy laid out above will always result in an equivalent grammar.
By "equivalent" we mean that the two grammars generate exactly the same strings --- there is no string such that the two grammars disagree on whether the string is well-formed or ill-formed.
This might seem like a mathematical curiosity to you, but it actually challenges one of the most fundamental assumptions of theoretical linguistics.

Linguists like to talk about **the** grammar, **the** right description, **the** correct generalization. **the** feature system, **the** constraints of the grammar, as if those were concrete objects of a singular nature --- like a chair is a chair is a chair.
Linguistics is driven by the search for **the** correct description of linguistic knowledge.
Linguists want the "source code" of the language program that runs in the human brain, not just any implementation that exhibits the same behavior.
To a linguist, true understanding of language is achieved when we have found the one and only true model.
If it looks like we have multiple equally viable analyses, descriptions, theories, or formalisms, then that just shows that we don't know enough about language yet to tease them apart.
Our mathematical findings show us that things aren't that simple, this quest for **the** one unique correct specification does not work for abstract concepts.
And all linguistic concepts are abstract.
When dealing with abstract ideas, you want to be able to conceptualize them in as many distinct ways as possible.
True understanding comes from the ability to describe one and the same thing in many different ways, each one with its unique advantages and its unique opportunities for new insights.

Now you might say that there is more linguistic data than just what strings are well-formed or ill-formed, and perhaps that data will tell us exactly is going on with language in the human mind.
For example, we can put native speakers into fMRI machines to get an inkling of an idea of what computations occur in a native speaker's brain when they are asked to determine whether a word is well-formed.
But the data one obtains this way is very different in nature from the models linguists operate with.
The brain data has to be given a specific interpretation in order to link it to linguistic models, a **linking hypothesis**.
Unsurprisingly, there are many plausible linking hypotheses to choose from.
Just like there may not be such a thing as **the** correct grammar, there may not be such a thing as **the** correct linking hypothesis.
We may well be living in a world where grammar $G$ plus linking hypothesis $H$ makes exactly the same predictions as grammar $G'$ with linking hypothesis $H'$.

Rather than reject this scenario or trying to argue it away, we should embrace it.
The conventional wisdom that true understanding of language means having converged on exactly one way of looking at language has it exactly the wrong way around.
True understanding of language means having many different ways of looking at language that we can effortlessly switch between depending on which view is most useful for the problem at hand.
In some cases, a positive grammar may be smaller than a negative one.
For some phenomena it is the other way round.
A negative grammar also has the advantage that they can be made more compact by using a mixed format instead of a fixed length for all $n$-grams.
Then again, positive grammars are easier to translate to **finite-state automata**, which we will encounter in a later chapter.
Each grammar format has its pros and cons, and there is no reason why we should insist that, say, mixed negative $n$-gram grammars are the one right answer.

Interdefinability results of this kind are one of the driving forces of mathematics.
Logical formulas, for example, can be put into a normal form that is harder to read for humans but easier to implement for computers.
Finite-state automata can be viewed as a special case of Boolean matrix multiplication (we'll talk about this one in quite some detail).
Interdefinability isn't a horror scenario to avoid, it is one of the most powerful results possible, but in order to get to these results, we need mathematics.


## Recap

- A positive $n$-gram grammar is a finite list of allowed $n$-grams.
- A string is generated by a positive $n$-gram grammar iff after addition of edge markers, it contains only $n$-grams that are allowed by the grammar.
- Positive grammars can be converted to negative grammars, and the other way round.
- Having multiple descriptions of the same thing is a boon, not a bane.

\includecollection{solutions}
