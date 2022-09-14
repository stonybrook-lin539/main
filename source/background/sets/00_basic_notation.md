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

::: jupyterpython
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
:::

Each property is explained in detail below, but let's first put some helpful notation in place.

## List notation

Sets are often written as lists with curly braces around them.
So $\setof{a, b, c, d}$ denotes the set containing $a$, $b$, $c$, $d$.
Here $a$, $b$, $c$, $d$ are some arbitrary objects.
This is known as **list notation**.
More complex sets are defined with [**set-builder notation**, which will be covered in a later unit](./fixme).

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

1. the first names of your three favorite actors/actresses,
1. the colors of the rainbow,
1. all prime numbers between 1 and 10 (remember, 1 is not a prime number!)

::: solution
- $\{$Bruce, Marlene, Bela$\}$
- $\{$red, orange, yellow, green, blue, indigo, violet$\}$
- $\{$2, 3, 5, 7$\}$
:::

::: solution_explained

1. Suppose that your favorite actors are Bruce Campbell (*Evil Dead*), Marlene Dietrich (*The Blue Angel*, *Witness for the Prosecution*), and Bela Lugosi (*Dracula*).
   Their first names are *Bruce*, *Marlene*, and *Bela*, so the set that contains their first names, and nothing else, is $\{$Bruce, Marlene, Bela$\}$.

1. If you're like me, you probably had to look this one up, but rainbows have six colors, which are red, orange, yellow, green, blue, indigo, and violet.
   So the set we're looking for contains these six colors. We can specify that set using the names of these colors, but it would also be okay to use colored squares instead of names, colored lines, anything that conveys clearly that this is the set that contains these six colors.

1. A number is prime if and only if it is at least 2 and cannot be divided by any number except 1 or itself without leaving a remainder.
   Between 1 and 10, that's 2, 3, 5, and 7.
:::

:::

## Elements and set membership

The objects contained in a set are called its **elements** or **members**.
One writes $e \in S$ to indicate that $e$ is an element of $S$.
The opposite is denoted $e \notin S$: $e$ is not an element of $S$.
The symbol $\in$ thus indicates **set membership**.

::: example
Let $W$ be the set of words in the string *If John slept, then Mary left*.
Then it holds that $\emph{left} \in W$ and $\emph{right} \notin W$.
But it is not the case that $\emph{then} \notin W$ or $\emph{awake} \in W$.
:::

Sometimes $\ni$ is used as the mirror image of $\in$.
For example, $a \in S$ could also be written as $S \ni a$.

::: example
Continuing the previous example, it is true that $\emph{left} \in W \ni \emph{then}$.
That is to say, both $\emph{left} \in W$ and $\emph{then} \in W$ are true.
:::

::: exercise
Put $\in$, $\ni$, $\notin$, $\not\ni$ in the gaps below as appropriate:

1. $5 \_ \setof{1,2,4,5,8}$
1. $6 \_ \setof{1,2,4,5,8}$
1. $\setof{5} \_ \setof{1,2,4,5,8}$
1. $5 \_ \setof{1,2,4,5,8} \_ 6$

::: solution
1. $5 \in \setof{1,2,4,5,8}$
1. $6 \notin \setof{1,2,4,5,8}$
1. $\setof{5} \notin \setof{1,2,4,5,8}$
1. $5 \in \setof{1,2,4,5,8} \notin 6$ or $5 \in \setof{1,2,4,5,8} \not\ni 6$.
:::

::: solution_explained

1. The set $\setof{1,2,4,5,8}$ has 5 as one of its members, which we write as $5 \in \setof{1,2,4,5,8}$.
1. On the other hand, $6$ is nowhere to be found in $\setof{1,2,4,5,8}$, its only elements are $1$, $2$, $4$, $5$, and $8$.
   Hence $6 \notin \setof{1,2,4,5,8}$.
1. This one is a bit tricky.
   We already know that $\setof{1,2,4,5,8}$ contains $5$, but that's not the same thing as containing $\setof{5}$, i.e. the set containing $5$.
   None of the elements of $\setof{1,2,4,5,8}$ is $\setof{5}$.
   By the way, this is also why $5 \notin \setof{1,2,4,\setof{5},8}$.
   Never confuse an object with a set containing that object, the two are very different things. 
1. We already know that $\setof{1,2,4,5,8}$ contains $5$, so the first gap must be $\in$.
   For the second gap, there are two options.
   If we fill the gap with $\notin$, we are saying that $\setof{1,2,4,5,8}$ is not a member of $6$, which is true, but it's an odd thing to say as $6$ isn't a set to begin with.
   Instead, it makes more sense to fill the gap with $\not\ni$, which states that $6$ is not a member of $\setof{1,2,4,5,8}$.
:::

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

::: jupyterpython
import re

def text_to_set(text):
    return set(re.findall(r"\w+", text.lower()))

text1 = "If John slept, then Mary left."
text2 = "If Mary left, then John slept."

set1, set2 = text_to_set(text1), text_to_set(text2)
print("Are the sets identical?")
print("Yes") if set1 == set2 else print("No")
:::

::: exercise
For each one of the following, fill the gap with $=$ or $\neq$ as appropriate:

1. $\setof{a,b} \_ \setof{a,b}$
1. $\setof{b,a} \_ \setof{a,b}$
1. $\setof{b,a,c,d} \_ \setof{e,a,b,d}$

::: solution
1. $\setof{a,b} = \setof{a,b}$
1. $\setof{b,a} = \setof{a,b}$
1. $\setof{b,a,c,d} \neq \setof{e,a,b,d}$ (assuming that $c$ and $e$ are distinct objects)
:::

::: solution_explained
1. Two sets are identical if they contain exactly the same elements.
   This is clearly the case here, both sets contain $a$, both of them also contain $b$, and they contain nothing else.
1. It may seem like $\setof{b,a}$ is different from $\setof{a,b}$, but remember that sets are unordered.
   It does not matter in what order we write down the elements, all that matters is whether the sets have the same members.
   And this is still the case here.
1. Each one of the sets contains four elements, three of which are $a$, $b$, and $d$.
   Only the first set contains $c$, and only the second set contains $e$.
   This suggests that the sets are not equivalent.
   However, we have to be careful here as $c$ and $e$ may just be different ways of referring to the same object.
   As a concrete example, suppose that we are talking about sets of actors, and we are looking at the sets $\{$Arnold$\}$ and $\{$Schwarzenegger$\}$.
   These are not actually distinct sets, they are just different ways of writing down the set that contains only the actor Arnold Schwarzenegger.
   So remember: what matters isn't how we choose to write down a set, what matters is what it actually contains. 
   If both $c$ and $e$ are just ways of referring to, say, the number $5$, then the two sets above are equivalent.
:::

:::

## Lack of duplicates/Idempotency

Sets are **idempotent**, which means that duplicates are ignored.
So $\setof{a,b} = \setof{a,a,b} = \setof{a,b,b,a,b,a,b,a,a}$.
It also holds that $\setof{a} = \setof{a,a} = \setof{a,a,a}$, and so on.

::: jupyterpython
import re

def text_to_set(text):
    return set(re.findall(r"\w+", text.lower()))

text1 = "If John slept, then Mary left."
text2 = "If Mary left, then John slept."

set1, set2 = text_to_set(text1), text_to_set(text2)
print("Are the sets identical?")
print(set1 == set2)
:::

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

1. $\setof{a,b} \_ \setof{a,a,b,b}$
1. $\setof{b,a} \_ \setof{a,b,a}$
1. $\setof{c,b,a,a,d,c} \_ \setof{a,a,b,d,c,c,c}$
1. $\setof{a} \_ \setof{a,a,a,a,a,a,c,a,a,a,a,a,a}$

::: solution
1. $\setof{a,b} = \setof{a,a,b,b}$
1. $\setof{b,a} = \setof{a,b,a}$
1. $\setof{c,b,a,a,d,c} = \setof{a,a,b,d,c,c,c}$
1. $\setof{a} \neq \setof{a,a,a,a,a,a,c,a,a,a,a,a,a}$
:::

::: solution_explained
1. Remember, one and the same element cannot be contained in a set multiple times.
   Either it is a member of the set, or it is not a member, it cannot be a member two times, or three times, or anything like that.
   Hence $\setof{a,a,b,b} = \setof{a,b,b} = \setof{a,b}$.
1. The same logic applies in this case: $\setof{a,b,a} = \setof{a,b}$, which is the same as $\setof{b,a}$ because sets are not ordered.
1. Again we have two identical sets.
   The first set contains $a$, $b$, $c$, $d$, and nothing else, and the same is true for the second set.
1. Finally we have two sets that are distinct.
   The second set could be written more compactly as $\setof{a,c}$, and that is not the same set as $\setof{a}$ because only the former contains $c$.
:::

:::

::: exercise
The sentence *If police police police, then police police police* actually uses two different word types.
It just just so happens that both are pronounced and spelled *police*.
But one is the noun *police*, the other one the verb *police*.
So we might want to annotate the string as follows:
*If police[N] police[V] police[N], then police[N] police[V] police[N]*.
Assume that words are annotated with their part of speech in this fashion.
Then what would be the corresponding set of words?

::: solution
$\setof{
\text{if},
\text{police[N]},
\text{police[V]},
\text{then}
}$.
:::

::: solution_explained
We can build this set incrementally by moving from left to right through the string *If police[N] police[V] police[N], then police[N] police[V] police[N]* (ignoring capitalization).
The string starts with *if*, so at this point our set is $\setof{\text{if}}$.
Next we see *police[N]*, and since this is not in our set yet, we add it and obtain $\setof{\text{if}, \text{police[N]}}$.
After that we encounter *police[V]*, which is not an element of our set yet --- the set only contains the noun *police*, not the verb *police*.
Hence we add *police[V]*, yielding $\setof{\text{if}, \text{police[N]}, \text{police[V]}}$.
Now the next word is *police[N]*, but since that's already in our set we do not need to add it again (there's no point in writing down the same element multiple times).
After that we add *then*, and at this point we are done.
Our set is $\setof{\text{if}, \text{police[N]}, \text{police[V]}, \text{then}}$, and our example sentence contains no words after *then* that aren't already members of this set.
:::

:::

## Recap

- Sets are collections of arbitrary objects.
- Sets are unordered and idempotent (= duplicates are ignored).
- Sets can be defined with list notation, e.g. $\setof{a, b}$.
- The objects contained in a set are called its *elements* or *members*.
- The symbols $\in$ and $\notin$ are used to indicate membership and non-membership, respectively.
- Occasionally, $\ni$ is used as the mirror image of $\in$.
