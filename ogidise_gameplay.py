import ogidise_module
from ogidise_module import *

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

game_on = True
while game_on:

    print("\n","\t"*2, "BOARD FILL-UP")
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

    board_view(board, fp, sp)

    ump.play_on()

    # first_player turn
    first_turn = True
    while first_turn:

        # first player selects where to begin picking from
        pot_name, picked_pot, pot_no = fp.fp_select_pot()

        # check if player chose to pick from an empty pot
        empty = fp.check_if_empty(picked_pot)

        # another chance for player to pick from a non-empty pot
        if empty:
            continue

        # player carries picked stones in their hand
        fp.from_pot_to_hand(picked_pot)

        board_view(board, fp, sp)

        ump.play_on()

        # stones in player's hand gets shared automatically
        board.distribute_stones(fp)

        board_view(board, fp, sp)

        ump.play_on()

        '''
        picked_pot, pot_name = sp.sp_select_pot()

        empty = sp.check_if_empty(picked_pot)

        if empty:
            continue
        sp.from_pot_to_hand(picked_pot)

        board.board_view(fp, sp)

        ump.play_on()
        '''
