---
pagetitle: >-
    Making n-grams more powerful: Phonological tiers
---

# Making n-grams more powerful: Phonological tiers

:::prereqs
- strings (parts of strings)
:::

We started this chapter with $n$-gram grammars as a basic model for studying the linguistic domains of phonotactics and morphotactics, i.e. the rules that govern the arrangement of sounds and parts of word like *un-*, *re-*, *-ly*, *-ize*, *-ation*, *-s*, and so on.
We have learned a lot about these grammars.
Positive and negative grammars are equally powerful, and the larger the value of $n$, the more patterns can be captured with $n$-gram grammars.
But we also saw that grammar size grows exponentially as we increase $n$.
Ideally, we don't end up positing grammars whose number of $n$-grams exceeds the number of seconds since the Big Bang.
So is there something like a small cutoff point of language, some value of $n$ that allows us to handle all aspects of phonotactics and morphotactics?
The answer is No.
The problem isn't just that there isn't a small cutoff point, there does not seem to be such a cutoff point at all!
There are phenomena that we cannot capture with our current $n$-gram grammars no matter how large a value of $n$ we pick.
That's not good, but not overly hard to fix either.

## The limits of $n$-gram grammars

We already know that (positive/negative) $n$-gram grammars can be used to describe various kinds of conditions on natural language phonotactics and morphotactics.
This includes word-final devoicing, intervocalic voicing, or penultimate stress, where primary stress must fall on the last but one syllable in a word.
For some patterns, though, $n$-gram grammars can be really clunky.

::: example
Vowel harmony is a common phenomenon where certain vowels cannot co-occur in a given word.
This happens in Hungarian, Finnish, Korean, and many other languages.
Take the case of Korean.
Korean distinguishes three classes of vowels: bright (B), mid dark (M), and high dark (H).
Let us ignore H for now and consider only words where all vowels belong to class B or to class M.
This is actually an exclusive *or*:  no word may mix vowels of class B with vowels of class M.
Can we express this with an $n$-gram grammar?
Yes, but it isn't exactly nice.

First, we need to consider the Korean syllable template.
The most complex syllables in Korean are of the form CGVC, where V is a vowel, C is a consonant, and G is a subtype of consonant called a *glide*.
In addition, there is also a constraint that no two vowels can be separated by more than two consonants.
All we have to do, then, is to rule out that these two vowels belong to different classes, which we can do very easily with a mixed negative $n$-gram grammar:

- BM
- MB
- BCM
- MCB
- BCCM
- MCCB

This looks pretty neat, so why did I say that $n$-gram grammars do not handle this well?
The problem is that we are cheating by using abstract classes like B, M, C, and G.
In order to truly capture what combinations are allowed, we have to use the real sounds instead.
Korean has 19 consonants, which means that the 4-gram BCCM actually corresponds to $19 \times 19 = 361$ 4-grams.
Actually, it's even more than that because we haven't yet replaced the abstract symbols B and M by the corresponding vowels.
Even if we refrain from doing that and only replace C in each $n$-gram with all possible consonants, we are looking at over 700 $n$-grams.
Replace B and M and the count will be in the thousands, and if you want to pad everything out to $4$-grams to get a strict negative $n$-gram grammar, it will be in the tens of thousands.
:::

That an $n$-gram grammar of Korean vowel harmony needs so many $n$-grams does not seem right, for two reasons.
First, it is strange that a simple and natural process like vowel harmony cannot be stated in a unified fashion and should require tons of $n$-grams.
Second, it is even stranger that the number of consonants should impact how elegantly we can describe vowel harmony.
Vowel harmony does not care about consonants, so why should the appeal of our model hinge on the language's consonant inventory?

::: example
For an even more extreme example, consider the case of **Samala**, which belongs to the group of Chumash languages spoken in southern California.
Samala displays a constraint known as **long-distance sibilant harmony**.
Sibilants are sounds like *s* and *ʃ* (ʃ is the IPA symbol corresponding to English *sh*).
All sibilants in a Samala word, no matter how far apart they are, must agree in a specific property called anteriority.
This means that a word can certainly contain multiple instances of *s* or multiple instances of *ʃ*, but it may never contain a mixture of the two.
So *haʃxintilawaʃ* is well-formed, whereas *hasxintilawaʃ* and *haʃxinitilawas* are both ill-formed.
The form *hasxintilawas*, while not an actual word of Samala, would also obey the sibilant harmony constraint.

Even a 10-gram grammar cannot capture these contrasts.
A negative 10-gram grammar that generates both *hasxinitilawas* and *haʃxintilawaʃ* must not forbid any of the following:

- *sxintilawa*
- *xintilawas*
- *ʃxintilawa*
- *xintilawaʃ*

But then this grammar would also allow for the illicit *hasxintilawaʃ* and *haʃxintilawas*.
Only an 11-gram grammar could capture the contrast.
:::

::: exercise
Write an 11-gram grammar that generates... you know what, no, don't do that, life is too short to write 11-gram grammars.
Instead, try to estimate how many $11$-grams a negative $n$-gram grammar would need so that it can generate
*hasxintilawas* and *haʃxintilawaʃ* but still rules out *hasxintilawaʃ* and *haʃxinitilawas*.
You may make the following simplifying assumptions:

- The only vowels and consonants are those that occur in the words above.
- There are no restrictions on the syllable template.
  That is to say, each position may be any one of the available vowels and consonants irrespective of the surrounding context.
:::

::: exercise
Actually, Samala has even longer words with instances of sibilant harmony.
For example, *ʃtajanowonowaʃ* is attested whereas *stajanowonowaʃ* is illicit.
Are 11-grams still enough to handle this?
If not, what is the new value of $n$, and how does that alter your estimate of a negative $n$-gram grammars size?
Would you say that this is a large grammar?
:::

Samala's long-distance sibilant harmony can be handled by $n$-gram grammars, but not in an elegant fashion.
Moreover, it only works because we assume that there is some upper bound $k < n$ such that sibilants in a Samala word are never separated by more than $k$ symbols.
That is technically true, but the value of $k$ may increase as new words are added to the language.
If that causes $k$ to become larger than $n$, the whole $n$-gram grammar would have to be tossed out and be replaced with one that uses a larger $n$.
Again this does not seem right.
The shape of our sibilant harmony grammar should not be contingent on a completely unrelated property such as the length of the longest word in Samala.
But we cannot do away with this unrelated property: without an upper bound on the distance between sibilants, sibilant harmony simply cannot be captured by any $n$-gram grammar.

::: example
Let us return to Korean vowel harmony one more time in order to illustrate the problem.
This time around, we will also consider the high dark vowels in class H.
These are neutral vowels, which means that they can occur together with bright (B) or mid dark (M) vowels.
So possible Korean words are CBCHCHCB and CMCHCHCM, among many others, but not CBCHCHCM or CMCHCHCB, where we have B and M in the same word, albeit separated by several neutral vowels.
The only way we can capture this with an $n$-gram grammar is to assume that there is some upper bound $k$ such that at most $k$ syllables in a row may contain H instead of B or M.

Suppose no such bound exists.
Then the following two strings must be well-formed, for arbitrary $k$.

- CB(CH)^k^CB
- CM(CH)^k^CM

The following string, however, should be ill-formed because we are mixing B and M:

- CB(CH)^k^CM

In order to rule out this string, we need to forbid at least one of the $n$-grams of ${{{L}}}^{n-1}$CB(CH)^k^CM${{{R}}}^{n-1}$.
But as long as $k > n$, every $n$-gram of
${{{L}}}^{n-1}$CB(CH)^k^CM${{{R}}}^{n-1}$
is also an $n$-gram of
${{{L}}}^{n-1}$CB(CH)^k^CB${{{R}}}^{n-1}$
or
${{{L}}}^{n-1}$CM(CH)^k^CM${{{R}}}^{n-1}$
(or both).
Consequently, it is impossible for an $n$-gram grammar to rule out CB(CH)^k^CM without incorrectly ruling out at least one of CB(CH)^k^CB and CM(CH)^k^CM.
:::

The only way to handle all these phenomena with $n$-gram grammars is to stipulate the existence of a fixed upper bound.
That is because $n$-gram grammars can only handle locally bounded dependencies, and stipulating an upper bound like a maximum length for words ensures that everything is a locally bounded dependency.
While doing so does get the job done, it results in giant, hideous grammars that do not capture the essence of the phenomenon and that have to be adapted and changed as the assumed upper bound changes.
For all intents and purposes, this is a horrible way of handling these phenomena.


## Phonological tiers allow for smaller grammars

If you have some background in phonology, you might already be thinking that there is a very simple solution to all this: **tiers**.
In phonological theory, tiers are substructures that represent only specific parts of a word.
Simplifying somewhat, we can model tiers as a particular kind of **subsequence**.

::: example
Consider once more the string *haʃxintilawaʃ*.
Its **vowel tier** is the subsequence that contains all vowels but omits all other sounds: *aiiaa*.
Note that the vowels appear in exactly the same order in the tier and the word itself.
:::

::: exercise
The consonant tier contains all symbols that aren't vowels.
What is the consonant tier of *haʃxintilawaʃ*?
:::

Tiers provide us with a new yet familiar way of using $n$-gram grammars.
For any given string, we project a tier that contains only the types of symbols that we care about and use an $n$-gram grammar to regulate the shape of that tier.

::: example
For sibilant harmony we want to construct a sibilant tier. 
As its name suggests, the sibilant tier contains all sibilants (*s* and *ʃ*) and nothing else.
In order to enforce sibilant harmony, we require this tier to be well-formed according to the negative bigram grammar that forbids *sʃ* and *ʃs*.
That's one darn small grammar.

The sibilant tier of the well-formed *hasxintilawas* is *ss*, which is allowed by the negative $n$-gram grammar.
The illicit *hasxintilawaʃ*, on the other hand, has the ill-formed sibilant tier *sʃ*.

~~~ {.include-tikz size=mid}
tier_good.tikz
~~~
~~~ {.include-tikz size=mid}
tier_bad.tikz
~~~

:::

::: exercise
Carry out the same calculations for

- *haʃxintilawaʃ*,
- *haʃxinitilawas*, and
- *ʃtajanowonowaʃ*.

That is to say, write down their sibilant tiers (or draw them), and then indicate whether the tier is well-formed or ill-formed according to the negative bigram grammar above.
:::

::: exercise
As an abstract example, suppose that our alphabet consists of $a$, $b$, and $c$, and that all symbols except $c$ should be projected on a tier (which we might call the *a-b*-tier).
What is the tier of $\String{aabaccacb}$?
:::

::: example
Tiers also provide a solution for Korean vowel harmony.
Let us once again consider only words that do not contain any instances of the neutral vowel H.
We construct a vowel harmony tier that contains every instance of B and M, and nothing else.
For example, a word of the form CGBCBCM would have the vowel harmony tier BBM.
On the vowel harmony tier, there must be no occurrences of BM or MB, which can easily be enforced by a negative bigram grammar.
:::

::: exercise
For each one of the strings below, construct its vowel harmony tier and say whether the tier is well-formed according to the negative bigram grammar above.

- CBCGBCB
- CGMCBCM
- CB
:::

::: exercise
Now let us also consider words with the neutral vowel class H, for instance the illicit CBCHCHCM.
Do we need to make any modifications to the vowel harmony tier or the negative bigram grammar?
If so, what are those modifications?
:::

::: exercise
For each one of the following, say whether it is true or false.
Justify your answer.

- The size of the negative bigram grammar regulating the vowel harmony tier is not contingent on the syllable structure of Korean.
- The size of the negative bigram grammar regulating the vowel harmony tier is not contingent on the number of consonants in Korean.
- The size of the negative bigram grammar regulating the vowel harmony tier is not contingent on the number of vowels in Korean.
- The size of the negative bigram grammar regulating the vowel harmony tier is not contingent on any fixed upper bound on the length of words.
:::

As you can see from those examples (and exercises), tiers are a wonderful addition to our toolbox.
They endow $n$-gram grammars with the ability to handle long-distance phenomena without unappealing assumptions such as an upper bound on the length of words.
Instead of applying directly to the string, the $n$-gram grammar instead regulates the shape of a tier.
Since the tier does not contain symbols that can never matter for the dependency, the grammar can state the relevant generalizations more succinctly without mentioning irrelevant material.
And as we will see in the next unit, tiers are a very minimal addition that preserve many of the properties we have previously established for $n$-gram grammars.

## Recap

- No $n$-gram grammar provides an elegant account of long-distance phenomena.
- The larger the $n$-grams, the larger the grammar; large grammars are unwieldy and inefficient.
- Phonological **tiers** allow for more compact grammars by filtering out irrelevant material.
- A tier is a specific type of subsequence that contains all symbols of a specific type, and only those.
- Unless one assumes an upper bound on the length of long-distance dependencies, $n$-gram grammars without tiers cannot capture certain phenomena.
