# setGame
Run with:
$ python3 setGame.py

A game for one or two players.

Player(s) chose a number of elements, N. A set is created with elements: { 1, 2, ... N }. The powerset of that set is computed and assigned to S. 

Ex: For N = 3, S = { {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3} }

P is initialized to S.

Players take turns picking a subset, s, of P. P is updated by removing all sets that are supersets of s (including s). Players may not chose {} or S itself. 

Ex: If P = { {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3} } and player 1 choses {1} P will be updated as { {}, {2}, {3}, {2,3} } removing any sets that contain the element 1.

The winner is the last to draw a/some non empty set(s) from P. The loser has no move because P = { {} } and they cannot draw the empty set. 

Conjecture: For any N, regardless of player 1's strategy, there is always a strategy for a player 2 win.
