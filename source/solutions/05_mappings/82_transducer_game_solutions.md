---
pagetitle: >-
    Finite-state transductions as a game (Solutions)
---

# Finite-state transductions as a game (Solutions)

::: exercise
How would the game have ended if Mary had decided to go with option 2 instead: place nothing and player 2 gets the next turn.
What would have been the sequence on the output token tray, assuming that John does not use his special power at all?

::: solution
John has placed a heart on the output token tray and given the next turn to Mary.
She draws spade and decides to go with option 2, placing nothing and giving the turn to John.
So now it is John who draws heart, once more placing heart and giving the next turn to Mary.
Mary draws {{{R}}}.
Mary is not a final player, and the game is lost.
Since the game is lost, the output token tray is cleared and no output is produced.
If the game had been won, the output token tray would have been *heart-heart*.
:::

:::

::: exercise
This continues the previous exercise.
What if Mary's rule sheet also contained the special power below?
Would there be a way to use this rule and finish the game?

- **Special power:** Instead of drawing an input token, place a diamond.
  Player 2 gets the next turn.

::: solution
Suppose that instead of drawing from the bag, which will result in {{{R}}}, Mary uses her special power.
She places diamond and John gets the next turn.
John draws {{{R}}}, but this is okay because he's a final player.
The sequence of tokens on the output token tray is *heart-heart-diamond*.
:::
:::

::: exercise
This one is just for fun: think about ways to spruce up this basic gameplay loop.
If you end up with something fun, get it published and donate some of the proceeds to the cause of mathematical linguistics.

::: solution
Modern board games have tons of intricate mechanics, e.g. bidding, action selection, deck building, or worker placement.
The problem with the current game is that there isn't much strategy because of the random draw of input tokens.
It's more like a game for toddlers, teaching turn-taking and the how to follow instructions.
In order to make this a real game, there needs to be tension, conflicting goals, and uncertainty.

Here is my proposal, which still needs playtesting:
The game stays exactly the way described above, but there are multiple rounds.
In the example above, Mary and John played only one round.
After drawing {{{R}}}, they tally up their score so far, then play again.
At the end of, say, 5 rounds, they check their total score.
The goal is to get as high a score as possible.
But here's the twist: the players do not know each other's rules and powers, and they may not talk to each other.
Now this is a hidden information game where you have to learn each other's rules on the fly over multiple rounds, and you need to be a well-oiled machine to get high scores.

It's still a pretty dry game --- no witty banter, no take-that moments, no victory condition beyond beating your own high score --- but at least it's an actual game now.
Let's try to make it a bit juicier: secret player objectives!
Rather then going for a single high score for all the players, every player has a list of secret objectives that they need to reach over the course of the game, e.g. "at the end of the round, gain 2 victory points if the output token tray contains the sequence heart-heart-heart".
At the end of the game, the player with the most victory points wins.
Now this is a semi-coop design: every player is pursuing their own goals, but there's still the shared goal of winning each round because nobody can meet their objectives with an empty output token tray (however, depending on whether players know each other's victory points, there might be a strategy to deliberately sabotage a round in order to stay in the lead).
It would be difficult to balance the secret objectives and special powers, but a good designer could make it work.
And the outcome would be something that I'd actually like to play!
:::

:::

::: exercise
Expand this table so that it also includes the special power of player 1 from the exercise above (instead of drawing an input token, place a diamond and player 2 gets the next turn).

::: solution

We have to add *nothing:diamond* to the cell in the row for Player 1 and the column for Player 2.

|              |                                    |                                               |             |           |
| --:          | :-:                                | :-:                                           | :-:         | :-:       |
|              | **Player 1**                       | **Player 2**                                  | **Initial** | **Final** |
| **Player 1** | spade:club-club                    | heart:diamond, spade:nothing, nothing:diamond | No          | No        |
| **Player 2** | heart:heart, spade:heart           | nothing:club                                  | Yes         | Yes       |

:::
:::

::: exercise
How would you modify the figure above so that it also includes the special power of player 1 from the previous exercise (instead of drawing an input token, place a diamond and player 2 gets the next turn)?

::: solution
We would have to add *nothing:diamond* as a third label to the arrow from player 1 to player 2.

~~~ {.include-tikz size=mid}
game_poweradded.tikz
~~~
:::

:::
