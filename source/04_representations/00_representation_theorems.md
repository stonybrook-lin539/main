# Switching between representations

The unit on universals argues that unrelated phenomena can be unified under the banner of monotonicity.
The apparent differences between the phenomena are due to differences in the structures that monotonicity is evaluated over:

- the person hierarchy ($1 < 2 < 3$),
- the adjectival gradation hierarchy ($\text{positive} < \text{comparative} < \text{superlative}$),
- the (partially ordered) case hierarchy,
- the person-person hierarchy for the PCC,
- the adjunct extension semilattices for the Adjunct Island Constraint.

What we have done, then, is given each empirical domain a specific **representation**.
A representation is a structure that expresses crucial properties of the object is represents.
Mathematically, we are free to choose our representations any way we want.
In fact, there are **representation theorems** that establish how, sometimes, one representation can be transferred into another representation without losing any essential properties.

::: example
Here is a very simple representation theorem.
Every set $S$ be represented as its **characteristic function** $f_S$ such that $f_S(x) = 1$ if $x \in S$ and $0$ otherwise.
For instance, if the set $S$ of students who cheated on an exam contains John and Mary, but not Sue, then its characteristic function $f_S$ maps John to $1$, Mary to $1$, and Sue to $0$.

Note how this preserves all crucial aspects of a set.
The set is still unordered because the characteristic function only expresses whether the element is in the set, not what position it occupies.
Idempotency also holds: $S \is \setof{a}$ is the same set as $T \is \setof{a,a}$ because $f_S$ and $f_T$ are the same function that maps $a$ to $1$, and everything else to $0$.

The functional view of sets is sometimes more convenient to work with.
That's particularly the case for semantics, the linguistic study of meaning.
Semanticists use a notational format that expresses everything in terms of functions (the **lambda calculus**).
We will see some of that in a later chapter.
:::

::: exercise
Suppose that the students in this class are
*John*,
*Sue*, and
*Mary*.
Write

- the characteristic function for the set of female students (assuming heteronormative naming conventions), and 
- the characteristic function for the set of students whose name contains exactly four letters, and
- the characteristic function for the union of the two sets.

Define each function by explicitly writing down the values, e.g. $\text{John} \mapsto 1$.

::: solution
1. The set of a female students' name $\is \setof{Sue, Mary}$ The characteristic function will map $\text{John} \mapsto 0, \text{Sue} \mapsto 1,\text{Mary} \mapsto 1$.
1. The set of a four-letter name $\is \setof{John, Mary}$. Therefore we have $\f(John) \mapsto 1, \f(Sue) \mapsto 0,\text(Mary)\mapsto 1$.
1. The set of a four-letter female name $\is \setof{Mary}$. Therefore we have $\text{John} \mapsto 0, \text{Sue} \mapsto 1,\text{Mary} \mapsto 1$.
:::
:::

::: exercise
Continuing the previous exercise, can you give a general definition for union that uses the values 0 and 1 assigned by characteristic functions?

*Hint*: Check out the **max** function in the backgrounds section.

::: solution
fixme
:::
:::

::: exercise
Can you define the analog of a characteristic function for multisets?

::: solution
fixme
:::
:::

::: example
A more complicated representation theorem is the Kuratovsky definition of pairs.
You might already be familiar with this definition if you have prior training in theoretical syntax, where this definition has gained some notoriety since the mid 90s.
Rather than taking tuples as a primitive, Kuratovsky defined $\tuple{a,b}$ as a shorthand for $\setof{ \setof{a}, \setof{a,b} }$.
Intuitively, the two don't seem to have anything in common.
But think about the crucial property of pairs: $\tuple{a,b} = \tuple{c,d}$ iff $a = c$ and $b = d$.
This equivalence also holds under Kuratovsky's definition of pairs.


Suppose that $\tuple{a,b} = \tuple{c,d}$.
Then by Kuratowsky's definition, $\setof{ \setof{a}, \setof{a,b} } = \setof{ \setof{c}, \setof{c,d}}$.
If $\setof{a} \neq \setof{c}$, then $\setof{a} = \setof{c,d}$, which can only hold if $c = d$.
But then $\setof{a} = \setof{c,d} = \setof{c,c} = \setof{c} \neq \setof{a}$.
As this is a contradiction, it must be the case that $\setof{a} = \setof{c}$.
From this it follows that $a = c$, wherefore $\setof{a,b} = \setof{c,d}$ implies $b = d$, exactly as desired.
:::

::: exercise
Explain why the equivalence also holds in the other direction: if $a = c$ and $b = d$, then $\setof{\setof{a}, \setof{a,b}} = \setof{\setof{c}, \setof{c,d}}$ (and thus $\tuple{a,b} = \tuple{c,d}$).

::: solution
If $a = c$, then $\setof{a} = \setof{c}$; 
if $b = d$, then $\setof{b} = \setof{d}$.
Then it holds that $\setof{a,b} = \setof{c,b} = \setof {c,d}$. 
Since we have $\setof{a} = \setof{c}$ and $\setof{a,b} = \setof {c,d}$, 
 thus $\setof{\setof{a}, \setof{a,b}} = \setof{\setof{c},\setof{c,d}}$(and thus $\tuple{a,b} = \tuple{c,d}$.
:::
:::

::: exercise
Under Kuratovsky's definition, what set corresponds to the pair $\tuple{a,a}$?

::: solution
Under Kuratovsky's definition, $\tuple {a,b}$ corresponds to $\setof{\setof{a},\setof{a,b}}$.
Then it follows $\tuple {a,a}$ corresponds to $\setof{\setof{a},\setof{a,a}}$.
Since $\setof{a,a} = \setof{a}$, $\setof{\setof{a},\setof{a,a}} = \setof{\setof{a},\setof{a}} = \setof{\setof{a}}$.
Therefore, $\tuple {a,a}$ corresponds to $\setof{\setof{a}}$.
:::
:::

::: exercise
In earlier units, we said that the crucial difference between sets and tuples is that the latter are ordered and not idempotent.
So $\tuple{a,b} \neq \tuple{b,a}$ ("order matters") and $\tuple{a} \neq \tuple{a,a}$ ("tuples are not idempotent").
But now we only checked that $\tuple{a,b} = \tuple{c,d}$ iff $a = c$ and $b = d$.
This biconditional actually entails that pairs are ordered and not idempotent, as desired.
Explain why!

::: solution
The biconditional $\tuple{a,b} = \tuple{c,d}$ iff $a = c$ and $b = d$ indicates two things:
1. the first element in the first tuple should align to the element of the same position in the second tuple. This indicates the order matters;
1. the number of two elements in the tuples should be the same for the equation to hold. This indicates the idemotence.
:::
:::

::: exercise
The Kuratowski definition does not hold for arbitrary tuples.
That is to say, $\tuple{a, b, c}$ cannot always be represented as $\setof{ \setof{a}, \setof{a, b}, \setof{a,b,c}}$.
To see this, try to represent the following two triples in terms of these sets:


- $\tuple{a, a, b}$
- $\tuple{a, b, b}$


What is the problem?

::: solution
If the above tuples can be represented under Kuratowski definitaion, we have:
- $\tuple{a, a, b}$ = $\setof{\setof{a},\setof{a,a},\setof{a,a,b}}$. Since a set does not have duplicate elements, this set will equal to $\setof{\setof{a},\setof{a,b}}$. According to the Kuratowski definiation, $\setof{\setof{a},\setof{a,b}}$ =  $\tuple{a, b}$. Since a tuple is not idempotent, $\tuple{a,a,b} \neq \tuple{a,b}$. Therefore, the Kuratowski definition does not hold for $\tuple{a, a, b}$.

- $\tuple{a, b, b} = $\setof{\setof{a},\setof{a,b},\setof{a,b,b}} = \setof{\setof{a},\setof{a,b}} = \tuple{a,b}$
The equation does not hold either. 

Based on these two examples, the problem seems to lie in the duplicates in the tuples. 
:::
:::

Alright, so mathematically the sky is the limit when it comes to representations.
That is certainly a good thing: using representation theorems, we can switch between representations in whatever way is convenient for the task at hand.
The linguists among you might find that irritating, though.
Linguists are used to talking about "*the* structure", and "*the* representation".
Their implicit assumption is that there is one specific representation used by the human mind, and that is what linguists should use in their descriptions.
But things simply aren't that straight-forward.
Even with computers, there is no clear notion of representation.
What exactly is the representation of, say, a set on your computer?
In the programming language, it is a specific construct X, but that does not at all reflect how X is instantiated by your computer's hardware.
And there's many intermediate representations between those two extremes.
Computers, a man-made product, do not allow us to identify a unique representation even though we know exatly how they work.
The human mind, by contrast, is still a giant black box to us.
There is no reason to believe that there is something like "*the* uniquely correct representation" --- and even if there is, odds are we will never get it quite right, so we might just as well switch between representations.

That said, linguists are right in insisting on the importance of representations in general.
We want to have a good idea of what properties hold of linguistic representations.
For instance, why is the person hierarchy $1 < 2 < 3$?
Why couldn't it simply be $1 < 2$, with $3$ completely unordered with respect to $1$ and $2$?
With such a hierarchy, we would expect a very different syncretism typology.
Ideally, there is some important property that separates these two hierarchies, making one natural and the other unnatural.
Both are weak partial orders, which we need for case syncretism and the PCC.
So whatever is the relevant property, it can't be a limitation to weak partial orders.

The answer is still largely open - that's how it is with research, it takes a lot of effort to clear up the fog.
But there are some simple restrictions that can be put in place.
Like monotonicity, they are ubiquitous in language.
In order to talk about them from a mathematical perspective, we need to bring in **graph theory**.
