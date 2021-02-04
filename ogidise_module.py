
import random
import string

class Board:

    pot = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}

    def __init__(self):

        self.pot_1 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_2 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_3 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_4 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_5 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_6 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_7 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_8 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_9 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_10 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_11 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}
        self.pot_12 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' ', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 48: ' '}

        section = []


    def assign_sections(self, first_player, second_player):
        first_player.pot_1 = self.pot_1
        first_player.pot_2 = self.pot_2
        first_player.pot_3 = self.pot_3
        first_player.pot_4 = self.pot_4
        first_player.pot_5 = self.pot_5
        first_player.pot_6 = self.pot_6
        second_player.pot_1 = self.pot_7
        second_player.pot_2 = self.pot_8
        second_player.pot_3 = self.pot_9
        second_player.pot_4 = self.pot_10
        second_player.pot_5 = self.pot_11
        second_player.pot_6 = self.pot_12



class Player:

    # USEFUL DATA
    def __init__(self, name):
        Board.__init__(self)
        # name of player instance
        self.name = name
        # list of stones in player's hands
        self.hand = []
        # total number of stones
        self.total_stones = 0
        # player's pots for stones
        self.pot_1 = None
        self.pot_2 = None
        self.pot_3 = None
        self.pot_4 = None
        self.pot_5 = None
        self.pot_6 = None
        # storage for stones claimed from the opponent
        self.captured_stones = []
        # cllection of player's six pots
        self.section = [self.pot_1, self.pot_2, self.pot_3, self.pot_4, self.pot_5, self.pot_6]


    # METHODS
    def section_stones(self):
        '''
        place all the stones in a player's section in one list (container)
        counts only stones, ignoring whitespaces
        '''
        container = []
        container.extend(list(self.pot_1.values()))
        container.extend(list(self.pot_2.values()))
        container.extend(list(self.pot_3.values()))
        container.extend(list(self.pot_4.values()))
        container.extend(list(self.pot_5.values()))
        container.extend(list(self.pot_6.values()))

        stones = ''
        for i in container:
            if i not in string.ascii_letters:
                continue
            else:
                stones += i
        print(f"{self.name} has {len(stones)} stones in his section")
        return len(stones)

    def pot_stones(self, pot):
        '''
        to get the number of stones in a pot
        '''
        listed = []
        listed.extend(list(pot.values()))
        stones = ''
        for char in listed:
            if char not in string.ascii_letters:
                continue
            else:
                stones += char
        print(f"{self.name} has {len(stones)} in the pot")
        return len(stones)

    def select_pot(self):
        '''
        player selects which of his pots to pick from
        '''
        print(f"{self.name}, which pot do you want to pick from?")
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
            return pick

    def from_pot_to_hand(self, feeder_pot):
        '''
        transfers stones from pot to hand
        and pot becomes empty
        '''
        listed = []
        listed.extend(list(feeder_pot.values()))
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
        print(f"{self.name} hands: {self.hand}")
        return self.hand


    def reset_pot(self, pot):
        '''
        resets a pot's content
        '''
        pot.update(Board.pot)

    def drop_stone(self):
        '''
        player drops from hand one stone at a time
        '''
        try:
            return self.hand.pop(0)
        except IndexError:
            print(f"{self.name} has {len(self.hand)} in his hand")

    def first_empty_key(self, pot):
        '''
        returns the first empty cell in a pot
        '''
        keys = []
        for k,v in pot.items():
            if v == ' ':
                keys.append(k)
            else:
                continue
        print(f"The first available key is at {keys[0]}")
        return keys[0]

    def occupied_keys(self, pot):
        '''
        returns a list of occupied cells in a pot
        '''
        keys = []
        for k,v in pot.items():
            if v == 'O':
                keys.append(k)
            else:
                continue
        print(f"This pot contains {len(keys)} stones at {keys}")
        return keys


    def empty_keys(self, pot):
        '''
        returns the number of empty cells in a pot
        '''
        empty_cells = 0
        for k,v in pot.items():
            if v == ' ':
                empty_cells += 1
            else:
                continue
        print(f"There are {empty_cells} empty cells in the dict")
        return empty_cells

    def pot_fill(self, pot):
        '''
        fill up empty cell in a pot
        '''
        first_key = self.first_empty_key(pot)
        pot[first_key] = 'O'

        second_key = self.first_empty_key(pot)
        pot[second_key] = 'O'

        third_key = self.first_empty_key(pot)
        pot[third_key] = 'O'

        fourth_key = self.first_empty_key(pot)
        pot[fourth_key] = 'O'

    def share_stones(self, *receiving_pots):
        '''
        fill up the first empty cells in the given number of pots
        '''

        # Nothing happens on the board if player's hand is empty
        if len(self.hand) < 1:
            return print(f"No more stones in {self.name}'s hand to drop.\nPlease refill hand from a non-empty pot!")

        # enlisting all the given pots
        pot_list = list(receiving_pots)
        emp_keys_list = []

        if len(self.hand) != len(pot_list):
            return print(f"Error:\n{self.name} is trying to share {len(self.hand)} stones into {len(pot_list)} pots!")

        # determining the first empty keys in each of the pots in the list
        for pot in pot_list:
            emp_keys_list.append(self.first_empty_key(pot))

        # dropping a stone from player's hand into each of the first empty keys of the given pots
        for pot in pot_list:
            for k in emp_keys_list:
                pot[k] = self.drop_stone()
                break


    def play_on(self):
        response = self.quick_check()
        if response:
            pass

    def quick_check(self):
        while True:
            print("\nScreen Pause!")
            val = input("\nPress Enter to continue, or 'e' to exit game:")

            acc_range = ['', 'e', 'exit']
            if val not in acc_range:
                print(f"\n{val} is not valid!")
                continue
            else:
                if val.lower() == '':
                    return True
                elif val.lower() in ['e', 'exit']:
                    return self.exit_play()

    def exit_play(self):
        print(f"{self.name}, thanks for playing!")
        quit()




# FUNCTIONS

def board_view(player1, player2):
    '''
    visual representation of the game board
    both players have opposite sections
    each section has six pots
    each pot can contain the maximum number of stones - 48
    displaying the pots and stones in each section
    '''
    print("\t\t\t\tSECTION A")
    print("  POT 1","      POT 2", "      POT 3", "      POT 4", "      POT 5", "      POT 6")
    print(' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ')
    print('|', player1.pot_1[1], player1.pot_1[2], player1.pot_1[3], player1.pot_1[4], '|', '|', player1.pot_2[1], player1.pot_2[2], player1.pot_2[3], player1.pot_2[4], '|', '|', player1.pot_3[1], player1.pot_3[2], player1.pot_3[3], player1.pot_3[4], '|', '|',  player1.pot_4[1], player1.pot_4[2], player1.pot_4[3], player1.pot_4[4], '|', '|', player1.pot_5[1], player1.pot_5[2], player1.pot_5[3], player1.pot_5[4], '|', '|', player1.pot_6[1], player1.pot_6[2], player1.pot_6[3], player1.pot_6[4], '|')
    print('|', player1.pot_1[5], player1.pot_1[6], player1.pot_1[7], player1.pot_1[8], '|', '|', player1.pot_2[5], player1.pot_2[6], player1.pot_2[7], player1.pot_2[8], '|', '|', player1.pot_3[5], player1.pot_3[6], player1.pot_3[7], player1.pot_3[8], '|', '|', player1.pot_4[5], player1.pot_4[6], player1.pot_4[7], player1.pot_4[8], '|', '|',  player1.pot_5[5], player1.pot_5[6], player1.pot_5[7], player1.pot_5[8], '|', '|', player1.pot_6[5], player1.pot_6[6], player1.pot_6[7], player1.pot_6[8], '|')
    print('|', player1.pot_1[9], player1.pot_1[10], player1.pot_1[11], player1.pot_1[12], '|', '|', player1.pot_2[9], player1.pot_2[10], player1.pot_2[11], player1.pot_2[12], '|', '|', player1.pot_3[9], player1.pot_3[10], player1.pot_3[11], player1.pot_3[12], '|', '|', player1.pot_4[9], player1.pot_4[10], player1.pot_4[11], player1.pot_4[12], '|', '|', player1.pot_5[9], player1.pot_5[10], player1.pot_5[11], player1.pot_5[12], '|', '|', player1.pot_6[9], player1.pot_6[10], player1.pot_6[11], player1.pot_6[12], '|')
    print('|', player1.pot_1[13], player1.pot_1[14], player1.pot_1[15], player1.pot_1[16], '|', '|', player1.pot_2[13], player1.pot_2[14], player1.pot_2[15], player1.pot_2[16], '|', '|', player1.pot_3[13], player1.pot_3[14], player1.pot_3[15], player1.pot_3[16],'|', '|', player1.pot_4[13], player1.pot_4[14], player1.pot_4[15], player1.pot_4[16], '|', '|', player1.pot_5[13], player1.pot_5[14], player1.pot_5[15], player1.pot_5[16], '|', '|', player1.pot_6[13], player1.pot_6[14], player1.pot_6[15], player1.pot_6[16], '|')
    print('|', player1.pot_1[17], player1.pot_1[18], player1.pot_1[19], player1.pot_1[20], '|', '|', player1.pot_2[17], player1.pot_2[18], player1.pot_2[19], player1.pot_2[20], '|', '|', player1.pot_3[17], player1.pot_3[18], player1.pot_3[19], player1.pot_3[20], '|', '|', player1.pot_4[17], player1.pot_4[18], player1.pot_4[19], player1.pot_4[20], '|', '|', player1.pot_5[17], player1.pot_5[18], player1.pot_5[19], player1.pot_5[20], '|', '|', player1.pot_6[17], player1.pot_6[18], player1.pot_6[19], player1.pot_6[20], '|')
    print('|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|')
    print(' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ')
    print('|', player2.pot_1[1], player2.pot_1[2], player2.pot_1[3], player2.pot_1[4], '|', '|', player2.pot_2[1], player2.pot_2[2], player2.pot_2[3], player2.pot_2[4], '|', '|', player2.pot_3[1], player2.pot_3[2], player2.pot_3[3], player2.pot_3[4], '|', '|',  player2.pot_4[1], player2.pot_4[2], player2.pot_4[3], player2.pot_4[4], '|', '|', player2.pot_5[1], player2.pot_5[2], player2.pot_5[3], player2.pot_5[4], '|', '|', player2.pot_6[1], player2.pot_6[2], player2.pot_6[3], player2.pot_6[4], '|')
    print('|', player2.pot_1[5], player2.pot_1[6], player2.pot_1[7], player2.pot_1[8], '|', '|', player2.pot_2[5], player2.pot_2[6], player2.pot_2[7], player2.pot_2[8], '|', '|', player2.pot_3[5], player2.pot_3[6], player2.pot_3[7], player2.pot_3[8], '|', '|', player2.pot_4[5], player2.pot_4[6], player2.pot_4[7], player2.pot_4[8], '|', '|',  player2.pot_5[5], player2.pot_5[6], player2.pot_5[7], player2.pot_5[8], '|', '|', player2.pot_6[5], player2.pot_6[6], player2.pot_6[7], player2.pot_6[8], '|')
    print('|', player2.pot_1[9], player2.pot_1[10], player2.pot_1[11], player2.pot_1[12], '|', '|', player2.pot_2[9], player2.pot_2[10], player2.pot_2[11], player2.pot_2[12], '|', '|', player2.pot_3[9], player2.pot_3[10], player2.pot_3[11], player2.pot_3[12], '|', '|', player2.pot_4[9], player2.pot_4[10], player2.pot_4[11], player2.pot_4[12], '|', '|', player2.pot_5[9], player2.pot_5[10], player2.pot_5[11], player2.pot_5[12], '|', '|', player2.pot_6[9], player2.pot_6[10], player2.pot_6[11], player2.pot_6[12], '|')
    print('|', player2.pot_1[13], player2.pot_1[14], player2.pot_1[15], player2.pot_1[16], '|', '|', player2.pot_2[13], player2.pot_2[14], player2.pot_2[15], player2.pot_2[16], '|', '|', player2.pot_3[13], player2.pot_3[14], player2.pot_3[15], player2.pot_3[16],'|', '|', player2.pot_4[13], player2.pot_4[14], player2.pot_4[15], player2.pot_4[16], '|', '|', player2.pot_5[13], player2.pot_5[14], player2.pot_5[15], player2.pot_5[16], '|', '|', player2.pot_6[13], player2.pot_6[14], player2.pot_6[15], player2.pot_6[16], '|')
    print('|', player2.pot_1[17], player2.pot_1[18], player2.pot_1[19], player2.pot_1[20], '|', '|', player2.pot_2[17], player2.pot_2[18], player2.pot_2[19], player2.pot_2[20], '|', '|', player2.pot_3[17], player2.pot_3[18], player2.pot_3[19], player2.pot_3[20], '|', '|', player2.pot_4[17], player2.pot_4[18], player2.pot_4[19], player2.pot_4[20], '|', '|', player2.pot_5[17], player2.pot_5[18], player2.pot_5[19], player2.pot_5[20], '|', '|', player2.pot_6[17], player2.pot_6[18], player2.pot_6[19], player2.pot_6[20], '|')
    print('|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|')
    print("  POT 1","      POT 2", "      POT 3", "      POT 4", "      POT 5", "      POT 6")
    print("\t\t\t\tSECTION B")



def player_name():
    while True:
        val = input("\n\t\tPlayer Name:   \n\t\t")
        if val.isdigit():
            print("\n\Enter a valid name")
            continue
        return val.upper()
