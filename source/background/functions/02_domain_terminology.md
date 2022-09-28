# Domains and co-domains

Every function has a **domain** and a **co-domain**.
The domain is the set of objects from which its arguments can be drawn, and the **co-domain** is the set of objects from which outputs can be drawn.
A function is undefined on any arguments that do not belong to its domain.
One commonly writes $f: D \rightarrow C$ to indicate that $f$ is a function from domain $D$ to co-domain $C$.

::: example
Consider the function $f(x) = x +1$.
This actually represents multiple functions depending on how one picks the domain and co-domain.

Suppose $f: \mathbb{N} \rightarrow \mathbb{N}$.
Then $f$ is a function from natural numbers (0, 1, 2, \ldots) to natural numbers.
In this case we have, for instance, $f(0) = 1$ and $f(500) = 501$.
However, $f(-1)$ or $f(2.5)$ would be undefined because $-1$ and $2.5$ are not natural numbers.
:::

::: example
Now suppose that we have $f(x) = x + 1$ with $f: \mathbb{R} \rightarrow \mathbb{R}$, i.e. $f$ is a function from real numbers to real numbers.
(We haven't encountered real numbers yet, just assume that $\mathbb{R}$ includes pretty much number you have encountered in high school, e.g. $1$, $1.38702$, $-\frac{5}{17}$, $\sqrt{2}$, and so on.)
Now $f(-1)$ = 0$ and $f(2.5) = 3.5$.
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
:::

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

::: example
When a car wash is viewed as a function, its domain is the set of all cars (both dirty and clean), whereas the co-domain only contains clean cars.
:::

::: exercise
What would be the domain and co-domain of a broken car wash that fails to remove even the tiniest speck of dirt?
:::

::: solution
Similar to the working car wash from the example above, the broken car wash would correspond to a function that the set of all cars (both dirty and clean) as its domain.
But now this set would also be its co-domain because dirty cars still come out dirty.
:::

:::

Since it is so important to know the domain and co-domain of a function, those are usually specified before the precise mapping from inputs to outputs is given.

::: example
Let $E$ be the set of English first names.
Then the function $f: E \rightarrow \setof{0,1}$ maps $n$ to $1$ iff $n$ contains at least three syllables.
:::

The mapping from arguments to outputs can be defined in various ways, e.g. in plain English, or as a formula like $f(x) = \frac{(x + x^2 + 5)^{x+1}}{1000^x}$.
For very simple functions whose name was already mentioned, one often writes $x \mapsto y$ instead of $f(x) = y$.

::: example
Instead of $f(x) = 5 \mult x - 3$, we may simple write $x \mapsto 5 \mult x - 3$.
:::

**Caution:**
Notice the difference between $\rightarrow$ and $\mapsto$.
The first is used when specifying the domain and co-domain, whereas the latter indicates the concrete mapping from an argument to an output.
