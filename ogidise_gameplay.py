# import sys

# pkg = 'C:\\Users\\welcome\\Desktop\\MyFuncs'

# if pkg not in sys.path:
#     sys.path.append(pkg)

from fave_app_funcs import generate_password, password_inp, ask_to_save, play_on, exit_play, game_mode

#importing classes and functions from modules
from GameModules.board_cls import Board
from GameModules.player_cls import Player
from GameModules.ogidise_funcs import board_view, welc_scrn, player_name, save_progress, retrieve


welc_scrn()

# Board instance created
board = Board()

# umpire instance created
ump = Player("Umpire")

START = True
while START:

    # start a new game or continue playing saved game
    mode = game_mode()

    # when continue
    if mode == 'c':

        contd_attr, fp_attr, sp_attr, FIRST_TURN = retrieve()

        # When incorrect password is given
        if contd_attr == '':
            continue

        fp, sp = Player(fp_attr['name']), Player(sp_attr['name'])

        board.__dict__, fp.__dict__, sp.__dict__ = contd_attr, fp_attr, sp_attr

        GAME_ON = True
        while GAME_ON:

            board_view(board, fp, sp)

            play_on()

            while FIRST_TURN:

                # first player selects where to begin picking from
                pot_obj = fp.fp_select_pot(board)

                # check if player chose to pick from an empty pot
                POT_IS_EMPTY = fp.check_if_empty(pot_obj)

                # another chance for player to pick from a non-empty pot
                if POT_IS_EMPTY:
                    continue

                # player carries picked stones in their hand
                fp.from_pot_to_hand(pot_obj)

                play_on()

                board_view(board, fp, sp)

                play_on()

                # stones in player's hand gets shared automatically accross board
                board.distribute_stones(fp)

                play_on()

                board_view(board, fp, sp)

                play_on()

                # check the last recipient pot for CLAIM, CONTINUE or STOP
                CLAIM_CONT_STOP = board.ccs_checker(fp, sp)

                # returns true if turn continues
                # returns false if claim occurs or turn stops
                CONTINUE_PLAY = board.enforce_ccs(CLAIM_CONT_STOP, fp)

                play_on()

                board_view(board, fp, sp)

                play_on()

                if CONTINUE_PLAY:
                    # returns false when player eventually hits an empty pot
                    FIRST_TURN = board.continue_playing(fp, fp, sp)

                FIRST_TURN = False

            board_view(board, fp, sp)

            # check for exit
            if exit_play():
                # saving game progress
                if ask_to_save():
                    save_progress(board_obj=board, first_player_obj=fp, second_player_obj=sp, FIRST_TURN=False)
                print("\n\nEXITING GAME...\nThanks For Playing <<<OGIDISE 2021>>>!")
                quit()

            # second player's turn
            SECOND_TURN = True
            while SECOND_TURN:

                # first player selects where to begin picking from
                # first player selects where to begin picking from
                pot_obj = sp.sp_select_pot(board)

                # check if player chose to pick from an empty pot
                POT_IS_EMPTY = sp.check_if_empty(pot_obj)

                # another chance for player to pick from a non-empty pot
                if POT_IS_EMPTY:
                    continue

                # player carries picked stones in their hand
                sp.from_pot_to_hand(pot_obj)

                play_on()

                board_view(board, fp, sp)

                play_on()

                # stones in player's hand gets shared automatically
                board.distribute_stones(sp)

                play_on()

                board_view(board, fp, sp)

                play_on()

                # check the last recipient pot for CLAIM, CONTINUE or STOP
                CLAIM_CONT_STOP = board.ccs_checker(sp, fp)

                # returns true if turn continues
                # returns false if claim occurs or turn stops
                CONTINUE_PLAY = board.enforce_ccs(CLAIM_CONT_STOP, sp)

                if CONTINUE_PLAY:

                    # returns false when player eventually hits an empty pot
                    SECOND_TURN = board.continue_playing(sp, fp, sp)

                SECOND_TURN, FIRST_TURN = False, True

                # check for exit
                if exit_play():
                    # saving game progress
                    if ask_to_save():
                        save_progress(board_obj=board, first_player_obj=fp, second_player_obj=sp, FIRST_TURN=True)
                    print("\n\nEXITING GAME...\nThanks For Playing <<<OGIDISE 2021>>>!")
                    quit()



    # start playing new game
    else:

        # two player names taken
        name1 = player_name()

        name2 = player_name()

        # two player instances created
        p1 = Player(name1)

        p2 = Player(name2)

        # first player picks head or tail
        coin_side = p1.pick_coin_sides()

        # umpire tosses coin
        starter = ump.game_starter(coin_side, p1, p2)

        play_on()

        # players are assigned instances whick determine order of turns based on coin toss
        if starter == p1.name:
            fp = Player(name1)
            sp = Player(name2)

        else:
            fp = Player(name2)
            sp = Player(name1)

        # players are assigned sides based on coin toss
        ump.assign_sections(board, fp, sp)

        # visualization of empty game board
        board_view(board, fp, sp)

        # game speed control
        # screen pause
        play_on()

        print("\n""\t"*2, "FILLING GAME BOARD WITH FOUR STONES IN EACH POT\n")

        play_on()

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

            play_on()

            # first player's turn
            FIRST_TURN = True
            while FIRST_TURN:

                # first player selects where to begin picking from
                pot_obj = fp.fp_select_pot(board)

                # check if player chose to pick from an empty pot
                POT_IS_EMPTY = fp.check_if_empty(pot_obj)

                # another chance for player to pick from a non-empty pot
                if POT_IS_EMPTY:
                    continue

                # player carries picked stones in their hand
                fp.from_pot_to_hand(pot_obj)

                play_on()

                board_view(board, fp, sp)

                play_on()

                # stones in player's hand gets shared automatically accross board
                board.distribute_stones(fp)

                play_on()

                board_view(board, fp, sp)

                play_on()

                # check the last recipient pot for CLAIM, CONTINUE or STOP
                CLAIM_CONT_STOP = board.ccs_checker(fp, sp)

                # returns true if turn continues
                # returns false if claim occurs or turn stops
                CONTINUE_PLAY = board.enforce_ccs(CLAIM_CONT_STOP, fp)

                play_on()

                board_view(board, fp, sp)

                play_on()

                if CONTINUE_PLAY:
                    # returns false when player eventually hits an empty pot
                    FIRST_TURN = board.continue_playing(fp, fp, sp)

                FIRST_TURN = False

            board_view(board, fp, sp)

            # check for exit
            if exit_play():
                # saving game progress
                if ask_to_save():
                    save_progress(board_obj=board, first_player_obj=fp, second_player_obj=sp, FIRST_TURN=False)
                print("\n\nEXITING GAME...\nThanks For Playing <<<OGIDISE 2021>>>!")
                quit()

            # second player's turn
            SECOND_TURN = True
            while SECOND_TURN:

                # first player selects where to begin picking from
                # first player selects where to begin picking from
                pot_obj = sp.sp_select_pot(board)

                # check if player chose to pick from an empty pot
                POT_IS_EMPTY = sp.check_if_empty(pot_obj)

                # another chance for player to pick from a non-empty pot
                if POT_IS_EMPTY:
                    continue

                # player carries picked stones in their hand
                sp.from_pot_to_hand(pot_obj)

                play_on()

                board_view(board, fp, sp)

                play_on()

                # stones in player's hand gets shared automatically
                board.distribute_stones(sp)

                play_on()

                board_view(board, fp, sp)

                play_on()

                # check the last recipient pot for CLAIM, CONTINUE or STOP
                CLAIM_CONT_STOP = board.ccs_checker(sp, fp)

                # returns true if turn continues
                # returns false if claim occurs or turn stops
                CONTINUE_PLAY = board.enforce_ccs(CLAIM_CONT_STOP, sp)

                if CONTINUE_PLAY:

                    # returns false when player eventually hits an empty pot
                    SECOND_TURN = board.continue_playing(sp, fp, sp)

                SECOND_TURN = False

                # check for exit
                if exit_play():
                    # saving game progress
                    if ask_to_save():
                        save_progress(board_obj=board, first_player_obj=fp, second_player_obj=sp, FIRST_TURN=True)
                    print("\n\nEXITING GAME...\nThanks For Playing <<<OGIDISE 2021>>>!")
                    quit()
