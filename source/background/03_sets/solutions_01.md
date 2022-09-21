# Sets: Additional notation (Solutions)

::: exercise
For each one of the statements below, say whether it is true or false.

1. $\emptyset = \setof{}$
1. $\emptyset \in \setof{a}$
1. $\setof{a,b} \neq \emptyset$

::: solution
1. $\emptyset = \setof{}$ is true
1. $\emptyset \in \setof{a}$ is false
1. $\setof{a,b} \neq \emptyset$ is true
:::

::: solution_explained
1. This is correct, $\emptyset$ is just a different way to refer to $\setof{}$, the set without any members.
1. The set $\setof{a}$ only contains the element $a$, it does not contain $\emptyset$.
   If it did, the set would be written $\setof{ \emptyset, a}$.
   Hence $\emptyset \notin \setof{a}$.
1. Two sets $A$ and $B$ are distinct if there is at least one element $x$ such that $x \in A$ but $x \notin B$ (which we can also write as $A \ni x \notin B$).
   In our case, there are two such elements, as $\setof{a,b} \ni a \notin \emptyset$ and $\setof{a,b} \ni b \notin \emptyset$.
:::

:::

::: exercise
For each one of the following, put $=$ or $\neq$ in the gap as appropriate:

1. $\setof{0,1,2,3,4,5} \_ \setof{ 10 - x \mid x \in \setof{5,6,7,8,9,10} }$
1. $\emptyset \_ \setof{ x \mid x \text{ is both a square and a circle}}$
1. $\setof{2,3,5,7} \_ \setof{n + 1 \mid n \text{ is a prime number between 0 and 10}}$

::: solution
1. $\setof{0,1,2,3,4,5} = \setof{ 10 - x \mid x \in \setof{5,6,7,8,9,10} }$
1. $\emptyset = \setof{ x \mid x \text{ is both a square and a circle}}$
1. $\setof{2,3,5,7} \neq \setof{n + 1 \mid n \text{ is a prime number between 0 and 10}}$
:::

::: solution_explained
1.  The set $\setof{ 10 - x \mid x \in \setof{5, 6, 7, 8, 9, 10}}$ contains
    $5$ ($10 - 5$),
    $4$ ($10 - 6$),
    $3$ ($10 - 7$),
    $2$ ($10 - 8$),
    $1$ ($10 - 9$),
    and
    $0$ ($10 - 10$),
    That is indeed the same as $\setof{0,1,2,3,4,5,}$.

1.  There is no $x$ both a square and a circle, hence the set $\setof{ x \mid x \text{ is both a square and a circle}}$ is empty and thus equivalent to $\emptyset$.

1.  The prime numbers between 0 and 10 are 2, 3, 5, and 7 (remember, 1 is not a prime number).
    The set $\setof{n + 1 \mid n \text{ is a prime number between 0 and 10}}$ thus consists of
    $3$ ($2 + 1$)
    $4$ ($3 + 1$)
    $6$ ($5 + 1$),
    and
    $8$ ($7 + 1$).
    But $\setof{3,4,6,8} \neq \setof{2,3,5,7}$.
:::

:::

::: exercise
Express the following in terms of set-builder notation:

1. $\setof{\text{George Washington}, \text{John Adams}, \text{Thomas Jefferson}}$
1. $\setof{\text{a}, \text{e}, \text{i}, \text{o}, \text{u}}$

::: solution
1. $\setof{x \mid x \text{ is one of the first three presidents of the United States}}$
1. $\setof{x \mid x \text{ is a vowel of the English alphabet}$
:::

::: solution_explained
1. Depending on how well you know your US history, this one might have required a bit of research.
   But once you know what these three names have in common and what separates them from everything else, you can easily talk about the set of all $x$ such that $x$ is one of the first three presidents of the United States.
   The rest is just a matter of transforming that English statement into set-builder notation.

   Note that there are many other ways to pick out the same set.
   For instance, the set $\setof{x \mid x \text{ was a US president before James Madison}}$ would describe the same set because Jame Madison was the fourth president.
   So one and the same set can be defined in many different ways via set-builder notation.

   In addition, the exercise doesn't actually tell us what exactly the set is supposed to contain.
   Is it the president's themselves, or strings that correspond to these presidents' names?
   Depending on your interpretation, this also gives us slightly different definitions.

1. Again there are many different possible definitions (and the one given is a little iffy anyways as English also uses *y* for vowels).
   Instead, we could have defined this as the set of characters that correspond to the numbers 97, 101, 105, 111, and 117 of the ASCII text encoding.
   Or the set of letters that are said at specific timestamps of the ABC song.
   Or the set of letters that you like best (assuming that those are actually *a*, *e*, *i*, *o*, and *u*).
   There's infinitely many solutions, the important thing is whether yours uses the set-builder notation correctly.
   
:::

:::
