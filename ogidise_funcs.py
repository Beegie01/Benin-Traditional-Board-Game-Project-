import sys, re

pkg = 'C:\\Users\\welcome\\Desktop\\MyFuncs'

if pkg not in sys.path:
    sys.path.append(pkg)

from fave_app_funcs import generate_password, password_inp

import colorama
from colorama import init, Fore, Back, Style
init()



# FUNCTIONS
def board_view(board, player1, player2):
    '''
    Displays both player's stats and current state of the board
    Runs a check for game WINNER or STALEMATE

    Example:

    board_view(board1, player1, player2) -->

    # STALEMATE (in red colors)
    STALEMATE!
    THERE IS NO WINNER!

    # WINNER EMERGES (in player's colors)
    osagie WINS!
    '''
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
    '''
    ensures that input is string
    and returns string in upper case

    Example:

    player_name() -->

    OSAGIE
    '''

    while True:
        val = input("\n\t\tPlayer Name:   \n\t\t")
        if val.isdigit():
            print("\n\Enter a valid name")
            continue
        return val.upper()

def welc_scrn():
    print("\n"*50,"\t"*4,"*****WELCOME*****")
    print("\n"*2,"\t"*4,"*******TO********")
    print("\n"*3,"\t"*4,"*****OGIDISE*****")
    print("\n"*2,"\t"*4,"****BOARD GAME****")
    print("\n","\t"*4,"**FEBRUARY, 2021**",'\n'*5)



def save_progress(board_obj, first_player_obj, second_player_obj, FIRST_TURN):
    '''
    to save game/app records
    input are file path of text file for saving, class instance/object
    and first turn is true/false
    '''

    password = generate_password()

    hand = open('C:\\Users\\welcome\\Desktop\\OgidiseBoardGame\\ogid_game_data.txt', 'a')

    # stored fields include
    # [password, board attributes, first player's attributes, second player's attributes]
    info = f"\n{dict( [ ('password', password), ('board_data', board_obj.__dict__), ('first_player', first_player_obj.__dict__), ('second_player', second_player_obj.__dict__), ('first_turn', FIRST_TURN) ])}"

    hand.write(info)

    hand.close()

    print(f"\n\nGame saved!\nTo continue playing as: \n{first_player_obj.name} and {second_player_obj.name} \nUse the password below:\n\nPassword>\t{password}")


def retrieve():
    '''
    to retrieve saved app/game records from file using given password

    outputs saved board_obj, first_player_obj, second_player_obj
    '''

    Found = False
    
    # ask for the saved usernames
    prompt = "\nEnter password below to continue saved game:\nPASSWORD>\t"
    pword = password_inp(prompt)


    # retrieve stored information from file
    with open('C:\\Users\\welcome\\Desktop\\OgidiseBoardGame\\ogid_game_data.txt') as h:

        file_data = h.read()

    # file data is a string of the file content
    # regular expression to extract only dictionaries from body of text
    pattern = r"{.+}"

    # result is list of dictionaries in string format
    result = re.findall(pattern, file_data)

    # now transforming the list of dict into a str of dict
    for dd in result:
        dd = eval(dd)

        for k,v in dd.items():
            if k == 'password':
                # when password is found
                if v == pword:
                    board_attr, fp_attr, sp_attr, first_turn = dd['board_data'], dd['first_player'], dd['second_player'], dd['first_turn']
                    print("\nPassword Found!")
                    Found = True

    if Found:
        return board_attr, fp_attr, sp_attr, first_turn

    print("\nPassword Not Found!")
    return '', '', '', ''
