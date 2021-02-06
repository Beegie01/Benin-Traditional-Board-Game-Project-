

import random
import string

class Board:

    pot = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '}

    def __init__(self):
        # pos [0: name, 1: dict, 2: number]
        self.pot_1 = ['pot_1',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      1]
        self.pot_2 = ['pot_2',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      2]
        self.pot_3 = ['pot_3',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      3]
        self.pot_4 = ['pot_4',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      4]
        self.pot_5 = ['pot_5',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      5]
        self.pot_6 = ['pot_6',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      6]
        self.pot_7 = ['pot_7',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      7]
        self.pot_8 = ['pot_8',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      8]
        self.pot_9 = ['pot_9',
                      {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                      9]
        self.pot_10 = ['pot_10',
                       {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                       10]
        self.pot_11 = ['pot_11',
                       {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                       11]
        self.pot_12 = ['pot_12',
                       {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '},
                       12]

        self.pots_name = {'pot_1': 1, 'pot_2': 2, 'pot_3': 3, 'pot_4': 4, 'pot_5': 5, 'pot_6': 6, 'pot_7': 7, 'pot_8': 8, 'pot_9': 9, 'pot_10': 10, 'pot_11': 11, 'pot_12': 12}
        self.pots_no = {1: {self.pot_1[0]: self.pot_1[1]}, 2: {self.pot_2[0]: self.pot_2[1]}, 3: {self.pot_3[0]: self.pot_3[1]}, 4: {self.pot_4[0]: self.pot_4[1]}, 5: {self.pot_5[0]: self.pot_5[1]}, 6: {self.pot_6[0]: self.pot_6[1]}, 7: {self.pot_7[0]: self.pot_7[1]}, 8: {self.pot_8[0]: self.pot_8[1]}, 9: {self.pot_9[0]: self.pot_9[1]}, 10: {self.pot_10[0]: self.pot_10[1]}, 11: {self.pot_11[0]: self.pot_11[1]}, 12: {self.pot_12[0]: self.pot_12[1]}}
        section = []


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

    def distribute_stones(self, current_player):
        '''
        immediately after player picks stones
        use the pot name from which the current player last picked from to determine movement/direction of stone spread
        '''
        steps = len(current_player.hand)
        count = 0
        receiving_pot_dict = {}

        #while count < steps:

        # if player picked from pot 1
        if current_player.last_picked_pot == self.pot_1[0]:
            print(f"\nLast_picked: {current_player.last_picked_pot} \n{self.pot_1}")
            pot_name_seq = [self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_10[0], self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_11[0], self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_12[0], self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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
            pot_name_seq = [self.pot_1[0], self.pot_2[0], self.pot_3[0], self.pot_4[0], self.pot_5[0], self.pot_6[0], self.pot_7[0], self.pot_8[0], self.pot_9[0], self.pot_10[0], self.pot_11[0], self.pot_12[0]]
            use_name = pot_name_seq[:steps]
            print(use_name)
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

        # storage for stones claimed from the opponent
        self.captured_stones = []

        # name of last pot player picked from
        self.last_picked_pot = None


    # METHODS
    def pick_coin_sides(self):

        print(f"{self.name} choose HEAD or TAIL")
        acc_range = ['head', 'h', 'tail', 't']
        pick = None
        while pick not in acc_range:
            val = input("Enter H for head, or T for tail:\n")

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
        second_player.pot_1 = board.pot_12
        second_player.pot_2 = board.pot_11
        second_player.pot_3 = board.pot_10
        second_player.pot_4 = board.pot_9
        second_player.pot_5 = board.pot_8
        second_player.pot_6 = board.pot_7

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


    def empty_keys(self, pot):
        '''
        input is a pot_obj
        counts the number of empty cells in a pot
        '''
        empty_cells = 0
        for k,v in pot[1].items():
            if v == ' ':
                empty_cells += 1
            else:
                continue
        return empty_cells

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
            return pick

    def fp_select_pot(board):
        '''
        converts first player's pick (1-6) into their corresponding pot instance
        outputs the pot_name, pot_object and number
        '''

        pick = board.fp_prompt_pot_no()

        if pick == board.pot_1[2]:
            return board.pot_1[0], board.pot_1,  pick
        elif pick == board.pot_2[2]:
            return board.pot_2[0], board.pot_2, pick
        elif pick == board.pot_3[2]:
            return board.pot_3[0], board.pot_3,  pick
        elif pick == board.pot_4[2]:
            return board.pot_4[0], board.pot_4,  pick
        elif pick == board.pot_5[2]:
            return board.pot_5[0], board.pot_5, pick
        elif pick == board.pot_6[2]:
            return board.pot_6[0], board.pot_6, pick

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
            return pick

    def sp_select_pot(board):
        '''
        converts second player's pick (7-12) into their corresponding pot instance
        outputs the pot_name, pot_object and number
        '''

        pick = board.sp_prompt_pot_no()

        if pick == board.pot_12[2]:
            return board.pot_12[0], board.pot_12, pick
        elif pick == board.pot_11[2]:
            return board.pot_11[0], board.pot_11, pick
        elif pick == board.pot_10[2]:
            return board.pot_10[0], board.pot_10, pick
        elif pick == board.pot_9[2]:
            return board.pot_9[0], board.pot_9, pick
        elif pick == board.pot_8[2]:
            return board.pot_8[0], board.pot_8, pick
        elif pick == board.pot_7[2]:
            return board.pot_7[0], board.pot_7, pick

    def check_if_empty(self, chosen_pot):
        '''
        check to see if pot is empty
        '''

        ek_count = self.empty_keys(chosen_pot)
        if ek_count == 48:
            print(f"{self.name} IS TRYING TO PICK FROM AN EMPTY POT")
            return True
        return False


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
        return print(f"{self.name} picked from {feeder_pot[0]}")


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
            print(f"{self.name} has {len(self.hand)} in his hand")

    def share_stones(self, receiving_pot_dicts):
        '''
        fill up the first empty cells in the given list of pot dicts
        '''

        # Nothing happens on the board if player's hand is empty
        if len(self.hand) < 1:
            return print(f"\nNo more stones in {self.name}'s hand to drop.\nPlease refill hand from a non-empty pot!")

        try:
            list(receiving_pot_dicts)
        except:
            print("\nError: wrong input!")

        # Nothing happens if input is not a list
        if type(receiving_pot_dicts) != type([]):
            return print(f"Error: input is not a list of dicts!")

        # enlisting all the given pots
        receiving_pot_dicts
        emp_keys_list = []

        if len(self.hand) != len(receiving_pot_dicts):
            return print(f"Error:\n{self.name} is trying to share {len(self.hand)} stones into {len(receiving_pot_dicts)} pots!")

        # determining the first empty keys in each of the pots in the list
        for pot_dict in receiving_pot_dicts:
            emp_keys_list.append(self.first_empty_key(pot_dict))

        # dropping a stone from player's hand into each of the first empty keys of the given pots
        for pot_dict in receiving_pot_dicts:
            for k in emp_keys_list:
                pot_dict[k] = self.drop_stone()
                break

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
        print(f"This pot contains {len(keys)} stones at {keys}")
        return keys



    def play_on(self):
        response = self.quick_check()
        if response:
            pass

    def quick_check(self):
        while True:
            print("\nScreen Pause!")
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
    print("\n","\t"*4,f"{player1.name}'s POTS: 1, 2, 3, 4, 5, 6 \nFIRST PLAYER: {player1.name}")
    print("___________________________________________________________________________")
    print(f"Board: {player1.section_stones()} stones\nHand: {len(player1.hand)} stones\nCaptured: {len(player1.captured_stones)} stones\nTOTAL: {player1.section_stones()+len(player1.hand)+len(player1.captured_stones)} stones\n")
    print("  POT 1","      POT 2", "      POT 3", "      POT 4", "      POT 5", "      POT 6")
    print(' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ')
    print('|', board.pot_1[1][1], board.pot_1[1][2], board.pot_1[1][3], board.pot_1[1][4], '|', '|', board.pot_2[1][1], board.pot_2[1][2], board.pot_2[1][3], board.pot_2[1][4], '|', '|', board.pot_3[1][1], board.pot_3[1][2], board.pot_3[1][3], board.pot_3[1][4], '|', '|',  board.pot_4[1][1], board.pot_4[1][2], board.pot_4[1][3], board.pot_4[1][4], '|', '|', board.pot_5[1][1], board.pot_5[1][2], board.pot_5[1][3], board.pot_5[1][4], '|', '|', board.pot_6[1][1], board.pot_6[1][2], board.pot_6[1][3], board.pot_6[1][4], '|')
    print('|', board.pot_1[1][5], board.pot_1[1][6], board.pot_1[1][7], board.pot_1[1][8], '|', '|', board.pot_2[1][5], board.pot_2[1][6], board.pot_2[1][7], board.pot_2[1][8], '|', '|', board.pot_3[1][5], board.pot_3[1][6], board.pot_3[1][7], board.pot_3[1][8], '|', '|', board.pot_4[1][5], board.pot_4[1][6], board.pot_4[1][7], board.pot_4[1][8], '|', '|',  board.pot_5[1][5], board.pot_5[1][6], board.pot_5[1][7], board.pot_5[1][8], '|', '|', board.pot_6[1][5], board.pot_6[1][6], board.pot_6[1][7], board.pot_6[1][8], '|')
    print('|', board.pot_1[1][9], board.pot_1[1][10], board.pot_1[1][11], board.pot_1[1][12], '|', '|', board.pot_2[1][9], board.pot_2[1][10], board.pot_2[1][11], board.pot_2[1][12], '|', '|', board.pot_3[1][9], board.pot_3[1][10], board.pot_3[1][11], board.pot_3[1][12], '|', '|', board.pot_4[1][9], board.pot_4[1][10], board.pot_4[1][11], board.pot_4[1][12], '|', '|', board.pot_5[1][9], board.pot_5[1][10], board.pot_5[1][11], board.pot_5[1][12], '|', '|', board.pot_6[1][9], board.pot_6[1][10], board.pot_6[1][11], board.pot_6[1][12], '|')
    print('|', board.pot_1[1][13], board.pot_1[1][14], board.pot_1[1][15], board.pot_1[1][16], '|', '|', board.pot_2[1][13], board.pot_2[1][14], board.pot_2[1][15], board.pot_2[1][16], '|', '|', board.pot_3[1][13], board.pot_3[1][14], board.pot_3[1][15], board.pot_3[1][16],'|', '|', board.pot_4[1][13], board.pot_4[1][14], board.pot_4[1][15], board.pot_4[1][16], '|', '|', board.pot_5[1][13], board.pot_5[1][14], board.pot_5[1][15], board.pot_5[1][16], '|', '|', board.pot_6[1][13], board.pot_6[1][14], board.pot_6[1][15], board.pot_6[1][16], '|')
    print('|', board.pot_1[1][17], board.pot_1[1][18], board.pot_1[1][19], board.pot_1[1][20], '|', '|', board.pot_2[1][17], board.pot_2[1][18], board.pot_2[1][19], board.pot_2[1][20], '|', '|', board.pot_3[1][17], board.pot_3[1][18], board.pot_3[1][19], board.pot_3[1][20], '|', '|', board.pot_4[1][17], board.pot_4[1][18], board.pot_4[1][19], board.pot_4[1][20], '|', '|', board.pot_5[1][17], board.pot_5[1][18], board.pot_5[1][19], board.pot_5[1][20], '|', '|', board.pot_6[1][17], board.pot_6[1][18], board.pot_6[1][19], board.pot_6[1][20], '|')
    print('|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '\n')
    print(' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ', ' _','_', '_', '_', '_ ')
    print('|', board.pot_12[1][1], board.pot_12[1][2], board.pot_12[1][3], board.pot_12[1][4], '|', '|', board.pot_11[1][1], board.pot_11[1][2], board.pot_11[1][3], board.pot_11[1][4], '|', '|', board.pot_10[1][1], board.pot_10[1][2], board.pot_10[1][3], board.pot_10[1][4], '|', '|',  board.pot_9[1][1], board.pot_9[1][2], board.pot_9[1][3], board.pot_9[1][4], '|', '|', board.pot_8[1][1], board.pot_8[1][2], board.pot_8[1][3], board.pot_8[1][4], '|', '|', board.pot_7[1][1], board.pot_7[1][2], board.pot_7[1][3], board.pot_7[1][4], '|')
    print('|', board.pot_12[1][5], board.pot_12[1][6], board.pot_12[1][7], board.pot_12[1][8], '|', '|', board.pot_11[1][5], board.pot_11[1][6], board.pot_11[1][7], board.pot_11[1][8], '|', '|', board.pot_10[1][5], board.pot_10[1][6], board.pot_10[1][7], board.pot_10[1][8], '|', '|', board.pot_9[1][5], board.pot_9[1][6], board.pot_9[1][7], board.pot_9[1][8], '|', '|',  board.pot_8[1][5], board.pot_8[1][6], board.pot_8[1][7], board.pot_8[1][8], '|', '|', board.pot_7[1][5], board.pot_7[1][6], board.pot_7[1][7], board.pot_7[1][8], '|')
    print('|', board.pot_12[1][9], board.pot_12[1][10], board.pot_12[1][11], board.pot_12[1][12], '|', '|', board.pot_11[1][9], board.pot_11[1][10], board.pot_11[1][11], board.pot_11[1][12], '|', '|', board.pot_10[1][9], board.pot_10[1][10], board.pot_10[1][11], board.pot_10[1][12], '|', '|', board.pot_9[1][9], board.pot_9[1][10], board.pot_9[1][11], board.pot_9[1][12], '|', '|', board.pot_8[1][9], board.pot_8[1][10], board.pot_8[1][11], board.pot_8[1][12], '|', '|', board.pot_7[1][9], board.pot_7[1][10], board.pot_7[1][11], board.pot_7[1][12], '|')
    print('|', board.pot_12[1][13], board.pot_12[1][14], board.pot_12[1][15], board.pot_12[1][16], '|', '|', board.pot_11[1][13], board.pot_11[1][14], board.pot_11[1][15], board.pot_11[1][16], '|', '|', board.pot_10[1][13], board.pot_10[1][14], board.pot_10[1][15], board.pot_10[1][16],'|', '|', board.pot_9[1][13], board.pot_9[1][14], board.pot_9[1][15], board.pot_9[1][16], '|', '|', board.pot_8[1][13], board.pot_8[1][14], board.pot_8[1][15], board.pot_8[1][16], '|', '|', board.pot_7[1][13], board.pot_7[1][14], board.pot_7[1][15], board.pot_7[1][16], '|')
    print('|', board.pot_12[1][17], board.pot_12[1][18], board.pot_12[1][19], board.pot_12[1][20], '|', '|', board.pot_11[1][17], board.pot_11[1][18], board.pot_11[1][19], board.pot_11[1][20], '|', '|', board.pot_10[1][17], board.pot_10[1][18], board.pot_10[1][19], board.pot_10[1][20], '|', '|', board.pot_9[1][17], board.pot_9[1][18], board.pot_9[1][19], board.pot_9[1][20], '|', '|', board.pot_8[1][17], board.pot_8[1][18], board.pot_8[1][19], board.pot_8[1][20], '|', '|', board.pot_7[1][17], board.pot_7[1][18], board.pot_7[1][19], board.pot_7[1][20], '|')
    print('|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|', '|_','_', '_', '_', '_|')
    print("  POT 12","      POT 11", "      POT 10", "      POT 9", "      POT 8", "      POT 7")
    print("\n","\t"*4,f"{player2.name}'s POTS: 7, 8, 9, 10, 11, 12 \nSECOND PLAYER: {player2.name}")
    print("___________________________________________________________________________")
    print(f"\nBoard: {player2.section_stones()} stones\nHand: {len(player2.hand)} stones\nCaptured: {len(player2.captured_stones)} stones\nTOTAL: {player2.section_stones()+len(player2.hand)+len(player2.captured_stones)} stones\n")




def player_name():
    while True:
        val = input("\n\t\tPlayer Name:   \n\t\t")
        if val.isdigit():
            print("\n\Enter a valid name")
            continue
        return val.upper()

def welc_scrn():
    print("\n","\t"*4,"*****WELCOME*****")
    print("\n","\t"*4,"*******TO********")
    print("\n","\t"*4,"*****OGIDISE*****")
    print("\n","\t"*4,"****BOARD GAME****")
    print("\n","\t"*4,"**FEBRUARY, 2021**")
