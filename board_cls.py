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


import colorama
from colorama import init, Fore, Back, Style
init()



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

    # check for a winner
    total_stones_inplay = player1.section_stones() + player2.section_stones() + len(player1.hand) + len(player2.hand)

    p1_total_stones = len(player1.captured_stones) + player1.section_stones() + len(player1.hand)
    p2_total_stones = len(player2.captured_stones) + player2.section_stones() + len(player2.hand)


    if (total_stones_inplay > 0 and total_stones_inplay < 17):
        # when there's a DRAW
        if (p1_total_stones == p2_total_stones):
            print(Fore.RED,"\n\n\nSTALEMATE!!!\n\nTHERE IS NO WINNER!", Fore.RESET)
            player1.play_on()
            return player1.exit_play()

        # when player1 wins
        elif (p1_total_stones > p2_total_stones):
            print(Fore.LIGHTGREEN_EX, "\n"*3,f"{player1.name} WINS!", Fore.RESET)
            player1.play_on()
            return player1.exit_play()

        # when the other player wins
        elif (p1_total_stones < p2_total_stones):
            print(Fore.LIGHTBLUE_EX, "\n"*3,f"{player2.name} WINS!", Fore.RESET)
            player1.play_on()
            return player1.exit_play()



def player_name():
    while True:
        val = input("\n\t\tPlayer Name:   \n\t\t")
        if val.isdigit():
            print("\n\Enter a valid name")
            continue
        return val.upper()

def welc_scrn():
    print("\n"*5,"\t"*4,"*****WELCOME*****")
    print("\n"*2,"\t"*4,"*******TO********")
    print("\n"*3,"\t"*4,"*****OGIDISE*****")
    print("\n"*2,"\t"*4,"****BOARD GAME****")
    print("\n","\t"*4,"**FEBRUARY, 2021**",'\n'*5)
