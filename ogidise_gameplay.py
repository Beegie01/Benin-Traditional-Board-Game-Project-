import ogidise_module
from ogidise_module import *

print("*****WELCOME*****")
print("*******TO********")
print("*****OGIDISE*****")
print("****BOARD GAME****")
print("**FEBRUARY, 2021**")

board = Board()

first = player_name()

second = player_name()

player1 = Player(first)

player2 = Player(second)

board_view(player1, player2)

player1.play_on()
