---
pagetitle: >-
    Dot product of vectors
---

# Dot product of vectors

:::prereqs
- linear algebra (vectors)
:::

Given two vectors of the same length, their **dot product** is the result of multiplying the vectors component-wise and summing all the products.

::: definition
Given vectors $u \is (u_1, u_2, \ldots, u_n)$ and $v \is (v_1, v_2, \ldots, v_n)$, the **dot product** $u \cdot v$ is

$$
u_1 \times v_1 + u_2 \times v_2 + \cdots + u_n \times v_n
$$

where $\times$ represents multiplication.
:::

::: example
For $u \is (1, 3, 5)$ and $v \is (2, 4, 6)$, we have $u \cdot v = 1 \times 2 + 3 \times 4 + 5 \times 6 = 44$.

Alternatively, we could have also written this as follows using column vectors:

$$
\begin{pmatrix}
1\\
3\\
5\\
\end{pmatrix}
\cdot
\begin{pmatrix}
2\\
4\\
6\\
\end{pmatrix}
=
1 \times 2 + 3 \times 4 + 5 \times 6 = 44
$$
:::

::: exercise
Calculate all of the following dot products.
If the dot product is not defined, say so.

1. $(1, 2) \cdot (-1, -2)$
1. $(1, 1, 1, 1) \cdot (2, 3, 4, 5)$
1. $(1, 2) \cdot (-1, \mathrm{True})$
1. $(1, 2) \cdot (7)$
1. $(1) \cdot (7)$
:::
