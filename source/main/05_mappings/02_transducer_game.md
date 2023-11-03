---
pagetitle: >-
    Finite-state transductions as a game
---

# Finite-state transductions as a game

A **transducer** is a machine that is given some input and then produces an output from that input.
That's obviously a very general concept, but in 90% of the cases where folks talk about transducers, they actually mean **finite-state string transducers** (FSTs).
These are heavily restricted types of transducers that translate an input string into an output string.
One also says that the FST **rewrites** an input string as an output string, and this term already suggests that FSTs may be a suitable model of phonology, where underlying representations (URs) are rewritten as surface forms.
FSTs are widely used across computer science, data science, language technology, bioinformatics, and many other fields, so phonology would be in good company.
And as we will see in subsequent units, FSTs indeed seem to be a good fit as they give us a lot of phonological mechanisms essentially for free.
But first we have to get a better intuition of what FSTs are.

## The intuition behind finite-state transducers

Imagine you are playing a turn-based, co-operative, hidden-information game with your friends (okay, it will be a pretty lame game on its own, but it would be a good foundation to build a more interesting game on top of).
You sit at a table, with the following items on it: an empty tray, a pile of "output tokens" (which may contain duplicates), and a bag that contains "input tokens" (without duplicates) and a token with the special symbol {{{R}}}.
At the beginning of a player's turn, they blindly draw an input token from the bag and based on what that input token is, they place some number of output token on the tray (to the right of any tokens that may have been placed on the tray during earlier turns).
They then return the input token to the bag.
So far, so boring.
There are several twists to this set up that make it a bit spicier:

1. Every player has their own set of rules, probably different from the rules for all other players, that tells them what token they should place on the tray.
   Sometimes, the rules leave the player a choice as to what token they may place on the tray.
1. The combination of the input token the player draws from the bag and the output token(s) they place on the tray determines which player gets the next turn.
1. Some players have the special power to place output tokens without drawing an input token from the bag.
1. The players choose freely who gets to play the very first turn, but the chosen player's rules must designate them as an "initial" player.
1. When a player draws the token with {{{R}}} from the game, the player checks whether their rules designate them as a "final" player.
   If so, the game is won and the players write down the sequence of symbols on the output token tray as their "victory string".
   Otherwise, the game is lost.

::: example
John and Mary have agreed to serve as playtesters for this early alpha version of a board game.
They sit down at the table and fill their token bag with all the input tokens: heart, spade, and the distinguished token {{{R}}}.
They also have access to a large pile of output tokens consisting of hearts, diamonds and clubs.
Their rule sheets are as follows:

1. **Mary's rules (Player 1)**:
    - If you draw a heart, place a diamond. Player 2 gets the next turn.
    - If you draw a spade, pick one of the following:
        - Place two clubs. You get the next turn.
        - Place no output token. Player 2 gets the next turn.
    - You are not an initial player.
    - You are not a final player.
1. **John's rules (Player 2)**:
    - **Special power:** Instead of drawing an input token, place a club. You still get the next turn.
    - If you draw a heart, place a heart. Player 1 gets the next turn.
    - If you draw a spade, place a heart. Player 1 gets the next turn.
    - You are an initial player.
    - You are a final player.

And thus the game begins:

- Since John is the only initial player, he starts the first turn.
  He draws a heart.
  Following his rules, he return the heart to the bag, places a heart on the output token tray, and then it is Mary's turn.
- Mary draws a spade, and she decides to go with option one: she places two clubs, and she also gets the next turn (and of course she returns the spade she drew to the input token bag).
- Mary then draws another heart and places a heart on the output tray as prescribed by her rules.
  John thus gets the next turn.
- John decides to use his special power to place a club without drawing from the input bag.
Doing so allows him to keep his turn.
- John decides once again to use his special power, placing one more club on the output token tray.
- Once again it is John's turn, but he can tell from Mary's death stare that she's getting annoyed with his special power.
  John instead decides to draw from the input token bag.
  He draws the special token {{{R}}}, signalling the end of the game.
  But fortunately John's rules designate him as a final player, and thus the game is won.

John and Mary celebrate their victory by writing down their victory string *heart-club-club-heart-club-club*, which they obtained from the sequence *heart-spade-heart-{{{R}}}* of input tokens.
:::

::: exercise
How would the game have ended if Mary had decided to go with option 2 instead: place nothing and player 2 gets the next turn.
What would have been the sequence on the output token tray, assuming that John does not use his special power at all?
:::

::: exercise
This continues the previous exercise.
What if Mary's rule sheet also contained the special power below?
Would there be a way to use this rule and finish the game?

- **Special power:** Instead of drawing an input token, place a diamond.
  Player 2 gets the next turn.
:::

::: exercise
This one is just for fun: think about ways to spruce up this basic gameplay loop.
If you end up with something fun, get it published and donate some of the proceeds to the cause of mathematical linguistics.
:::

## Compact representations for the transduction game

For any given gaming session, we can represent its rules of all players very compactly in the form of a table.
For *n* players, the table will have *n* rows and *n+2* columns. An entry like, say, *a:b* in row 2 and column 3 means that if player 2 draws input token *a*, the should place output token *b*, after which it is player 3's turn.
A cell may have multiple entries like *a:b* if the rules for player 2 have multiple cases that result in player 3 getting the next turn.
The last two columns track whether a player is initial and/or final.


::: example
The rules for John and Mary's gaming session can be represented as the following table:

|              |                                    |                              |             |           |
| --:          | :-:                                | :-:                          | :-:         | :-:       |
|              | **Player 1**                       | **Player 2**                 | **Initial** | **Final** |
| **Player 1** | spade:club-club                    | heart:diamond, spade:nothing | No          | No        |
| **Player 2** | heart:heart, spade:heart           | nothing:club                 | Yes         | Yes       |

:::

::: exercise
Expand this table so that it also includes the special power of player 1 from the exercise above (instead of drawing an input token, place a diamond and player 2 gets the next turn).
:::

Tables are nice and all, but humans typically need something more visual in order to fully take in all the information.
We can use a graph format where each player is a circled node.
Nodes are connected by arrows (or **directed edges**) that are labeled with expressions like *a:b* to indicate that if the player where the arrow originates draws an *a* and places a *b*, the player where the arrow ends gets the next turn.
In addition, an arrow from the special label *Start* to a player indicates that this is an initial player, and every final player's node has an outgoing arrow labeled {{{R}}}:nothing.

::: example
The rules for the game played by John and Mary correspond to the following graph.
 
~~~ {.include-tikz size=mid}
game.tikz
~~~

We have two circles, one for player 1 and one for player 2.
The special label *Start* is connected to player 1 but not player 2, marking the former as an initial player.
Player 1 also has an outgoing arrow labeled {{{R}}}:nothing, which indicates that it is a final player.
Besides this special arrow, there are four more:

1. An arrow from player 1 back to itself, labeled *spade:club-club*.
   This corresponds to the cell in row 1 and column 1 of the table above.
1. Another arrow goes from player 1 to player 2 and is labeled with *heart:diamond* and *spade:nothing*.
   This is the counterpart for the cell in row 1 and column 2.
1. An arrow from player 2 back to itself, labeled *nothing:club*.
   This is player 2's special power to place a club without drawing from the input token bag.
1. Finally, an arrow connects player 2 to player 1, and its labels are *heart:heart* and *spade:heart*.
   This matches the cell in row 2 and cell 1 of the table.
:::

::: exercise
How would you modify the figure above so that it also includes the special power of player 1 from the previous exercise (instead of drawing an input token, place a diamond and player 2 gets the next turn)?
:::

And believe it or not, this is all you need to know to grog finite-state transducers.

## Recap

- Finite-state transducers can be regarded as a particular (and somewhat boring) game.
- There are finitely many players: *Player 1*, *Player 2*, and so on.
  Players may be initial players, final players, neither, or both.
- Each player has a finite set of rules of the form "if you draw this input token, then place these output tokens (or possibly none at all), and *Player n* gets the next turn".
  Some players may get special powers that allow them to place output tokens without drawing an input token.
- The game stops when a player draws the input token {{{R}}}.
  If that player is a final player, you all win and get to keep the tokens on the output tray as your victory string.
  Otherwise, you all lose.
- Given a specific set of players with specific rules assigned to each one of them, we can represent the game more compactly as a table or as a graph.
