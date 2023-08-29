# Domains and co-domains (Solutions)

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

::: exercise
What would be the domain and co-domain of a broken car wash that fails to remove even the tiniest speck of dirt?

::: solution
Similar to the working car wash from the example above, the broken car wash would correspond to a function that the set of all cars (both dirty and clean) as its domain.
But now this set would also be its co-domain because dirty cars still come out dirty.
:::

:::
