# The Powerset (Solutions)

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
1. $\wp(\setof{a,b}) = \setof{\emptyset, \setof{a}, \setof{b}, \setof{a,b}}$
1. $\wp(\setof{a,b,c,d})$ contains the following 16 elements
    1. $\setof{a,b,c,d}$
    1. $\setof{a,b,c}$
    1. $\setof{a,b,d}$
    1. $\setof{a,c,d}$
    1. $\setof{b,c,d}$
    1. $\setof{a,b}$
    1. $\setof{a,c}$
    1. $\setof{a,d}$
    1. $\setof{b,c}$
    1. $\setof{b,d}$
    1. $\setof{c,d}$
    1. $\setof{a}$
    1. $\setof{b}$
    1. $\setof{c}$
    1. $\setof{d}$
    1. $\emptyset$
1. $\wp(\setof{\setof{a}}) = \setof{ \emptyset, \setof{\setof{a}} }$
1. $\wp(\emptyset) = \setof{ \emptyset }$
1. $\wp(\setof{\emptyset}) = \setof{ \emptyset, \setof{\emptyset} }$
1. $\wp(\wp(\setof{\setof{a}})) = \wp( \setof{ \emptyset, \setof{\setof{a}} }) = \setof{ \emptyset, \setof{\emptyset}, \setof{\setof{\setof{a}}}, \setof{ \emptyset, \setof{\setof{a}}}}$
1. $\wp(\wp(\wp(\emptyset))) = \wp(\wp( \setof{ \emptyset })) = \wp ( \setof{ \emptyset, \setof{\emptyset}} )$, which is the set containing all of the following (and nothing else):
    1. $\emptyset$
    1. $\setof{\emptyset}$,
    1. $\setof{\setof{\emptyset}}$,
    1. $\setof{\emptyset, \setof{\emptyset}}$.
:::

::: solution_explained
1. The subsets of $\setof{a,b}$ are the empty set (as it is a subset of every set), $\setof{a}$, $\setof{b}$, and $\setof{a,b}$.
1. Again all we have to do is list all subsets and construct a set that contains all those sets, and nothing else.
1. This one might be a little confusing because we now have a set inside the set whose powerset we want to construct.
   However, remember that the powerset of some set $A$ is just the set of all subsets of $A$, and for that it does not matter what exactly the elements of $A$ look like.
   If you still find it confusing to have sets as elements, you can use the following trick: suppose $s \is \setof{a}$ so that we can write $\setof{\setof{a}}$ simply as $\setof{s}$.
   Then $\wp(\setof{s})$ is $\setof{ \emptyset, \setof{s}}$.
   Now we go back and replace $s$ with $\setof{a}$ following our initial definition, yielding $\setof{ \emptyset, \setof{\setof{a}}}$.
1. This is where things can get confusing if you don't pay attention.
   The powerset of $\emptyset$ is the set of all subsets of $\emptyset$.
   But the only subset of $\emptyset$ is $\emptyset$ itself, so that $\wp(\emptyset) = \setof{ \emptyset }$.
1. Now things get really confusing: $\wp(\setof{\emptyset})$, how could anybody figure that out?
   Well, this case works exactly the same $\wp(\setof{\setof{a}})$, except that we now have $\emptyset$ instead of $\setof{a}$.
   Again, what we care about is the elements of the set whose powerset we are constructing, now that those elements actually look like.
   So we could again do our substitution trick, with $s \is \emptyset$, and then we have $\wp(\setof{s}) = \setof{ \emptyset, \setof{s}}$, and substituting for $s$, we get $\setof{\emptyset, \setof{\emptyset}}$.
1. God have mercy on us, $\wp(\wp(\setof{\setof{a}}))$, nobody could possibly figure that out!
   Actually it's pretty simple.
   We already know that $\wp(\setof{\setof{a}})$ is $\setof{ \emptyset, \setof{\setof{a}}}$.
   For the sake of clarity, let us do our substitution trick again: $s \is \emptyset$, and $t \is \setof{\setof{a}}$.
   Then $\setof{ \emptyset, \setof{\setof{a}}} = \setof{s,t}$, and $\wp(\setof{s,t}) = \setof{ \emptyset, \setof{s}, \setof{t}, \setof{s,t}}$.
   Substitute for $s$ and $t$, and we get $\setof{ \emptyset, \setof{\emptyset}, \setof{\setof{\setof{a}}}, \setof{\emptyset, \setof{\setof{a}}}}$.
1. Alright, but now the universe is surely about to implode, $\wp(\wp(\wp(\emptyset)))$, that's plain lunacy!
   Nope, once again straight-forward, we just have to take our time.
   We already know that $\wp(\wp(\emptyset))$ is $\setof{ \emptyset, \setof{\emptyset}}$.
   We do our substitution trick one more time, now with $s \is \emptyset$ and $t \is \setof{\emptyset}$.
   Again we calculate $\wp(\setof{s,t})$, and substituting for $s$ and $t$ we get $\{ \emptyset, \setof{\emptyset}, \setof{\setof{\emptyset}}, \setof{\emptyset, \setof{\emptyset}}\}$.
:::

:::

## Powerset notation

::: exercise
For each set $A$ in the previous exercise, verify that $\card{\wp(A)} = 2^{\card{A}}$.

::: solution
1. $\card{\setof{a,b}} = 2$ and $\card{\wp(\setof{a,b})} = 2^2 = 4$
1. $\card{\setof{a,b,c,d}} = 4$ and $\card{\wp(\setof{a,b,c,d}} = 2^4 = 16$
1. $\card{\setof{\setof{a}}} = 1$ and $\card{\wp(\setof{\setof{a}}} = 2^1 = 2$
1. $\card{\emptyset} = 0$  and $\card{\wp(\emptyset)} = 2^0 = 1$
1. $\card{\setof{\emptyset}} = 1$ and $\card{\wp(\setof{\emptyset}} = 2^1 = 2$
1. $\card{\wp(\setof{\setof{a}})} = 2$ and $\card{\wp(\wp(\setof{\setof{a}}))} = 2^2 = 4$
1. $\card{\wp(\wp(\emptyset))} = 2$ and $\card{\wp(\wp(\wp(\emptyset)))} = 2^2 = 4$
:::

:::
