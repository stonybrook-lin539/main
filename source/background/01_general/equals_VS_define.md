---
pagetitle: >-
    Equals VS Define: Why = is not the same as :=
---

# Equals VS Define: Why = is not the same as :=

I assume that you have all seen the "equals" sign $=$ before, as in $1 + 1 = 2$.
You have probably also seen usages such as *Compute $f(x)$ for $x = 5$*.
These are actually two very distinct uses of $=$.

In $1 + 1 = 2$, the equals sign expresses an equality.
An equality may or may not hold, and a statement about equality may be true or false.
While $1 + 1 = 2$ is in general a true statement when talking about numbers, there can be cases when it is false.
For example, in Boolean matrix multiplication we cannot have values larger than 1 and hence $1 + 1 = 1$, which means that $1 + 1 = 2$ would be false in that case.

In our $x = 5$ example, on the other hand, we are not saying that $x$ is equal to $5$, we are defining $x$ to be $5$.
There is no way for this to be true or false, you cannot tell me that I am wrong to define $x$ as $5$.
I could have just as well defined it to be $7$, or $-35.3$, and there is nothing you could have done to stop me.
There is no way for you to show that $x = 5$ is false.

In linguistic terms, the equals sign in $1 + 1 = 2$ expresses a proposition, whereas in $x = 5$ it expresses the speech act of establishing in the discourse that the name $x$ refers to the number $5$.
If you have some experience with programming languages, then you can think of this as the difference between a truth condition and a variable assignment.
Mathematicians care so much about this difference that they use two distinct symbols.
Equalities are expressed with $=$ as usual, but the speech act meaning of $=$ is denoted by $\is$ instead.
Hence a mathematician would not write "Suppose $x = 5$" but rather "Suppose $x \is 5$".

Long story short: Don't get confused when you see $\is$ instead of $=$, it simply means that you are looking at a definition/variable assignment rather than an equality.
