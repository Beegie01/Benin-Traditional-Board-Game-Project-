AN INDEPENDENT PYTHON PROJECT

My Simulation of A Traditional Board Game - *OGIDISE*

Here, I simulated a traditional board game that I once played growing up in Benin City, called 'Ogidise'. The game is a competition between two players (opponents) as they try to claim as many of the opponent's stones as possible. The board consists of two sides with 6 holes/pots each, making a total of 12 holes/pots. Each pot is meant to accommodate stones, and there is a total of 48 stones in play. Each side is assigned to a player based on a coin flip. 

THE GAME:

PICK: when a player transfers the content of a pot to their hand

CYCLE OF DROP: while dropping stones, player drops one stone at a time going from pot 1 to pot 12 and if they still have stones after reaching 12, then they should go back to pot 1 and restart the cycle.

1. COIN TOSS: to determine first turn and assignment of board side to each player

2 BOARD FILL-UP: At the beginning, each pot (12) have 4 stones, and each has 24 stones on their side

3. FIRST PLAYER TURN: The first player enters a number corresponding to the pot that they want to pick from ranging between 1 and 6 or 7 and 12 depending on their side of the board. Then, player drops stones into the next series of pots one at a time from their hand, moving in a clockwise direction (from 1 to 12). This is done across the board until their hand is empty of stones.

CHANGE OF PLAYER TURN: If the last stone falls into an empty pot, then the current player must stop for the next player's turn to begin. Else (if the last stone was dropped into a non-empty pot), then the current player must pick up all the stones in that last pot and continue dropping one stone at a time into each of the following pot while maintaining the cycle of drop.

CLAIM: If the last stone droppend from hand was into any pot on the opponent's side containing three stones thereby making it four stones, then the player picks up all four stones and transfers them into their reservoir pot thereby reducing the total number of stones in play by four. After each claim, turn switches to next player. 

WINNER:
Generally, the player in possession of a higher number of stones (including the stones in their reserve) wins the game. An undisputable winner emerges when a player succeeds in CLAIMING more stones than the opponent by the time the total number of stones still in play gets to 16.
