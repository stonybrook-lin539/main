# Connectedness of graphs (Solutions)

::: exercise
Is every strongly connected graph weakly connected?
Justify your answer.

::: solution
Yes, every strongly connected graph is weakly connected.

Consider first the intuitive argument.
In a strongly connected graph, it holds that every vertex is reachable from every vertex.
In a weakly connected graph, every vertex is reachable from every vertex if we ignore the directionality of edges.
As the latter is a relaxation of the former, strong connectivity implies weak connectivity.

Now let us state this in precise, mathematical terms:
In a strongly connected graph, the reflexive, transitive closure $E^*$ of the edge relation is identical to $V \times V$.
In a weakly connected graph, the reflexive, transitive, symmetric closure $E^*_S$ of the edge relation is identical to $V \times V$.
As $E^* \subseteq E^*_S$, $E^* = V \times V$ implies $E^*_S = V \times V$, and thus being strongly connected entails being weekly connected.
:::

:::

::: exercise
Suppose that a graph $G$ is weakly connected.
Is it guaranteed to be connected if we take the reflexive, symmetric, transitive closure of the edge relation?

::: solution
Yes, $G$ is guaranteed to be connected.
In fact, $G$ is guaranteed to be strongly connected, which implies being connected.

Consider first the intuitive argument.
If $G$ is weakly connected, then every vertex can be reached from every vertex if we ignore the directionality of edges.
If we know construct a new edge relation by taking the symmetric closure (the reflexive and transitive part is a bit of a red herring), that is the same as ignoring the directionality of edges because for every edge $\tuple{a,b}$ we now also have an edge $\tuple{b,a}$.
Hence it holds for this new edge relation that every vertex is reachable from every vertex, which means that the graph is strongly connected.

Now let us express the same in precise, mathematical terms:
Remember that $G \is \tuple{V,E}$ is weakly connected iff the reflexive, symmetric, transitive closure $E^*_S$ of the edge relation $E$ is identical to $V \times V$.
Hence if we define a new graph $G' \is \tuple{V,E'}$ such that $E' = E^*_S$, then it holds that the reflexive, transitive closure of $E'$ is identical to $V \times V$.
By definition, then, $G'$ is strongly connected, which implies that it is connected.
:::

:::
