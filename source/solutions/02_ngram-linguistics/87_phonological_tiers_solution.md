---
pagetitle: >-
    Making n-grams more powerful: Phonological tiers (Solutions)
---

# Making n-grams more powerful: Phonological tiers (Solutions)

::: exercise
Write an 11-gram grammar that generates... you know what, no, don't do that, life is too short to write 11-gram grammars.
Instead, try to estimate how many $11$-grams a negative $n$-gram grammar would need so that it can generate
*hasxintilawas* and *haʃxintilawaʃ* but still rules out *hasxintilawaʃ* and *haʃxinitilawas*.
You may make the following simplifying assumptions:

- The only vowel and consonants are those that occur in the words above.
- There are no restrictions on the syllable template.
  That is to say, each position may be any one of the available vowels and consonants irrespective of the surrounding context.

::: solution
2 billion
:::

::: solution_explained
The two words contain 10 symbols:

1. h
1. a
1. s
1. x
1. i
1. n
1. t
1. l
1. w
1. ʃ

A negative 11-gram grammar has to contain all 11-grams that start with *s* and end with *ʃ*, of which there are $10^9 = 1,000,000,000$ because there are 9 positions between *s* and *ʃ*, each one of which can be filled by one out of the ten symbols above.
The grammar also has to contain all 11-ngrams that start with *ʃ* and end with *s*, of which there are also $10^9 = 1,000,000,000$.

Keep in mind that these are just the numbers for generating strings where *s* and *ʃ* are separated by exactly 9 symbols, as this is all that is needed for a grammar that generates *hasxintilawas* and *haʃxintilawaʃ* but not *hasxintilawaʃ* and *haʃxinitilawas*.
If we also want to cover the cases where the two sibilants are separated by less than 9 symbols, we have to add another $2 \times 9 \times 10^9$ 11-grams to the grammar, for a total of 20 billion $11$-grams.
That's quite the grammar (admittedly we could make the grammar smaller by allowing $n$-grams of varying lengths, but it would still be huge).
:::

:::

::: exercise
Actually, Samala has even longer words with instances of sibilant harmony.
For example, *ʃtajanowonowaʃ* is attested whereas *stajanowonowaʃ* is illicit.
Are 11-grams still enough to handle this?
If not, what is the new value of $n$, and how does that alter your estimate of a negative $n$-gram grammars size?
Would you say that this is a large grammar?

::: solution
The grammar now needs to use 14-grams, and the grammar would have to contain at least 2 trillion 14-grams ($2 \times 10^12 = 2,000,000,000,000$).
The grammar was already large before, but this is tremendous increase in size.
:::

:::

::: exercise
Carry out the same calculations for

- *haʃxintilawaʃ*,
- *haʃxinitilawas*, and
- *ʃtajanowonowaʃ*.

That is to say, write down their tiers (or draw them), and then indicate whether the tier is well-formed or ill-formed according to the negative bigram grammar above.

::: solution

- The sibilant tier of *haʃxintilawaʃ* is *ʃʃ*, which is well-formed.
- The sibilant tier of *haʃxinitilawas* is *ʃs*, which is ill-formed.
- The sibilant tier of*ʃtajanowonowaʃ* is *ʃʃ*, which is well-formed.
:::

:::

::: exercise
As an abstract example, suppose that our alphabet consists of $a$, $b$, and $c$, and that all symbols except $c$ should be projected on the tier.
What is the tier of $\String{aabaccacb}$?

::: solution
$\mathit{aabaab}$
:::

:::

::: exercise
For each one of the strings below, construct its vowel harmony tier and say whether the tier is well-formed according to the negative bigram grammar above.

1. CBCGBCB
1. CGMCBCM
1. CB

::: solution
1. BBB, well-formed
1. MBM, ill-formed
1. B, well-formed
:::

::: solution_explained
1. After removing all instances of C and G from the string, we are left with BBB, which does not contain any instances of the forbidden bigrams BM and MB.
1. Removal of C and G yields the vowel tier MBM, which is clearly illicit as it contains MB (and also BM).
1. After removing the single instance of C, we are left with B, which does not contain any forbidden bigrams.
:::

:::

::: exercise
Now let us also consider words with the neutral vowel class H, for instance the illicit CBCHCHCM.
Do we need to make any modifications to the vowel harmony tier or the negative bigram grammar?
If so, what are those modifications?

::: solution
No, we can keep everything as is.
Since neutral vowels do not matter for the purposes of vowel harmony, they should not be projected onto the vowel harmony tier.
This means that the illicit CBCHCHCM has the tier BM, which is correctly ruled out as illicit by our unmodified bigram grammar.
:::

:::

::: exercise
For each one of the following, say whether it is true or false.
Justify your answer.

1. The size of the negative bigram grammar regulating the vowel harmony tier is not contingent on the syllable structure of Korean.
1. The size of the negative bigram grammar regulating the vowel harmony tier is not contingent on the number of consonants in Korean.
1. The size of the negative bigram grammar regulating the vowel harmony tier is not contingent on the number of vowels in Korean.
1. The size of the negative bigram grammar regulating the vowel harmony tier is not contingent on any fixed upper bound on the length of words.

::: solution
1. True. Since we only project vowels and ignore other materials like consonants, syllables can be arbitrarily complex without affecting the shape of tiers, and consequently the bigram grammar does not need to be altered.
1. True. The size of the bigram grammar regulating the shape of tiers is independent of the number of consonants because consonants are not projected onto the tier in the first place.
1. False. While we used abstract symbols like B, M, and H, these are just shorthands for classes of vowels.
   Once we replace B, M, and H by their corresponding vowels, the number of bigrams is contingent on the overall number of vowels.
1. True. Two vowels on the vowel harmony tier can be arbitrarily far apart in the string --- for example, CBCM and CBCHCHCHCHCHCHCHCHCM have exactly the same vowel harmony tier.
:::

:::
