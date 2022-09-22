**Prerequisites**

- sets (basic notation)

# Sets: Additional notation

## The empty set

While the intuition of sets as collections is fairly intuitive, intuition only goes so far.
Many sets are rather strange and do not gel with the metaphor of sets as containers.
One example of that is the *empty set*, written $\setof{}$ or more commonly $\emptyset$.

The empty set contains nothing.
So there is no $a$ such that $a \in \emptyset$.
At the same time, the empty set is not simply nothing because it is still a set.
A set is not nothing.
This might make more sense if you think of sets as boxes or bags: an empty bag is still a bag, it just happens to contain nothing.

The empty set may seem rather useless to you at this point, but it actually has a very important role to play. 
You will see it quite a bit in definitions, but also in the construction of abstract mathematical objects such as [monoids](fixme).

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

## Set-builder notation

### Motivation

Defining a set by listing all its elements is only feasible for small sets.
But many sets are very large, for example the set of atoms in the universe (10^82^), or the set of bad horror movies produced after *Scream* (not quite as big, but too big to write down).
Some sets can even be infinite, like the set of natural numbers or just the even natural numbers.
If one cannot write down a list of all the elements, just how does on specify such a list?

One could approximate these sets, e.g. by writing $\setof{2, 4, \ldots}$ for the set of natural numbers that are even and greater than $0$.
But this is imprecise because there are many other sets that contain these numbers, for example the set of powers of 2: $\setof{1, 2, 4, 8, 16, \ldots}$.
You might object that $1$ is implicitly excluded because we the set started with $2$, but that's just your intuition, not a firm rule.
Remember, sets have no order, so a set does not start with anything.
And even if we take such human intuitions into account, it's still too imprecise for more complex cases.
Rather than rely on human intuition about what would be a natural interpretation of the ellipsis dots, we can use *set-builder notation* to succinctly describe large/infinite sets.

### Format

Set-builder notation uses the general template

$$
\setof{ \text{expression using variable} \mid \text{definition of variable} }
$$

::: example
Instead of $\setof{2, 4, 6, \ldots}$ for the set of natural numbers that are both positive and even, one can write the following:
$$
\setof{ 2n \mid \text{$n$ a natural number and $n \geq 1$}}
$$
This means that for every $n$ that is a natural number and is at least $1$, the set contains $2n$.

The table below illustrates this for a few values.
:::

| $n$ | Satisfies definition? | $2n$ | 
| :-- | :-:                   | --:  | 
| 0   | No                    | -    | 
| 0.3 | No                    | -    | 
| 1   | Yes                   | 2    | 
| 1.7 | No                    | -    | 
| 2   | Yes                   | 4    | 
| 3   | Yes                   | 6    | 


::: jupyterpython
# set-builder notation even exists in some programming languages like Python
built_set = set(2*n for n in [0, 1, 2, 3, 4, 5])
print(built_set)
:::

There is no limit on the complexity of set-builder notation.
For example, one could nest multiple set definitions, as in $\setof{ \setof{ i \mid 0 \leq i \leq n } \mid n \text{ a natural number} }$.
This is a set that contains all initial intervals of the natural numbers: $\setof{ \setof{0}, \setof{0,1}, \setof{0,1,2}, \setof{0,1,2,3}, \ldots }$ (yes, sets can contain other sets, more on that in a later unit).
However, such nested definitions are often cumbersome to read, so try to avoid this.
Quite generally, definitions should not intimidate or dazzle the reader.

::: advice
A good definition is as complex as necessary and as simple as possible.
:::

::: example
The following definition is more complex because it uses multiple variables and uses the expression to define two values at the same time.
But it is still fairly simple and could be used in a definition:
$$
\setof{ x^y, y^{10} | 1 \leq x \leq 3, y \in \setof{2,7}, \text{ and } x + y \geq 5}
$$

The table below shows all the values for the variables and the resulting elements of the set.
:::

| $x$ | $y$ | $x + y \geq 5$? | added $x^y$ | added  $y^{10}$ | 
| :-  | :-  | :-              | :-          | :-              |
| 1   | 2   | no              | -           | -               | 
| 1   | 7   | yes             | 1           | 282,475,249     | 
| 2   | 2   | no              | -           | -               | 
| 2   | 7   | yes             | 128         | 282,475,249     | 
| 3   | 2   | yes             | 9           | 1024            | 
| 3   | 7   | yes             | 2187        | 282,475,249     | 

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

## Summary

- The empty set, denoted $\emptyset$, contains no elements at all.
- Set-builder notation uses the format $\setof{ \text{expression using variable(s)} \mid \text{definition of variable(s)} }$.
