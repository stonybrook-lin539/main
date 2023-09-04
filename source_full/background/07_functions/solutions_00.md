# Functions: Basic notation (Solutions)

::: exercise
Let $f$ be a function that takes as its input a number $n$ and returns $n+1$ on a weekday and $n+2$ on the weekend.

1. Is $f$ a function?
1. What if $f$ instead takes two arguments: a number $n$, and the name of the day of the week.
   Is this version of $f$ a function?

::: solution
1. No.
2. Yes.
:::

::: solution_explained
1. No, $f$ is not a function because one and the same input can produce different outputs.
   The output is predictable if the current day of the week is known, but this does not change the fact that a single input like $5$ is sometimes mapped to $6$ and sometimes to $7$, which is not possible with functions.
2. Yes, if we make the day of the week an argument of the function, then the output varies together with the input.
   For example, the input consisting of the two arguments $5$ and \emph{Friday}$ is mapped to $6$, whereas the input consisting of the two arguments $5$ and \emph{Sunday} is mapped to $7$.
   It is no longer possible for the same input, consisting of a number and a day of the week, to be mapped to two distinct outputs.
:::

:::
