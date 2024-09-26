---
pagetitle: >-
    Strings: Basic notation
---

# Strings: Basic notation

:::prereqs
- sets (basic notation)
:::

Strings play a very prominent role in linguistics and language technology.
A string is a sequence of symbols, like *nfm*, *wendigo*, or *105§/*.
In contrast to sets, strings are ordered and can contain duplicates.

::: example
The sets $\setof{m,a,d}$, $\setof{d,a,m}$, and $\setof{a,d,a,m}$  are equivalent, but for strings $\mathit{mad} \neq \mathit{dam} \neq \mathit{adam}$.
:::

::: exercise
Fill in $=$ or $\neq$ as appropriate for each pair of strings below.

- $\mathit{abba}$ \_ $\mathit{ABBA}$
- $10$ \_ $5 + 5$
- $\setof{m,a,d} \_ \setof{d,a,m}$

Caution: $\{$ and $\}$ can be symbols just like $m$, $a$, or $d$.

::: solution
1. $\mathit{abba} \neq \mathit{ABBA}$
1. $10 \neq 5 + 5$
1. $\setof{m,a,d} \neq \setof{d,a,m}$

::: solution_explained
1. The symbols $a$ and $A$ are distinct (and so are $b$ and $B$).
   Hence $\mathit{abba}$ and $\mathit{ABBA}$ already contain different symbols in their very first position, and consequently the strings are distinct.
1. While it is true that the sum of $5$ and $5$ is $10$, the exercise asks you to compare the string $5 + 5$ to the string $10$.
   These are very different strings.
   For example, only the former contains the symbol $+$, and only the latter contains $1$ and $0$.
1. This one is tricky.
   If we were talking about sets, then it would be the case that $\setof{m,a,d}$ is equivalent to $\setof{d,a,m}$ because sets are unordered.
   But here you are asked to consider strings, not sets.
   These strings just so happen to start with $\{$ and end with $\}$, but they are still strings.
   And since the second symbol of the left string is $m$, whereas the right string has $d$ in its second position, these two strings are distinct.
:::
:::
:::

## Alphabet

When talking about strings, one usually fixes a finite set of symbols over which the strings are built.
This is called an **alphabet**.
It is common but not necessary to require alphabets to contain at least one symbol.
Alphabets are often given labels like $\Sigma$ or $\Omega$.
A string **over alphabet $\Sigma$** is also called a **$\Sigma$-string**.

::: example
The set of Latin characters (A-Z, a-z) is an alphabet that's familiar to all of you.
Strings over it include:

- string
- alphabet
- aaaaaaa
- c

:::

::: example
The set of Arabic digits is an alphabet with symbols 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.
Every natural number (0, 1, 2, ...), when represented in decimal as usual, is a string over this alphabet.
But not every string over this alphabet is a number of the decimal system.
For instance, 000134095 is not a valid number, although 134095 is.
:::

::: example
The set $\mathbb{N}$ of all natural numbers (0, 1, 2, and so on) is not a valid alphabet because it isn't finite.
:::

::: exercise
For each one of the following, say whether it is a valid alphabet.
Justify your answer.

- $\setof{a}$
- $\setof{0,1}$
- the set of all English words that are spelled with at most 5 characters
- the set of all natural numbers less than 1000
- the set of the nucleobases of DNA: adenine, cytosine, guanine, thymine 

::: solution
An alphabet must be a finite set of symbols.
Therefore:

- The set $\setof{a}$ is a valid alphabet because it contains exactly one symbol and thus is finite.
- The set $\setof{0,1}$ is a valid alphabet because it contains exactly two symbols and thus is finite.
- The set of all English words that are spelled with at most 5 characters is also a finite set: The English alphabet has 26 letters, which means that there are at most $26^5 = 11,881,376$ words that fit these requirements.
  While that is a large number, it is still finite.
  The fact that each symbol is itself a string of characters does not matter, that is an artefact of our writing system.
  If instead we had a unique symbol to refer to each one of these words, e.g. pictograms, the issue wouldn't even arise.
- The set of all natural numbers less than 1000 is also a possible alphabet because this set is finite.
  Again you might be concerned that we write natural numbers as strings of digits and it may seem weird to you to have symbols that are internally complex.
  But just like with the English words, this is just an artefact of how we write numbers.
  In hexademical notation, for instance, the natural number $11$ would be a single symbol $b$.
- The nucleobases of DNA once again form a finite set and hence are a valid alphabet.
  Again these are symbols with internal structure, in this case their molecular structure.
  When we treat the nucleobases as the symbols of our alphabet, we are making a decision to ignore their internal structure and treat them as the smallest unit of analysis (just like, say, a phonologist may treat sounds as the smallest unit of analysis and ignore the sound waves that actually give rise to the sounds).
:::
:::


## String length

The length of a $\Sigma$-string $s$ is indicated by $\length{s}$.
For instance,
$\length{\text{ant}} = 3$,
$\length{0770001} = 7$,
and $\length{\text{a}} = 1$.
The set of all strings over $\Sigma$ whose length is exactly $n$ is denoted by $\Sigma^n$.

::: example
Let $\Sigma \is \setof{a,b}$.
Then $\Sigma^3$ contains all of the following strings, and only those:


- $\mathit{aaa}$
- $\mathit{aab}$
- $\mathit{aba}$
- $\mathit{abb}$
- $\mathit{baa}$
- $\mathit{bab}$
- $\mathit{bba}$
- $\mathit{bbb}$

:::

The size of $\Sigma^n$ is always fixed.
If $\Sigma$ has $m$ members, then $\Sigma^n$ contains $m^n$ strings.

::: example
In the previous example, $\Sigma$ contains two symbols, so $\Sigma^n$ should consist of $2^3 = 8$ distinct strings.
That's exactly what we found.
:::

::: exercise
Which one of the following are members of $\setof{a,b}^4$, i.e. $\Sigma^4$ where $\Sigma$ contains $a$, $b$, and nothing else?

- $\mathit{aaab}$
- $\mathit{aba}$
- $\mathit{aaaaa}$
- $\mathit{b}$
- $\mathit{abca}$

::: solution
Among the listed strings, $\mathit{aaab}$ is the only member of $\setof{a,b}^4$.

::: solution_explained
The $\setof{a,b}^4$ contains all strings that meet both of the following criteria:

1. The only symbols that may occur in the string are $a$ and $b$.
1. The string must contain exactly four symbols.

The only strings above with exactly four symbols are $\mathit{aaab}$ and $\mathit{abca}$, and only the former contains no symbols besides $a$ and $b$.
Note that $\mathit{aaaa}$, which isn't listed above, is also a member $\setof{a,b}^4$ --- the requirement that the strings may contain no symbols other than $a$ and $b$ does not entail that the strings must contain both $a$ and $b$.
:::
:::
:::

::: exercise
List all members of $\setof{k,o,z}^2$.

::: solution
The members are $kk$, $ko$, $kz$, $ok$, $oo$, $oz$, $zk$, $zo$, $zz$.

::: solution_explained
The set $\setof{k,o,z}^2$ contains all strings of length $2$ that can be built using only the symbols $k$, $o$, and $z$.
This gives us three options starting with $k$ ($kk$, $ko$, $kz$), three options starting with $o$ ($ok$, $oo$, $oz$), and three options starting with $z$ ($zk$, $zo$, $zz$).
:::
:::
:::

Very often expressions like $a^n$ are used as a shorthand for $\setof{a}^n$.

::: example
The expression $\mathit{b a^5 c^3 d}$ is a shorthand for $\mathit{baaaaacccd}$.
:::

::: exercise
Write each one of the following in a more compact fashion using exponents.

- ABBA
- loool
- aardvark

::: solution
1. AB$^2$A
1. lo$^3$l
1. a$^2$rdvark

::: solution_explained
The general strategy is to find parts of the string where the same symbol $x$ is iterated $n$ times and to then replace that part with $x^n$.
For example, in *ABBA* we have *A* followed by two *B*s and then another *A*, i.e. $\mathit{A B^2 A}$.
:::
:::
:::

## Infinite string sets over $\Sigma$

Since alphabets must be finite, $\Sigma^n$ is necessarily finite for any alphabet $\Sigma$ and $n \geq 0$.
But the set of all strings over $\Sigma$ is infinite.

::: example
Let $\Sigma \is \setof{a}$.
Then $a$ is a string over $\Sigma$, and so are $\mathit{aa}$, $\mathit{aaa}$, $\mathit{aaaa}$, and so on.
This enumeration continues indefinitely, so there must be infinitely many distinct strings over $\Sigma$.
:::

Two infinite string sets are commonly defined over $\Sigma$.
They are $\Sigma^*$ and $\Sigma^+$, respectively.
The set $\Sigma^*$ contains all strings over $\Sigma$, whereas $\Sigma^+$ contains all strings whose length is at least $1$.
The only difference between the two is that $\Sigma^*$ also contains the **empty string** $\emptystring$.
The empty string is the string counterpart of the number 0: it represents nothing.
In fact, $\emptystring$ is the only string whose length is 0.

::: example
Let $\Sigma = \setof{a,b}$.
Then $\Sigma^*$ contains

- $\emptystring$,
- $\mathit{a}$
- $\mathit{b}$
- $\mathit{aa}$
- $\mathit{ab}$
- $\mathit{ba}$
- $\mathit{bb}$
- $\mathit{aaa}$
- $\mathit{aab}$
- $\mathit{aba}$
- $\mathit{abb}$
- and so on

All these strings are also members of $\Sigma^+$, except $\emptystring$.
:::

$\Sigma^*$ is also called the **Kleene closure**, named after [Stephen C. Kleene](https://en.wikipedia.org/wiki/Stephen_Cole_Kleene).

Here's a little bit of background to make it easier for you to remember the difference between $\Sigma^*$ and $\Sigma^+$.
As you might know from search engines, the Kleene star `*` is sometimes used as a wildcard that matches everything.
So $\Sigma^*$ can be translated as "every string built over $\Sigma$".
On the other hand $\Sigma^+$ only contains those strings whose length is at least 1, or in other words, whose length is positive.
And $+$ is a common abbreviation for positive (e.g. with batteries).

::: exercise
Enumerate the five shortest members of $\setof{a}^*$.

::: solution
1. $\emptystring$
1. $\String{a}$
1. $\String{aa}$
1. $\String{aaa}$
1. $\String{aaaa}$

::: solution_explained
The expression $\setof{a}^*$ is short for "the set of all strings of length 0 or more that can be built over the alphabet $\setof{a}$".
With only one symbol to choose from, there can never be two distinct strings of the same length.
Hence we just start with the shortest possible string, which is the empty string $\emptystring$, and then keep adding $a$s until we have enumerated five strings.
:::
:::
:::

## Concatenation

Given two $\Sigma$-strings $u$ and $v$, their **concatenation** $u \stringcat v$ is the result of "glueing" the left end of $v$ to the right end of $u$.

::: example
Here are a few examples of concatenation:

- $\mathit{math} \stringcat \mathit{ematics} = \mathit{mathematics}$,
- $2000 \stringcat 18 = 200018$,
- $\text{Thomas} \stringcat \text{Graf} = \text{ThomasGraf}$.

:::

Just like addition, concatenation is **associative**.
This means that if we carry out multiple concatenations, it does not matter in what order we resolve the concatenation steps: $u \stringcat (v \stringcat w) = (u \stringcat v) \stringcat w = u \stringcat v \stringcat w$.

::: example
It does not matter in which order we combine *is* with *concatenation* and *associative* below:

- $(\mathit{concatenation} \stringcat \mathit{is}) \stringcat \mathit{associative} = \mathit{concatenation is} \stringcat \mathit{associative} = \mathit{concatenation is associative}$
- $\mathit{concatenation} \stringcat (\mathit{is} \stringcat \mathit{associative}) = \mathit{concatenation} \stringcat \mathit{is associative} = \mathit{concatenation is associative}$

:::

Even though concatenation is associative, it is not **commutative**.
That is to say, $u \stringcat v$ and $v \stringcat u$ are not necessarily the same.
They might be, but it's not guaranteed.

::: example
Let $u \is \text{house}$ and $v \is \text{boat}$.
Then $u \stringcat v$ is *houseboat*, whereas $v \stringcat u$ is *boathouse*.
Those are not the same strings (and they also happen to mean completely different things).
:::

Note the special behavior of the empty string: $u \stringcat \emptystring = \emptystring \stringcat u = u$. 
This is fairly intuitive because adding a string of length 0 to $u$ should not change the length of $u$, which means that $u$ does not change at all --- just like adding 0 to a number does not change that number.

Sometimes concatenation is not explicitly indicated, so that instead of $u \stringcat v$ one may simply write $\mathit{uv}$.

::: exercise
Give an example of distinct strings $u$ and $v$ such that $\mathit{uv} = \mathit{vu}$ and neither $u$ nor $v$ is the empty string.

::: solution
There are infinitely many solutions.
For example, if $u \is \mathit{aba}$ and $v \is \mathit{abaaba}$, then $u \stringcat v = \mathit{aba} \stringcat \mathit{abaaba} = \mathit{abaabaaba} = \mathit{abaaba} \stringcat \mathit{aba} = v \stringcat u$.
The simplest solution is actually $u \is \mathit{a}$ and $v \is \mathit{aa}$, where we have $u \stringcat v = \mathit{a} \stringcat \mathit{aa} = \mathit{aaa} = \mathit{aa} \stringcat \mathit{a} = v \stringcat u$.
Quite generally, we can pick any non-empty string $u$, set $v = uu$, and it will always be the case that $u \neq v$ yet $u \stringcat v = v \stringcat u = uuu$.

Note that $u \is a$ and $v \is ab$ is not a valid solution.
In this case, $u \stringcat v = \mathit{aab}$, whereas $v \stringcat u = \mathit{aba}$, which is distinct from $\mathit{aab}$.
Similarly, $u \is a$ and $v \is a$ is not a valid solution because the exercise requires $u$ and $v$ to be distinct strings.
:::
:::

::: exercise
Is the following true or false?
If $u \neq v$, then $\mathit{uv} \neq \mathit{vu}$?

::: solution
False.

::: solution_explained
This follows immediately from the previous exercise, where you had to pick distinct $u$ and $v$ such that $u \stringcat v \neq v \stringcat u$.
:::
:::
:::

::: exercise
Is the following true or false?
If $\mathit{uv} \neq \mathit{vu}$, then $u \neq v$?

::: solution
True.

::: solution_explained
Assume towards a contradiction that $\String{uv} \neq \String{vu}$ yet $u = v$.
If $u = v$, then $\String{uv} = \String{uu} = \String{vv} = \String{vu}$, which contradicts our initial assumption that $\String{uv} \neq \String{vu}$.
:::
:::

## Recap

- A string is a sequence of symbols drawn from some alphabet.
- A $\Sigma$-string is a string over alphabet $\Sigma$.
- The length of string $s$ is denoted by $\length{s}$.
- The empty string $\emptystring$ is the unique string of length $0$.
- $\Sigma^n$ is the set of all $\Sigma$-strings $s$ such that $\length{s} = n$.
- $a^n$ is a shorthand for $\setof{a}^n$.
- The Kleene closure $\Sigma^*$ is the set of all $\Sigma$-strings (including $\emptystring$).
- The positive closure $\Sigma^+$ contains all $\Sigma$-strings except $\emptystring$.
- Concatenation of strings $u$ and $v$ is denoted by $u \stringcat v$ or simply $\mathit{uv}$.

\includecollection{solutions}
