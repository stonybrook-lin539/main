---
pagetitle: >-
    Exponentiation
---

# Exponentiation

You are probably familiar with the expressions like $2^5$, which is the same as multiplying five instances of $2$.
That is to say, $2^5 = 2 \times 2 \times 2 \times 2 \times 2 = 32$ (don't confuse this with the string notation $2^5$, which would yield $22222$).
But there are some more advanced or subtle aspects of exponentiation that you might not have come across before or that you might have forgotten about in the meantime.

## Terminology: Base and exponent

In an expression like $x^y$, we say that $x$ is the **base** and $y$ is the **exponent**.
This is true even if $x$ or $y$ are complex expressions, and even if they themselves contain exponents

::: example
In
$$(10^3 \times \frac{3}{17}  - 7)^{5^\frac{2}{3}},$$
the base is
$$(10^3 \times \frac{3}{17}  - 7)$$
and the exponent is
$$5^\frac{2}{3}.$$
We see that the base contains another instance of exponentiation, $10^3$, where $10$ is the base and $3$ the exponent.
Similarly, the exponent $5^\frac{2}{3}$ is itself an instance of exponentiation with base $5$ and exponent $\frac{2}{3}$.
:::

## Addition of exponents is multiplication of bases

Since exponents may be arbitrarily complex formulas, they can contain instances of addition, e.g. $2^{2+3} = 2^5 = 32$.
Addition of exponents corresponds to multiplication of bases.

::: example
Consider once more the formula $2^{2+3}$.
We show that we can get the correct result either by adding up exponents or by multiplying bases.

- **Addition of exponents**: $2^{2+3} = 2^5 = 32$
- **Multiplication of bases**: $2^{2+3} = 2^2 \times 2^3 = 4 \times 8 = 32$
:::

This is intuitive enough.
Suppose $y = m + n$.
Then $x^y$ means "multiply $y$ instances of $x$", but that is the same as "multiply $m$ instances of $x$, multiply $n$ instances of $y$, and then multiply those two values".

## Negative exponents are fractions

For every positive number $y$, it holds that $x^{-y} = \frac{1}{x^y}$.
For example, $2^{-3} = \frac{1}{2^3} = \frac{1}{8} = 0.125$.

At first, this does not seem very intuitive.
The expression $2^{-3}$ could be translated as "multiply negative 3 instances of $2$", which sounds like gibberish.
Why should this be $\frac{1}{2^3}$?
Here is a somewhat intuitive way you can think about it (the full explanation requires a bit more abstract algebra than you might have seen at this point):

Consider the formula $4 \times 3 \times 2^{3} \times 2^{-3}$.
Whatever it means to "multiply negative 3 instances of $2$" in this formula, it should undo the effects of "multiplying 3 instances of $2$" so that we are left with just $4 \times 3$.
Another way of saying this is $2^{3} \times 2^{-3}$ should yield some number $n$ such that $4 \times 3 \times n$ is the same as $4 \times 3$.
Obviously the only possible value for $n$ is $1$.
So whatever the value of $2^{-3}$, it must be such that $2^{3} \times 2^{-3} = 1$.
But that is exactly what fractions do: $2^{3} \times 2^{-3} = 2^{3} \times \frac{1}{2^3} = \frac{2^3}{2^3} = 1$.

Once you understand this line of reasoning, it makes perfect sense that $x^{-y} = \frac{1}{x^y}$.

## Subtraction of exponents is division of bases

Just like addition of exponents corresponds to multiplication of bases, subtraction of exponents corresponds to division of bases.
This follows from the fact that subtraction is equivalent to addition with negative numbers.

::: example
Consider the formula $2^{3-2}$.
We show that we can get the correct result either by subtraction of exponents or by division of bases.

- **Subraction of exponents**: $2^{3-2} = 2^1 = 2$
- **Division of bases**: $2^{3-2} = \frac{2^3}{2^2} = \frac{8}{4} = 2$

This is a corollary of the fact that 1) subtraction is addition with negative numbers and 2) $x^{-y} = \frac{1}{x^y}$.
Hence we have:

$$2^{3-2} = 2^{3 + (-2)} = 2^3 \mult 2^{-2} = 2^3 \mult \frac{1}{2^2} = \frac{2^3}{2^2} = \frac{8}{4} = 2$$

:::

## $x^0 = 1$

When you ask a random person on the street to compute $10^0$, they will probably tell you that the result is $0$.
But the correct answer is $1$.
In fact, $x^0 = 1$ for any number $x$.
Again this seems intuitively wrong.
If $x^0$ means "multiply 0 instances of $x$", then it seems the result should be $0$, not $1$.

But given everything said so far, we can derive that $x^0$ must in fact be $1$.
First, observe that for any natural number $n$, it holds that $0 = n - n$.
So we can rewrite $x^0$ and $x^{(n-n)}$.
But we already know that subtraction of exponents corresponds to division, hence $x^{(n-n)} = \frac{x^n}{x^n}$.
And this must be $1$ because no matter what the actual value $v$ of $x^n$ might be, $\frac{v}{v}$ is always $1$.

## $x\mathrm{e}y$ notation for exponentiation

fixme: to be added

## The Euler number $e$ and exp notation

fixme: to be added
