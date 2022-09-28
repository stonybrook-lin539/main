# Monotonicity

When the domain and co-domain of a function each have an order defined over them, one can ask whether the function is order-preserving.

::: example
Consider the function $f: \mathbb{N} \rightarrow \mathbb{N}$ with $x \mapsto 2x$.
The domain of $f$ is $\mathbb{N}$, the set of natural numbers, which is also the co-domain of $f$.
The set of natural numbers can be ordered by $\leq$ in the usual fashion, e.g. $2 \leq 4$ or $0 \leq 0$.
The function $f$ respects the order induced by $\leq$.
For any two $x$ and $y$ such that $x \leq y$, it also holds that $f(x) \leq f(y)$.
For instance, $4 \leq 10$ and $f(4) = 8 \leq 20 = f(10)$.
:::

::: example
Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be a function from real numbers to real numbers such that $f(x) = x^2 - 5x$.
Then $f$ does not preserve order in all cases.
We have $3 \leq 5$ and $f(3) = 9 - 5 \mult 3 = -6 \leq 0 = 25 - 5 \mult 5 = f(5)$.
But we also have $0 \leq 1$ yet $f(0) = 0 - 5 \mult 0 = 0 \geq -4 = 1 - 5 \mult 1 = f(1)$.
:::

This property of order preservation is known as **monotonicity**.
You might have already encountered monotonicity in the special case of a function from reals to reals.
In this case, one can draw the function as a line or curve in a coordinate system.

<!-- ```python -->
<!-- import numpy as np -->
<!-- import matplotlib.pyplot as plt -->
<!--  -->
<!-- f = lambda x: 2*x -->
<!-- g = lambda x: x**2 -->
<!-- h = lambda x: 2*x - 2**(x - 5) + 2**10 -->
<!-- i = lambda x: x/2 - 2**x -->
<!--  -->
<!-- for func in [f, g, h, i]: -->
<!--     values = np.linspace(-10, 10) -->
<!--     plt.plot(values, func(values)) -->
<!--     plt.show() -->
<!-- ``` -->

<!-- ```python -->
<!-- import numpy as np -->
<!-- import matplotlib.pyplot as plt -->
<!-- import ipywidgets -->
<!-- from ipywidgets import Button, Layout -->
<!--  -->
<!-- from IPython.display import display -->
<!--  -->
<!-- f = lambda x: 2*x -->
<!-- g = lambda x: x**2 -->
<!-- h = lambda x: 2*x - 2**(x - 5) + 2**10 -->
<!-- i = lambda x: x/2 - 2**x -->
<!--  -->
<!-- b = ipywidgets.Button(description='Show graphs', -->
<!--            layout=Layout(width='50%', height='80px')) -->
<!-- display(b) -->
<!--  -->
<!-- def on_button_clicked(b): -->
<!--     for func in [f, g, h, i]: -->
<!--         values = np.linspace(-10, 10) -->
<!--         plt.plot(values, func(values)) -->
<!--         plt.show() -->
<!--      -->
<!-- b.on_click(on_button_clicked) -->
<!-- ``` -->

~~~ {.include-tikz size=mid}
monotonicity_f.tikz
~~~
~~~ {.include-tikz size=mid}
monotonicity_g.tikz
~~~
~~~ {.include-tikz size=mid}
monotonicity_h.tikz
~~~

A function is monotonic iff it does not change direction: once it goes up, it cannot go down, and the other way round.
However, it may stall, or never move at all.
The functions $f$ and $g$ above are monotonic, but $h$ is not as it changes direction, from going down to going up.
Note that $g$ is monotonic even though it rises more steeply at some points than at others --- this is immaterial for monotonicity, it only matters that $g$ never reaches a point where it suddenly changes direction and starts going down after having gone up before (or going up after having gone down before).

::: exercise
For each one of the following functions, say whether it is monotonic.

~~~ {.include-tikz size=mid}
monotonicity_i.tikz
~~~
~~~ {.include-tikz size=mid}
monotonicity_j.tikz
~~~
~~~ {.include-tikz size=mid}
monotonicity_k.tikz
~~~
~~~ {.include-tikz size=mid}
monotonicity_l.tikz
~~~

::: solution
1. Not monotonic
1. Not monotonic
1. Monotonic
1. Not monotonic
:::

::: solution_explained
The functions $i$, $j$, and $l$ all change direction at some point.
The function $k$ is a constant function, it neither goes up nor down.
Since that entails never changing direction, it is monotonic.
:::

:::

::: exercise
Give another example of a function that is not monotonic.

::: solution
The function $f$ that maps even numbers to $0$ and odd numbers to $1$.
:::

::: solution_explained
The sky is the limit here, there is no shortage of functions that are not monotonic.
For example, take a function from natural numbers to natural numbers that maps $100$ to $0$ and every other number to $1$.
This function is not monotonic.
But instead of $100$, we could have picked $1$, or $3$, or $17$, or some other natural number that is not $0$, and the result would have been a non-monotonic function.
This already shows us that there are infinitely many functions that are not monotonic.
:::

:::


While such numerical functions are a good starting point for grasping the intuition behind monotonicity, they provide an incomplete picture.
The concept of monotonicity is much broader than that, and it extends far beyond functions from numbers to numbers.
See the unit on universals for various linguistic applications of monotonicity, none of which have anything to do with numbers.

## Isotonicity and antitonicity

Monotonicity is actually an umbrella term for two distinct properties: **monotonic increasing** (**isotonic**) and **monotonic decreasing** (**antitonic**).

::: definition
Let $A$ and $B$ be arbitrary sets and $\leq_A$ and $\leq_B$ ordering relations over these respective sets.
Then a function $f: A \rightarrow B$ is **monotonic increasing** (or **isotonic**) iff $x \leq_A y$ implies $f(x) \leq_B f(y)$ for all $x$ and $y$ in $A$.
We call $f$ **monotonic decreasing** (or **antitonic**) iff $x \leq_A y$ implies $f(y) \leq_B f(x)$ for all $x$ and $y$ in $A$.
A function is **monotonic** iff it is monotonic increasing or monotonic decreasing.
:::

::: exercise
For each one of the following functions say whether it is monotonic increasing, monotonic decreasing, or neither.

1. $f: \mathbb{N} \rightarrow \mathbb{Z}$, $x \mapsto -x$
1. $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto x - 10$
1. $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto x^2$
1. $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto \frac{x}{2}$
1. $f: \mathbb{N} \rightarrow \mathbb{N}$, $f(n)$ is $1$ if $n = 0$ and $n \mult f(n-1)$ otherwise

::: solution
1. $f: \mathbb{N} \rightarrow \mathbb{Z}$, $x \mapsto -x$ is monotonic decreasing
1. $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto x - 10$ is monotonic increasing
1. $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto x^2$ is neither
1. $f: \mathbb{R} \rightarrow \mathbb{R}$, $x \mapsto \frac{x}{2}$ is monotonic increasing
1. $f: \mathbb{N} \rightarrow \mathbb{N}$, $f(n)$ is $1$ if $n = 0$ and $n \mult f(n-1)$ otherwise is monotonic increasing
:::

::: solution_explained
1. If $x$ and $y$ are natural numbers such that $x \leq y$, then it must be the case that $-x \geq -y$.
   For example, $1 \leq 5$, and $-1 \geq -5$.
1. If $x$ and $y$ are reals such that $x \leq y$, then $x - 10 \leq y - 10$.
   For example, $-1 \leq 1$ and $-11 \leq -9$.
1. It suffices to consider two concrete cases here.
   Suppose $x = -5$ and $y = 1$.
   Then $x \leq y$, but $x^2 = 25 \geq 1 = y^2$.
   On the other hand, if $x = 5$ and $y = 10$, then $x^2 = 25 \leq 100 = y^2$.
   Hence we sometimes have $f(x) \leq f(y)$ and sometimes $f(x) \geq f(y)$, which means that $f$ is neither monotonic increasing nor monotonic decreasing.
1. This might be easiest to understand by drawing a diagram, but we can also consider some representative values:
   $f(-10) = -5$, $f(-6) = -3$, $f(-1) = -0.5$, $f(0) = 0$, $f(1) = 0.5$, $f(6) = 3$, and $f(10) = 5$.
   As you can see, whenever $x \leq y$, it holds that $f(x) \leq f(y)$.
1. The hardest part here is to understand the definition of $f$.
   We start out with $f(0) = 1$.
   We then have $f(1) = 1 \mult f(0) = 1 \mult 1 = 1$.
   After that, $f(2) = 2 \mult f(1) = 2 \mult 1 = 2$, and $f(3) = 3 \mult f(2) = 3 \mult 2 = 6$.
   Then $f(4) = 4 \mult f(3) = 4 \mult 6 = 24$, and so on.
   As you might have noticed, $f$ is just the factorial, that is to say $f(n) = n!$.
   And if $x \leq y$, then it always holds that $x! \leq y!$ because $y!$ is the result of taking $x!$ and multiplying if with the numbers between $x$ and $y$ (including $y$ itself).
   For example, $2 \leq 4$, and $4! = 4 \mult 3 \mult 2! = 24$, which is necessarily greater than $2! = 2$.
:::

:::

::: exercise
Given an example of a function that is both isotonic and antitonic.

::: solution
The constant function $k(x) = 2$ from earlier on.
:::

::: solution_explained
There are several cases where a function is both monotonic increasing and monotonic decreasing.

The more intuitive case arises with constant functions, where all inputs are mapped to the same fixed output:
since we have $f(x) = f(y)$ for all $x$ and $y$, it holds that $f(x) \leq_B f(y)$ and $f(y) \leq_B f(x)$ irrespective of whether we have $x \leq_A y$ or $y \leq_A x$.

Another case arises if $A$ has only one member $x$.
In this case, we only have $x \leq_A x$, and obviously both $f(x) \leq_B f(x)$ and $f(x) \geq_B f(x)$ always hold.

Finally, we could also be dealing with the degenerate scenario where $\leq_A$ does not order any elements of $A$.
Perhaps $A$ is the empty set, or perhaps it is a non-empty set but $\leq_A$ is the empty order relation that does not actually order any elements.
In this case, both monotonicity properties are trivially true for every function $f$ with domain $A$.
The reasoning is as follows:
in order to show that $f$ is not monotonic increasing, we would need two $x$ and $y$ such that $x \leq_A y$ but $f(x) \not\leq_A f(y)$.
But we already know that there are no $x$ and $y$ such that $x \leq_A y$, hence there are no counterexamples to $f$ being monotonic increasing, which means that it is monotonic increasing.
The same reasoning also establishes that $f$ is monotonic decreasing.
:::

:::
