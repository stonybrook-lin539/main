---
pagetitle: Succinctness and choosing between grammars
---

# Succinctness and choosing between grammars

:::prereqs
- general (exponentiation)
- functions (basics, function growth)
:::

Thanks to all the math we have put to good use, we now have three expressively equivalent models of phonotactics:

1. strict negative $n$-gram grammars, and
1. mixed negative $n$-gram grammars, and
1. strict positive $n$-gram grammars.

By "expressively equivalent" we mean that every string language that can be generated by a grammar of one of those tree types can also be generated by grammars of the other two types.
In fact, we can automatically translate between these three grammar types as we see fit.

But this also means that we cannot distinguish between these three types of grammars based purely on typological data.
There is no phonotactic phenomenon that allows us to advocate conclusively for, say, strict negative $n$-gram grammars and against the other two types.
However, we should not conflate expressive equivalence with total equivalence.
These three grammar types can still differ in other respects, and one of them is succinctness: how many $n$-grams does the grammar need to capture a given phenomenon?

## Differences in grammar size

The three grammar types above vary hugely in how compactly they can model specific phenomena.
You already saw a glimpse of this in earlier exercises, but the true extent only becomes evident once we consider a few artificial examples.

::: example
Suppose our alphabet contains the symbols *a*, *b*, *c*, *d* (and nothing else).
Now consider the language $L$ that contains *ab*, *aab*, *aaab*, and so on (more succinctly, we can write $L$ as *a^+^b*).
This is very easy to express as a positive grammar:

1. {{{L}}}a
1. aa
1. ab
1. b{{{R}}}

The smallest mixed negative grammar for this language isn't much bigger:

1. c
1. d
1. {{{L}}}{{{R}}}
1. {{{L}}}b
1. ba
1. bb
1. a{{{R}}}

The strict negative grammar is twice the size by comparison, making it hard to decipher what pattern it is supposed to capture:

1. {{{L}}}{{{R}}}
1. {{{L}}}b
1. {{{L}}}c
1. {{{L}}}d
1. ac
1. ad
1. ba
1. bb
1. bc
1. bd
1. a{{{R}}}
1. b{{{R}}}
1. c{{{R}}}
:::

::: example
Suppose that our alphabet still contains only *a*, *b*, *c*, *d*, but $L$ now follows a more general pattern: 1 or more instances of *a*, followed by exactly one instance of *b* or *c* or *d*.
Hence $L$ contains *ab*, *ac*, *ad*, *aab*, *aac*, *aad*, *aaab*, *aaac*, *aaad*, and so on.

The positive grammar is still fairly small.

1. {{{L}}}a
1. aa
1. ab
1. ac
1. ad
1. b{{{R}}}
1. c{{{R}}}
1. d{{{R}}}

The mixed negative grammar grows a lot in size: 

1. {{{L}}}{{{R}}}
1. {{{L}}}b
1. {{{L}}}c
1. {{{L}}}d
1. ba
1. bb
1. bc
1. bd
1. ca
1. cb
1. cc
1. cd
1. da
1. db
1. dc
1. dd
1. a{{{R}}}

In fact, this also happens to be the strict negative grammar.
For $L$, allowing $n$-grams of variable length does not help at all.
:::

::: example
Now suppose our alphabet is $\setof{a}$ and consider the language $L$ that contains all strings over *a* whose length is at least 2 (i.e. *aa*, *aaa*, and so on).
The mixed negative grammar is incredibly small:

1. {{{L}}}{{{R}}}
1. {{{L}}}a{{{R}}}

The strict negative grammar looks slightly different, but has the same size.

1. {{{L}}}{{{L}}}{{{R}}}
1. {{{L}}}a{{{R}}}

This time the positive grammar is the largest:

1. {{{L}}}{{{L}}}a
1. {{{L}}}aa
1. aaa
1. aa{{{R}}}
1. a{{{R}}}{{{R}}}
:::

::: example
Finally, assume that the alphabet $\Sigma$ is $\setof{a,b,c,d,e,f}$ and that $L$ contains all strings over this alphabet except that no string may have 5 or more instances of *a* in a row.
For instance, *baaaab* and *caaadaaaf* are well-formed, but not *baaaaab* or *ffaaaaaaacabec*.
The negative grammar for this is maximally simple:

1. aaaaa

The positive grammar, on the other hand, is enormous.
It contains all $n$-grams in $\Sigma_E^5$ except *aaaaa*.
That's $32,767$ $n$-grams: since there are 6 symbols in $\Sigma$ and 2 edge markers, $\Sigma_E^5$ contains $(6+2)^5 = 8^5 = 32,768$ 5-grams.
:::

Overall, there doesn't seem to be much regularity.
Sometimes a positive grammar is smaller, sometimes a negative one, and sometimes it matters whether the negative grammar is strict or mixed while in other cases the two look exactly the same.
Sometimes the differences is only one or two $n$-grams, sometimes it's tens of thousands.
So is this a case of anything goes where one can never be quite sure how things will pan out?
No, quite to the contrary.

## Upper bounds and rates of growth

Even though it is difficult to tell how things may pan out for a specific phenomenon or string language, that does not mean that there are no regularities.
It's just that these regularities are a bit more abstract in nature as they take the form of **upper bounds**.
Since every strict grammar, whether positive or negative, is built from members of $\Sigma_E^n$ for some alphabet $\Sigma$ and some choice of $n$, its size cannot exceed that of $\Sigma_E^n$.
And that size is easy to calculate.
Each $n$-gram furnishes $n$ positions, each one of which must be a symbol from $\Sigma$ or one of the two edge markers.
So if $\Sigma$ contains $m$ symbols, there are $m+2$ choices for each position, and since there are $n$ positions, this means there are $(m+2)^n$ different combinations.
Hence the size of $\Sigma_E^n$ is $(m+2)^n$, and that's a fixed upper bound on the size of any $n$-gram grammar over $\Sigma$.

::: example
Suppose $\Sigma \is \setof{a,b}$.
Then $\Sigma_E^2$ has $(2+2)^2 = 4^2 = 16$ members.
We can list them all:

1. {{{L}}}{{{L}}}
1. {{{L}}}{{{R}}}
1. {{{L}}}a
1. {{{L}}}b
1. a{{{L}}}
1. a{{{R}}}
1. aa
1. ab
1. b{{{L}}}
1. b{{{R}}}
1. ba
1. bb
1. {{{R}}}{{{L}}}
1. {{{R}}}{{{R}}}
1. {{{R}}}a
1. {{{R}}}b
:::

::: exercise
For $n \geq 2$, no grammar ever needs to contain every member of $\Sigma_E^n$.
Explain why.

::: solution
There are two answers here.
First, if $\Sigma_E^n$ is taken to contain useless $n$-grams like ${{{R}}}{{{L}}}$ or ${{{R}}}ab$, then these do not need to be included in the grammar because no string will ever have ${{{R}}}$ preceding another symbol that is not ${{{R}}}$.

Second, it is also true that there is always a more compact alternative to using a grammar that contains every member of $\Sigma_E^n$.
Suppose that you have a positive grammar that contains every possible $n$-gram over $\Sigma_E$, where $n \geq 2$.
In this case, the grammar generates $\Sigma^*$, the set of all possible strings over $\Sigma$.
But $\Sigma^*$ could have just as well been defined by a negative grammar $G$ that forbids no $n$-grams at all (formally, $G = \emptyset$).
Similarly, suppose that you have a negative grammar that contains every possible $n$-gram over $\Sigma_E$, with $n \geq 2$.
In this grammar, nothing is allowed at all, not even the empty string, so the grammar generates the empty language $\emptyset$.
But the empty language could also be generated by the positive $n$-gram grammar $G$ that contains no $n$-grams at all (formally, $G = \emptyset$).

The same strategy of switching polarities can be used to show that for every $n$-grammar $G$ that contains more than half of all possible $n$-grams (rounded up) there is a smaller grammar of opposite polarity that generates the same string language as $G$.
:::
:::

This insight provides us with a fixed upper bound for any given choice of $\Sigma$ and $n$ such that no grammar can be bigger than that.
But that by itself isn't really that interesting, we want to know how that upper bound changes as we vary $\Sigma$ and $n$.
We can make this more visual by drawing a table, where rows indicate the size of the alphabet (plus both edge markers) and columns indicate the length of the $n$-grams.
Each cell tells us how many $n$-grams there are for that specific combination of those two values.

|           | 1    | 2         | 3           | 4             | 5              |
| --:       | --:  | --:       | --:         | --:           | --:            |
| **3**     | 3    | 9         | 27          | 81            | 243            |
| **4**     | 4    | 16        | 64          | 256           | 1024           |
| **5**     | 5    | 25        | 125         | 625           | 3125           |
| **6**     | 6    | 36        | 216         | 1296          | 7776           |
| **7**     | 7    | 49        | 343         | 2401          | 16807          |
| **8**     | 8    | 64        | 512         | 4096          | 32768          |
| **9**     | 9    | 81        | 729         | 6561          | 59049          |
| **10**    | 10   | 100       | 1,000       | 10,0000       | 100,000        |
| **100**   | 100  | 10,000    | 1,000,000   | 100,000,000   | 10,000,000,000 |

As you can see, the numbers grow quite a bit from the top to the bottom, but much faster from left to right.
In other words, $n$ plays a much bigger role in determining the size of $\Sigma_E^n$.
The number of bigrams over an alphabet with 100 symbols (including edge markers) is 10,000, which is still smaller than the number of 5-grams over an alphabet with 7 symbols (i.e. 16,807).
Our upper bound grows **exponentially** with $n$, but only **polynomially** with $\Sigma$.

What does this tell us?
While we can freely choose between strict negative grammars, mixed negative grammars, and (strict) positive grammars because they are interchangeable, grammar size can vary a lot depending on the phenomenon.
This does not matter too much as long as $\Sigma$ and $n$ are both small, but as we increase the size of the alphabet and the length of the $n$-grams, it becomes more noticeable.
In fact, we do not even need to worry too much about $\Sigma$ as $n$ has a much bigger impact on this.
Even with very small alphabets, $\Sigma_E^n$ is giant for $n > 5$.

::: example
For an alphabet with just two symbols, $\Sigma_E^6$ is 4,096, and $\Sigma_E^{10}$ is 1,048,576.
That's more than the number of trigrams over an alphabet with close to 100 symbols.
:::

::: exercise
Calculate the number of 100-grams over an alphabet with 3 symbols (including edge markers) and compare it to the number of trigrams over an alphabet with 100 symbols.

::: solution
There are $3^{100}$ distinct 100-grams over an alphabet with 3 symbols.
That is a ridiculously large number with 48 digits.
By comparison, the set of trigrams over an alphabet with 100 symbols has $100^3$ distinct elements, which is exactly 1 million.
That is still a large number, but much smaller than any number with 48 digits.
We see again that the length of $n$-grams is much more impactful than the size of the alphabet.
:::
:::

::: example
The age of the universe is estimated to be around $436, 000, 000, 000, 000, 000$ seconds.
That's 436 quadrillion seconds, which one can also write mathematically as $4.36 \times 10^{17}$.
This means that given an alphabet with 8 symbols plus 2 edge markers, the set of all 18-grams already exceeds the number of seconds since the Big Bang.
And it doesn't do that by just a slim margin.
If, starting from the birth of the universe, you had been listing all 18-grams over that alphabet with edge markers, uttering two 18-grams per second, you still wouldn't be done for another 128 quadrillion seconds, which is 4 billion years (I've rounded this a bit for your convenience).
Needless to say, we should be skeptical if our investigation ever leads us to conclude that natural languages use $n$-grams with a large value for $n$.
:::

::: exercise
Natural languages tend to use much more than just 8 distinct sounds.
In fact, some languages have been argued to use close to a 100 distinct sounds.
Calculate the smallest value of $n$ for which the number of $n$-grams over an alphabet with 100 symbols (including edge markers) exceeds the number of seconds since the Big Bang.

::: solution
The smallest such value for $n$ is $9$.

::: solution_explained
This answer can be brute-forced by calculating the values of $100^n$ starting from $n$.
A smarter solution, however, uses some basic laws of exponentiation.
Since $100 = 10^2$, we can write $100^n$ as $(10^2)^n$.
But this is the same as $10^{2n}$.
So the exercise reduces to the fairly simple task of finding the smallest $n$ such than $2n > 17$.
:::
:::
:::

::: exercise
One can also use $n$-grams to model certain aspects of sentences, which each word corresponding to a position of the $n$-gram.
For example, *John likes* would be a bigram and *bought these truffles* would be a trigram.
Native speakers of English know at least 10,000 distinct words, and that's if we count distinct surface forms such as *buy* and *buys* as a single word.
Without that distinction, a native speaker's vocabulary can quickly reach six digit territory.

Given an alphabet with 10,000 distinct symbols (including edge markers), what is the smallest value of $n$ such that the number of $n$-grams is greater than the age of the universe in seconds?

::: solution
The smallest such value for $n$ is $5$.

::: solution_explained
We can use the same strategy as in the previous solution.
The number 10,000 is the same as $10^4$, and $(10^4)^n$ is the same as $10^{4n}$.
And the smallest $n$ such that $4n \geq 17$ is $5$.
:::
:::
:::

So what are we to infer from all these calculations?
First and foremost, scaling up the size of $n$-grams isn't a very appealing strategy.
Since grammar size grows exponentially with $n$, even small increases of $n$ have a huge impact on grammar size.
Ideally, we keep $n$ limited to 2 or 3.
At no point should we go beyond 5 as this is where the combinatorial explosion quickly becomes unmanageable.
Yes, we can mitigate some of the blow-up by carefully switching between strict positive, strict negative, and mixed negative grammars, but that can only do so much.
The good news is that it is very rare for a phenomenon to require more than 5-grams.
Such phenomena do exist, but as we will see next, they can actually be given a very compact and intuitively pleasing account in terms of bigrams if we make a small change to our formalism.

## Recap

- Depending on the phenomenon at hand, a positive or a negative grammar may be more succinct.
- The difference in grammar size may not always be very pronounced, but it can be.
- The difference cannot exceed the size of $\Sigma_E^n$, which grows polynomially with $\Sigma$ and exponentially with $n$.
- If your analysis requires you to move beyond 5-grams, you are better off exploring other formalisms or analyses.

\includecollection{solutions}
