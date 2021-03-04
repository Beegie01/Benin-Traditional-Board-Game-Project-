# import sys

# pkg = 'C:\\Users\\welcome\\Desktop\\MyFuncs'

# if pkg not in sys.path:
#     sys.path.append(pkg)

from fave_app_funcs import play_on

from GameModules.ogidise_funcs import board_view

class Board:

    # spare pot_cells for resetting each pot after each player pick
    pot = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' ', 26: ' ', 27: ' ', 28: ' ', 29: ' ', 30: ' '}

    def __init__(self):
        # positions [0: pot_name, 1: pot_cells, 2: pot_number, 3: board_side]
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
        input is pot object
        to get the number of stones in a pot

        Example:
        board1.pot_stones(player1.pot_1) -->

        "There are 4 stones in pot_1"
        '''

        listed = []
        listed.extend(list(pot[1].values()))
        stones = ''

        for char in listed:
            if char != 'O':
                continue
            else:
                stones += char

        if len(stones) == 1:
            print(f"\nOnly {len(stones)} stone in {pot[0]}")
        elif len(stones) < 1:
            print(f"\n{pot[0]} is empty!")
        else:
            print(f"There are {len(stones)} stones in {pot[0]}")
        return len(stones)


    def distribute_stones(self, current_player):
        '''
        immediately after player picks stones
        use the pot name from which the current player last picked
        to determine movement/direction of stone spread across game board
        assigns new value to player's last recipient pot attribute

        Example:

        board1.distribute_stones(player1) -->

        Osagie picked from: pot_1
        Move Steps: [pot_2, pot_3, pot_4, pot_5]
        Next Stop: pot_5
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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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
            print(f"\n\n{current_player.name} picked {len(use_name)} stones from: {current_player.last_picked_pot}\nMove Steps: {', '.join(use_name)}\nNext Stop: {use_name[-1]}")

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

        Example:
        board.css_checker(player1, player2) -->

        # in case of claim
        CLAIM!!
        osagie CLAIMS pot_5

        # in case of turn switch
        osagie STOP!
        elliot START YOUR TURN!

        # in case of continue
        osagie's TURN CONTINUES
        '''


        # for pot 1
        if current_player.last_recipient_pot == self.pot_1[0]:
            stone_count = self.pot_stones(self.pot_1)

            # check for CLAIM
            if (current_player.board_side != self.pot_1[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 2
        elif current_player.last_recipient_pot == self.pot_2[0]:
            stone_count = self.pot_stones(self.pot_2)

            # check for CLAIM
            if (current_player.board_side != self.pot_2[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 3
        elif current_player.last_recipient_pot == self.pot_3[0]:
            stone_count = self.pot_stones(self.pot_3)

            # check for CLAIM
            if (current_player.board_side != self.pot_3[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 4
        elif current_player.last_recipient_pot == self.pot_4[0]:
            stone_count = self.pot_stones(self.pot_4)

            # check for CLAIM
            if (current_player.board_side != self.pot_4[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 5
        elif current_player.last_recipient_pot == self.pot_5[0]:
            stone_count = self.pot_stones(self.pot_5)

            # check for CLAIM
            if (current_player.board_side != self.pot_5[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 6
        elif current_player.last_recipient_pot == self.pot_6[0]:
            stone_count = self.pot_stones(self.pot_6)

            # check for CLAIM
            if (current_player.board_side != self.pot_6[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 7
        elif current_player.last_recipient_pot == self.pot_7[0]:
            stone_count = self.pot_stones(self.pot_7)

            # check for CLAIM
            if (current_player.board_side != self.pot_7[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 8
        elif current_player.last_recipient_pot == self.pot_8[0]:
            stone_count = self.pot_stones(self.pot_8)

            # check for CLAIM
            if (current_player.board_side != self.pot_8[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 9
        elif current_player.last_recipient_pot == self.pot_9[0]:
            stone_count = self.pot_stones(self.pot_9)

            # check for CLAIM
            if (current_player.board_side != self.pot_9[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 10
        elif current_player.last_recipient_pot == self.pot_10[0]:
            stone_count = self.pot_stones(self.pot_10)

            # check for CLAIM
            if (current_player.board_side != self.pot_10[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 11
        elif current_player.last_recipient_pot == self.pot_11[0]:
            stone_count = self.pot_stones(self.pot_11)

            # check for CLAIM
            if (current_player.board_side != self.pot_11[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

        # for pot 12
        elif current_player.last_recipient_pot == self.pot_12[0]:
            stone_count = self.pot_stones(self.pot_12)

            # check for CLAIM
            if (current_player.board_side != self.pot_12[3]) and (stone_count == 4):
                print("\n"*2,f"CLAIM!!\n{current_player.name} CLAIMS {current_player.last_recipient_pot}")
                return "claim"

            # check for TURN SWITCH
            elif stone_count < 2:
                print("\n",f"{current_player.name} STOP!!")
                return 'switch_turns'

            # check for CONTINUE
            else:
                print("\n", f"{current_player.name}'s TURN CONTINUES!!")
                return "continue"

    def enforce_ccs(self, ccs_result, current_player):
        '''
        input is the result from ccs_checker(), current and next player objects

        Example:

        board1.enforce_ccs(result, player1) -->

        # if result == 'claim'
        4 stones are transferred from the pot into player's reserve
        then return False

        # if result == 'switch_turns'
        return False

        # if result == 'continue'
        return True
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

        Example:

        board1.continue_playing(player1, player1, player2) -->

        # Inplace operations
        transfer stones from pot to hand
        stones in hand get distributed automatically
        check the last receiving pot for continue, claim, or turn_switch
        claim stones, continue playing or switch to next player based on the above result
        '''

        while True:

            # for pot 1
            if current_player.last_recipient_pot == self.pot_1[0]:

                # transfer stones from last recipient pot to hand
                current_player.from_pot_to_hand(self.pot_1)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                play_on()

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

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

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # stones are automatically distributed across game board
                self.distribute_stones(current_player)

                play_on()

                board_view(self, first_player, second_player)

                play_on()

                # board check is done on the last recipient pot for claim, continue or turn switch
                result = self.ccs_checker(current_player, second_player)

                # return false if claim or turn switch occurs
                # and true if continue
                continue_play = self.enforce_ccs(result, current_player)

                if continue_play:
                    continue

                return False
