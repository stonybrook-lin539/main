---
pagetitle: >-
    Tuples: The basics
---

# Tuples: The basics

::: prereqs
- sets (basic notation)
:::


Like sets, tuples are collections of elements.
Tuples also allow an element to be present multiple times, so they are not idempotent.
And tuples also care about the order of the elements.
This makes them very similar to strings, but tuples are more general because they can contain arbitrary objects, including other tuples.


## Notation

An $n$-tuple $u$ consists of exactly $n$ elements.
We also say that $u$ has **length** $n$
One also writes $\length{u} = n$ to indicate that the tuple $u$ has length $n$, and in this case we say that $u$ has $n$ components.
Tuples are usually written between pointy brackets, e.g. the pair $\tuple{a,b}$, the triple $\tuple{a,b,c}$, or the $1$-tuple $\tuple{a}$.

::: example
The pair $\tuple{a,b}$ is of length $2$. 
Its first component is $a$, its second component is $b$.

The pair $\tuple{a,a}$ is also of length $2$.
Its first component is $a$, and its second component is also $a$.
:::

Tuples may contain complex objects, including other tuples.
The content of these objects is not considered when computing a tuples length.

::: example
Consider $\tuple{a,b}$ and $\tuple{a,\setof{b,c}}$.
They are distinct tuples, but they are both of length 2.
:::

::: exercise
For each one of the following tuples, compute its length.

- $\tuple{a,b,a}$
- $\tuple{a,\tuple{b},a}$
- $\tuple{a,\tuple{b,a}}$
- $\tuple{\setof{a,b}, \tuple{a}}$
- $\tuple{\tuple{a, b,\setof{a,a}}}$
:::

Sometimes we are only interested in a specific component of a tuple.
In this case, we write $\pi_i(u)$ for the $i$-th component of $u$.
Sometimes this is also called the $i$-th **projection** of $u$.

::: example
Consider once more the pair $\tuple{a,b}$.
Here $\pi_1(\tuple{a,b}) = a$ and $\pi_2(\tuple{a,b}) = b$.

For the pair $\tuple{a,a}$, $\pi_1(\tuple{a,a})$ and $\pi_2(\tuple{a,a})$ are both $a$.
:::

Note that $\pi_i(u)$ is undefined if $u$ is not a tuple or if $i$ exceeds the length of $u$.

::: example
There is no defined value for $\pi_3(\tuple{a,b})$ because $\tuple{a,b}$ has only two components and thus cannot have a third component.
Similarly, $\pi_3(\setof{a,b,c})$ is undefined because sets only have elements, not components.
:::

::: exercise
For each one of the formulas below, what is its value?

- $\pi_3(\tuple{a,b,c,d})$
- $\pi_8(\tuple{a,b,c,d})$
- $\pi_0(\tuple{a,b,c,d})$
- $\pi_3(\tuple{a,b,\tuple{c,d}})$
- $\pi_1(\pi_3(\tuple{a,b,\tuple{c,d}}))$
:::


## Identity

Two tuples $u$ and $v$ are identical iff they are of the same length $n$ and agree on all their components: for all $0 < i \leq n$, it must hold that $\pi_i(u) = \pi_i(v)$.

::: example
The pair $\tuple{a,a}$ is distinct from the 1-tuple $\tuple{a}$, the triple $\tuple{a,a,a}$, or the $4$-tuple $\tuple{a,a,a,a}$ because all these tuples have distinct length.
:::

::: example
The tuple $\tuple{3,5}$ is distinct from the tuple $\tuple{5,3}$.
While they have the same length, they differ on their first component: $\pi_1(\tuple{3,5}) = 3 \neq 5 = \pi_1(\tuple{5,3})$.
They also differ on their second component, but we don't even need to consider this because disagreeing on a single component is enough to render tuples distinct.
:::

::: exercise
Explain why $\tuple{a,b} = \tuple{b,a}$ implies $a = b$.
:::

This definition of identity of tuples immediately implies two crucial properties:

1. In contrast to sets, tuples are not idempotent.
1. In contrast to sets, tuples care about order.

::: exercise
Fill in the gaps with $=$ and $\neq$ as appropriate, assuming that $a$ and $b$ are distinct elements:

- $\tuple{a} \_ \tuple{b}$
- $\tuple{a,b,a} \_ \tuple{a,b,b}$
- $\tuple{a,b,a,a} \_ \tuple{a,b,a,a}$
- $\tuple{a,a,b,a} \_ \tuple{a,b,a,a}$
- $\tuple{a,a,b,a} \_ \tuple{a,a,\setof{b},a}$
- $\tuple{a,a,b,a} \_ \tuple{a,\tuple{a,b},a}$
:::

Note that just like $a \neq \setof{a}$, it also holds that $a \neq \tuple{a}$.
A container with $a$ in it is not the same thing as $a$ by itself.


## Concatenation

Two tuples $a$ and $b$ can be concatenated into a single large tuple $a \tuplecat b$ that contains all elements of $a$ and $b$, in the same order.

::: definition
Given an $m$-tuple $a \is \tuple{a_1, \ldots, a_m}$ and an $n$-tuple $b \is \tuple{b_1, \ldots, b_n}$,
their **concatenation** is the $m+n$-tuple
$a \tuplecat b \is \tuple{a_1, \ldots, a_m, b_1, \ldots, b_n}$.
:::

Tuple concatenation is associative.
This means that for any tuples $a$, $b$, and $c$, it holds that $a \tuplecat (b \tuplecat c) = (a \tuplecat b) \tuplecat c$.

::: example
The concatenation of $\tuple{x,y}$ and $\tuple{z}$ is $\tuple{x,y,z}$.
If we concatenate $\tuple{x,y,z}$ and $\tuple{y,y,y}$, we get $\tuple{x,y,z,y,y,y}$.

We could have gotten the same result by proceeding in a different order.
We first concatenate $\tuple{z}$ and $\tuple{y,y,y}$ into $\tuple{z,y,y,y}$.
We then concatenate $\tuple{x,y}$ and $\tuple{z,y,y,y}$ to obtain $\tuple{x,y,z,y,y,y}$.
That's indeed the same output as before.
Overall, then,
$$(\tuple{x,y} \tuplecat \tuple{z}) \tuplecat \tuple{y,y,y} = \tuple{x,y} \tuplecat (\tuple{z} \tuplecat \tuple{y,y,y}) = \tuple{x,y,z,y,y,y,y}.$$
:::

::: exercise
Calculate the result of the following concatenations.

- $\tuple{a,b} \tuplecat ((\tuple{c} \tuplecat \tuple{a,b}) \tuplecat \tuple{a,c,e})$
- $(\tuple{a,b} \tuplecat \tuple{c}) \tuplecat (\tuple{a,b} \tuplecat \tuple{a,c,e})$

:::

::: exercise
Write down all possible ways of obtaining $\tuple{a,b,c,d}$ via concatenation of tuples whose length is at least $1$.
For instance, one possible way is $\tuple{a,b} \tuplecat \tuple{c, d}$, but there's several more.
:::

::: exercise
Tuple concatenation is not commutative.
That is to say, for some tuples $a$ and $b$ it is not the case that $a \tuplecat b = b \tuplecat a$.
Illustrate this with an example.
:::

Keep in mind that tuple concatenation is only defined for tuples.

::: example
None of the following are valid instances of tuple concatenation:

- $\tuple{a,b} \tuplecat 5$
- $\tuple{a,b} \tuplecat \setof{5}$
:::


## The empty tuple

Remember that strings had a special empty string $\emptystring$.
The tuple-counterpart for this is the **empty tuple** $\tuple{}$.
It is the only 0-tuple.
With respect to concatenation, the empty tuple behaves like $0$ with respect to addition.
That is to say, concatenating a tuple with the empty tuple does not change said tuple.

::: exercise
Compute $\tuple{a} \tuplecat \tuple{}$ and $\tuple{} \tuplecat \tuple{a,a,a}$.
:::


## Difference to strings

Strings can be regarded tuples over some fixed alphabet of symbols.
For instance, the string $\String{abc}$ can be viewed as the tuple $\tuple{a,b,c}$.
However, tuples are more general because their elements do not need to be symbols of some alphabet.
Just like sets (and multisets, if you have encountered those already), tuples can contain arbitrary objects.
So a tuple may consist of sets, multisets, other tuples, functions, relations, any combination of those, and much, much more.

::: example
All of the following are valid tuples, but none of them are possible strings:


- $\tuple{\setof{5, -5}, 25}$ is a pair that consists of the set $\setof{5, -5}$ and the number $25$.
- $\tuple{\mathbb{N}, \mathbb{N}, \mathbb{N}}$ is a triple where each component is the set of natural numbers.
- $\tuple{\mathbb{N}, \setof{3,7, \setof{112}}, +, -}$ is a $4$-tuple that consists of the set of natural numbers, the set $\setof{3,7, \setof{112}}$, and the operations of addition and subtraction.
- $\tuple{a, \tuple{b, \tuple{}, \tuple{c}, \tuple{d,e}, b}, \setof{1,2,3, \tuple{}}}$ is triple that consists of $a$, the 5-tuple $\tuple{b, \tuple, \tuple{c}, \tuple{d,e}, b}$, and the set $\setof{1,2,3, \tuple{}}$

:::

::: exercise
Does the concatenation of $\tuple{a,b}$ and $\tuple{c}$ yield the same result as the concatenation of $\tuple{a,b}$ and $\tuple{\tuple{c}}$?
Justify your answer!
:::


## Recap

- Tuples can be regarded as a generalization of strings.
  In fact, strings are often defined as just a shorthand notation for tuples.
- The **length** of $n$-tuple $u$ is denoted $\length{u}$, and we say that $u$ has $n$ **components**.
- The $i$-th component of $n$-tuple $u$ (for $0 < i \leq n$) is denoted $\pi_i(u)$, which is also called the $i$-th **projection** of $u$.

::: definition
Two tuples $u$ and $v$ are identical iff all of the following hold:

1. $\length{u} = \length{v}$, and
1. for all $0 < i \leq \length{u}$, $\pi_i(u) = \pi(v)$.
:::

- Like strings, tuples are ordered ($\tuple{a,b} \neq \tuple{b,a}$) and lack idempotency ($\tuple{a} \neq \tuple{a,a}$).
- Tuples can be concatenated ($u \tuplecat v$), again just like strings.
- The empty tuple $\tuple{}$ contains no elements at all.
  It is the tuple-counterpart to the empty string $\emptystring$.
- In contrast to strings, tuples can consist of objects of arbitrary complexity, not just symbols drawn from a fixed alphabet.

|           | **unordered** | **idempotent** | **can only contain symbols** |
| --:       | :-:           | :-:            | :-:                          |
| sets      | Y             | Y              | N                            |
| multisets | Y             | N              | N                            |
| tuples    | N             | N              | N                            |
| strings   | N             | N              | Y                            |

