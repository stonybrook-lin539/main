---
pagetitle: >-
    Sets: The Basics
---

# Sets: The basics

Sets are the fundamental building block of modern mathematics.
Intuitively, a set is a collection of objects, but with two important twists:

1. Sets are unordered.
1. Sets contain no duplicates.

::: example
Suppose you want to keep a record of which words occur in a text.
You aren't interested in how often a given word occurred, just whether it occurs at all.
Nor do you care in which order the words occurred in the text.
So you are actually interested in the *set* of words that occur in the text.
:::

``` jupyterpython
# Converting a text to the set of words
import re

def text_to_set(text):
    return set(re.findall(r"\w+", text.lower()))

# change the string below as you see fit
text = "If police police police, then police police police."
print("The original text is:")
print(text)
print("The set of words is:")
print(text_to_set(text))
```

Each property is explained in detail below, but let's first put some helpful notation in place.

## List notation

Sets are often written as lists with curly braces around them.
So $\setof{a, b, c, d}$ denotes the set containing $a$, $b$, $c$, $d$.
Here $a$, $b$, $c$, $d$ are some arbitrary objects.
This is known as **list notation**.
More complex sets are defined with **set-builder notation**, which will be covered in a later unit.
<!-- fixme: add link to unit -->

::: example
Consider the string *If John slept, then Mary left*.
Its set of words (ignoring sentence-initial capitalization) is
$\setof{
\text{if},
\text{John},
\text{left},
\text{Mary},
\text{slept},
\text{then}
}$.
:::

::: exercise
Write the following as a set:

- the first names of your three favorite actors/actresses,
- the colors of the rainbow,
- all even numbers between 1 and 11

:::

## Elements and set membership

The objects contained in a set are called its **elements** or **members**.
One writes $e \in S$ to indicate that $e$ is an element of $S$.
The opposite is denoted $e \notin S$: $e$ is not an element of $S$.
The symbol $\in$ thus indicates **set membership**.

::: example
Let $W$ be the set of words in the string *If John slept, then Mary left*.
Then it holds that $\mathit{left} \in W$ and $\mathit{right} \notin W$.
But it is not the case that $\mathit{then} \notin W$ or $\mathit{awake} \in W$.
:::

You might be wondering why we use the symbol $\in$ for set membership.
The following mnemonic, while historically inaccurate, may help you with remembering the notation: $\in$ looks like a stylized *E*, and $x \in S$ means that $x$ is an *E*lement of $S$.

Sometimes $\ni$ is used as the mirror image of $\in$.
For example, $a \in S$ could also be written as $S \ni a$.

::: example
Continuing the previous example, it is true that $\mathit{left} \in W \ni \mathit{then}$.
That is to say, both $\mathit{left} \in W$ and $\mathit{then} \in W$ are true.
:::

::: exercise
Put $\in$, $\ni$, $\notin$, $\not\ni$ in the gaps below as appropriate:

- $5 \_ \setof{1,2,4,5,8}$
- $6 \_ \setof{1,2,4,5,8}$
- $\setof{5} \_ \setof{1,2,4,5,8}$
- $5 \_ \setof{1,2,4,5,8} \_ 6$

:::

Sets can contain arbitrary objects, including other sets.
However, the members of a set are just the elements immediately contained by the set, not what might in turn be contained inside of those elements.

::: example
The set $\setof{a, \setof{b}}$ has two members: $a$ and $\setof{b}$.
While $b$ is an element of $\setof{b}$, it is not an element of $\setof{a, \setof{b}}$.
:::

::: exercise
Put $\in$, $\ni$, $\notin$, $\not\ni$ in the gaps below as appropriate:

- $5 \_ \setof{1,\setof{2,4},5,8}$
- $6 \_ \setof{1,\setof{2,4,5,8}}$
- $\setof{5} \_ \setof{1,\setof{2,4},\setof{5},8}$
- $5 \_ \setof{\setof{1,2,4,5,8}} \_ 6$

:::

## Lack of order

Even though we may write sets in a linear fashion as lists, they have no internal order.
The set $\setof{a,b}$ could also be written as $\setof{b,a}$.
So we have $\setof{a,b} = \setof{b,a}$, and
$\setof{a,b,c} =
 \setof{a,c,b} =
 \setof{b,a,c} =
 \setof{b,c,a} =
 \setof{c,a,b} =
 \setof{c,b,a}$.

::: example
Consider the strings
*If John slept, then Mary left* and
*If Mary left, then John slept*.
While they are clearly distinct sentences, their sets of words are identical.
:::

``` jupyterpython
import re

def text_to_set(text):
    return set(re.findall(r"\w+", text.lower()))

text1 = "If John slept, then Mary left."
text2 = "If Mary left, then John slept."

set1, set2 = text_to_set(text1), text_to_set(text2)
print("Are the sets identical?")
print("Yes") if set1 == set2 else print("No")
```

::: exercise
For each one of the following, fill the gap with $=$ or $\neq$ as appropriate:

- $\setof{a,b} \_ \setof{a,b}$
- $\setof{b,a} \_ \setof{a,b}$
- $\setof{b,a,c,d} \_ \setof{e,a,b,d}$

:::

## Lack of duplicates/Idempotency

Sets are **idempotent**, which means that duplicates are ignored.
So $\setof{a,b} = \setof{a,a,b} = \setof{a,b,b,a,b,a,b,a,a}$.
It also holds that $\setof{a} = \setof{a,a} = \setof{a,a,a}$, and so on.

``` jupyterpython
import re

def text_to_set(text):
    return set(re.findall(r"\w+", text.lower()))

text1 = "If John slept, then Mary left."
text2 = "If Mary left, then John slept."

set1, set2 = text_to_set(text1), text_to_set(text2)
print("Are the sets identical?")
print(set1 == set2)
```

::: example
Linguists distinguish between **word types** and **word tokens**.
The sentence *dogs love dogs* contain two tokens of the type *dogs*, and one token of the type *love*.
The sentences *dogs love* and *dogs love dogs* are different with respect to word tokens, but identical with respect to word types.
So if you care about word types rather than word tokens, you're dealing with a set because the only thing that matters is which words the text contains, not how many tokens of each word.
:::

::: example
Consider the sentence *If police police police, then police police police*.
Its set of words (ignoring capitalization) is 
$\setof{
\text{if},
\text{police},
\text{then}
}$.
:::

::: exercise
For each one of the following, fill the gap with $=$ or $\neq$ as appropriate:

- $\setof{a,b} \_ \setof{a,a,b,b}$
- $\setof{b,a} \_ \setof{a,b,a}$
- $\setof{c,b,a,a,d,c} \_ \setof{a,a,b,d,c,c,c}$
- $\setof{a} \_ \setof{a,a,a,a,a,a,c,a,a,a,a,a,a}$

:::

::: exercise
The sentence *If police police police, then police police police* actually uses two different word types.
It just just so happens that both are pronounced and spelled *police*.
But one is the **noun** *police*, the other one the **verb** *police*.
We can use the **parts of speech** N and V, respectively, to distinguish between the noun *police* and the verb *police*.
Let us add parts of speech to all the words in the string (we use C for the **complementizers** *if* and *then*):
*If[C] police[N] police[V] police[N], then[C] police[N] police[V] police[N]*.
What would be the corresponding set of words for this string (i.e. where we now distinguish between *police[N]* and *police[V]*)?
:::

It is important to keep in mind that idempotency only holds with respect to the elements of a set, not what may be contained by those elements.

::: example
Even though $\setof{a} = \setof{a,a}$, it is not the case that $\setof{a} = \setof{a, \setof{a}}$.
The former is the set containing $a$, the other is the set containing $a$ and the set of $a$.
:::

::: exercise
For each one of the following, fill the gap with $=$ or $\neq$ as appropriate:

- $\setof{a,b} \_ \setof{a,a,b,\setof{b}}$
- $\setof{\setof{b},\setof{a}} \_ \setof{\setof{a},\setof{b},\setof{a}}$
- $\setof{c,b,\setof{a,a},d,c} \_ \setof{\setof{a},b,d,c,c,c}$
- $\setof{a} \_ \setof{a,a,a,a,a,a,\setof{a},a,a,a,a,a,a}$

:::

## Recap

- Sets are collections of arbitrary objects.
- Sets are unordered and idempotent (= duplicates are ignored).
- Sets can be defined with list notation, e.g. $\setof{a, b}$.
- The objects contained in a set are called its *elements* or *members*.
- The symbols $\in$ and $\notin$ are used to indicate membership and non-membership, respectively.
- Occasionally, $\ni$ is used as the mirror image of $\in$.
- While sets may contain objects that are themselves collections of other objects, these objects inside objects are not considered for set membership.
  Remember: $a \in \setof{a}$ and $\setof{a} \in \setof{\setof{a}}$, but $a \notin \setof{\setof{a}}$.
