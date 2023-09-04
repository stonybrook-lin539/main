# Taking the closure of a relation (Solutions)

::: exercise
Calculate all of the following, assuming that the relation's domain is $D \is \setof{a,b,c,d}$:

1. the reflexive closure of $\setof{\tuple{a,b}, \tuple{b,a}}$
1. the transitive closure of $\setof{\tuple{a,b}, \tuple{b,a}}$
1. the transitive closure of $\setof{\tuple{a,b}, \tuple{b,c}, \tuple{c,d}, \tuple{d,a}}$
1. the reflexive, symmetric, transitive closure of $\setof{\tuple{a,b}, \tuple{a,c}, \tuple{d,c}}$
1. the reflexive, symmetric, transitive closure of $\emptyset$

::: solution

1. the reflexive closure of $\setof{\tuple{a,b}, \tuple{b,a}}$: $\{ \tuple{a,a}, \tuple{a,b}, \tuple{b,a}, \tuple{b,b} \}$
1. the transitive closure of $\setof{\tuple{a,b}, \tuple{b,a}}$: $\{ \tuple{a,a}, \tuple{a,b}, \tuple{b,a} \}$
1. the transitive closure of $\setof{\tuple{a,b}, \tuple{b,c}, \tuple{c,d}, \tuple{d,a}}$: $\setof{a,b,c,d} \times \setof{a,b,c,d}$
1. the reflexive, symmetric, transitive closure of $\setof{\tuple{a,b}, \tuple{a,c}, \tuple{d,c}}$: $\setof{a,b,c,d} \times \setof{a,b,c,d}$
1. the reflexive, symmetric, transitive closure of $\emptyset$: $\emptyset$

:::

::: solution_explained
In the third exercise, we have a loop: $a$ is related to $b$, which is related to $c$, which is related to $d$, which is related to $a$.
Remember that transitivity means, intuitively, that whatever we can reach in multiple steps we can reach in a single step.
Here everything can be reached from everything in multiple steps, so the transitive closure will relate every element to every element (including the special where every element is related to itself).
Rather than write down those 16 pairs, we can define them more succinctly via the crossproduct.

A similar case arises in the fourth exercise.
Because of closure under reflexivity and symmetry, the relation must contain at least the following pairs:
$\tuple{a,a}, \tuple{a,b}, \tuple{a,c}, \tuple{b,a}, \tuple{b,b}, \tuple{c,a}, \tuple{c,c}, \tuple{c,d}, \tuple{d,c}, \tuple{d,d}$.
At this point, transitive closure ends up relating everything to everything:

1. $\tuple{a,d}$ is added because of $\tuple{a,c}$ and $\tuple{c,d}$.
1. $\tuple{d,a}$ is added because of $\tuple{d,c}$ and $\tuple{c,a}$.
1. $\tuple{b,c}$ is added because of $\tuple{b,a}$ and $\tuple{a,c}$.
1. $\tuple{b,d}$ is added because of $\tuple{b,a}$ and $\tuple{a,d}$.
1. $\tuple{c,b}$ is added because of $\tuple{c,a}$ and $\tuple{a,b}$.
1. $\tuple{d,b}$ is added because of $\tuple{d,a}$ and $\tuple{a,b}$.
:::

:::
