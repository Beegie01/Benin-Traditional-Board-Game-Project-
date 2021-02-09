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


print("\n""\t"*2, "FILLING GAME BOARD WITH FOUR STONES IN EACH POT\n")

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

GAME_ON = True
while GAME_ON:

    board_view(board, fp, sp)

    ump.play_on()

    # first player's turn
    FIRST_TURN = True
    while FIRST_TURN:

        # first player selects where to begin picking from
        pot_obj = fp.fp_select_pot(board)

        # check if player chose to pick from an empty pot
        EMPTY = fp.check_if_empty(pot_obj)

        # another chance for player to pick from a non-empty pot
        if EMPTY:
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
        CONTINUE_PLAY = board.enforce_ccs(result, fp)

        ump.play_on()

        board_view(board, fp, sp)

        ump.play_on()

        if CONTINUE_PLAY:
            # returns false when player eventually hits an empty pot
            FIRST_TURN = board.continue_playing(fp, fp, sp)

        FIRST_TURN = False

    board_view(board, fp, sp)

    # second player's turn
    SECOND_TURN = True
    while SECOND_TURN:

        # first player selects where to begin picking from
        # first player selects where to begin picking from
        pot_obj = sp.sp_select_pot(board)

        # check if player chose to pick from an empty pot
        EMPTY = sp.check_if_empty(pot_obj)

        # another chance for player to pick from a non-empty pot
        if EMPTY:
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
        CONTINUE_PLAY = board.enforce_ccs(result, sp)

        if CONTINUE_PLAY:

            # returns false when player eventually hits an empty pot
            SECOND_TURN = board.continue_playing(sp, fp, sp)

        SECOND_TURN = False
