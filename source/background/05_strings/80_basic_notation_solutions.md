---
pagetitle: >-
    Strings: Basic notation (Solutions)
---


# Strings: Basic notation (Solutions)

::: exercise
Fill in $=$ or $\neq$ as appropriate for each pair of strings below.

1. $\mathit{abba}$ \_ $\mathit{ABBA}$
1. $10$ \_ $5 + 5$
1. $\setof{m,a,d} \_ \setof{d,a,m}$


Caution: $\{$ and $\}$ can be symbols just like $m$, $a$, or $d$.

::: solution
1. $\mathit{abba} \neq \mathit{ABBA}$
1. $10 \neq 5 + 5$
1. $\setof{m,a,d} \neq \setof{d,a,m}$
:::

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

::: exercise
For each one of the following, say whether it is a valid alphabet.
Justify your answer.

- $\setof{a}$
- $\setof{0,1}$
- the set of all English words that are spelled with at most 5 characters
- the set of all natural numbers less than 1000
- the nucleobases of DNA: adenine, cytosine, guanine, thymine 

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

::: exercise
Which one of the following are members of $\setof{a,b}^4$, i.e. $\Sigma^4$ where $\Sigma$ contains $a$, $b$, and nothing else?

1. $\mathit{aaab}$
1. $\mathit{aba}$
1. $\mathit{aaaaa}$
1. $\mathit{b}$
1. $\mathit{abca}$

::: solution
Among the listed strings, $\mathit{aaab}$ is the only member of $\setof{a,b}^4$.
:::

::: solution_explained
The $\setof{a,b}^4$ contains all strings that meet both of the following criteria:

1. The only symbols that may occur in the string are $a$ and $b$.
1. The string must contain exactly four symbols.

The only strings above with exactly four symbols are $\mathit{aaab}$ and $\mathit{abca}$, and only the former contains no symbols besides $a$ and $b$.
Note that $\mathit{aaaa}$, which isn't listed above, is also a member $\setof{a,b}^4$ --- the requirement that the strings may contain no symbols other than $a$ and $b$ does not entail that the strings must contain both $a$ and $b$.
:::

:::

::: exercise
List all members of $\setof{k,o,z}^2$.

::: solution
The members are $kk$, $ko$, $kz$, $ok$, $oo$, $oz$, $zk$, $zo$, $zz$.
:::

::: solution_explained
The set $\setof{k,o,z}^2$ contains all strings of length $2$ that can be built using only the symbols $k$, $o$, and $z$.
This gives us three options starting with $k$ ($kk$, $ko$, $kz$), three options starting with $o$ ($ok$, $oo$, $oz$), and three options starting with $z$ ($zk$, $zo$, $zz$).
:::

:::

::: exercise
Write each one of the following in a more compact fashion using exponents.

1. ABBA
1. loool
1. aardvark

::: solution
1. $\mathit{A B^2 A}$
1. $\mathit{l o^3 l}$
1. $\mathit{a^2rdvark}$
:::

::: solution_explained
The general strategy is to find parts of the string where the same symbol $x$ is iterated $n$ times and to then replace that part with $x^n$.
For example, in *ABBA* we have *A* followed by two *B*s and then another *A*, i.e. $\mathit{A B^2 A}$.
:::

:::

::: exercise
Enumerate the five shortest members of $\setof{a}^*$.

::: solution
1. $\emptystring$,
1. $\mathit{a}$,
1. $\mathit{aa}$,
1. $\mathit{aaa}$,
1. $\mathit{aaaa}$
:::

::: solution_explained
The expression $\setof{a}^*$ is short for "the set of all strings of length 0 or more that can be built over the alphabet $\setof{a}$".
With only one symbol to choose from, there can never be two distinct strings of the same length.
Hence we just start with the shortest possible string, which is the empty string $\emptystring$, and then keep adding $a$s until we have enumerated five strings.
:::

:::

::: exercise
Give an example of distinct $u$ and $v$ such that $u \stringcat v = v \stringcat u$ and neither $u$ nor $v$ is the empty string.

::: solution
There are infinitely many solutions.
For example, if $u \is \mathit{aba}$ and $v \is \mathit{abaaba}$, then $u \stringcat v = \mathit{aba} \stringcat \mathit{abaaba} = \mathit{abaabaaba} = \mathit{abaaba} \stringcat \mathit{aba} = v \stringcat u$.
The simplest solution is actually $u \is \mathit{a}$ and $v \is \mathit{aa}$, where we have $u \stringcat v = \mathit{a} \stringcat \mathit{aa} = \mathit{aaa} = \mathit{aa} \stringcat \mathit{a} = v \stringcat u$.

Note that $u \is a$ and $v \is ab$ is not a valid solution.
In this case, $u \stringcat v = \mathit{aab}$, whereas $v \stringcat u = \mathit{aba}$, which is distinct from $\mathit{aab}$.
Similarly, $u \is a$ and $v \is a$ is not a valid solution because the exercise requires $u$ and $v$ to be distinct strings.
:::

:::

::: exercise
Is the following true or false?
If $u \neq v$, then $u \stringcat v \neq v \stringcat u$?

::: solution
False.
:::

::: solution_explained
This follows immediately from the previous exercise, where you had to pick distinct $u$ and $v$ such that $u \stringcat v \neq v \stringcat u$.
:::

:::
