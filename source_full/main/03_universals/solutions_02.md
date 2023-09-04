# NPIs and monotonicity (Solutions)

::: exercise
Consider the sentence *every student slept*.
Does it allow for similar inferences via entailment?

::: solution
Yes. If *every student slept*, then both of the following are true:

1. Every male student slept.
1. Every sophomore slept.
:::

:::

::: exercise
Construct a similar argument to show that *every* is downward entailing.

::: solution
We can do this by substituting just a few terms in the example:

Let $A$ be the set of all students.
The sentence *Every student slept* asserts for each student $s \in A$ that $s$ did in fact sleep.
Suppose this is true.
Then *Every X slept* is necessarily true if X denotes some set $B \subseteq A$ because we already know for each $s \in B$ that $s$ did sleep.
Since there is no subset of $A$ for which this entailment fails, *every* is indeed downward entailing.
:::
:::

::: exercise
Represent the following sentences in terms of this functional notation:

1. No professor writes good lecture notes.
1. Every professor could earn more in industry.
1. This professor, no student likes.

::: solution
1. No(professor, writes good lecture notes)
1. Every(professor, could earn more in industry)
1. No(student, likes this professor)
:::

::: solution_explained
The central thing to keep in mind here is that the arguments are determined by meaning, not the linear order in the string.
The first argument expresses what we are quantifying over, the second one what is being done.
For the first two examples, this is straight-forward.
For the third example, we have to figure out first that *this professor* is the object of *likes*.
So the sentence means the same as *no student likes this professor*, even though the word order is different.
:::

:::

::: exercise
Show that *no* is downward entailing with respect to Y.

::: solution
Consider a concrete example first.
Suppose *No student runs* is true.
Then *No student runs a 5k* is also true.
The set of individuals that run a 5k is a subset of the individuals that run, so we made an inference from a set $S$ (the set of runners) to a subset of $S$ (the set of 5k runners), which means that we have downward entailment.

More generally, if $\mathrm{No}(X,Y)$ is true, then there is no individual $i \in X$ such that $i$ belongs to the set of individuals that do $Y$.
But then $i$ cannot belong to any subset of $Y$, either.
Or in set-theoretic terms: if $\mathrm{No}(X,Y)$ is true, then $X \cap Y = \emptyset$, which implies $X \cap Z = \emptyset$ for every subset $Z$ of $Y$.
This shows that *no* is downward entailing with respect to $Y$.
:::

:::

::: exercise
Construct an example for downward entailment similar to the one above for upward entailment.

::: solution
Again this only requires swapping out a few words:

Consider the sentences
*No student ran a 5k*
and
*No student ran*.
Clearly if the latter is true, the former must be too.
We also know already that the set of students that ran a 5k (call it $5k$) is a subset of the students that ran (call it $R$).
So we have $5k \subseteq R$.

Now suppose that $\text{\emph{no student}}(R) = 1$.
Then $\text{\emph{every student}}(5k) \geq 1$ because $5k \subseteq R$ and the function is monotonically decreasing.
So the fact that the sentence is true for $R$ entails that it is true for every subset of $R$.
This is exactly what it means to be downward entailing.
:::
:::

::: exercise
Alternatively, we may view downward entailment as a monotonically increasing function if sets are ordered by the superset relation instead of subset.
Explain why!

::: solution
By ordering sets by the superset relation instead of the subset relation, we flip their order: if $X < Y$ (i.e. $X \subseteq Y$), we now have $Y < X$ (i.e. $Y \supseteq X$).
Downward entailment means that if a statement is true with respect to $Y$, then it is true with respect to every $X$ that $Y$ is a superset of.
But in our new ordering, that's every $X$ such that $Y < X$.
Hence downward entailment can be rephrased as follows: if $f(Y) = 1$, then $f(X) \geq 1$ for every $X > Y$.
And that is an instance of being monotonically increasing.
:::
:::
