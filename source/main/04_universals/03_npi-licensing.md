---
pagetitle: >-
    NPIs and monotonicity
---

# NPIs and monotonicity

:::prereqs
- sets (comparisons)
:::

Monotonicity is not limited to morphology, it also shows up in areas where syntax (= sentence structure) interacts with semantics (= meaning).
One instance is the licensing of **Negative Polarity Items**.
That's quite a mouthful, so linguists usually say **NPIs**.
NPIs are a fascinating aspect of natural languages, and they reveal just how much math languages hide under their hood.
You might not have realized it, but the language brain is really sensitive to monotonic functions.

## A puzzle: distribution of NPIs

One of the most common NPIs in English is *ever*.
If you're a native speaker of English, you've probably never noticed that *ever* is quite a special guy, but you definitely agree that the first sentence below is well-formed, whereas the second is clearly bad.

1. No student should ever sleep in class.
1. Every student should ever sleep in class.

Quite curious, what's going on here?
Here we have two sentences that use two distinct **quantifiers**, one being *no* and the other *every*.
For some reason, *ever* can occur in the sentence with *no* but not with *every*.
We could posit a constraint that forbids *ever* and *every* to co-occur, this is rather unsatisfying as it only states the facts rather than explaining them.
But more importantly, it is also false.
Both of the following sentences are okay in standard dialects of English.

1. No student who ever slept in class should get a degree.
1. Every student who ever slept in class should get a degree.

So both *no* and *every* can be fine with *ever*, it's only in some cases where they diverge.
And when they do, we never find cases where *ever* is okay with *every* but not with *no*.
Quite puzzling, but fortunately we have decades of research to build on.
Linguists have studied NPIs for a long time, and one thing that has become clear is that in order to understand the contrast illustrated above, one has to look at the meaning of *every* and *no* from a mathematical perspective.

## Entailment

One important fact about sentences with *every* and *no* is that depending on whether they are true or false, other sentences can immediately be inferred to be true or false.
Consider the following sentence:

1. No student slept.

Suppose that this is true.
Then we can tell right away that both of the sentences below are also true.

1. No male students slept.
1. No sophomores slept.

After all, male students are students, and sophomores are students in their second year.
If a sophomore had indeed slept, then there would be at least one student that slept, but we already know that no student slept.
Hence it is impossible for *no student slept* to be true but *no sophomore slept* to be false.
The sentences stand in an **entailment relation** such that the truth of the first implies the truth of the other.

::: exercise
Consider the sentence *every student slept*.
Does it allow for similar inferences via entailment?

::: solution
Yes. If *every student slept*, then both of the following are true:

1. Every male student slept.
1. Every sophomore slept.
:::
:::

Note that the entailment only holds in one direction.
Even if *no sophomores slept* is true, it might still be the case that *no students slept* is false --- perhaps there's a freshman or junior who dozed off.
So entailment has a directionality.

We can actually express the directionality of entailment by looking at sets.
Consider the set of all students.
Clearly it contains all sophomores, but the set of sophomores does not contain all students.
So the set of sophomores is a **subset** of the set of students.
A sentence with *no* is **downward entailing**: if the sentence is true for a set $A$, then it is true for all subsets of $A$.

::: example
Let $A$ be the set of all students.
The sentence *No student slept* asserts for each student $s \in A$ that $s$ did not sleep.
Suppose this is true.
Then *No X slept* is necessarily true if X denotes some set $B \subseteq A$ because we already know for each $s \in B$ that $s$ did not sleep.
Since there is no subset of $A$ for which this entailment fails, *no* is indeed downward entailing.
:::

A similar argument can be used to show that *every* is downward entailing, too.

::: exercise
Construct such an argument that *every* is downward entailing.

::: solution
We can do this by substituting just a few terms in the example:

Let $A$ be the set of all students.
The sentence *Every student slept* asserts for each student $s \in A$ that $s$ did in fact sleep.
Suppose this is true.
Then *Every X slept* is necessarily true if X denotes some set $B \subseteq A$ because we already know for each $s \in B$ that $s$ did sleep.
Since there is no subset of $A$ for which this entailment fails, *every* is indeed downward entailing.
:::
:::

All this talk about downward entailment is nice and dandy, but it doesn't really help us with our problem.
We are looking for an explanation why there are cases where *ever* is fine with *no* but not with *every*.
If both *no* and *every* are downward entailing, then that can't be the relevant property to explain the contrast.
But it actually is, we just haven't been looking in the right (or left) place.

## Left entailment and right entailment

To bring out the difference between *every* and *no*, we have to make things a bit more mathematical.
We shall think of *no* and *every* as functions that take two arguments and return either true or false.

::: example
The sentence *no student slept* can instead be written as *no(student, slept)*, i.e. a function *no* that takes the arguments *student* and *slept*.
On the other hand, *no(old man that I know, snores louder than 125db)* corresponds to the sentence *no old man that I know snores louder than 125db*.
:::

The intuition here is that *no*-sentences are of the general form *no X does/is Y*, with *X* as the first argument and *Y* as the second.

::: exercise
Represent the following sentences in terms of this functional notation:

- No professor writes good lecture notes.
- Every professor could earn more in industry.
- This professor, no student likes.

::: solution
1. No(professor, writes good lecture notes)
1. Every(professor, could earn more in industry)
1. No(student, likes this professor)

::: solution_explained
The central thing to keep in mind here is that the arguments are determined by meaning, not the linear order in the string.
The first argument expresses what we are quantifying over, the second one what is being done.
For the first two examples, this is straight-forward.
For the third example, we have to figure out first that *this professor* is the object of *likes*.
So the sentence means the same as *no student likes this professor*, even though the word order is different.
:::
:::
:::

One thing the functional notation makes very clear is that a sentence like *no student slept* consists of two distinct parts that contribute to the meaning.
The first one, represented by X, is the set of things or objects that *no* picks from.
The second one, represented by Y, states what each one of them does.
Our previous examples of entailment only looked at X.
We made inferences from *no students* to *no sophomores* and *no male student*.
But what happens if we instead look at Y?

The answer is "not much" if we look at *no*.
But things get more interesting with *every*, so let us look at that one first.
Consider a sentence like *every student ran*, and contrast it against *every student ran a 5k*.
Is there an entailment here, and if so, in what direction?
Every person who runs a 5k is a person who runs, but the opposite is not true because somebody who runs, say, 1 mile is still a person who runs, but they're not a person who runs a 5k.
So the set of 5k-runners is necessarily a subset of all runners, but the set of runners is not guaranteed to be a subset of the set of 5k-runners (although this can happen if literally every runner is running a 5k).
It is also clear that if every student ran a 5k, then every student ran, whereas the opposite does not hold. 
So all of a sudden the direction of inference is the other way round --- if the sentence is true for Y, then it is true for every **superset** of Y.
This shows that even though *every* was downward entailing with respect to X, it is **upward entailing** with respect to Y --- whereas *no* is downward entailing with respect to both X and Y.

::: exercise
Show that *no* is downward entailing with respect to Y.

::: solution
Consider a concrete example first.
Suppose *No student runs* is true.
Then *No student runs a 5k* is also true.
The set of individuals that run a 5k is a subset of the individuals that run, so we made an inference from a set $S$ (the set of runners) to a subset of $S$ (the set of 5k runners), which means that we have downward entailment.

More generally, if $\mathrm{No}(X,Y)$ is true, then there is no individual $i \in X$ such that $i$ belongs to the set of individuals that do $Y$.
But then $i$ cannot belong to any subset of $Y$, either.
Or in set-theoretic terms: if $\mathrm{No}(X,Y)$ is true, then $X \cap Y = \emptyset$, which implies $X \cap Z = \emptyset$ for every subset $Z$ of $Y$.
This shows that *no* is downward entailing with respect to $Y$.
:::
:::

And now we have the contrast between *every* and *no* that we need.
For *every*, we see that it is downward entailing with respect to X but upward entailing with respect to Y.
This is also called **left downward entailing** and **right upward entailing** (because X is the left argument of the function and Y the right argument).
But *no* is both **left downward entailing** and **right downward entailing**.
Now look once more at the example sentences from the beginning of the notebook.

1. No student should ever sleep in class. (well-formed)
1. No student who ever slept in class should get a degree. (well-formed)
1. Every student should ever sleep in class. (ill-formed)
1. Every student who ever slept in class should get a degree. (well-formed)

For clarity, let's rewrite this in the form of a table

| **Quantifier** | **X**                           | **Y**                      | **Status**  |
| --:            | :-:                             | :-:                        | :--         |
| no             | student                         | should ever sleep in class | well-formed |
| no             | student who ever slept in class | should get a degree        | well-formed |
| every          | student                         | should ever sleep in class | ill-formed  |
| every          | student who ever slept in class | should get a degree        | well-formed |

When *ever* occurs in X, then it is fine with both *no* and *every*, which are both left downward entailing (i.e. downward entailing with respect to X).
But when *ever* occurs in Y, it must be with the right downward entailing *no* rather than the right upward entailing *every*.
So we finally have our answer: downward entailing contexts allow for NPIs like *ever*, upward entailing ones do not.


## Connection to monotonicity

Upward entailing and downward entailing are both instances of monotonicity.
In order to see this, we have to make our treatment a bit more mathematical (it's still fairly informal for mathematicians' standards).

In the preceding section, we essentially treated quantifiers like *no* and *every* as binary functions that take two arguments and maps them to a truth value.
More abstractly, we analyze every quantifier $Q$ as a function of the form $Q(X,Y)$.
Since we haven't really looked at monotonicity for functions with more than one argument, we first need to simplify things a bit.
Instead of considering the quantifiers themselves, which take two arguments, we will only consider unary functions that fix one of arguments.
In other words, instead of the function $Q(X,Y)$, we will consider the functions $Q_X(Y)$ and $Q_Y(X)$.

Let $f$ be some function that takes as its input a set (X or Y in the notation above) and maps it to either 1 (for True) or 0 (for False).
Intuitively, you can think of $f$ as a sentence with a hole in it that must be filled by the argument.

::: example
Consider the sentence
*Every male student snored loudly*.
We could take this to define the function *every*(*male student*, *snored loudly*), which returns 1 iff every male student snored loudly.

But we could also take it to be an instance of the function
*every $\Box$ snored loudly*
applied to the argument
*male student*.
The function maps *male student* to 1 iff, once again, every male student snored loudly.

And we can also view the sentence as an instance of the function
*every male student $\Box$*
applied to the argument
*snored loudly*.
This function, too, returns 1 iff it is true that every male student snored loudly.
:::

The domain of such a function $f$ consists of all possible sets of individuals and objects.
For instance, it contains the set of all students, the set of all male students, the set of all US presidents, the set of all loud snorers, and so on.
We can order the domain by the subset relation $\subseteq$ such that $A \subseteq B$ iff every member of $A$ is also a member of $B$.
Similarly, we order the co-domain $\setof{0,1}$ in the usual fashion such that $0 < 1$.

Now suppose that $f$ is monotonically increasing.
Then $A \subseteq B$ implies $f(A) \leq f(B)$.
Whenever $f(A) = 1$, it must be the case that $f(B) = 1$.
In other words, $f$ is upward entailing.

::: example
Consider the sentences
*Every student ran a 5k*
and
*Every student ran*.
Clearly if the former is true, the latter must be too.
We also know already that the set of students that ran a 5k (call it $5k$) is a subset of the students that ran (call it $R$).
So we have $5k \subseteq R$.

Now suppose that *every student*$(5k) = 1$.
Then *every student*$(R) \geq 1$ because $R \supseteq 5k$ and the function is monotonically increasing.
So the fact that the sentence is true for $5k$ entails that it is true for every superset of $5k$.
This is exactly what it means to be upward entailing.
:::

Downward entailment works exactly the same except that the function is monotonically decreasing.

::: exercise
Construct an example for downward entailment similar to the one above for upward entailment.

::: solution
Again this only requires swapping out a few words:

Consider the sentences
*No student ran a 5k*
and
*No student ran*.
Clearly if the latter is true, the former must be too.
We also know already that the set of students that ran a 5k (call it $5k$) is a subset of the students that ran (call it $R$).
So we have $5k \subseteq R$.

Now suppose that *no student*$(R) = 1$.
Then *no student*$(5k) \geq 1$ because $5k \subseteq R$ and the function is monotonically decreasing.
So the fact that the sentence is true for $R$ entails that it is true for every subset of $R$.
This is exactly what it means to be downward entailing.
:::
:::

::: exercise
Alternatively, we may view downward entailment as a monotonically increasing function if sets are ordered by the superset relation instead of subset.
Explain why!

::: solution
By ordering sets by the superset relation instead of the subset relation, we flip their order: if we previously had $X < Y$ (i.e. $X \subseteq Y$), we now have $Y < X$ (i.e. $Y \supseteq X$).
Downward entailment means that if a statement is true with respect to $Y$, then it is true with respect to every $X$ that $Y$ is a superset of.
But in our new ordering, that's every $X$ such that $Y < X$.
Hence downward entailment can be rephrased as follows: if $f(Y) = 1$, then $f(X) \geq 1$ for every $X > Y$.
And that is an instance of being monotonically increasing.
:::
:::

::: exercise
Determine whether *some* is right downward entailing or right upward entailing.
What does this predict for the distribution of *ever* in a sentence with *some*, and does this prediction match your intuitions?

::: solution
Consider the sentences *Some student ran* and *Some student ran a 5k*.
Since the latter entails the former, *some* is right upward entailing.
Hence we expect *Some student should ever sleep in class* to be illicit, which it is indeed.
:::
:::

::: exercise
Determine whether *some* is left downward entailing or left upward entailing.
What does this predict for the distribution of *ever* in a sentence with *some*, and does this prediction match your intuitions?

::: solution
Consider the sentences *Some student ran* and *Some sophomore ran*.
Since the latter entails the former, *some* is left upward entailing.
Hence we expect *Some student who ever slept in class should get a degree* to be illicit, which it is indeed.
:::
:::

As you can see, monotonicity isn't limited to morphological paradigms.
Without mathematics, it wouldn't be obvious that the No Crossing constraint of phonology has anything to do with the $^*$ABA generalization or the distribution of *ever*.
The abstract notion of monotonicity allows us to tie them all together, gaining a deeper understanding of universals across language modules.

::: exercise
In the case of adjectival gradation, the formal universal of monotonicity had to be supplemented with the ordering *positive* $<$ *comparative* $<$ superlative, a substantive universal.
In this unit, we again used monotonicity as a formal universal to restrict the distribution of *ever*.
What is the substantive universal we had to combine monotonicity with?
Does this strike you as a language-specific universal, or is it more likely an aspect of human cognition in general?

::: solution
The substantive universal is the order of sets in terms of supersets.
This is not a language-specific aspect of human cognition, it is an instance of the general ability to group objects and individuals into groups and to establish relations between those groups.
:::
:::

## Recap

- **Negative polarity items** (NPIs) like *ever* have a peculiar distribution that is conditioned by entailment relations.
- A sentence $s$ **entails** another sentence $t$ iff $t$ must be true whenever $s$ is true.
- Every quantifier $Q$ can be regarded as a binary function of the form $Q(X, Y)$ where $X$ describes the set of individuals/object/entities $Q$ quantifies over (students, sophomores, ...) and $Y$ is another set of individuals (the set of runner, 5k runners, and so on).
- A quantifier $Q$ can be left/right downward/upward entailing depending on which of the clauses below hold whenever $Q(X, Y)$ is true.
    - **left downward**: $Q(Z, Y)$ is true for every $Z \subseteq X$.
    - **right downward**: $Q(X, Z)$ is true for every $Z \subseteq Y$.
    - **left upward**: $Q(Z, Y)$ is true for every $Z \supseteq X$.
    - **right upward**: $Q(X, Z)$ is true for every $Z \supseteq Y$.
- Upward entailment (downward entailment) is the same as being monotonic increasing (monotonic decreasing).

\includecollection{solutions}
