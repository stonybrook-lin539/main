# The Myhill-Nerode Theorem: Automata as quotient structures (Solutions)

::: exercise
Describe the good continuations of $\String{ab}$ with respect to $(ab)^+$ and show that $\String{ab} \equiv_L \String{abab}$.


**Caution:** The empty string is a possible continuation, too.

::: solution
The good continuations of $\String{ab}$ with respect to $(ab)^+$ are

1. $\emptystring$ because $\String{ab} \cdot \emptystring = \String{ab}$, which is a string of $(ab)^+$,
1. $\String{ab}$ because $\String{ab} \cdot \String{ab} = \String{abab}$, which is a string of $(ab)^+$,
1. $\String{abab}$ because $\String{ab} \cdot \String{abab} = \String{ababab}$, which is a string of $(ab)^+$,
1. and so on.

Hence the set of all continuations of $\String{ab}$ with respect to $(ab)^+$ is $(ab)^*$.
But this is also the set of good continuations for $\String{abab}$:

1. $\String{abab} \cdot \emptystring = \String{abab} \in (ab)^+$,
1. $\String{abab} \cdot \String{ab}= \String{ababab} \in (ab)^+$,
1. $\String{abab} \cdot \String{abab}= \String{abababab} \in (ab)^+$,
1. and so on.

Hence $\String{ab} \equiv_L \String{abab}$.
:::
:::

::: exercise
Just because two strings are right congruent with respect to some string language $L$ does not mean that they are right congruent with respect to some other string language $L'$.
Suppose that $L'$ is $\String{ababc}(ab)^+$.
Show that $\String{ab}$ and $\String{abab}$ are not right congruent with respect to $L'$.

::: solution
Since all strings of the language $\String{ababc}(ab)^+$ must start with $\String{ababc}$, all the good continuations of $\String{ab}$ must start with $\String{abc}$.
The good continuations of $\String{abab}$, on the other hand, must all start with $\String{c}$.
Hence there is at least one string that is a good continuation of $\String{ab}$ but not $\String{abab}$ (for example, $\String{abcab}$), which implies that $\String{ab}$ and $\String{abab}$ are not right congruent with respect to $L'$.
:::
:::

::: exercise
It is fairly easy to see that $\equiv_L$ is an equivalence relation.
Explain why!
You'll have to remember which properties a relation has to meet in order to be an equivalence relation.
For each property, explain in intuitive terms why it holds.

::: solution
A binary relation is an equivalence relation iff it is transitive, reflexive, and symmetric.
All these properties hold of the right congruence relation $\equiv_L$.

1. **transitive**: Suppose $a \equiv_L b$ and $b \equiv_L c$.
   Then $a$ has the same good continuations as $b$, which in turn has the same good continuations as $c$.
   But then $a$ must have the same good continuations as $c$, and hence $a \equiv_L c$.
1. **reflexive**: It is trivially true that every string $a$ has the same good continuations as $a$, and hence $a \equiv_L a$.
1. **symmetric**: Suppose $a \equiv_L b$.
   Then $a$ has the same good continuations as $b$, or in other words, $b$ has the same good continuations as $a$.
   But then $b \equiv_L a$.
:::
:::

::: exercise
If $u \equiv_L v$, then $[u] = [v]$.
Explain why!

::: solution
The equivalence class of $u$ (i.e. $[u]$) is the set of all strings $x$ such that $u \equiv_L x$.
Since $\equiv_L$ is an equivalence relation, $u \equiv_L v$ entails for all $x$ that $u \equiv_L x$ iff $v \equiv_L x$.
But then the set of all strings $x$ such that $u \equiv_L x$ is exactly the same as the set of all strings $x$ such that $v \equiv_L x$.
In other words, $[u] = [v]$.
:::
:::

::: exercise
Describe the partition induced by $\equiv_L$ if $L \is (ab)^*$ --- that is to say, $L$ contains the empty string, every member of $(ab)^+$, and nothing else.
Then draw the automaton for $L$.
Which state corresponds to which equivalence class?

::: solution
There are 3 equivalence classes.

1. $[\emptystring]$ consists of every string in $(ab)^*$, each one of which can be continued with a member of $(ab)^*$,
1. $[a]$ consists of every string in $(ab)^* a$, each one of which can be continued with a member of $(bab)^+$.
1. $[b]$ consists of every string that has no good continuations at all.

The corresponding automaton with an explicit sink state is shown below.
The state names indicate which state corresponds to which equivalence class.

~~~ {.include-tikz size=mid}
abstar.tikz
~~~

:::
:::

::: exercise
Use the Myhill-Nerode theorem to show that the following language is not regular if the alphabet $\Sigma$ contains at least two distinct symbols (e.g. $a$ and $b$):
$\setof{ww^R \mid w \in \Sigma^*}$, where $w^R$ is the reverse of $w$.
This language is known as the **palindrome language**.
The palindrome language contains strings such as $abccba$ or $aaaa$, but not $abcabc$ or $aaab$.

::: solution
Consider the strings $a^n b$ and $a^{n+1} b$ ($n \geq 0$).
One possible continuation of $a^n b$ is $b a^n$ ($a^n b \cdot b a^n = \String{a^n bb a^n}$, which is a string of the palindrome language).
This is not a possible continuation of $a^{n+1} b$ ($\String{a^{n+1} b b a^n}$ is not a well-formed string of the palindrome language).
Hence $a^n b$ and $a^{n+1} b$ have distinct sets of good continuations for any choice of $n \geq 0$.
As there are infinitely many choices for $n$, $\equiv_L$ necessarily induces infinitely many equivalence classes.
:::
:::

::: exercise
Use the Myhill-Nerode theorem to show that the following language is not regular if the alphabet $\Sigma$ contains at least two distinct symbols (e.g. $a$ and $b$):
$\setof{ww \mid w \in \Sigma^*}$.
This language is known as the **copy language**.
The copy language contains strings like $abab$, $aaaa$, or $abbababbab$, but not $abba$, $aabaa$, or $baaaba$.

::: solution
Consider the strings $a^n b$ and $a^{n+1} b$ ($n \geq 0$).
One possible continuation of $a^n b$ is $a^n b$ ($a^n b \cdot a^n b = \String{a^n b a^n b}$, which is a string of the copy language).
This is not a possible continuation of $a^{n+1} b$ ($\String{a^{n+1} b a^n b}$ is not a well-formed string of the palindrome language).
Hence $a^n b$ and $a^{n+1} b$ have distinct sets of good continuations for any choice of $n \geq 0$.
As there are infinitely many choices for $n$, $\equiv_L$ necessarily induces infinitely many equivalence classes.
:::
:::

::: exercise
Show that both the palindrome language and the copy language are regular if the alphabet contains only a single symbol, e.g. $a$.

::: solution
If $\Sigma = \setof{a}$, then $\Sigma^*$ is $a^*$.
In addition, if $\Sigma = \setof{a}$, then $w = w^R$ for every $w \in a^*$.
Both the palindrome language and the copy language thus reduce to $\setof{ ww \mid w \in a^*}$.
But this is simply the set of all strings over $a$ of even length, i.e. $(aa)^*$, and this string language is generated by the automaton below.

~~~ {.include-tikz size=mid}
aastar.tikz
~~~

:::
:::
