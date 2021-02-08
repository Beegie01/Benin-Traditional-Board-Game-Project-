# importing from a standard modules
import random

# importing from modules
from . import board_cls
from .board_cls import Board

class Player(Board):

    # USEFUL DATA
    def __init__(self, name):

        Board.__init__(self)

        # name of player instance
        self.name = name.upper()

        # list of stones in player's hands
        self.hand = []

        # total number of stones on player's side of the board
        self.board_stones = 0

        # player's pots for stones
        self.pot_1 = None
        self.pot_2 = None
        self.pot_3 = None
        self.pot_4 = None
        self.pot_5 = None
        self.pot_6 = None

        self.board_side = None

        # storage for stones claimed from the opponent
        self.captured_stones = []

        # record of last pot player picked from
        self.last_picked_pot = None

        # record of last recipient pot of player's stone
        self.last_recipient_pot = None


    # METHODS
    def pick_coin_sides(self):

        print(f"\n\n{self.name} choose HEAD or TAIL")
        acc_range = ['head', 'h', 'tail', 't']
        pick = None
        while pick not in acc_range:
            val = input("\nEnter H for head, or T for tail:\n")

            try:
                pick = val.lower()
            except:
                print(f"{val} is invalid!")
                continue

            if pick not in acc_range:
                print(f"{pick} is out of range!")
                continue

            if pick == 'h' or pick == 'head':
                print(f"{self.name} picks HEAD")
                return 'HEAD'
            else:
                print(f"{self.name} picks TAIL")
                return 'TAIL'

    def coin_toss(self):
        coin = ['HEAD', 'TAIL']
        return random.choice(coin)

    def game_starter(self, picked_side, player1, player2):

        toss_result = self.coin_toss()

        print(f"\n{self.name} FLIPS COIN!\n{toss_result} emerges!")

        if picked_side == toss_result:
            print(f"{player1.name} STARTS!")
            return player1.name
        else:
            print(f"{player2.name} STARTS!")
            return player2.name

    def assign_sections(self, board, first_player, second_player):
        first_player.pot_1 = board.pot_1
        first_player.pot_2 = board.pot_2
        first_player.pot_3 = board.pot_3
        first_player.pot_4 = board.pot_4
        first_player.pot_5 = board.pot_5
        first_player.pot_6 = board.pot_6
        first_player.board_side = board.pot_1[3]
        second_player.pot_1 = board.pot_12
        second_player.pot_2 = board.pot_11
        second_player.pot_3 = board.pot_10
        second_player.pot_4 = board.pot_9
        second_player.pot_5 = board.pot_8
        second_player.pot_6 = board.pot_7
        second_player.board_side = board.pot_7[3]

    def pot_fill(self, pot):
        '''
        input is pot object
        fill up empty cell in a pot
        '''
        first_key = self.first_empty_key(pot)
        pot[1][first_key] = 'O'

        second_key = self.first_empty_key(pot)
        pot[1][second_key] = 'O'

        third_key = self.first_empty_key(pot)
        pot[1][third_key] = 'O'

        fourth_key = self.first_empty_key(pot)
        pot[1][fourth_key] = 'O'

    def first_empty_key(self, pot):
        '''
        input is a pot_obj
        returns the first empty cell in a pot
        '''
        keys = []
        for k,v in pot[1].items():
            if v == ' ':
                keys.append(k)
            else:
                continue
        return keys[0]


    def fp_prompt_pot_no(self):
        '''
        first player selects which of his pots to pick from
        '''
        print(f"{self.name} TURN:\n\nChoose pot to pick from?")
        acc_range = range(1,7)
        pick = -1

        while pick not in acc_range:
            val = input("Select a non-empty pot between 1-6:\n")
            try:
                pick = int(val)
            except:
                print(f"{val} is invalid!")
                continue
            if pick not in acc_range:
                print(f"{pick} is out of range!")
                continue
            break
        return pick

    def fp_select_pot(self, board):
        '''
        converts first player's pick (1-6) into their corresponding pot instance
        outputs the pot_name, pot_object and number
        '''

        pick = self.fp_prompt_pot_no()

        if pick == board.pot_1[2]:
            return board.pot_1
        elif pick == board.pot_2[2]:
            return board.pot_2
        elif pick == board.pot_3[2]:
            return board.pot_3
        elif pick == board.pot_4[2]:
            return board.pot_4
        elif pick == board.pot_5[2]:
            return board.pot_5
        elif pick == board.pot_6[2]:
            return board.pot_6

    def sp_prompt_pot_no(self):
        '''
        second player selects which of his pots to pick from
        '''
        print(f"{self.name} TURN:\n\nChoose pot to pick from?")
        acc_range = range(7,13)
        pick = -1

        while pick not in acc_range:
            val = input("Select a non-empty pot between 7-12:\n")
            try:
                pick = int(val)
            except:
                print(f"{val} is invalid!")
                continue
            if pick not in acc_range:
                print(f"{pick} is out of range!")
                continue
            break
        return pick

    def sp_select_pot(self, board):
        '''
        converts second player's pick (7-12) into their corresponding pot instance
        outputs the pot_name, pot_object and number
        '''

        pick = self.sp_prompt_pot_no()

        if pick == board.pot_12[2]:
            return board.pot_12
        elif pick == board.pot_11[2]:
            return board.pot_11
        elif pick == board.pot_10[2]:
            return board.pot_10
        elif pick == board.pot_9[2]:
            return board.pot_9
        elif pick == board.pot_8[2]:
            return board.pot_8
        elif pick == board.pot_7[2]:
            return board.pot_7

    def check_if_empty(self, chosen_pot):
        '''
        check to see if pot is empty
        '''

        ok_count = self.occupied_keys(chosen_pot)
        if ok_count < 1:
            print(f"\n\n{self.name} IS TRYING TO PICK FROM AN EMPTY {chosen_pot[0]}")
            return True
        return False

    def occupied_keys(self, pot):
        '''
        input is a pot_object
        returns a list of occupied cells in a pot
        '''
        keys = []
        for k,v in pot[1].items():
            if v == 'O':
                keys.append(k)
            else:
                continue
        print("\n"*2,f"{pot[0].upper()} contains {len(keys)} stones")
        return len(keys)


    def section_stones(self):
        '''
        place all the stones in a player's section in one list (container)
        counts only stones, ignoring whitespaces
        '''
        container = []
        container.extend(list(self.pot_1[1].values()))
        container.extend(list(self.pot_2[1].values()))
        container.extend(list(self.pot_3[1].values()))
        container.extend(list(self.pot_4[1].values()))
        container.extend(list(self.pot_5[1].values()))
        container.extend(list(self.pot_6[1].values()))


        stones = ''
        for char in container:
            if char != 'O':
                continue
            else:
                stones += char
        self.board_stones = len(stones)
        return len(stones)

    def from_pot_to_hand(self, feeder_pot):
        '''
        input is board pot object
        transfers stones from pot to hand
        and pot becomes empty
        '''

        listed = []
        listed.extend(list(feeder_pot[1].values()))
        stones = []
        string = ''
        for char in listed:
            # Only stones get picked by hands
            if char != 'O':
                continue
            else:
                stones += char

        self.hand += stones
        self.reset_pot(feeder_pot)
        self.last_picked_pot = feeder_pot[0]
        return print(f"\n{self.name} picked from {feeder_pot[0]}")


    def reset_pot(self, pot):
        '''
        resets a pot's content
        '''
        pot[1].update(Board.pot)

    def drop_stone(self):
        '''
        player drops from hand one stone at a time
        '''
        try:
            return self.hand.pop(0)
        except IndexError:
            print(f"\n{self.name} has {len(self.hand)} in his hand")


    def play_on(self):
        response = self.quick_check()
        if response:
            pass

    def quick_check(self):
        while True:
            val = input("\nPress Enter to continue, or 'e' to exit game:\n")

            acc_range = ['', 'e', 'exit']
            if val.lower() not in acc_range:
                print(f"\n{val} is not valid!")
                continue
            else:
                if val.lower() == '':
                    '\n'
                    return True
                elif val.lower() in ['e', 'exit']:
                    return self.exit_play()

    def exit_play(self):
        print(f"\n\nThanks for playing!")
        quit()
