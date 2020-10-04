# Nim

An AI that teaches itself to play Nim through reinforcement learning. [Watch it in action!](https://youtu.be/htNaL07k5H0)

## Usage

```bash
$ python play.py
Playing training game 1
Playing training game 2
Playing training game 3
...
Playing training game 9999
Playing training game 10000
Done training

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

AI's Turn
AI chose to take 1 from pile 2.
```

## Table of content

- [Nim](#nim)
  - [Usage](#usage)
  - [Table of content](#table-of-content)
  - [Playing the game](#playing-the-game)
  - [Algorithm](#algorithm)
  - [Game representation](#game-representation)
  - [Nim.py](#nimpy)
    - [Nim Class](#nim-class)
    - [NimAI Class](#nimai-class)
    - [Train function](#train-function)
    - [Play function](#play-function)
  - [Play.py](#playpy)
  - [Acknowledgements](#acknowledgements)

## Playing the game

The game begins with some number of piles, each with some number of objects. Players take turns: on a player’s turn, the player removes any non-negative number of objects from any one non-empty pile. Whoever removes the last object loses.

## Algorithm

Instead of creating a strategy for teh AI to follow we'll let the AI learn its own strategy using **reinforcement learning**. Specifically, we'll use Q-learning letting the AI play a number of games against itself and evaluating its performance after each game.

In **Q-learning**, we try to learn a reward value (a number) for every (state, action) pair. An action that loses the game will have a reward of -1, an action that results in the other player losing the game will have a reward of 1, and an action that results in the game continuing has an immediate reward of 0, but will also have some future reward.

> Q(s, a) <- Q(s, a) + alpha * (new value estimate - old value estimate)

## Game representation

A “state” of the Nim game is just the current size of all of the piles. A state, for example, might be `[1, 1, 3, 5]`, representing the state with 1 object in pile 0, 1 object in pile 1, 3 objects in pile 2, and 5 objects in pile 3. An “action” in the Nim game will be a pair of integers `(i, j)`, representing the action of taking j objects from pile i. So the action `(3, 5)` represents the action “from pile 3, take away 5 objects.” Applying that action to the state `[1, 1, 3, 5]` would result in the new state `[1, 1, 3, 0]` (the same state, but with pile 3 now empty).

---

## [Nim.py](nim.py)

### Nim Class

the Nim class defines how a Nim game is played. In the `__init__` function, notice that every Nim game needs to keep track of a list of piles, a current player (0 or 1), and the winner of the game (if one exists). The available_actions function returns a set of all the available actions in a state. For example, `Nim.available_actions([2, 1, 0, 0])` returns the set `{(0, 1), (1, 1), (0, 2)}`, since the three possible actions are to take either 1 or 2 objects from pile 0, or to take 1 object from pile 1.

The remaining functions are used to define the gameplay: the `other_player` function determines who the opponent of a given player is, `switch_player` changes the current player to the opposing player, and `move` performs an action on the current state and switches the current player to the opposing player.

### NimAI Class

Defines our AI that will learn to play Nim. The `__init__` function, we start with an empty `self.q` dictionary. The `self.q` dictionary will keep track of all of the current Q-values learned by our AI by mapping (state, action) pairs to a numerical value.

As an *implementation detail*, though we usually represent state as a list, since lists can’t be used as Python dictionary keys, we’ll instead use a tuple version of the state when getting or setting values in `self.q`. For example, if we wanted to set the Q-value of the state `[0, 0, 0, 2]` and the action `(3, 2)` to `-1`, we would write something like

```python
self.q[(0, 0, 0, 2), (3, 2)] = -1
```

Every NimAI object has an `alpha` and `epsilon` value that will be used for Q-learning and for action selection, respectively.

The `update` function takes as input state `old_state`, an action take in that state action, the resulting state after performing that action `new_state`, and an immediate reward for taking that action reward. The function then performs Q-learning by first getting the current Q-value for the state and action (by calling `get_q_value`), determining the best possible future rewards (by calling `best_future_reward`), and then using both of those values to update the Q-value (by calling `update_q_value`).

Finally, the `choose_action` function selects an action to take in a given state (either greedily, or using the epsilon-greedy algorithm).

### Train function

Train an AI by playing `n` games against itself.

### Play function

Play human game against the AI. `human_player` can be set to 0 or 1 to specify whether human player moves first or second.

## [Play.py](play.py)

Imports the `train` and `play` functions from [nim.py](nim.py), calling `train` specifying how many practice games the AI plays, and then calling `play` passing in the trained AI.

---

## Acknowledgements

`Nim`, `train`, and `play` along with the `init` and `update` methods of the `NimAI` class in [nim.py](nim.py) have already been implemented by the CS50AI staff.
