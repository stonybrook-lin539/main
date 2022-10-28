# Relations (Solutions)

::: exercise
Let $R$ be the relation that connects words to their parts of speech (N for nouns, V for verbs, A for adjectives, P for prepositions, D for determiners, and so on).
List the following for English:

1. export $R$
1. apple $R$
1. $R$ P

::: solution
1. export $R$ $= \setof{N, V}$
1. apple $R$ $= \setof{N}$
1. $R$ P is the set of all English prepositions: *on*, *in, *to*, *onto*, *into*, *up*, *down*, *above*, *under*, *next to*, and so on.
:::

:::

::: exercise
For each one of the following, say whether it is a function or just a relation.

1. the parent-of relation (e.g. $j \mathrel{P} m$ for "John is a parent of Mary")
1. the parent-of relation in a world where the one-child policy is enforced globally
1. the relation between a car's license plate and its owners
1. the prefix relation, where $u$ is a prefix of $v$ iff there is some $w \in \Sigma^*$ such that $v = u \stringcat w$

::: solution
1. Since an individual can be the parent of more than one individual, this is a relation but not a function.
1. If we assume that everybody actually obeys this policy, and that the policy has been active for so long that nobody who reached puberty before the policy is still alive, then it is true for all individuals currently alive that each one of them has at most one child.
   Hence the parent-of relation for individuals currently alive would be a function.
1. If a car can be registered to multiple owners, then this is not a function, but it is still a relation of course.
1. The prefix relation is not a function.
   For example, the string *ab* is a prefix of infinitely many strings, including *ab*, *aba*, *abab*, and so on.
:::

:::

::: exercise
Is the following statement true or false?
Justify your answer.

Every relation $R$ can be regarded as a function that maps $x$ to $x \mathrel{R}$.

::: solution
This statement is true.
Suppose, for instance, $R \is \setof{ \tuple{a,b}, \tuple{a,c} , \tuple{b,c}}$.
Then we may construct a new function $r$ from $R$ such that $r(a) = \setof{b,c}$ and $r(b) = \setof{c}$, and $r(c) = \emptyset$.
This function $r$ conveys the same information as $R$.

Reasoning a bit more abstractly:
Let $r$ be a function such that $r(x) = x \mathrel{R}$.
First, it is indeed the case that $r$ is a function since, given how we defined $r$, there can be no two $y$ and $z$ such that $r(x) = y$ and $r(x) = z$ and $y \neq z$.
If there were two such $y$ and $z$, then that would mean that there are two distinct sets that are both identical to $x \mathrel{R}$, which is impossible.
Second, we can construct a relation $R'$ from $r$: for every $x$ in the domain of $r$, $R'$ contains every pair $\tuple{x,y}$ such that $y \in r(x)$.
But $R'$ is exactly the same as $R$, which shows that we can freely switch between the relation $R$ and the function $r$ as we see fit.
:::

:::
