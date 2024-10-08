---
pagetitle: N-gram models of grammaticality
---

# N-gram models of grammaticality

This unit presents a very simple model of language.
As you will see, even simple models can give rise to complex questions, questions that cannot easily be answered without math.
It might not look like the math you know from high school, but it is still math (some might say it is the high school math that barely qualifies as math because it is about calculating rather than reasoning).

If you already have some mathematical experience, you might want to skip two sections ahead and only come back here to see the linguistic motivation for the mathematics.
And the trained linguist may find some of the content here overly simplistic, but we will move on to more intricate problems as our mathematical toolkit grows.

## A simple fact about English

English has a large number of different sounds, but not all combinations are possible.
For instance, *blink* is a word but *kbinl* is not.
And *kbinl* will never be a word of English because it does not obey English **phonotactics**, i.e. the laws that govern in what order sounds may be arranged.
This is what separates *kbinl* from *kobinal* or *karbinolium*.
None of them are existing words of English, but *kobinal* and *karbinolium* are potential words.
We can give them a meaning, start using them, and no native speaker of English will have a problem picking them up.
These words obey the phonotactic laws of English, whereas *kbinl* violates the requirement that English words cannot start with *kb*.

The knowledge of English phonotactics is what allows native speakers to coin new terms that fit in with the rest of the vocabulary.
It is also what makes it hard for English speakers to learn other languages.
German, for example, is very happy to start a word with *k* and *n*, as in *Knoblauch*, the German word for garlic. 
English has words that are spelled with *kn* at the start, like *knight*, but the *k* is never pronounced.
In terms of pronunciation, *knight* and *night* are the same word, and a native speaker of English would never pronounce *knight* with a *k* at the beginning.
Phonotactics is one of the most basic aspects of **natural language**.
By natural language I mean languages like English, Chinese, Tongan, Inuktitut, various dialects of Italian, or the specific language that you grew up with.
This is in contrast to **formal languages**, which includes languages designed by humans (e.g. Esperanto, Klingon, Quenya), programming languages like Python or Brainfuck (yes, seriously), or the strands of DNA in your body (yes, we can describe that mathematically as a particular kind of language).
Linguists seek to gain a deeper understanding of the laws, principles, and regularities of natural languages, and this includes the laws of natural language phonotactics.
Linguists want to do this at both the language-specific level and across languages, and this yields very different questions even if we consider just phonotactics:

- **Language specific**: What are the phonotactics of English? German? Language X?
- **General**: What is a possible phonotactic system? What shape can the laws of phonotactics take? What kind of logically conceivable systems of phonotactics can never occur in a natural language?

In order to tackle these questions in a precise manner, we need a formal model of phonotactics.
What might that be?
One plausible assumption is that a word is phonotactically well-formed iff none of its subparts are ill-formed.
So *kobinal* is a possible word because there is nothing wrong with a word that starts with *kobina*, has *obina* in the middle, and ends with *obinal*.
But this just raises the question why *kobina* is an acceptable start, and *obina* is a well-formed middle, and *obinal* is an acceptable end.
Well, because their subparts are fine.
For example, *kobina* is fine because a word can start with *kobin* and have *obin* in the middle and *bina* at the end.
Then why can a word start with *kobin*?
Well, because its subparts are fine: a word can start with *kobi*, have *obi* in the middle, and *obin* at the end.
As you can already see, we can play that game for a long time, breaking well-formed parts into smaller well-formed parts.

But eventually, things will break down.
If we want to know why *ko* is a good start, it's not enough to say that words can start with *k* and have *o* in the middle.
Because it is also true that words can start with *k* and have *b* in the middle (as in *kobinal*), yet *kbinal* is not okay even though it starts with *k* and has a *b* in the middle.
By looking at individual sounds, we have decomposed things too much to capture the phonotactics of English.
So let's take one step up and consider pairs of consecutive sounds.
In more technical terms, let's describe English phonotactics in terms of **bigrams**.

## Bigrams

### Extracting bigrams

A bigram is a string of two elements.
For phonotactics, the elements are sounds (to all trained linguists: we do not need to distinguish between phones, allophones, or phonemes yet, so please don't get your panties in a twist).
Examples of bigrams include *ko*, *ob*, or *bn*.
A given word's **set of bigrams** is the collection of all bigrams that occur in it, without repetitions.

::: example
The bigrams of
*kobinal*
are *ko*, *ob*, *bi*, *in*, *na*, and *al*.
The bigrams of *banana* are *ba*, *an*, and *na*.
:::

``` jupyterpython
def bigrams(word):
    return sorted(list(set(''.join(bigram)
                           for bigram in zip(word,word[1:]))))

def bigram_print(word):
    print("The bigrams of", word, "are:")
    print(bigrams(word))

bigram_print("kobinal")
bigram_print("banana")
# try some words of your own
bigram_print("wordone")
bigram_print("wordtwo")
```

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

::: solution_explained
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

:::

### Adding edge markers

One shortcoming of this simple notion of bigrams is that one cannot tell which bigrams occurred at the beginning and the end of the word.
For example, *ababa* and *babab* have the same bigrams, *ab* and *ba*.

``` jupyterpython
def bigrams(word):
    return sorted(list(set(''.join(bigram)
                           for bigram in zip(word,word[1:]))))

def bigram_print(word):
    print("The bigrams of", word, "are:")
    print(bigrams(word))

bigram_print("ababa")
bigram_print("babab")
```

But for phonotactics it is actually important to know how a word starts and how it ends.
We already saw that in our discussion of word-initial *kn* in German.
English is perfectly fine with *kn* when it is not at the beginning of a word, e.g. in *acknowledge*.
But at the beginning of a word English phonotactics bring out the banhammer and just won't allow *kn*.
The beginning and the end of words seems to be privileged positions, and our current notion of bigrams does not allow us to capture that.

We have to expand our notion of bigrams a bit, then. 
Concretely, we will add edge markers to indicate the left or right edge of a word.
One could use a single edge marker like *\$*.
In that case, *ababa* would be *\$ababa\$*, and *babab* would be *\$babab\$*.
But once we dive deeper into the mathematics, it will be more convenient to have separate markers: {{{L}}} for the left edge and {{{R}}} for the right edge.
This means that *ababa* will be *{{{L}}}ababa{{{R}}}*, and *babab* will be *{{{L}}}babab{{{R}}}*.

Now one can tell clearly which sounds occurred at the start and the end.

::: example
To calculate the bigrams of *kobinal*, we first expand it to *{{{L}}}kobinal{{{R}}}*.
Then we extract bigrams as usual, giving us the following list: *{{{L}}}k*, *ko*, *ob*, *bi*, *in*, *na*, *al*, *l{{{R}}}*.
:::

``` jupyterpython
def bigrams(word):
    word = "$" + word + "$"
    return sorted(list(set(''.join(bigram)
                           for bigram in zip(word,word[1:]))))

def bigram_print(word):
    print("The bigrams of", word, "are:")
    print(bigrams(word))

bigram_print("ababa")
bigram_print("babab")
```

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

::: solution_explained
Once we consider edge markers, the long list of bigrams from the previous solution gains two new members: *{{{L}}}s* and *s{{{R}}}*.
Bigrams that were already on the original list without edge markers are still bigrams, so *fr* is still a bigram of *supercalifragilisticexpialidocious*.
Similarly *n*-grams that do not consist of exactly two symbols are still not possible bigrams, which rules out *z* (only 1 symbol) and *s{{{R}}}{{{R}}}* (3 symbols).
This leaves us with {{{L}}}{{{R}}} and {{{L}}}s.
The latter is one of the two new members, but the former is not.
In fact, {{{L}}}{{{R}}} can never be a bigram of any string that consists of one or more symbols.
:::

:::

:::

(For particularly observant readers: Yes, bigrams with edge markers are still not quite enough to detect that the consonant cluster *kn* occurred at the beginning of a word, but we will get there soon.)

## Bigram grammars

Now that we have a firm grasp of bigrams, it is actually fairly easy to formulate our first hypothesis about natural language phonotactics: every phonotactic system is described by a set of forbidden bigrams.
If a word contains at least one forbidden bigram, it is illicit.
We call such a collection of forbidden bigrams a **negative bigram grammar**.

If our hypothesis is correct, then it should be possible to write down a collection of bigrams for English so that all phonotactically well-formed words are allowed, and only those.
Every ill-formed word must contain at least one forbidden bigram.

::: example
Contrast the well-formed *kobinal* against the ill-formed *kbin*.
If *kb* is a forbidden bigram of English, then *kbin* is ill-formed.
In order for *kobinal* to be well-formed, none of the following bigrams may be forbidden:
*{{{L}}}k*,
*ko*,
*ob*,
*bi*,
*in*,
*na*,
*al*,
*l{{{R}}}*.
:::

As the example above shows, forbidding the bigram *kb* rules out *kbin* as an illicit word for English.
But there is a problem: *kb* does occur in some well-formed words, such as *cookbook* or *workbench*.
Linguists might object that each one of them is a compound and thus, as far as phonotactics is concerned, might be two words rather than one.
However, that does not solve the problem of Star Wars's Admiral Ackbar, pronounced *akbar*.
The problem with *kbin* is not *kb*, it's *kb* at the start of the word.
The forbidden sequence is not *kb*, but rather *{{{L}}}kb*.
And the ban against starting English words with *kn* does not mean that *kn* is a forbidden sequence, it means that *{{{L}}}kn* is forbidden.
These are not bigrams, they are **trigrams**.

## From bigram grammars to n-gram grammars

We can generalize the notion of bigram to sequences of arbitrary length.
A trigram is a sequence of three elements, a 4-gram contains four elements, and quite generally, an **n-gram** consists of **n** elements.

::: example
Let us first look at the bigrams, trigrams, and 4-grams of *kobinal* (without edge markers).
The bigrams of *kobinal* are
*ko*, *ob*, *bi*, *in*, *na*, and *al*.
The trigrams are *kob*, *obi*, *bin*, *ina*, and *nal*.
The 4-grams are *kobi*, *obin*, *bina*, and *inal*.

For *banana*, the only bigrams are *ba*, *an*, and *na*.
The trigrams are *ban*, *ana*, and *nan*.
The 4-grams are *bana*, *anan*, and *nana*.
:::

``` jupyterpython
def ngrams(word, n):
    return sorted(list(set(''.join(ngram)
                           for ngram in zip(*[word[i:]
                                              for i in range(n)]))))

def ngram_print(word, n):
    print("The {}-grams of {} are:".format(n, word))
    print(ngrams(word, n))

for n in [2, 3, 4]:
    ngram_print("ababa", n)
    ngram_print("babab", n)
    print()
```

One problem with large $n$-grams is that some words may be shorter than $n$ even after edge markers have been added.
Just what are the 4-grams of *{{{L}}}a{{{R}}}*?
There's many ways this could be fixed.
We will use a method that is conceptually simple even though may seem awkward at first: if the grammar uses $n$-grams, we pad out the word with $n-1$ edge markers.
In a later unit, you will see why this actually makes a lot of sense.

::: example
Consider now the bigrams, trigrams, and 4-grams of *kobinal* with edge markers {{{L}}} and {{{R}}}.
For bigrams, we have to look at *{{{L}}}kobinal{{{R}}}*, which has the bigrams 
*{{{L}}}k*,
*ko*,
*ob*,
*bi*,
*in*,
*na*,
*al*, and
*l{{{R}}}*.
The trigrams are computed over *{{{L}}}{{{L}}}kobinal{{{R}}}{{{R}}}*, so they're
*{{{L}}}{{{L}}}k*,
*{{{L}}}ko*,
*kob*,
*obi*,
*bin*,
*nal*,
*al{{{R}}}*,
and *l{{{R}}}{{{R}}}*.
The 4-grams are computed over *{{{L}}}{{{L}}}{{{L}}}kobinal{{{R}}}{{{R}}}{{{R}}}* and thus they are
*{{{L}}}{{{L}}}{{{L}}}k*,
*{{{L}}}{{{L}}}ko*,
*{{{L}}}kob*,
*kobi*,
*obin*,
*bina*,
*inal*,
*nal{{{R}}}*,
*al{{{R}}}{{{R}}}*,
and *l{{{R}}}{{{R}}}*.

For *banana*,
the bigrams are now
*{{{L}}}b*,
*ba*,
*an*,
*na*,
and *a{{{R}}}*.
Its trigrams are
*{{{L}}}{{{L}}}b*,
*{{{L}}}ba*,
*ban*,
*ana*,
*nan*,
*na{{{R}}}*,
and *a{{{R}}}{{{R}}}{{{R}}}*.
The 4-grams are
*{{{L}}}{{{L}}}{{{L}}}b*,
*{{{L}}}{{{L}}}ba*,
*{{{L}}}{{{L}}}ban*,
*bana*,
*anan*,
*nana*,
*ana{{{R}}}*,
*na{{{R}}}{{{R}}}*,
and
*a{{{R}}}{{{R}}}{{{R}}}*.
:::

``` jupyterpython
def ngrams(word, n):
    word = "$" * (n-1) + word + "$" * (n-1)
    return sorted(list(set(''.join(ngram)
                           for ngram in zip(*[word[i:]
                                              for i in range(n)]))))

def ngram_print(word, n):
    print("The {}-grams of {} are:".format(n, word))
    print(ngrams(word, n))

for n in [2, 3, 4]:
    ngram_print("ababa", n)
    ngram_print("babab", n)
    print()
```

::: exercise
For each one of the following strings with the appropriate number of edge markers, say whether it has been padded for use with a bigram grammar, a trigram grammar, or a 4-gram grammar.

- {{{L}}}{{{L}}}kbin{{{R}}}{{{R}}}
- {{{L}}}{{{L}}}{{{L}}}workbench{{{R}}}{{{R}}}{{{R}}}
- {{{L}}}akbar{{{R}}}

::: solution

- trigram grammar
- 4-gram grammar
- bigram grammar

::: solution_explained
As all the strings have the same number of left edge and right edge markers, they are correctly padded for some kind of $n$-gram grammar.
All we have to do, then, is to count the number of left edge markers (or alternatively, the number of right edge markers) and add $1$ to that in order to obtain the value of $n$ for the $n$-gram grammar.
:::

:::

:::

Now we can finally state clearly why *kobinal*, *workbench* and *akbar* are all phonotactically well-formed, whereas *kbin* is not: the latter contains the illicit trigram *{{{L}}}kb*.

We also refine our original hypothesis about the phonotactics of natural languages: every phonotactic system is described by a set of forbidden $n$-grams.

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

::: solution_explained

- {{{L}}}fr:
  The word starts with *su*, not *fr*, so *{{{L}}}fr* does not occur in the word.
- z:
  This is a unigram, but we are only considering bigrams, trigrams, and 4-grams.
  And even if we did consider unigrams, the word does not contain *z* at all.
- do{{{R}}}c:
  This is a 4-gram but it can never occur in any string because it is impossible to have any symbol after {{{R}}} (except additional instances of {{{R}}} itself).
- s{{{R}}}{{{R}}}{{{R}}}:
  This is a 4-gram.
  For 4-grams, we have to assume three edge markers on each side of the string, and since the word ends in *s*, the string with edge markers must indeed contain s{{{R}}}{{{R}}}{{{R}}}.
- sit:
  This is a trigram, but it does not occur in the word.
- cious:
  This is a 5-gram that occurs in the word, but we are only considering bigrams, trigrams, and 4-grams.
- {{{L}}}sup:
  This is a 4-gram and since the word starts with *sup*, *{{{L}}}sup* is indeed a 4-gram of the string once we include edge markers.
:::
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

::: solution_explained
Intervocalic voicing only occurs if *s* is surrounded by two vowels.
So the forbidden trigrams must be of the form *VsV*, where *V* is a vowel.
We have to replace each *V* in *VsV* with every possible vowel.
Since our toy Italian only has the vowels *a* and *o*, this leaves us with $2 \times 2 = 4$ possible substitutions, yielding the four trigrams above.
:::

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
In technical terms, *a* and *sociale* are two separate **morphemes**, and we should represent *asociale* more accurately as *a+sociale* with the morpheme boundary symbol *+* between *a* and *s*.
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

## A look at German

Unlike English, German is perfectly fine with words that start with *kn*.
But just like English, it does not like words that start with *rb*.
We can capture this by writing a trigram grammar for German that contains the forbidden trigram *{{{L}}}rb*.
But German also has a process known as word-final devoicing: voiced sounds become voiceless at the end of a word.
So whereas an English speaker will happily pronounce *woods* with a *z* at the end, a German speaker turns the *z* into an *s* like in *trinkets*.
Alright, no big deal, we just forbid *z{{{R}}}* too.
Or do we?

We now have a forbidden trigram *{{{L}}}rb* and a forbidden bigram *z{{{R}}}*.
Are we allowed to mix bigrams and trigrams this way?
More generally, can every negative $n$-gram grammar also contain $k$-grams, where $k < n$?
Could this create inconsistencies, or make negative $n$-gram grammars more powerful?
The answers is not obvious at this point.

::: exercise
Consider the formal language where all strings are sequences of *a*, *b*, and *c* such that

- every string starts with *a*
- no string ends with *c*
- *a* and *c* are always separated by at least two symbols.

Write a negative 4-gram grammar for this language.
**Caution:** This will be a big grammar.
Try to write down all the 4-grams, and once you get sick of it, you can use a template like "xcyc where x and y are *a* or *b* or *c*" (this specific template is just an example, it isn't needed for the constraints above).

Now that you are appropriately enraged, write an equivalent negative grammar that mixes bigrams, trigrams and 4-grams.
Which one strikes you as a more direct description of the constraints above?
Which one gave you less grief?

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
But we can do even better by replacing many of the 4-grams with trigrams.
This allows us to express more succinctly that *a must not be one symbol before c* and *c must not be one symbol before a*.

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

Even if one does not care about succinctness or stating generalizations as explicitly as possible, it is clear that the small grammar above is much less of a hassle to write down.
:::

:::

## Studying formalisms ~ studying language

Let's take stock.
We started out with some very profound questions: how can we describe the phonotactic laws we find in specific languages, and more generally, what separates a possible law of phonotactics from an impossible one?
We have proposed $n$-gram grammars as a model of phonotactics.
Even though they are very simple, they seem flexible enough to capture quite a lot of phonotactics.
We quickly realized that bigrams are sometimes too short to state the relevant conditions, but it is easy to take a step up to trigrams or 4-grams.
But we also saw that we sometimes need to use $n$-grams of different lengths, which seems quite a bit more complicated than grammars where all $n$-grams have the same length.
But that is just a hunch, we do not know whether this is actually true.

This isn't just a mathematical curiosity, it is a profound question about human cognition.
If we take seriously the notion that negative $n$-gram grammar provide a model of phonotactics, then whatever knowledge a native speaker of English has about English phonotactics is in some sense similar to our negative $n$-gram models.
Of course this involves numerous abstraction steps --- we should not expect MRIs and other tools of neuroscience to find anything like the *negative $n$-gram center* of the brain where words get broken down into their $n$-grams and each $n$-gram is checked for correctness.
But we are making a cognitive commitment that phonotactics involves reasoning steps comparable to those of a negative $n$-gram grammar and not something completely different, like keeping track of the number of consonants and penalizing words with an even number of consonants.
That kind of "even-consonant filter" would be something completely unlike what the negative $n$-gram grammars are doing, and it would be a fundamental change to what we think is going on in a speaker's mind when they determine that, say, *kbinl* is not a possible word of English.

But what about more innocuous changes like allowing $n$-grams of various lengths?
Is that just a matter of notational convenience, or does it fundamentally change the model and hence the cognitive commitments that come from adopting this model?
Or what if we used $n$-grams to encode allowed sequences rather than forbidden ones?
Intuitively this feels like a very different kind of grammar, but is it really?

Linguistics is actually full of discussions of this type.
Somebody proposes model M and then somebody else argues that M fails to account for phenomenon P in language L and needs some extension X.
But then somebody else argues that X is not needed after all because P has been misanalyzed and the more accurate description of P is perfectly compatible with the original model M.
This kind of argumentation has proven very productive for linguistics, but it is very labor intensive and the results are not very transferable.
One minor change to model M could completely change whether we need extension X after all to handle phenomenon P, and it can be difficult to tell what changes to M are such that X becomes indispensable for P.
Linguistic results tend to be very specific and detailed, but among the many pieces of data and the intricate reasoning steps it can be hard to determine what is truly essential for the argument.

Mathematics allows us to study formalisms at a more general level, and this in turn enables us to make discoveries that would be unattainable with linguistic methods.
For example, we will be able to show that allowing $n$-grams of varying length does not fundamentally change our negative $n$-gram model, and this will be true no matter how long the $n$-grams are.
We can make claims that are provably correct for every negative $n$-gram grammar.
And we can do that even though there are infinitely many such grammars (because there are infinitely many values $n$ may take) and it is impossible to ever look at each one of them.
Our mathematical proof will also tell us exactly why this fact holds and under what circumstances it would no longer go through.
And by extension, the mathematics tells us that there is a whole class of models that are equivalent to ours in terms of what they claim about the nature of an English speaker's cognitive ability to distinguish the well-formed *blink* from the ill-formed *kbinl*.
Buckle up everyone, we have some mathematical analysis to do!


## Recap

- An **n-gram** is a sequence of **n** symbols.
- The special symbols {{{L}}} and {{{R}}} are **edge markers** for the left and right edge of the word, respectively.
- A **negative $n$-gram grammar** is a finite collection of forbidden $n$-grams.
- In order to determine whether a negative $n$-gram grammar deems a given string well-formed or ill-formed, we carry out the following steps:
    1. Pad out the string with $n-1$ instances of {{{L}}} and $n-1$ instances of {{{R}}}.
    1. Look at all the $n$-grams of the string augmented with edge markers.
    1. If at least one of those $n$-grams is a forbidden $n$-gram of our negative $n$-gram grammar, the string is illicit.
       Otherwise, it is well-formed.
- Some linguistic phenomena can be captured with negative bigram grammars, some like intervocalic voicing require trigram grammars.
  Other phenomena may require even longer $n$-grams.

\includecollection{solutions}
