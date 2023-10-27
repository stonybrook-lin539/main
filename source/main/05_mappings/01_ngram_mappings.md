---
pagetitle: >-
    Generalizing n-grams to mappings: a failed attempt
---

# Generalizing n-grams to mappings: a failed attempt

## Underlying representations and rewrite rules

Our mathematical investigation of language started with phonotactics, i.e. the laws that govern the distribution of sounds in a word.
We chose phonotactics as our starting point because it is complex enough to run into some interesting issues, yet it is simple enough that we get to avoid many complicating factors.
But now that we are more comfortable with the mathematical view of language, it is time to confront some of these complicating factors head-on.
For instance, phonology is more than just phonotactics.
Phonology isn't really about determining whether a given string is a possible word, it is about establishing connections between strings.

::: example
We have seen several examples of word-final devoicing, e.g. in German.
The German word for *song* is *li:t* in the singular, with a voiceless *t*, but *li:dɐ* in the plural with a voiced *d* (actually, a phonetician will tell you that German has a constricted-glottis distinction rather than a voicing distinction, but that doesn't matter for this example).
Once we remove the plural marker from *li:dɐ* we are left with the stem *li:d*.
This is distinct from *li:t*, yet native speakers of German somehow know that these are both just different outputs of the same lexical item for *song*.
They know that these two forms are phonologically related to each other.
:::

Given these relations between surface forms, phonologists have argued that phonology actually involves **underlying representations** (URs) that are modified via **rewrite rules** to yield the surface forms that we actually see.

::: example
One could say that German has a UR *li:d* for *song*.
If we want the plural of that, we use a rewrite rule that appends the plural marker *ɐ* to this UR, yielding *li:dɐ*.
The singular of *li:d*, on the other hand, has no special marker, so the rule for singular would not add any pronounced material to the UR.
But this means that the UR is subject to the rewrite rule for word-final devoicing, which replaces *d* with *t*, yielding *li:t*.
Hence both *li:dɐ* and *li:t* are surface forms of the same UR *li:d*, which explains why native speakers of German can recognize them as related forms even though they only share *l* and *i:*.
:::

There are many excellent phonology textbooks that explain the appropriate use of URs and rewrite rules in great detail.
We do not need to worry about these details, but we do want to be able to say something about these proposals from a mathematical perspective.
Are they more powerful than the n-gram models we used for phonotactics?
Are there certain normal forms that we can use to make our life as researchers easier, just like we could switch between positive and negative n-gram grammars as we see fit?
Just what exactly are we claiming about phonology if we say it can be described in terms of mappings from URs to surface forms?

## N-grams for mappings

In previous chapters, it usually worked well for us to take a simple model, ideally one we have encountered before, and make some small tweaks to it in order to capture some new phenomenon.
It sure seems like a good idea, then, to try to take our familiar n-gram grammars and generalize them in a way that allows them to capture mappings.

Suppose, then, that we use an enriched format of n-grams where one specific symbol in the n-gram can be rewritten as something else.
Instead of the n-gram *abc*, we would now have a mapping n-gram *ab[d]c* to indicate that *b* can be rewritten as *d*, provided that *b* is surrounded by *a* and *c*.
Given some UR, padded out with edge markers, we build the corresponding surface form by moving through the UR from left to right and checking for each symbol $\sigma$ whether there is a matching mapping n-gram.
If there is not, we add $\sigma$ to the surface form.
But if there is such a matching mapping n-gram, we instead a new symbol to the surface form according to the rewrite specification in the mapping n-gram.

::: example
When we looked at word-final devoicing as a phonotactic constraint, we treated it as a ban against voiced segments like *d*, *v*, or *z* at the end of the word.
Formally, we captured this with the bigrams *d{{{R}}}* and *v{{{R}}}* and *z{{{R}}}*.
If we want to treat word-final devoicing as a mapping, we have to rewrite URs such that word-final *d*, *v*, and *z* become *t*, *f*, and *s*, respectively.
The corresponding bigrams look as follows:

- d[t]{{{R}}}
- v[f]{{{R}}}
- z[s]{{{R}}}

Now consider how these n-grams are used to map German *li:d* to the surface form *li:t*.
First, since they are bigrams, we have to pad out *li:d* with one edge marker on each side, yielding *{{{L}}}li:d{{{R}}}*.
Then, we move through this string from left to right, checking each symbol.
If we find a matching configuration for some symbol, we carry out the corresponding rewrite step:

- *{{{L}}}*, no match, add *{{{L}}}* to surface form
- *l*, no match, add *l* to surface form
- *i:*, no match, add *i:* to surface form
- *d*, matched by *d{{{R}}}*, add *t* to surface form
- {{{R}}}, no match, add {{{R}}} to surface form

The only matching configuration is *d{{{R}}}*, so we replace *d* with *t* while keeping everything else the same.
After removal of edge markers, we are left with *li:t*.
:::

::: exercise
The English plural marker has multiple forms that are phonologically conditioned.
Roughly speaking, we get

1. *es* after *s*, *z*, *ʃ*, and *tʃ*,
2. *s* after any other voiceless consonants (e.g. *t*, *k*),
3. *z* everywhere else (that is to say, after vowels and voiced consonants).

Assume that a form like *gases* is underlyingly *gasP*, where P is a single abstract symbol indicating plural.
Provide a list of n-grams that rewrite P as the correct surface form.
For simplicity, you may assume that the alphabet only consists of *g*, *s*, *t*, *a*, and *e*.
:::

::: exercise
Specify the mapping n-grams for intervocalic voicing.
You may assume that the alphabet only consists of *a*, *o*, *s*, *z*, and *l*.
:::

## Problems with mapping n-grams

Our mapping n-grams have multiple problems.
First of all, it is unclear what should be done when we have multiple matching mapping n-grams.

::: example
Suppose that we have some language German' that works exactly like German except that it also has a ban against clusters that consist of a nasal followed by a voiced plosive.
When such a cluster is encountered, the voiced plosive is removed.
For instance, *nd* is reduced to *n*.
We can capture this with the mapping bigram *nd[$\emptystring$]*, where replacing *d* with the empty string amounts to removal of *d*.
But then we run into an issue with words like *land* (which has the same meaning as English *land*).
According to the mapping bigram *nd[$\emptystring$], we should delete *d* and thus end up with *lan*.
But the mapping bigram *d[t]{{{R}}}* for word-final devoicing requires us to replace *d* with *t* so we get *lant*.
Well, which one is it?
:::

Phonologists avoids issues of this kind by assuming that rewrite rules are ordered. 
If two rules $R_1$ and $R_2$ could both apply, we always apply $R_1$ first.
If this means that $R_2$ can on longer apply, we skip that rewrite rule.

::: example
Suppose that word-final devoicing precedes all other rules of German'.
Then *land* must be realized as *lant* because *d[t]{{{R}}}* takes precedence over *nd[$\emptystring$]*.
:::

While this certainly fixes the problem, it is quite a deviation from n-gram grammars, which we defined as sets exactly because there is no order between the n-grams.
Of course we could now go from sets to posets, but that opens a giant can of worms: can we use any partial order, or does it have to be linear order, or something in between like a lattice?
That's a lot of added complexity that we would like to avoid.

But beyond this impediment to our own laziness, there are also some serious empirical issues.
Iterative processes, for example, seem to be impossible to capture this way.
You might remember the case of vowel harmony.
In terms of phonotactics, vowel harmony is a ban against vowels of distinct harmony classes appearing in the same word.
But as a mapping from URs to surface forms, it means that a vowel that isn't in the right harmony class is replaced with a vowel that does meet the harmony requirement.
Crucially, vowel harmony can apply iteratively, with the replacement of one vowel triggering the replacement of the next vowel after that.
This seems to be impossible to pull off with mapping n-grams.

::: example
Suppose that we have a language with two classes of harmonic vowels: bright (B) and dark (D).
If a B is followed by a D (ignoring vowels), then D is replaced by B.
But crucially, this replacement can itself trigger another replacement of a D by a B.
Such a sequence of rewrite steps is shown below.

1. CBCDCD
2. CBCBCD
3. CBCBCB

This would not work with mapping n-grams.
Suppose our input is *CBCDCD*.
We go through the string from left to right and incrementally build up a surface form.
Suppose we use mapping trigrams like *BCD[B]*.
This will allow us to rewrite the first *D* in *CBCDCD* with *B*.
At that point, the surface form is *CBCB*.
However, the UR is still *CBCDCD* because we are not making any changes to the UR, we are simply building a corresponding surface form from scratch.
But then, once we reach the second *D* in the UR, the mapping trigram *BCD[B]* does not actually match --- the context in the UR is *DCD*, not *BCD*.
And since we can build arbitrarily long URs of this form, this problem will arise even if we use ludicrously large n-grams, e.g. 17-grams.
:::

The problem here is that we use URs to determine whether a mapping n-gram has a match, and since URs do not change, we miss cases where application of an earlier rewrite step did actually yield a matching configuration.
We could fix this by allowing mapping n-grams to specify whether the match should be checked for the UR or the surface form.
But that's yet another complicating factor in what is quickly becoming a much more complicated system than the simple n-gram grammars we had for phonotactics.

::: exercise
Matching n-grams also run into issues with unbounded processes like sibilant harmony.
Suppose that *s* becomes *ʃ* after *ʃ*, no matter how far the two are apart.
For instance,
*ʃtojowonowas*
would become
*ʃtojowonowaʃ*.
Explain why this cannot be handled with matching n-grams if the number of intervening segments is truly unbounded.
:::

::: exercise
Continuing the previous exercise, suggest a way matching n-grams could be amended to handle such unbounded dependencies.
:::

Finally, matching n-grams do not seem to address the primary reason why we moved to mappings in the first place: native speakers' ability to quickly and effortlessly establish relations between strings.
Matching n-grams provide an easy way to map a UR to a surface form, but speakers primarily do the opposite, they map surface forms to URs in order to establish whether they are connected in some way.
This is a messy process with mapping n-grams.

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

:::

We could plow ahead and fix all these issues with brute-force stipulations, idiosyncratic additions and restrictions, and quite generally just keep hammering away at the problem until we've pushed that square peg through the round hole.
Or we could take the hint that we're not quite thinking about this the right way and look for an alternative.
In the next unit, we'll take a mathematically more natural starting point and we will see that this gives us pretty much everything one could want for phonology.

## Recap

- Phonotactics is a very reductionist view of phonology.
  A native speaker's mental grammar of phonology isn't just a collection of well-formedness conditions, it allows them to identify principled connections between strings that may look very different.
- Phonologists capture this by positing a split between surface forms and **underlying representations**, with the former obtained from the latter via rewrite rules.
- Extending n-grams from phonotactics to mappings does not work well and runs into issues with rule ordering, iterativity, and recoverability of URs.
