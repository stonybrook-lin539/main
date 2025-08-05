---
pagetitle: How to read mathematics
---

# How to read mathematics

While this book is designed to be as approachable as possible, a certain mathematical style of writing is indispensable.
This includes special notation, some math-specific jargon, and even a particular way of interpreting English sentences.
Mathematicians do not do this to sound smarter than they are or to isolate themselves from the uninformed layman, but because it makes it easier for them to communicate their ideas.
This is no different from any other field of research --- a specialized field of study requires a specialized means of communication.
It will take you a while to get used to this way of talking and writing, but here are a few tips to make sure you don't throw in the towel too early.

## Dealing with symbol shock

The most salient aspect of mathematical communication is the heavy reliance on special symbols.
This starts with formulas like $f(x) = kx + d$ and quickly develops into very complex statements.
Here's a small sample for your entertainment.
If you don't understand a word and can feel your blood pressure spike, that's exactly the point!

::: example
Let $\mathcal{L}$ be a totally ordered collection of languages $L_1, \ldots, L_n$ ($n \geq 1$) such that for all $1 \leq i,j \leq n$ we have $L_j \not\subseteq L_i$ iff $i < j$.
:::

::: example
For any given string $s$ and PCFG $G$, the probability of $s$ is $\sum_{d \in D_G(s)} \prod_{r \in d} p_G(r)$ where $D_G(s)$ is the set of derivation trees of $G$ that yield $s$, $r$ is a tree bigram of a derivation tree, and $p_G(r)$ is the probability of $r$ according to $G$.
:::

::: example
A *$k$-interval*, or simply *$k$-val*, is a $5$-tuple $\tuple{k,G_l, G_r, G_o, G_f}$ such that $k \geq 1$ and each $G$ is an SL-$1$ grammar that specifies, respectively, the left edge, right edge, open slots, and the fillers.
The corresponding *$k$-val formula* (with free variables $x_1$, $\ldots$, $x_k$) is 
\begin{multline*}
    \exists l,r
    \bigg [
        \bigwedge_{g \in G_l} \neg g(l)
        \wedge
        \bigwedge_{g \in G_r} \neg g(r)
        \wedge
        \bigwedge_{1 \leq i \leq k} 
        \bigwedge_{g \in G_o} \neg g(x_i)
        \wedge
        l \prec x_1
        \wedge
        x_k \prec r
        \wedge
        \\
        \forall z
        \Big [
            \big (
                (l \prec z \wedge z \prec x_1)
                \vee
                (x_k \prec z \wedge z \prec r)
                \vee
                \bigvee_{1 \leq i < k}
                (x_i \prec z \wedge z \prec x_{i+1})
            \big )
            \rightarrow
            \bigwedge_{g \in G_f} \neg g(z)
        \Big ]
    \bigg ]
\end{multline*}
For any empty $G$, $\bigwedge_{g \in G} \neg g(x)$ is always satisfied.
:::

Unless you've had previous mathematical training, these examples probably make your eyes glaze over and your brain freeze in horror:
"What is this stuff?
What's $i$ again, why is there a big sigma, and what is the subscript there?
Why can't they just say what they mean in plain English?
I can't understand this, it's hopeless, I'm just not made for math."
Don't despair, you've just experienced **symbol shock**.

Symbol shock refers to the phenomenon that just looking at a page of math can be so disheartening that you can't think clearly.
It's like being at the base of Mount Everest, looking up, and feeling that you'll never be able to reach the top.
So rather than trying you give up immediately, or you overcompensate and rush forward in a frenzy without paying attention to what you're doing.
Neither approach will get you to the goal.
In order to deal with symbol shock, you have to develop the central survival skills of mathematics: **take your time**, and **keep a cool head**.

You cannot read math like a novel or even your average textbook.
An 8 page paper can easily keep you busy for days before you fully understand it.
Revolutionary proofs may only span a few pages yet take trained mathematicians months to understand.
Math takes time, so do not rush.
As soon as you internalize this simple rule, symbol shock will be much less of a problem.
When a new symbol is introduced, pause and commit it to memory.
When you see a complex formula, work through it symbol by symbol until you understand what's going on.
Just. Take. Your. Time.

This is actually why I think that math is easier to learn from a book than a class.
With a text, you can reread every sentence until you get it.
You can go back three pages to revisit a point you thought was clear to you but now seems to be at odds with what you're reading.
You can't do that in a lecture.
But you actually have to do all those things, you have to slow down, go back, reread.
Math isn't all that hard, but you have to be very disciplined about it.

With time, you will get much better at reading math and it will take you much less effort, but for the beginning I suggest that you do the following to better deal with symbol shock:

- Assign colors to specific symbols and types of objects.
  In my personal experience, I can tell pretty easily how well I understand a mathematical text based on how I would color its math.
  At first, it's all just black, but as I gain a deeper understanding of the objects and how they hang together I construct an internal coloring system for myself.
  So grammars are blue, automata green, certain variables that keep reoccurring are purple and teal, and so on.
  If you have a hardcopy of this book in front of you, you can literally add colors to all the symbols, and that way the logic of the pages will reveal itself more clearly to you.

- Think about **why** certain symbols were chosen.
  Mathematicians care a great deal about good notation, and it really shows.
  A math text with a well-designed notation is a pleasure to read.
  There's certain established conventions.
  For instance, indices are usually chosen to be $i, j, k$, variables are $x, y, z$, and functions are $f, g, h$.
  But that's just a rule of thumb.
  A labeling function may be $\ell$, which looks like an $l$ but is slightly different so that $l$ can be used to refer to labels instead.
  Never try to memorize notation in a brute-force manner, try to understand the design principles behind it.
  If you know why the notation looks the way it does, you'll have a much easier time remembering even minor details and nuances.

- Set yourself realistic goals.
  Don't attempt to read 20 pages in one sitting.
  Instead, plan for 3 or 4 reading sessions of 5 pages each.
  And go in with the expectation that you will have to read some passages multiple times, and that you'll have to go back a few pages to look up some symbol or definition.

- Don't give up.
  None of the things we cover are super-advanced hardcore math problems that will make your head explode unless you have an IQ of 150.
  What we are doing is the math-equivalent of running a 5k: most college students aren't fit enough to do it on their first try, but they can reach that level with a few months of training.
  It requires tenacity and discipline, though.


## Dealing with some other stumbling blocks

### No implicatures

Mathematical writing is also peculiar because, as we linguists like to say, implicatures are often cancelled implicitly.
That's a smarty pants way of saying that only the literal meaning is the intended one.
For the uninitiated reader, it is easy to miss something important by assuming that a mathematical statement is more specific than it actually is.

::: example
The phrase "Let $S$ be a set containing two odd numbers" does not entail that $S$ only contains two odd numbers.
It could contain all kinds of additional things, including other odd numbers, but at the very least it contains two odd numbers.
If we wanted the set to contain two odd numbers and nothing else, we would have written "Let $S$ be a set containing exactly two odd numbers, and nothing else".
Tricky, hmm?
:::

Another common pitfall arises with statements that use *every*.
Consider the sentence "Every blue dragon is a chain smoker".
Is this claim true or false?
A linguist will tell you that it is neither, and instead contains a presupposition violation (yes, linguists like their fancy terms).
It is a presupposition violation because the sentence assumes that blue dragons exist, which they obviously do not.
A mathematician doesn't care for such linguistic subtleties and instead considers the statement true because there is no counterexample to prove it wrong.
Their chain of reasoning is as follows:

1. There exists no blue dragon that isn't a chain smoker.
1. Hence there is no counterexample to the claim that every blue dragon is a chain smoker.
1. Since there is no counterexample to the statement "Every blue dragon is a chain smoker", it isn't false.
1. Since the statement "Every blue dragon is a chain smoker" isn't false, it is true.

That reasoning is perfectly fine for mathematics, but it's very different from how a layperson would think about the statement "Every blue dragon is a chain smoker".
Again, when dealing with math you shouldn't assume anything that isn't stated explicitly.

Quite generally, you should try to identify minimal examples:
when you see a statement or definition, always think about the simplest object that satisfies it, and ask yourself how much this object can change before it no longer fits the description.

::: advice
Don't assume more than what was actually said.
:::

### Questioning definitions

Speaking of definitions, you should always ask yourself why something is defined the way it is.
I don't mean this in some kind of existentialist way like "What does it mean to be red?", but a utilitarian one: considering that we could have defined something in a million slightly different ways, what might be the reason that this is considered the most useful, elegant or productive definition?
Remember, definitions cannot be true or false, they can only be useful or useless.
According to biologists, tomatoes aren't vegetables, yet that doesn't mean that their definition of *vegetable* is false.
It just means that their definition serves a specific use case that does not align with common usage.
So whenever you encounter a definition, you should ask yourself what is it that makes that definition useful.
Why did the person decide to go with this definition rather than some other conceivable alternative?
In exploring this question, you will get a much better understanding of what the definition even defines, and that is key to studying the kind of object that is being defined.

:::advice
Think about why things are defined the way they are.
:::

### Making definitions concrete

Another helpful strategy in dealing with definitions is to come up with two distinct lists: examples that fit the definition, and examples that do not fit the definition.
Both are equally important.
Sometimes a definition may be so abstract and general that it is hard to see what would not fit the definition.
In seeking out those examples, you gain a much better idea of the defined class of objects.

::: example
Consider the following example, which is a lot more abstract than most of the things you will encounter in this book:
An *algebra* is a set $S$ with an operation that takes elements of $S$ as input and produces elements of $S$ as its output.

That is a very general definition, and there are tons of things that are algebras in this sense:

- the natural numbers (0, 1, 2, 3, ...) with addition: you take two natural numbers, add them together, and you still have a natural number.
- the integers (..., -3, -2, -1 0, 1, 2, 3, ...) with subtraction: you take two integers, subtract the second from the first, and you'll still have an integer
- the real numbers with base 2 logarithm: if you don't know yet what that means, rest assure that you will learn about logarithms at some point in this book
- the set of all possible strings with concatenation: again, you will know very soon what this means

But with such a general description, what could possibly fail to be an algebra?
Well, the natural numbers with division, for instance.
The natural numbers are 0, 1, 2, 3, and so on, but $\frac{5}{2} = 2.5$, which is not a natural number.
This shows that division can take two natural numbers as input and return something that is not a natural number.
Hence the natural numbers with division is not an algebra.
:::

A brief remark:
If you're worried now because this example mentioned natural numbers, integers, logarithms, or anything else you don't quite remember from your high school days, don't despair.
While these are convenient examples for mathematical concepts, we won't actually encounter them all that often.
They certainly aren't the focus of this book, and high school math will rarely make an appearance.
Where we do need these concepts, they're slowly introduced like any other new concept.
So don't let this distract you, focus on the important insight here:

::: advice
Whenever you see an abstract definition, think about what kind of more concrete objects would (not) fit the definition.
:::


### Implication and equivalence are not the same

English, as all natural languages, is pretty sloppy in how it expresses conditions.
Consider the following lovely sentence: "If you don't give me your money, I will shoot you".
Now the common understanding is that you won't be shot as long as you hand over your money.
But if your robber happens to be a mathematician you are very unlucky because they might still shoot you --- while you draw your final breath they will gleefully point out that they didn't say "If you don't give me your money, I will shoot you, and if you give me your money I will not shoot you."
Your murderer took advantage of the fact that English often expresses a biconditional ($a$ implies $b$, and the other way round) with the same language we use for implications ($a$ implies $b$, but $b$ does not necessarily imply $a$).

::: example
In "If you don't give me your money, I will shoot you", the *if* is a biconditional: whichever choice you make fully determines what the robber will do next.
Not forking over your hard-earned cash implies getting shot by the robber, and getting shot by the robber implies that you chose not to fork over your hard-earned cash.
But the very same *if* is just an implication in "If it rains, the road is wet": if it does not rain, the road may still be wet, e.g. because of a homeowner's overzealous sprinklers.
Here the absence of rain does not imply the absence of wet roads.
It is an implication, but not a biconditional.
:::

English does not explicitly mark the distinction between a biconditional and an implication, the reader is supposed to figure it out from context.
But in mathematics, the distinction is very important, and this is why mathematicians explicit distinguish the implication *if* from the biconditional *iff* (which is short for *if and only if*).
So pay close attention to whether the text uses an *if* or an *iff*.

::: example
The following is an implication but not an equivalence/biconditional: "If you are an actress, then you are female".
After all, not every female is an actress.
On the other hand, "You are a bachelor iff you are an unmarried man" is a biconditional.
Every unmarried man is a bachelor, and every bachelor (in the non-academic sense) is an unmarried man.
:::

::: advice
Never confuse the conditional *if* with the biconditional *iff*.
:::

## Recap

- Avoid symbol shock!
    - Don't rush, take your time.
    - Break readings into chunks.
    - Add colors.
    - Try to understand the notation.
- Definitions
    - Read them carefully.
    - Think about what would (not) fit the definition.
    - Think about why this particular definition was chosen, rather than some alternative.
- Writing style
    - Don't assume implicatures.
      Read in a very literal fashion.
    - Don't confuse implications (*if*) and biconditionals (*iff*).
