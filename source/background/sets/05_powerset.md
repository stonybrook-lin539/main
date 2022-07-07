**Prerequisites**

- sets (notation, operations, cardinality)

# The Powerset

Sometimes it is useful to take a set and consider all sets one could build from its elements.
For example, each one of the following sets can be built from the elements of $\setof{1,2,3}$: 

1. $\emptyset$
1. $\setof{1}$
1. $\setof{2}$
1. $\setof{3}$
1. $\setof{1,2}$
1. $\setof{1,3}$
1. $\setof{2,3}$
1. $\setof{1,2,3}$

Note that each one of the sets in this list is a subset of $\setof{1,2,3}$, and every subset of $\setof{1,2,3}$ is on this list.
So the above is the list of all subsets of $\setof{1,2,3}$.
The set of all these sets is called the **powerset** of $\setof{1,2,3}$.

::: definition
For $A$ a set, the **powerset** of $A$ is $\wp(A) \is \setof{ S \mid S \subseteq A }$.
:::

::: example
Suppose we have the set $\setof{a}$ and want to compute $\wp(\setof{a})$.
This can be done in many ways, but here is one that's easy for beginners.

1. First, we write down the set itself: $\setof{a}$
1. Next, we write down all proper subsets of the set.
   In this case, there's only one: $\emptyset$
1. Finally, we put set brackets around the list of sets we wrote down:
   $\wp(\setof{a}, \emptyset)$.

And that's it.
As long as the set in question isn't too large, you can always follow this mechanical procedure when you aren't sure how to compute the set's powerset.
:::

::: exercise
For each one of the following sets, compute its powerset.

1. $\setof{a,b}$
1. $\setof{a,b,c,d}$
1. $\setof{\setof{a}}$
1. $\emptyset$
1. $\setof{\emptyset}$
1. $\wp(\setof{\setof{a}})$
1. $\wp(\wp(\emptyset))$

::: solution
1. $\wp(\setof{a,b}) = \setof{\setof{a,b}, \setof{a}, \setof {b}, \emptyset)}$
1. $\wp(\setof{a,b,c,d}) = \setof{\setof{a,b,c,d},
    \setof{a,b,c}, \setof{b,c,d}, \setof{a,c,d}, \setof{a,b,d},
    \setof {a,b}, \setof {a,c}, \setof {a,d},\setof{b,c}, \setof{b,d}, \setof{c,d},
    \setof{a}, \setof {b}, \setof {c}, \setof {d},
    \emptyset)}$
1. $\wp(\setof{\setof{a}}) = \setof{\setof{\setof{a}},\emptyset}$
1. $\wp(\emptyset) = \setof{\emptyset}$
1. $\wp(\setof{\emptyset}) = \setof{\setof{\emptyset}, \emptyset}$
1. $\wp(\wp(\setof{\setof{a}})) = \wp(\setof{\setof{\setof{a}},\emptyset}) = \setof{\setof{\setof{a}},\setof{\emptyset}, \setof{\setof{\setof{a}},\emptyset}, \emptyset}$

:::
:::

## Powerset notation

There are many alternative notations for the powerset.
A particularly common one is $2^A$ as it highlights two interesting aspects of the powerset.
Remember that the cardinality of a set $A$ measures the number elements it contains, and we denote it by $\card{A}$.
For example, $\card{\setof{1,2,3}} = 3$.
Now we can state a universal truth for the cardinality of powersets.

::: theorem
For every set $A$ with $\card{A} = n$, it holds that $\card{\wp(A)} = \card{2^A} = 2^{\card{A}} = 2^n$.
:::

This is witnessed by our example set $\setof{1,2,3}$, the powerset of which has $8$ members (see the list at the beginning of this unit).

::: exercise
For each set $A$ in the previous exercise, verify that $\card{\wp(A)} = 2^{\card{A}}$.

::: solution
1. $\card{\setof{a,b}} = 2, \card{\wp(\setof{a,b})} = 4 = 2^2$
1. $\card{\setof{a,b,c,d}} = 4, \card{\wp(\setof{a,b,c,d})} = 12 = 2^4$
1. $\card{\setof{\setof{a}}} = 1, \card{\wp(\setof{\setof{a}})} = 2 = 2^1$
1. $\card{\emptyset} = 0, \card{\wp(\emptyset)} = 1 = 2^0$
1. $\card{setof{\emptyset}} = 1, \card{\wp(\setof{\emptyset})} = 2 = 2^1$
1. $\card{\wp(\setof{\setof{a}})} = \card{\setof{\setof{\setof{a}}},\emptyset} = 2, \card{\wp(\wp(\setof{\setof{a}}))} = 4 = 2^2$
1. $\card{\wp(\wp(\emptyset))}= $ 
:::
:::

<!-- But the $2^A$ notation for powersets has a deeper meaning that goes beyond mere numbers. -->
<!-- The notation $B^A$ is sometimes used to represent the set of all functions from $A$ to $B$. -->
<!-- And $2$ can be construed not just as the number $2$, but as any set with cardinality $2$, including $\setof{\top, \bot}$. -->
<!-- So $2^A$ can be taken to denote the set of all functions from $A$ to $\setof{\top, \bot}$. -->
<!-- But since functions are sets, this is exactly the class of all subsets of $A$. -->

<!-- In sum, the $2^A$ notation for powersets is very pleasing on a theoretical level. -->
<!-- But humans are a practical bunch, and since superscripts are slightly strenuous to read, $\wp(A)$ is the preferred notation for powersets. -->

## Recap

- The powerset of a set $A$ is the set of all subsets of $A$, including $A$ itself.
- For every finite set $A$, it holds that $\card{\wp(A)} = 2^{\card{A}}$.
