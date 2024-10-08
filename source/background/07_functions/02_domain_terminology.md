---
pagetitle: >-
    Domains and co-domains
---

# Domains and co-domains

:::prereqs
- functions (basic notation)
- sets (basic notation)
:::

Every function has a **domain** and a **co-domain**.
The domain is the set of objects from which its arguments can be drawn, and the **co-domain** is the set of objects from which outputs can be drawn.

## Notation

One commonly writes $f: D \rightarrow C$ to indicate that $f$ is a function from domain $D$ to co-domain $C$.
A function is always undefined on all arguments that do not belong to its domain.

::: example
Consider the function $f(x) = x +1$.
This actually represents multiple functions depending on how one picks the domain and co-domain.

Suppose $f: \mathbb{N} \rightarrow \mathbb{N}$.
Then $f$ is a function from natural numbers (0, 1, 2, \ldots) to natural numbers.
In this case we have, among others, $f(0) = 1$ and $f(500) = 501$.
However, $f(-1)$ or $f(2.5)$ would be undefined because $-1$ and $2.5$ are not natural numbers.
:::

::: example
Now suppose that we have $f(x) = x + 1$ with $f: \mathbb{R} \rightarrow \mathbb{R}$, i.e. $f$ is a function from real numbers to real numbers.
The set of real numbers, denoted $\mathbb{R}$, includes every number you came across in high school, e.g. $1$, $1.38702$, $-\frac{5}{17}$, $\sqrt{2}$, $\pi$, and so on.
Since the domain and co-domain of this version of $f$ are a lot larger, $f$ is defined on a lot more values and we have $f(-1) = 0$ and $f(2.5) = 3.5$.
:::

::: exercise
Suppose that $f$ is still defined by $f(x) = x + 1$, but we have $f: \mathbb{R} \rightarrow \mathbb{N}$.
For each one of the following, say whether it is defined or undefined.

1. $f(0)$
1. $f(-1)$
1. $f(-2)$
1. $f(2.5)$

::: solution
1. Defined
1. Defined
1. Undefined
1. Undefined

::: solution_explained
We have to pay attention to two separate issues for every instance of $f(x)$:

1. Is the input $x$ a member of the domain $\mathbb{R}$, which consists of all real numbers.
1. Is the output $x+1$ a member of the co-domain $\mathbb{N}$, which consists of $0$, $1$, $2$, $3$, and so on.

Since $0$, $-1$, $-2$, and $2.5$ are all real numbers, all the cases in the exercise involve valid inputs for the function (an example of an invalid input would be $f(\mathit{hello})$). 
However, not all of these valid inputs result in valid outputs.
The inputs $0$ and $-1$ are mapped to $1$ and $0$, respectively, which are members of the co-domain $\mathbb{N}$.
However, the output of $-2$ is $-1$, and $2.5$ is mapped to $3.5$.
Neither $-1$ nor $3.5$ are natural numbers.
Hence our function $f$ is undefined for $-2$ and $2.5$ even though they are members of the domain of $f$.
:::
:::
:::

::: example
When a car wash is viewed as a function, its domain is the set of all cars (both dirty and clean), whereas the co-domain only contains clean cars (again, in an ideal world where there's no such think as broken car washes).
:::

::: exercise
What would be the domain and co-domain of a broken car wash that fails to remove even the tiniest speck of dirt?

::: solution
Similar to the working car wash from the example above, the broken car wash would correspond to a function that the set of all cars (both dirty and clean) as its domain.
But now this set would also be its co-domain because dirty cars still come out dirty.
:::
:::

It is important to keep in mind that the domain and co-domain do not need to provide a perfect fit.
Not every element in the domain may actually be mapped to some element of the co-domain, and not every element of the co-domain may be an output for some input.

::: example
Consider the function $f: \mathbb{N} \rightarrow \mathbb{N}$ such that $f(x) = 2x - 1$.
Even though $0$ is a natural number and hence in the domain of $f$, $f(0)$ is undefined because $f(0) = 2 \mult 0 - 1 = -1$ is not a natural number and hence not in the co-domain of $f$.
But there are also many natural numbers in the co-domain that can never be the output of $f$, e.g. $4$.
:::

::: exercise
Explain why there is no natural number $x$ such that $f$ from the example above maps $x$ to $4$.

::: solution
The function is $f: \mathbb{N} \rightarrow \mathbb{N}$ with $f(x) = 2x - 1$.
Note that as $x$ increases, so does the value of $f(x)$.
We have $f(2) = 4 - 1 = 3$ and $f(3) = 6 - 1 = 5$.
Hence any $x$ that is mapped to $4$ would have to be such that we have $2 < x < 3$.
But the domain of $f$ is limited to natural numbers, and the set of natural numbers contains no such $x$ strictly between $2$ and $3$.
:::
:::

## Total and partial functions

In the example above, the function $f$ is **partial** because it is not defined on all values of the domain.
A **total** function, on the other hand, maps every element of its domain to some element of its co-domain.
Fields differ in whether they take total or partial functions to be the default.
For example, computer scientists usually assume total functions and explicitly mention it when a function is partial, whereas it is common in calculus to assume partial functions and explicitly mention it when a function is total.
Of course every partial function can be made total by giving a tighter definition of its domain, but this is not always practical.
Sometimes the function is so complex that one simply cannot say what elements it is defined on, and hence one can only approximate its domain.

Quite generally, it is a matter of taste how tightly one wants to define the domain and co-domain.
A loose definition tells the reader very little about what gets mapped to what by the function, but a definition with a very tight fit, if it can be found at all, makes things difficult to read.
Nonetheless, the domain and co-domain are a crucial part of a function's definition, and this is why they are usually specified before the precise mapping from inputs to outputs is even given.

::: example
Here is an example of what this may look like:
Let $E$ be the set of English first names.
Then the function $f: E \rightarrow \setof{0,1}$ maps $n$ to $1$ iff $n$ contains at least three syllables.
:::

## The $\mapsto$ notation

Irrespective of how one defines the domain and co-domain, and irrespective of whether a function is total or partial, the mapping from arguments to outputs can be defined in various ways, e.g. in plain English, or as a formula like $f(x) = \frac{(x + x^2 + 5)^{x+1}}{1000^x}$.
For very simple functions whose name was already mentioned, one often writes $x \mapsto y$ instead of $f(x) = y$.

::: example
Instead of $f(x) = 5 \mult x - 3$, we may simply write $x \mapsto 5 \mult x - 3$.
:::

The same notation can be used to indicate $f(x)$ for specific choices of $x$.

::: example
Instead of $f(2) = 7$, we may simply write $2 \mapsto 7$.
:::

**Caution:**
Notice the difference between $\rightarrow$ and $\mapsto$.
The first is used when specifying the domain and co-domain, whereas the latter indicates the concrete mapping from an argument to an output.

## Recap

- The behavior of a function depends greatly on its **domain** and **co-domain**.
  The domain specifies the set that inputs can be drawn from, and the co-domain is the set that outputs can be drawn from.
- The standard notation is *function name: domain $\rightarrow$ co-domain*, e.g. $f: \Sigma^* \rightarrow \mathbb{N}$.
- A function is **total** if it is defined for all elements of its domain.
  Otherwise it is **partial**.
- When the function we are defining is already clear from context, we may write $x \mapsto y$ instead of $f(x) = y$.
  For example, $x \mapsto 2^x - 5$ is an alternative to $f(x) = 2^x - 5$.

\includecollection{solutions}
