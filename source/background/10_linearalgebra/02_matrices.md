---
pagetitle: >-
    Matrices and matrix multiplication
---

# Matrices and matrix multiplication

:::prereqs
- linear algebra (vectors, dotproduct)
:::

Matrices are a generalization of row vectors where we can have multiple columns, or alternatively, a generalization of column vectors where we can have multiple rows.

::: example
Below is a matrix with three rows and two columns.

$$
\begin{pmatrix}
    5 & 2\\
    3 & 1\\
    0 & 2\\
\end{pmatrix}
$$
:::

Like vectors, matrices can also be combined with an operation that combines multiplication and addition, which is called **matrix multiplication**.
Whereas the dot product for vectors requires both vectors to have the same length, matrix multiplication requires that the number of columns of the first matrix must match the number of rows of the second matrix.

::: example
Below we are trying to combine a matrix that has 3 rows and 2 columns with a matrix that has 2 rows and 4 columns.
That is okay because the first matrix's 2 columns are matched by the second matrix's 2 row.

$$
\begin{pmatrix}
    5 & 2\\
    3 & 1\\
    0 & 2\\
\end{pmatrix}
\cdot
\begin{pmatrix}
    1 & 2 & 0 & 2\\
    3 & 0 & 1 & 3\\
\end{pmatrix}
=
\mathbf{\color{blue!75}alright,\ let's\ do\ this!}
$$
:::

::: example
Below we are once again trying to do matrix multiplication for the two matrices as above, but now in the opposite order.
Now the first matrix has 4 columns whereas the second matrix has 3 rows.
Due to this mismatch we are not able to carry out matrix multiplication.
$$
\begin{pmatrix}
    1 & 2 & 0 & 2\\
    3 & 0 & 1 & 3\\
\end{pmatrix}
\cdot
\begin{pmatrix}
    5 & 2\\
    3 & 1\\
    0 & 2\\
\end{pmatrix}
=
\mathbf{\color{red!75}sorry,\ no\ can\ do!}
$$
:::

::: exercise
For each one of the following matrices, say whether they can be combined via matrix multiplication.

1. $\begin{pmatrix} 0 & 1\\ 1 & 0 \\\end{pmatrix} \cdot \begin{pmatrix} 0 & 1\\ 1 & 0\\ \end{pmatrix}$
1. $\begin{pmatrix} 0 & 1\\ \end{pmatrix} \cdot \begin{pmatrix} 0 & 1\\ \end{pmatrix}$
1. $\begin{pmatrix} 0 & 1\\ \end{pmatrix} \cdot \begin{pmatrix} 0\\ 1\\ \end{pmatrix}$
1. $\begin{pmatrix} 0\\ \end{pmatrix} \cdot \begin{pmatrix} 1\\ \end{pmatrix}$
1. $\begin{pmatrix} 0\\1\\ \end{pmatrix} \cdot \begin{pmatrix} 1\\ \end{pmatrix}$
:::

Given two compatible matrices, matrix multiplication proceeds as follows:

1. Write down the **first row of the first matrix** as a column vector (basically, rotate it 90 degrees clockwise)
1. Calculate the dot product of this vector and the **first column of the second matrix**.
   Write down the value.
1. Do the same with the **second column of the second matrix**, and put the result next to the one you already wrote down.
1. Do the same with all other columns of the second matrix.
1. First cycle done.
   Now repeat the same steps with the **second row of the first matrix**.
1. Continue until all rows are done.
   You've got yourself a shiny new matrix.

::: example
Let's try the following matrix multiplication:

$$
\begin{pmatrix}
    5 & 2\\
    3 & 1\\
    0 & 2\\
\end{pmatrix}
\cdot
\begin{pmatrix}
    1 & 2 & 0 & 2\\
    3 & 0 & 1 & 3\\
\end{pmatrix}
=
\mathbf{???}
$$

We write down the first row of the first matrix as a column vector.

$$
\begin{pmatrix}
    5\\
    2\\
\end{pmatrix}
$$

Next we have to calculate the dot products for each column of the second matrix.

$$
\begin{pmatrix}
    5\\
    2\\
\end{pmatrix}
\cdot
\begin{pmatrix}
    1\\
    3\\
\end{pmatrix}
=
5 \times 1 + 2 \times 3
=
11
$$
$$
\begin{pmatrix}
    5\\
    2\\
\end{pmatrix}
\cdot
\begin{pmatrix}
    2\\
    0\\
\end{pmatrix}
=
5 \times 2 + 2 \times 0 =
10
$$
$$
\begin{pmatrix}
    5\\
    2\\
\end{pmatrix}
\cdot
\begin{pmatrix}
    0\\
    1\\
\end{pmatrix}
=
5 \times 0 + 2 \times 1 =
2
$$
$$
\begin{pmatrix}
    5\\
    2\\
\end{pmatrix}
\cdot
\begin{pmatrix}
    2\\
    3\\
\end{pmatrix}
=
5 \times 2 + 2 \times 3
=
16
$$
So the first row for the new matrix is $(11\ 10\ 2\ 16)$.
Repeating the same procedure with the second and third row, we can solve the full equation.

$$
\begin{pmatrix}
    5 & 2\\
    3 & 1\\
    0 & 2\\
\end{pmatrix}
\cdot
\begin{pmatrix}
    1 & 2 & 0 & 2\\
    3 & 0 & 1 & 3\\
\end{pmatrix}
=
\begin{pmatrix}
    11 & 10 & 2 & 16\\
    6 & 6 & 1 & 9\\
    6 & 0 & 2 & 6\\
\end{pmatrix}
$$
:::

More formally, when we matrix multiply a matrix $u$ with $m$ rows and $n$ columns with a matrix $v$ with $n$ rows and $p$ columns, the result is a matrix $w$ with $m$ rows and $p$ columns such that the value in row $i$ and column $j$ is the dot product of the $i$-th row of $u$ and the $j$-th column of $v$.

::: exercise
Calculate the result of matrix multiplication for all of the following.
If the result is undefined, say so.

1. $\begin{pmatrix} 1 & 5\\ -1 & -5\\ \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 & 1\\ -1 & -1 & -1\\ \end{pmatrix}$
1. $\begin{pmatrix} 1 & 5\\ -1 & -5\\ 1 & 5\\ \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 & 1\\ -1 & -1 & -1\\ \end{pmatrix}$
1. $\begin{pmatrix} 1 & 5\\ -1 & -5\\ 1 & 5\\ \end{pmatrix} \cdot \begin{pmatrix} 1 & -1 & 1 & -1\\ 1 & 1 & -1 & -1\\ \end{pmatrix}$
:::
