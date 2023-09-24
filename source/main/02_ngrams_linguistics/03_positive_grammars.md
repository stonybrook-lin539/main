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
If this is interpreted as positive bigram grammar, then only *denaturalization* is well-formed.
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
:::

::: exercise
Continuing the previous exercise, suppose that we use actual consonants and vowels instead of the abstract symbols C and V.
Assume that the language has 5 consonants (*p*, *t*, *k*, *s*, *f*) and only one vowel (*a*).
So this language allows strings like *papa* or *tasa*, but not *tas*, *psafa*, or *saaka*.
Write both a positive and a negative grammar that only allows strings of this form.
Is one grammar significantly smaller than the other?
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

Now compare this to the list of all possible bigrams over *a*, *b*, and the edge markers {{{L}}} and {{{R}}} (we ignore useless bigrams such as {{{R}}}{{{L}}}, which can never occur in a string):

1. *{{{L}}}{{{R}}}*,
1. *{{{L}}}a*,
1. *{{{L}}}b*,
1. *a{{{R}}}*,
1. *aa*,
1. *ab*,
1. *b{{{R}}}*,
1. *ba*,
1. *bb*.

Notice anything?
Each one of those bigrams is either in the negative grammar or in the positive one, but never in both.
So in order to convert a positive grammar to a negative one, or the other way round, it suffices to first compute all possible $n$-grams and then remove all those that are in the grammar that is to be converted to the opposite polarity.

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
:::

## An important take-home message

The next section will give a formal proof that the simple conversion strategy laid out above will always result in an equivalent grammar.
By "equivalent" we mean that the two grammars generate exactly the same strings --- there is no string such that the two grammars disagree on whether the string is well-formed or ill-formed.
This might seem like a mathematical curiosity to you, but it actually challenges one of the most fundamental assumptions of theoretical linguistics.

Linguists like to talk about **the** grammar, **the** right description, **the** correct generalization. **the** feature system, **the** constraints of the grammar, as if those were concrete objects of a singular nature --- like a chair is a chair is a chair.
Linguistics is driven by the search for **the** correct description of linguistic knowledge.
Linguists want the "source code" of the language program that runs in the human brain, not just any implementation that exhibits the same behavior.
To a linguist, true understanding of language is achieved when we have found the one and only true model.
If it looks like we have multiple equally viable analyses, descriptions, theories, or formalisms, then that just shows that we don't know enough about language yet to tease them apart.
Our mathematical findings show us that things aren't that simple, this quest for *the* one unique correct specification does not work for abstract concepts.
And all linguistic concepts are abstract.
When dealing with abstract ideas, you want to be able to conceptualize them in as many distinct ways as possible.
True understanding comes from the ability to describe one and the same thing in many different ways, each one with its unique advantages and its unique opportunities for new insights.

Now admittedly there is more linguistic data than just what strings are well-formed or ill-formed.
For example, we can put native speakers into fMRI machines to get an inkling of an idea of what computations occur in a native speaker's brain when they are asked to determine whether a word is well-formed.
But the data one obtains this way is very different in nature from the models linguists operate with.
The brain data has to be given a specific interpretation in order to link it to linguistic models, and there are many different plausible implementations to choose from.
Just like there may not be such a thing as **the** correct grammar, there may not be such a thing as **the** correct linking hypothesis.
We may well be living in a world where grammar $G$ plus linking hypothesis $L$ makes exactly the same predictions as grammar $G'$ with linking hypothesis $L'$.

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
