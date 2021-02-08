# importing modules from package
from GameModules import board_cls, player_cls

#importing class from modules
from GameModules.board_cls import *
from GameModules.player_cls import *



welc_scrn()

# Board instance created
board = Board()

# two player names taken
first = player_name()

second = player_name()

# umpire instance created
ump = Player("Umpire")

# two player instances created
p1 = Player(first)

p2 = Player(second)

# first player picks head or tail
coin_side = p1.pick_coin_sides()

# umpire tosses coin
starter = ump.game_starter(coin_side, p1, p2)

ump.play_on()

# players are assigned instances whick determine order of turns based on coin toss
if starter == p1.name:
    fp = Player(first)
    sp = Player(second)

else:
    fp = Player(second)
    sp = Player(first)

# players are assigned sides based on coin toss
ump.assign_sections(board, fp, sp)

# visualization of empty game board
board_view(board, fp, sp)

# game speed control
# screen pause
ump.play_on()


print("\n","\t"*2, "FILLING GAME BOARD WITH FOUR STONES IN EACH POT\n")

ump.play_on()
# all 12 pots are filled with stones
ump.pot_fill(fp.pot_1)
ump.pot_fill(fp.pot_2)
ump.pot_fill(fp.pot_3)
ump.pot_fill(fp.pot_4)
ump.pot_fill(fp.pot_5)
ump.pot_fill(fp.pot_6)

ump.pot_fill(sp.pot_1)
ump.pot_fill(sp.pot_2)
ump.pot_fill(sp.pot_3)
ump.pot_fill(sp.pot_4)
ump.pot_fill(sp.pot_5)
ump.pot_fill(sp.pot_6)

game_on = True
while game_on:

    board_view(board, fp, sp)

    ump.play_on()

    # first player's turn
    first_turn = True
    while first_turn:

        # first player selects where to begin picking from
        pot_obj = fp.fp_select_pot(board)

        # check if player chose to pick from an empty pot
        empty = fp.check_if_empty(pot_obj)

        # another chance for player to pick from a non-empty pot
        if empty:
            continue

        # player carries picked stones in their hand
        fp.from_pot_to_hand(pot_obj)

        ump.play_on()

        board_view(board, fp, sp)

        ump.play_on()

        # stones in player's hand gets shared automatically
        board.distribute_stones(fp)

        ump.play_on()

        board_view(board, fp, sp)

        ump.play_on()

        # check the last recipient pot for CLAIM, CONTINUE or STOP
        result = board.ccs_checker(fp, sp)

        ump.play_on()

        # returns true if turn continues
        # returns false if claim occurs or turn stops
        continue_play = board.enforce_ccs(result, fp)

        ump.play_on()

        board_view(board, fp, sp)

        ump.play_on()

        if continue_play:
            # returns false when player eventually hits an empty pot
            first_turn = board.continue_playing(fp, fp, sp)

        first_turn = False

    board_view(board, fp, sp)

    # second player's turn
    second_turn = True
    while second_turn:

        # first player selects where to begin picking from
        # first player selects where to begin picking from
        pot_obj = sp.sp_select_pot(board)

        # check if player chose to pick from an empty pot
        empty = sp.check_if_empty(pot_obj)

        # another chance for player to pick from a non-empty pot
        if empty:
            continue

        # player carries picked stones in their hand
        sp.from_pot_to_hand(pot_obj)

        ump.play_on()

        board_view(board, fp, sp)

        ump.play_on()

        # stones in player's hand gets shared automatically
        board.distribute_stones(sp)

        ump.play_on()

        board_view(board, fp, sp)

        ump.play_on()

        # check the last recipient pot for CLAIM, CONTINUE or STOP
        result = board.ccs_checker(sp, fp)

        ump.play_on()

        # returns true if turn continues
        # returns false if claim occurs or turn stops
        continue_play = board.enforce_ccs(result, sp)

        if continue_play:

            # returns false when player eventually hits an empty pot
            second_turn = board.continue_playing(sp, fp, sp)

        second_turn = False
