import random
import string
import colorama
from colorama import init, Fore, Back, Style
init()

class Board:

    pot = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '}

    def __init__(self):
        # pos [0: name, 1: dict, 2: number]
        self.pot_1 = ['pot_1',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      1,
                      'side_A']
        self.pot_2 = ['pot_2',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      2,
                      'side_A']
        self.pot_3 = ['pot_3',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      3,
                      'side_A']
        self.pot_4 = ['pot_4',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      4,
                      'side_A']
        self.pot_5 = ['pot_5',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      5,
                      'side_A']
        self.pot_6 = ['pot_6',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      6,
                      'side_A']
        self.pot_7 = ['pot_7',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      7,
                      'side_B']
        self.pot_8 = ['pot_8',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      8,
                      'side_B']
        self.pot_9 = ['pot_9',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      9,
                      'side_B']
        self.pot_10 = ['pot_10',
                       {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                       10,
                       'side_B']
        self.pot_11 = ['pot_11',
                       {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                       11,
                       'side_B']
        self.pot_12 = ['pot_12',
                       {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                       12,
                       'side_B']


    def pot_stones(self, pot):
        '''
        input is pot obj
        to get the number of stones in a pot
        '''

        listed = []
        listed.extend(list(pot[1].values()))
        stones = ''

        for char in listed:
            if char != 'O':
                continue
            else:
                stones += char
        print(f"There are {len(stones)} stones in {pot[0]}")
        return len(stones)

    def get_pot_from_no(self, pot_no):
        '''
        return corresponding pot (name, dict) from pot no
        '''
        if pot_no == self.pot_1[2]:
            return self.pot_1[0], self.pot_1[1]
        elif pot_no == self.pot_2[2]:
            return self.pot_2[0], self.pot_2[1]
        elif pot_no == self.pot_3[2]:
            return self.pot_3[0], self.pot_3[1]
        elif pot_no == self.pot_4[2]:
            return self.pot_4[0], self.pot_4[1]
        elif pot_no == self.pot_5[2]:
            return self.pot_5[0], self.pot_5[1]
        elif pot_no == self.pot_6[2]:
            return self.pot_6[0], self.pot_6[1]
        elif pot_no == self.pot_7[2]:
            return self.pot_7[0], self.pot_7[1]
        elif pot_no == self.pot_8[2]:
            return self.pot_8[0], self.pot_8[1]
        elif pot_no == self.pot_9[2]:
            return self.pot_9[0], self.pot_9[1]
        elif pot_no == self.pot_10[2]:
            return self.pot_10[0], self.pot_10[1]
        elif pot_no == self.pot_11[2]:
            return self.pot_11[0], self.pot_11[1]
        elif pot_no == self.pot_12[2]:
            return self.pot_12[0], self.pot_12[1]

    def get_pot_from_name(self, pot_name):
        '''
        return corresponding pot (dict, no) from pot name
        '''
        if pot_name == self.pot_1[0]:
            return self.pot_1[1], self.pot_1[2]
        elif pot_name == self.pot_2[0]:
            return self.pot_2[1], self.pot_2[2]
        elif pot_name == self.pot_3[0]:
            return self.pot_3[1], self.pot_3[2]
        elif pot_name == self.pot_4[0]:
            return self.pot_4[1], self.pot_4[2]
        elif pot_name == self.pot_5[0]:
            return self.pot_5[1], self.pot_5[2]
        elif pot_name == self.pot_6[0]:
            return self.pot_6[1], self.pot_6[2]
        elif pot_name == self.pot_7[0]:
            return self.pot_7[1], self.pot_7[2]
        elif pot_name == self.pot_8[0]:
            return self.pot_8[1], self.pot_8[2]
        elif pot_name == self.pot_9[0]:
            return self.pot_9[1], self.pot_9[2]
        elif pot_name == self.pot_10[0]:
            return self.pot_10[1], self.pot_10[2]
        elif pot_name == self.pot_11[0]:
            return self.pot_11[1], self.pot_11[2]
        elif pot_name == self.pot_12[0]:
            return self.pot_12[1], self.pot_12[2]

    def calc_board_stones(self, current_player, next_player):
        '''
        inputs are current and next player instances
        records the total number
        '''
        board_stones = current_player.section_stones() + next_player.section_stones()
        return board_stones

    def distribute_stones(self, current_player):
        '''
        immediately after player picks stones
        use the pot name from which the current player last picked
        to determine movement/direction of stone spread across game board
        assigns new value to player's last recipient pot attribute
        '''
        steps = len(current_player.hand)

        # if player picked from pot 1
        if current_player.last_picked_pot == self.pot_1[0]:
            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0],
            self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0],
            self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0],
            self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:

                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue

         # if player picked from pot 2
        elif current_player.last_picked_pot == self.pot_2[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0],
            self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0],
            self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0],
            self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue


        # if player picked from pot 3
        elif current_player.last_picked_pot == self.pot_3[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0],
            self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0],
            self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0],
            self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue

        # if player picked from pot 4
        elif current_player.last_picked_pot == self.pot_4[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0],
            self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0],
            self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0],
            self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue


        # if player picked from pot 5
        elif current_player.last_picked_pot == self.pot_5[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0],
            self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0],
            self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0],
            self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue

        # if player picked from pot 6
        elif current_player.last_picked_pot == self.pot_6[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0],
            self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0],
            self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0],
            self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue

        # if player picked from pot 7
        elif current_player.last_picked_pot == self.pot_7[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0],
            self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0],
            self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0],
            self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue

        # if player picked from pot 8
        elif current_player.last_picked_pot == self.pot_8[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0],
            self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0],
            self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0],
            self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue

        # if player picked from pot 9
        elif current_player.last_picked_pot == self.pot_9[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0],
            self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0],
            self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0],
            self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue

        # if player picked from pot 10
        elif current_player.last_picked_pot == self.pot_10[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0],
            self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0],
            self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0],
            self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue

        # if player picked from pot 11
        elif current_player.last_picked_pot == self.pot_11[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0],
            self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0],
            self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0],
            self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue

        # if player picked from pot 12
        elif current_player.last_picked_pot == self.pot_12[0]:

            # list of all board pot names in the right order based on last picked pot
            pot_name_seq = [self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0],
            self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0],
            self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0],
            self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0]]

            # shortlisting of the pots into which the player can fill up
            # based on the number of stones the player has
            use_name = pot_name_seq[:steps]
            print(f"\n\n{current_player.name} picked from: {current_player.last_picked_pot}\nMove Steps: {use_name}\nNext Stop: {use_name[-1]}")

            # storage of last pot name from shortlisted pot names player's last recipient pot
            current_player.last_recipient_pot = use_name[-1]

            # fill up each available pot cell based on the number of stones in hand
            for pot_name in use_name:
                if pot_name == self.pot_1[0]:
                    fk = current_player.first_empty_key(self.pot_1)
                    self.pot_1[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_2[0]:
                    fk = current_player.first_empty_key(self.pot_2)
                    self.pot_2[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_3[0]:
                    fk = current_player.first_empty_key(self.pot_3)
                    self.pot_3[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_4[0]:
                    fk = current_player.first_empty_key(self.pot_4)
                    self.pot_4[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_5[0]:
                    fk = current_player.first_empty_key(self.pot_5)
                    self.pot_5[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_6[0]:
                    fk = current_player.first_empty_key(self.pot_6)
                    self.pot_6[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_7[0]:
                    fk = current_player.first_empty_key(self.pot_7)
                    self.pot_7[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_8[0]:
                    fk = current_player.first_empty_key(self.pot_8)
                    self.pot_8[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_9[0]:
                    fk = current_player.first_empty_key(self.pot_9)
                    self.pot_9[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_10[0]:
                    fk = current_player.first_empty_key(self.pot_10)
                    self.pot_10[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_11[0]:
                    fk = current_player.first_empty_key(self.pot_11)
                    self.pot_11[1][fk] = current_player.drop_stone()
                    continue

                elif pot_name == self.pot_12[0]:
                    fk = current_player.first_empty_key(self.pot_12)
                    self.pot_12[1][fk] = current_player.drop_stone()
                    continue

    def ccs_checker(self, current_player, next_player):
        '''
        input are the current and next players' instances
        Check for CLAIM, CONTINUE, or TURN SWITCH
        '''

        # check for winner
        total_board_stones = self.calc_board_stones(current_player, next_player)
        # condition for win check
        if total_board_stones < 16:
            cp_total_stones = len(current_player.captured_stones) + current_player.section_stones()
            np_total_stones = len(next_player.captured_stones) + next_player.section_stones()
            # when there's a DRAW
            if cp_total_stones == np_total_stones:
                print("\n\nTHIS IS A DRAW!!!\nNO WINNER HAS EMERGED!")
                current_player.play_on()
                return current_player.exit_play()

            # when current_player wins
            elif cp_total_stones > np_total_stones:
                print("\n"*3,f"{current_player} WINS!")
                current_player.play_on()
                return current_player.exit_play()

            # when the other player wins
            else:
                print("\n"*3,f"{next_player} WINS!")
                current_player.play_on()
                return current_player.exit_play()


        # for pot 1
        if current_player.last_recipient_pot == self.pot_1[0]:
            stone_count = self.pot_stones(self.pot_1)

            # check for CLAIM
            if (current_player.board_side != self.pot_1[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 2
        elif current_player.last_recipient_pot == self.pot_2[0]:
            stone_count = self.pot_stones(self.pot_2)

            # check for CLAIM
            if (current_player.board_side != self.pot_2[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 3
        elif current_player.last_recipient_pot == self.pot_3[0]:
            stone_count = self.pot_stones(self.pot_3)

            # check for CLAIM
            if (current_player.board_side != self.pot_3[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 4
        elif current_player.last_recipient_pot == self.pot_4[0]:
            stone_count = self.pot_stones(self.pot_4)

            # check for CLAIM
            if (current_player.board_side != self.pot_4[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 5
        elif current_player.last_recipient_pot == self.pot_5[0]:
            stone_count = self.pot_stones(self.pot_5)

            # check for CLAIM
            if (current_player.board_side != self.pot_5[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 6
        elif current_player.last_recipient_pot == self.pot_6[0]:
            stone_count = self.pot_stones(self.pot_6)

            # check for CLAIM
            if (current_player.board_side != self.pot_6[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 7
        elif current_player.last_recipient_pot == self.pot_7[0]:
            stone_count = self.pot_stones(self.pot_7)

            # check for CLAIM
            if (current_player.board_side != self.pot_7[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 8
        elif current_player.last_recipient_pot == self.pot_8[0]:
            stone_count = self.pot_stones(self.pot_8)

            # check for CLAIM
            if (current_player.board_side != self.pot_8[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 9
        elif current_player.last_recipient_pot == self.pot_9[0]:
            stone_count = self.pot_stones(self.pot_9)

            # check for CLAIM
            if (current_player.board_side != self.pot_9[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 10
        elif current_player.last_recipient_pot == self.pot_10[0]:
            stone_count = self.pot_stones(self.pot_10)

            # check for CLAIM
            if (current_player.board_side != self.pot_10[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 11
        elif current_player.last_recipient_pot == self.pot_11[0]:
            stone_count = self.pot_stones(self.pot_11)

            # check for CLAIM
            if (current_player.board_side != self.pot_11[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

        # for pot 12
        elif current_player.last_recipient_pot == self.pot_12[0]:
            stone_count = self.pot_stones(self.pot_12)

            # check for CLAIM
            if (current_player.board_side != self.pot_12[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} lays claim on pot {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!\n\n{next_player.name} START YOUR TURN!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name} TURN CONTINUES!!")
                return "continue"

    def enforce_ccs(self, ccs_result, current_player):
        '''
        input is the result from ccs_checker(), current and next player objects
        '''

        # CLAIM
        if ccs_result == 'claim':
            # for pot 1
            if current_player.last_recipient_pot == self.pot_1[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_1)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 2
            elif current_player.last_recipient_pot == self.pot_2[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_2)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 3
            elif current_player.last_recipient_pot == self.pot_3[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_3)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 4
            elif current_player.last_recipient_pot == self.pot_4[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_4)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 5
            elif current_player.last_recipient_pot == self.pot_5[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_5)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 6
            elif current_player.last_recipient_pot == self.pot_6[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_6)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 7
            elif current_player.last_recipient_pot == self.pot_7[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_7)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 8
            elif current_player.last_recipient_pot == self.pot_8[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_8)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 9
            elif current_player.last_recipient_pot == self.pot_9[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_9)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 10
            elif current_player.last_recipient_pot == self.pot_10[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_10)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 11
            elif current_player.last_recipient_pot == self.pot_11[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_11)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue

            # for pot 12
            elif current_player.last_recipient_pot == self.pot_12[0]:

                # transfer the pot's four stones into player's hand
                current_player.from_pot_to_hand(self.pot_12)

                # drop all stones into player's reservoir (one by one)
                for n in range(len(current_player.hand)):
                    current_player.captured_stones.append(current_player.drop_stone())
                    continue


        # NEXT TURN
        elif ccs_result == 'switch_turns':
            return False

        # CONTINUE TURN
        else:
            return True

        # NEXT TURN
        return False

    def continue_playing(self, current_player, first_player, second_player):
        '''
        inputs are first, second, and current player objects
        to automatically run the play
        until the last stone of player hits an empty pot
        '''

        while True:

            # for pot 1
            if current_player.last_recipient_pot == self.pot_1[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_1)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False

            # for pot 2
            elif current_player.last_recipient_pot == self.pot_2[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_2)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False



            # for pot 3
            elif current_player.last_recipient_pot == self.pot_3[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_3)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False

            # for pot 4
            elif current_player.last_recipient_pot == self.pot_4[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_4)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False


            # for pot 4
            elif current_player.last_recipient_pot == self.pot_5[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_5)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False


            # for pot 6
            elif current_player.last_recipient_pot == self.pot_6[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_6)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False


            # for pot 7
            elif current_player.last_recipient_pot == self.pot_7[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_7)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False


            # for pot 8
            elif current_player.last_recipient_pot == self.pot_8[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_8)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False


            # for pot 9
            elif current_player.last_recipient_pot == self.pot_9[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_9)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False


            # for pot 10
            elif current_player.last_recipient_pot == self.pot_10[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_10)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False


            # for pot 11
            elif current_player.last_recipient_pot == self.pot_11[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_11)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False


            # for pot 12
            elif current_player.last_recipient_pot == self.pot_12[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_12)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                current_player.play_on()

                board_view(self, first_player, second_player)

                current_player.play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                current_player.play_on()

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False




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




# FUNCTIONS
def board_view(board, player1, player2):
    print("\n", "\t"*10, f"\n\t\tFIRST PLAYER: {Fore.LIGHTGREEN_EX} {player1.name}\t\t\t\t{player1.board_side.upper()}: 1, 2, 3, 4, 5, 6 {Fore.RESET}")
    print("\t\t___________________________________________________________________________")
    print(f"\t\tBoard: {player1.section_stones()} stones\n\t\tHand: {len(player1.hand)} stones\n\t\tCaptured: {len(player1.captured_stones)} stones | Claims: {int(len(player1.captured_stones)/4)}\t\tReserve:  {Fore.LIGHTBLUE_EX}{player1.captured_stones}{Fore.RESET}\n\t\tTOTAL: {player1.section_stones()+len(player1.hand)+len(player1.captured_stones)} stones\n")
    print(Fore.LIGHTGREEN_EX, '\t\t'"  POT 1","      POT 2", "      POT 3", "      POT 4", "      POT 5", "      POT 6", Fore.RESET)
    print(Fore.LIGHTGREEN_EX)
    print('\t\t'' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ')
    print('\t\t''|', board.pot_1[1][1], board.pot_1[1][2], board.pot_1[1][3], board.pot_1[1][4], '|', '|', board.pot_2[1][1], board.pot_2[1][2], board.pot_2[1][3], board.pot_2[1][4], '|', '|', board.pot_3[1][1], board.pot_3[1][2], board.pot_3[1][3], board.pot_3[1][4], '|', '|',  board.pot_4[1][1], board.pot_4[1][2], board.pot_4[1][3], board.pot_4[1][4], '|', '|', board.pot_5[1][1], board.pot_5[1][2], board.pot_5[1][3], board.pot_5[1][4], '|', '|', board.pot_6[1][1], board.pot_6[1][2], board.pot_6[1][3], board.pot_6[1][4], '|')
    print('\t\t''|', board.pot_1[1][5], board.pot_1[1][6], board.pot_1[1][7], board.pot_1[1][8], '|', '|', board.pot_2[1][5], board.pot_2[1][6], board.pot_2[1][7], board.pot_2[1][8], '|', '|', board.pot_3[1][5], board.pot_3[1][6], board.pot_3[1][7], board.pot_3[1][8], '|', '|', board.pot_4[1][5], board.pot_4[1][6], board.pot_4[1][7], board.pot_4[1][8], '|', '|',  board.pot_5[1][5], board.pot_5[1][6], board.pot_5[1][7], board.pot_5[1][8], '|', '|', board.pot_6[1][5], board.pot_6[1][6], board.pot_6[1][7], board.pot_6[1][8], '|')
    print('\t\t''|', board.pot_1[1][9], board.pot_1[1][10], board.pot_1[1][11], board.pot_1[1][12], '|', '|', board.pot_2[1][9], board.pot_2[1][10], board.pot_2[1][11], board.pot_2[1][12], '|', '|', board.pot_3[1][9], board.pot_3[1][10], board.pot_3[1][11], board.pot_3[1][12], '|', '|', board.pot_4[1][9], board.pot_4[1][10], board.pot_4[1][11], board.pot_4[1][12], '|', '|', board.pot_5[1][9], board.pot_5[1][10], board.pot_5[1][11], board.pot_5[1][12], '|', '|', board.pot_6[1][9], board.pot_6[1][10], board.pot_6[1][11], board.pot_6[1][12], '|')
    print('\t\t''|', board.pot_1[1][13], board.pot_1[1][14], board.pot_1[1][15], board.pot_1[1][16], '|', '|', board.pot_2[1][13], board.pot_2[1][14], board.pot_2[1][15], board.pot_2[1][16], '|', '|', board.pot_3[1][13], board.pot_3[1][14], board.pot_3[1][15], board.pot_3[1][16],'|', '|', board.pot_4[1][13], board.pot_4[1][14], board.pot_4[1][15], board.pot_4[1][16], '|', '|', board.pot_5[1][13], board.pot_5[1][14], board.pot_5[1][15], board.pot_5[1][16], '|', '|', board.pot_6[1][13], board.pot_6[1][14], board.pot_6[1][15], board.pot_6[1][16], '|')
    print('\t\t''|', board.pot_1[1][17], board.pot_1[1][18], board.pot_1[1][19], board.pot_1[1][20], '|', '|', board.pot_2[1][17], board.pot_2[1][18], board.pot_2[1][19], board.pot_2[1][20], '|', '|', board.pot_3[1][17], board.pot_3[1][18], board.pot_3[1][19], board.pot_3[1][20], '|', '|', board.pot_4[1][17], board.pot_4[1][18], board.pot_4[1][19], board.pot_4[1][20], '|', '|', board.pot_5[1][17], board.pot_5[1][18], board.pot_5[1][19], board.pot_5[1][20], '|', '|', board.pot_6[1][17], board.pot_6[1][18], board.pot_6[1][19], board.pot_6[1][20], '|')
    print('\t\t''|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '\n')
    print(Fore.RESET)
    print("\t"*5, f"{Fore.LIGHTYELLOW_EX}{player1.name} VERSUS {player2.name} {Fore.RESET}")
    print(Fore.LIGHTBLUE_EX)
    print('\t\t'' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ')
    print('\t\t''|', board.pot_12[1][1], board.pot_12[1][2], board.pot_12[1][3], board.pot_12[1][4], '|', '|', board.pot_11[1][1], board.pot_11[1][2], board.pot_11[1][3], board.pot_11[1][4], '|', '|', board.pot_10[1][1], board.pot_10[1][2], board.pot_10[1][3], board.pot_10[1][4], '|', '|',  board.pot_9[1][1], board.pot_9[1][2], board.pot_9[1][3], board.pot_9[1][4], '|', '|', board.pot_8[1][1], board.pot_8[1][2], board.pot_8[1][3], board.pot_8[1][4], '|', '|', board.pot_7[1][1], board.pot_7[1][2], board.pot_7[1][3], board.pot_7[1][4], '|')
    print('\t\t''|', board.pot_12[1][5], board.pot_12[1][6], board.pot_12[1][7], board.pot_12[1][8], '|', '|', board.pot_11[1][5], board.pot_11[1][6], board.pot_11[1][7], board.pot_11[1][8], '|', '|', board.pot_10[1][5], board.pot_10[1][6], board.pot_10[1][7], board.pot_10[1][8], '|', '|', board.pot_9[1][5], board.pot_9[1][6], board.pot_9[1][7], board.pot_9[1][8], '|', '|',  board.pot_8[1][5], board.pot_8[1][6], board.pot_8[1][7], board.pot_8[1][8], '|', '|', board.pot_7[1][5], board.pot_7[1][6], board.pot_7[1][7], board.pot_7[1][8], '|')
    print('\t\t''|', board.pot_12[1][9], board.pot_12[1][10], board.pot_12[1][11], board.pot_12[1][12], '|', '|', board.pot_11[1][9], board.pot_11[1][10], board.pot_11[1][11], board.pot_11[1][12], '|', '|', board.pot_10[1][9], board.pot_10[1][10], board.pot_10[1][11], board.pot_10[1][12], '|', '|', board.pot_9[1][9], board.pot_9[1][10], board.pot_9[1][11], board.pot_9[1][12], '|', '|', board.pot_8[1][9], board.pot_8[1][10], board.pot_8[1][11], board.pot_8[1][12], '|', '|', board.pot_7[1][9], board.pot_7[1][10], board.pot_7[1][11], board.pot_7[1][12], '|')
    print('\t\t''|', board.pot_12[1][13], board.pot_12[1][14], board.pot_12[1][15], board.pot_12[1][16], '|', '|', board.pot_11[1][13], board.pot_11[1][14], board.pot_11[1][15], board.pot_11[1][16], '|', '|', board.pot_10[1][13], board.pot_10[1][14], board.pot_10[1][15], board.pot_10[1][16],'|', '|', board.pot_9[1][13], board.pot_9[1][14], board.pot_9[1][15], board.pot_9[1][16], '|', '|', board.pot_8[1][13], board.pot_8[1][14], board.pot_8[1][15], board.pot_8[1][16], '|', '|', board.pot_7[1][13], board.pot_7[1][14], board.pot_7[1][15], board.pot_7[1][16], '|')
    print('\t\t''|', board.pot_12[1][17], board.pot_12[1][18], board.pot_12[1][19], board.pot_12[1][20], '|', '|', board.pot_11[1][17], board.pot_11[1][18], board.pot_11[1][19], board.pot_11[1][20], '|', '|', board.pot_10[1][17], board.pot_10[1][18], board.pot_10[1][19], board.pot_10[1][20], '|', '|', board.pot_9[1][17], board.pot_9[1][18], board.pot_9[1][19], board.pot_9[1][20], '|', '|', board.pot_8[1][17], board.pot_8[1][18], board.pot_8[1][19], board.pot_8[1][20], '|', '|', board.pot_7[1][17], board.pot_7[1][18], board.pot_7[1][19], board.pot_7[1][20], '|')
    print('\t\t''|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|')
    print( Fore.RESET)
    print(Fore.LIGHTBLUE_EX, '\t\t'"  POT 12","      POT 11", "      POT 10", "      POT 9", "      POT 8", "      POT 7", Fore.RESET)
    print("\n", "\t"*10, f"\n\t\tSECOND PLAYER: {Fore.LIGHTBLUE_EX} {player2.name}\t\t\t\t{player2.board_side.upper()}: 7, 8, 9, 10, 11, 12 {Fore.RESET}")
    print('\t\t'"___________________________________________________________________________")
    print(f"\n\t\tBoard: {player2.section_stones()} stones\n\t\tHand: {len(player2.hand)} stones\n\t\tCaptured: {len(player2.captured_stones)} stones | Claims: {int(len(player2.captured_stones)/4)}\t\tReserve:  {Fore.LIGHTGREEN_EX}{player2.captured_stones}{Fore.RESET}\n\t\tTOTAL: {player2.section_stones()+len(player2.hand)+len(player2.captured_stones)} stones\n")




def player_name():
    while True:
        val = input("\n\t\tPlayer Name:   \n\t\t")
        if val.isdigit():
            print("\n\Enter a valid name")
            continue
        return val.upper()

def welc_scrn():
    print("\n","\t"*4,"*****WELCOME*****")
    print("\n"*2,"\t"*4,"*******TO********")
    print("\n"*3,"\t"*4,"*****OGIDISE*****")
    print("\n"*2,"\t"*4,"****BOARD GAME****")
    print("\n","\t"*4,"**FEBRUARY, 2021**")
