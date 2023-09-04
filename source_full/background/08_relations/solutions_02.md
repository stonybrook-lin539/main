# Strict order relations (Solutions)

::: exercise
Indicate in the table below which properties hold of the respective relations.

*Remarks*:

- Assume suitable sets that the relations are defined over. For instance, the substring relation is defined over the set of all possible strings, and the subset relation should be defined over all possible sets.
- Lexicographic order refers to how words would be ordered in a dictionary, e.g. $\text{aardvark} < \text{apple} < \text{be} < \text{bet} < \text{zoom}$.
- For some relations, you might want to justify why you think they (do not) satisfy a certain property.

::: solution

| **Properties**       | substring | proper substring | $\subsetneq$ | $\subseteq$ | lexicographic order | taller than |
| :--                  | :--       | :--              | :-:          | :-:         | :-:                 | :-:         |
| transitive           | Yes       | Yes              | Yes          | Yes         | Yes                 | Yes         |
| irreflexive          | No        | Yes              | Yes          | No          | Yes                 | Yes         |
| asymmetric           | No        | Yes              | Yes          | No          | Yes                 | Yes         |
| semi-connex          | No        | No               | No           | No          | Yes                 | Yes         |
| strict partial order | No        | Yes              | Yes          | No          | Yes                 | Yes         |
| strict total order   | No        | No               | No           | No          | Yes                 | Yes         |

The solution above gives two interpretations for substring.
The *substring* ($\sqsubseteq$) relation is reflexive, whereas the *proper substring* ($\sqsubsetneq$) relation is irreflexive.
The substring relation is reflexive, but the proper substring is not.

For the lexicographic order and *taller than*, the solution assumes that no word precedes itself in the dictionary, and that no individual or object is taller than itself.
:::

:::

::: exercise
Give a real-world example of a strict partial order that is not a strict total order.

::: solution
There are many possible answers here.

One option is the ancestor relation over the set of all humans that have ever lived.
It is transitive: the ancestor of an ancestor of $x$ is an ancestor $x$.
It is also irreflexive because nobody is their own ancestor, and it is asymmetric because if $x$ is an ancestor of $y$, then $y$ cannot be an ancestor of $x$.
But the relation is not semi-connex because there are individuals $x$ and $y$ such that $x$ and $y$ are distinct yet neither is an ancestor of the other.
Hence the ancestor relation is a strict partial order over the set of all humans that have ever lived, but not a strict total order.
:::

:::
