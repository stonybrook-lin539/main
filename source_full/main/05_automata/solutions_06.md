# Finite-state recognition as Boolean matrix multiplication (Solutions)

::: exercise
For each one of the following equations, give its result under Boolean matrix multiplication.
If the output is undefined, say so.

$$
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1\\ 
    1\\
\end{bmatrix}
$$

$$
\begin{bmatrix}
    0 & 1\\
    1 & 2\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
$$

$$
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
$$

$$
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    0 & 0 & 1 & 1\\
    0 & 1 & 0 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1\\
    1\\
    0\\
    1\\
\end{bmatrix}
$$

::: solution
$$
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1\\ 
    1\\
\end{bmatrix}
=
\begin{bmatrix}
    1\\
    1\\
\end{bmatrix}
$$

$$
\begin{bmatrix}
    0 & 1\\
    1 & 2\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
=
$$
undefined because Boolean matrices cannot contain $2$

$$
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
=
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
$$

$$
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    0 & 0 & 1 & 1\\
    0 & 1 & 0 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1\\
    1\\
    0\\
    1\\
\end{bmatrix}
=
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
\otimes
\begin{bmatrix}
   1\\
   1\\
\end{bmatrix}
=
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
   1\\
   1\\
\end{bmatrix}
=
\begin{bmatrix}
   1\\
   1\\
\end{bmatrix}
$$

:::
:::

::: exercise
Recompute the values for the formulas from the previous exercise, using the faster procedure now.
Write down the relevant steps as in the example above.
Skip any formulas that you said were not well-defined for Boolean matrix multiplication.

::: solution

$$
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1\\ 
    1\\
\end{bmatrix}
=
\begin{bmatrix}
    1\\
    1\\
\end{bmatrix}
$$

As the second row of the first matrix is all $1$s and the second matrix is all $1$s, we can immediately put a $1$ in the second row of our matrix.
We also see that the second column of row 1 of matrix 1 is a $1$, which is matched by the second row of column 1 of matrix 2.

$$
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
=
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
$$

As column 2 of matrix 2 is all $0$s, we can immediately fill the second column of our matrix with $0$s.
For row 1, column 1, we see that only column 2 of row 1 matrix 1 has a $1$, which is matched by the $1$ of row 2, column 1 of matrix 2.
Finally, row 2 of matrix 1 and column 1 of matrix 2 are all $1$s, so we can put a $1$ in row 2, column 1 of our matrix.

$$
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1 & 0\\ 
    1 & 0\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    0 & 0 & 1 & 1\\
    0 & 1 & 0 & 1\\
\end{bmatrix}
\otimes
\begin{bmatrix}
    1\\
    1\\
    0\\
    1\\
\end{bmatrix}
$$

Consider first matrix 3 and matrix 4, the product of which is a matrix with two rows and one column.
We see that column 4 of matrix 3 is all $1$s, and that row 4 of matrix 4 is all $1$s.
Hence the resulting matrix must be all $1$s.

Now consider the product of matrix 2 and this new matrix, which is again a matrix with two rows and one column.
Since matrix 2 has a $1$ in every row, and the new matrix only contains $1$s, their product will again contain only $1$s.

The same reasoning applies for the product of matrix 1 and the matrix computed so far.
:::
:::

::: exercise
Solve the equation in the example above in two ways:

1. proceeding from left to right, starting with the first matrix,
1. proceeding from left to right but starting with the second matrix; only multiply with the first matrix at the very end.

Both routes return the same result because matrix multiplication is associative.
But one will be much less work for you than the other.

::: solution

**Left-to-right from first matrix**

\begin{align*}
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 0 & 1\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
%
1
\end{align*}

**Left-to-right from second matrix**

\begin{align*}
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 1\\
    0 & 0 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    1 & 0 & 0\\
    0 & 0 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    1\\
    0\\
    0\\
\end{bmatrix}
%
&
=
%
1
\end{align*}

:::
:::

::: exercise
Use Boolean matrix multiplication to determine for each one of the following strings whether it is a member of $a(\String{baa})^*$:

1. $\String{aab}$
1. $\String{aba}$
1. $a$
1. $\emptystring$

::: solution
$\String{aab}$

\begin{align*}
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
0
\end{align*}

$\String{aba}$

\begin{align*}
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 0 & 1\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
0
\end{align*}

$a$

\begin{align*}
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 0 & 0\\
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
%
1
\end{align*}

$\emptystring$

\begin{align*}
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    0\\
\end{bmatrix}
%
&
=
%
0
\end{align*}

:::
:::

::: exercise
Consider the non-deterministic FSA below for $a^+b^*$.

~~~ {.include-tikz size=mid}
aplusb_nondet.tikz
~~~

Construct the corresponding matrices for this automaton.
Then use matrix multiplication to determine for each one of the following strings whether it is recognized by the automaton.
Solve the equations from left to right and pay close attention to how the distribution of $1$s reflects which states the automaton may be in.


1. $\String{a}$
1. $\String{ab}$
1. $\String{aaab}$

::: solution

$$
a \is
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
%
\qquad
%
b \is
\begin{bmatrix}
    0 & 0 \\
    0 & 1 \\
\end{bmatrix}
%
\qquad
%
I \is
\begin{bmatrix}
    1 & 0 \\
\end{bmatrix}
%
\qquad
%
F \is
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
$$

$\String{a}$

\begin{align*}
\begin{bmatrix}
    1 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
%
&
=
%
1
\end{align*}

$\String{ab}$

\begin{align*}
\begin{bmatrix}
    1 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 \\
    0 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 \\
    0 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
%
&
=
1
\end{align*}

$\String{aaab}$

\begin{align*}
\begin{bmatrix}
    1 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 \\
    0 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 \\
    0 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    1 & 1 \\
    0 & 0 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 \\
    0 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    1 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 \\
    0 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 \\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
\end{bmatrix}
%
&
=
1
\end{align*}
:::
:::

::: exercise
Continuing the previous exercise, determinize the automaton.
Then repeat the previous steps using the deterministic automaton instead.

::: solution
The deterministic automaton is as follows:

~~~ {.include-tikz size=mid}
aplusb_det.tikz
~~~

$$
a \is
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 1 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\qquad
%
b \is
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 1\\
\end{bmatrix}
%
\qquad
%
I \is
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\qquad
%
F \is
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
$$

$\String{a}$

\begin{align*}
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 1 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
%
&
=
%
1
\end{align*}

$\String{ab}$

\begin{align*}
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 1 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 1\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 1\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 0 & 1\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
&
=
1
\end{align*}

$\String{aaab}$

\begin{align*}
\begin{bmatrix}
    1 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 1 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 1 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 1 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 1\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 1 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 1 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 1\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 1 & 0\\
    0 & 1 & 0\\
    0 & 0 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 1\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 1 & 0\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0 & 0 & 0\\
    0 & 0 & 1\\
    0 & 0 & 1\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
%
&
=
\\
%
\begin{bmatrix}
    0 & 0 & 1\\
\end{bmatrix}
%
\otimes
%
\begin{bmatrix}
    0\\
    1\\
    1\\
\end{bmatrix}
&
=
1
\end{align*}

:::
:::


::: exercise
Carefully read through the definition above.
Try to make sense of it based on the previously established intuition.
Write down anything you do not understand, and discuss it in class.
:::
