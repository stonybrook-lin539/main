---
pagetitle: >-
    Functions: Basic notation
---

# Functions: Basic notation

**Functions**, also called **maps** or **mappings**, are ubiquitous in mathematics.
When the laymen hears the term *function*, they usually thinks of things like $f(x) = x + 1$.
But the concept is much more general.
Anything can be thought of as a function as long as it takes a fixed number of **arguments** as its input and returns some output.
Crucially, the output is not allowed to vary when the input is kept the same.

::: example
Sticking with numbers, suppose $f(x)$ randomly maps $x$ to either $x+2$ or $x \mult 2$.
This is not a function because one and the same input can produce different outputs.
Yes, $f(2)$ would always yield $4$ because $2 + 2 = 4$ and $2 \mult 2 = 4$.
But for $3$, the two diverge: $3 + 2 = 5$ but $3 \mult 2 = 6$.
So $f(3)$ would sometimes be $5$ and sometimes $6$, which means that $f$ is not a function.

However, if we turned $f$ into a binary function that takes some number $x$ as its first argument and some operation $\oplus$ as its second argument and maps that to $x \oplus 2$, then $f$ is a function.
In that case, $f(3, +) = 3 + 2 = 5$ and $f(3, \mult) = 3 \mult 2 = 6$.
Now it is okay that the outputs vary because we are also varying the inputs.
:::

::: example
A car wash can be regarded as a function that takes as input a car and returns as its output a clean car (in an ideal world, at least).
A dirty Dodge Viper comes out as a clean Dodge Viper, and a clean Audi A4 still comes out as a clean Audi A4.
The output is always perfectly predictable from the input.
:::

::: example
English has a construction where a word is doubled and its beginning replaced with *shm*, as in *rules shmules* or *fancy shmancy*.
This construction, called **shm-reduplication**, is borrowed from Yiddish and conveys a kind of derision.
We can regard this as a function that takes a word as its input and returns the corresponding *shm*-form.
:::

::: exercise
Speakers vary as to what they accept as the correct *shm*-reduplicant for some words.
For example, some speakers turn *breakfast* into *shmeakfast*, replacing both *b* and *r*, whereas other only replace *b*, yielding *shmreakfast*.
Explain why this does not contradict the claim that *shm*-reduplication can be regarded as a function.

::: solution
The exercise states that speakers may vary in how they form *shm*-reduplicants.
But this variation across speakers has no bearing on whether a given speaker's version of *shm*-reduplication is a function.
As long as the speaker can only produce one *shm*-reduplicant for any given word, their version of *shm*-reduplication is a function.
Only if the speaker accepts multiple *shm*-reduplicants for the same word does *shm*-reduplication cease to be a function.
:::
:::

::: exercise
Let $f$ be a function that takes as its input a number $n$ and returns $n+1$ on a workday and $n+2$ on the weekend.

- Is $f$ a function?
- What if $f$ instead takes two arguments: a number $n$, and the name of the day of the week.
  Is this version of $f$ a function?

::: solution
1. No.
2. Yes.

::: solution_explained
1. No, $f$ is not a function because one and the same input can produce different outputs.
   The output is predictable if the current day of the week is known, but this does not change the fact that a single input like $5$ is sometimes mapped to $6$ and sometimes to $7$, which is not possible with functions.
2. Yes, if we make the day of the week an argument of the function, then the output varies together with the input.
   For example, the input consisting of the two arguments $5$ and \emph{Friday}$ is mapped to $6$, whereas the input consisting of the two arguments $5$ and \emph{Sunday} is mapped to $7$.
   It is no longer possible for the same input, consisting of a number and a day of the week, to be mapped to two distinct outputs.
:::
:::
:::

The fact that functions cannot map one and the same input to multiple outputs is known as **right uniqueness**.
Right uniqueness guarantees that functions are deterministic in the sense that one can predict the output from the input with 100% accuracy.

**Caution**: The functions used in programming languages are not necessarily functions in the mathematical sense.
In programming, the output of a function can vary even if the arguments to the function stay the same.

``` jupyterpython
import random
import re

# a programming function that is not a mathematical function
def random_output(number):
    # randomly choose between two outputs
    if random.choice([True, False]):
        return 2 * number
    else:
        return 3 * number

# let's see what happens when we run the function multiple times
for _ in range(10):
    print("The output of random_output({}) is {}".format(5, random_output(5)))
```

<!-- ```python -->
<!-- import random -->
<!-- import re -->
<!-- import ipywidgets -->
<!-- from ipywidgets import Button, Layout -->
<!--  -->
<!-- from IPython.display import display -->
<!--  -->
<!-- # a programming function that is not a mathematical function -->
<!-- def random_output(number): -->
<!--     # randomly choose between two outputs -->
<!--     if random.choice([True, False]): -->
<!--         return 2 * number -->
<!--     else: -->
<!--         return 3 * number -->
<!--  -->
<!-- b = ipywidgets.Button(description='Click to run randomization', -->
<!--            layout=Layout(width='50%', height='80px')) -->
<!-- display(b) -->
<!--  -->
<!-- def on_button_clicked(b): -->
<!--     for _ in range(10): -->
<!--         print("The output of random_output({}) is {}".format(5, random_output(5))) -->
<!--      -->
<!-- b.on_click(on_button_clicked) -->
<!-- ``` -->

## Recap

- A function takes a fixed number of arguments as its input and returns a single output that is uniquely determined by the inputs.
- Functions are not limited to numbers, all kinds of things can be the input or output of a function.

\includecollection{solutions}
