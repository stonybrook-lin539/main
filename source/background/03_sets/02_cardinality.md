---
pagetitle: >-
    Cardinality
---

# Cardinality

:::prereqs
- functions (basic notation, domain terminology)
- sets (basic notation, operations)
:::

Sets can be compared based on how many elements they contain.

::: example
The set $A \is \setof{a,b,c}$ contains exactly as many elements as the set $X \is \setof{x,y,z}$, namely $3$.
Each set has fewer members than $A \cup X$, which contains $6$ elements, whereas $A \cap X$ has $0$ members.
:::

This is commonly called the **size** of a set, but the more accurate term is **cardinality**.
The cardinality of a set $A$ is denoted $\card{A}$.

Often we do not care about the exact value of $\card{A}$ but rather how it compares to $\card{B}$ for some other set $B$.
In such cases it isn't always practical to simply count how many members each set has (the sets may be very large, or perhaps even infinite).
Instead, one can use functions to compare the cardinality of sets.
We say that $\card{A} \leq B$ iff there is a (total) function $f$ such that every element of $A$ is mapped to some element of $B$ and every element of $B$ has at most one element of $A$ mapped to it.
The second half of that clause means that $f$ must be **injective** (or equivalently, **one-to-one**): if $x \neq y$, then $f(x) \neq f(y)$.

::: example
Suppose that $A \is \setof{a,b,c}$ and $D \is \setof{d,e,f,g}$.
Then $\card{A} \leq \card{D}$, as every element of $A$ can be mapped to some distinct element of $D$.
For instance, we could have a function with
$a \mapsto f$,
$b \mapsto d$,
$c \mapsto g$.

In the other direction, $\card{D} \not\leq \card{A}$.
No matter how one maps the elements of $D$ to members of $A$, at least two members of $D$ will have to be mapped to the same element in $A$.
:::

::: exercise
Show that $\card{\setof{3, \emptyset, 3}} \leq \card{\setof{\mathit{John}, \mathit{Mary}, \emptyset}}$ by giving a function that maps every element of the former set to some member of the latter.
:::

Given the definition above, we have $\card{A} = \card{B}$ iff $\card{A} \leq \card{B}$ and $\card{B} \leq \card{A}$ are both true.
But this means we would have to specify two separate functions, one from $A$ to $B$ and one from $B$ to $A$.
There is a more direct definition that does this with just one function.
First, a (total) function $f: A \rightarrow B$ is a **bijection** or **one-to-one correspondence** iff it is injective and for every $b \in B$ there is some $a \in A$ such that $f(a) = b$ (we also say that the function is **surjective** or **onto**).
In other words, $f$ maps every element of $A$ to some element of $B$ and every element of $B$ has exactly one element of $A$ mapped to it.
Then $\card{A} = \card{B}$ iff there is a bijection $f: A \rightarrow B$.

::: example
We already saw that $\card{A} = \card{X}$ for $A \is \setof{a,b,c}$ and $X \is \setof{x,y,z}$.
A possible choice of $f$ would be
$a \mapsto x$,
$b \mapsto y$,
$c \mapsto z$.
:::

::: example
The sets $A \is \setof{0,1,2}$ and $B \is \setof{2,3}$ obviously have distinct cardinality.
The set $A$ contains 3 elements, the set $B$ only 2.
But let us see how we get the same result via our mathematical definition.

Suppose we have some arbitrary function $f: A \rightarrow B$.
If $f$ is a bijection, then it must map every element of $A$ to some element of $B$.
But since there are three elements in $A$ and only two in $B$, some element of $B$ must be the output for at least two elements of $A$.
But then $f$ is not a bijection.

In the other direction, consider some arbitrary function $g: B \rightarrow A$.
Since a function maps each input to at most one output, the two elements of $B$ are mapped to at most two elements of $A$.
But $A$ has three elements, so one element of $A$ cannot be an output for any element of $B$.
Again we find that $g$ cannot be bijection.

This exhausts all cases we need to consider, and we may conclude that no function from $A$ to $B$, or the other way round, can be a bijection.
Hence $A$ and $B$ must have distinct cardinality.
:::

::: exercise
Show that
Let $O$ be the set of all odd natural numbers that are at least $0$ and at most $9$, and $E$ the set of all even natural numbers that are at least $0$ and at most $9$.
Show that $\card{O} = \card{E}$.
:::

For finite sets, our intuitive notion of size closely matches the technical term of cardinality.
However, size and cardinality diverge once we look at infinite sets.

::: example
Consider the set $\mathbb{N} \is \setof{0,1,2,\ldots}$ of all natural numbers and the set $\mathbb{N}_+ \is \setof{1,2,\ldots}$ of all positive natural numbers.
Intuitively, $\mathbb{N}$ is larger than $\mathbb{N}_+$ because it contains all members of $\mathbb{N}_+$ as well as 0, which is not in $\mathbb{N}_+$.
But the function $f: \mathbb{N} \rightarrow \mathbb{N}_+$ with $n \mapsto n+1$ is a bijection.
It maps $0$ to $1$, $1$ to $2$, and so on, so that every natural number is mapped to a positive natural number, and every positive natural number has some natural number mapped to it.
Hence $\card{\mathbb{N}} = \card{\mathbb{N}_+}$ even though intuitively the two sets have distinct size.
:::

::: exercise
Show that the set of natural numbers has the same cardinality as the set of all even natural numbers.
:::

In a later chapter, we will see that our definition of cardinality entails that there are different "sizes" of infinity, and that we want one specific infinity size to talk about language.

## Recap

- Instead of the intuitive notion of size, we use the formal notion of **cardinality** to measure how many elements a set contains.
- For every finite set $A$, its cardinality $\card{A}$ is the number of elements it contains.
- We can use functions to measure the relative cardinality of distinct sets $A$ and $B$.
    - $\card{A} \leq \card{B}$: there exists a total, injective function $f: A \rightarrow B$ (where $f$ is **injective** iff $x \neq y$ implies $f(x) \neq f(y)$).
    - $\card{A} \geq \card{B}$: there exists a total, surjective function $f: A \rightarrow B$ (where $f$ is **surjective** iff for every $b \in B$ there is some $a \in A$ such that $f(a) = b$).
    - $\card{A} = \card{B}$: there exists a bijection $f: A \rightarrow B$ (where $f$ is a **bijection** iff it is both injective and surjective).
- When the name of function $f$ is clear from context, one may write $x \mapsto y$ instead of $f(x) = y$.
- While cardinality is very intuitive for finite sets, it yields surprising results with infinite sets.
