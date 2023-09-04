# Sets: The basics (Solutions)

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
