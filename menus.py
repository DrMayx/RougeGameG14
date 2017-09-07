from filehandling import unfile
from movement import getch
from clear import resize_and_clear as clear
from button import change_button as button
from about import print_about as about
from introscreen import intro as intro

def logo():  # printing logo
    with open("menu.uie") as picture:
        for line in picture:
            print(line[:-1])

    # maps, current_choice, last_input, user


def display_menu(args):
    
    maps = args['maps']
    current_choice = args['current_choice']
    user_input = args['last_input']
    user = args['player']
    
    logo()
    
    current_choice = button(user_input, current_choice)
    
    print('\n\n')
    print("player:".rjust(65), "name:".rjust(24))
    print(user.player_char.rjust(71), user.name.rjust(26))
    user_input = getch()

    if user_input == '\r' and current_choice == 4:
        return
    if user_input == '\r' and current_choice == 1:
        # Change map to lvl 1
        # Can be modified to show story

        clear()
        intro()
        board = unfile(maps[1])
        original_board = unfile(maps[1])
        return (1, None, board, original_board)

    if user_input == '\r' and current_choice == 2:
        # Change to about screen

        clear()
        about()
        clear()
        logo()
        return ('menu', current_choice, user_input)

    if user_input == '\r' and current_choice == 3:
        # Change to about screen

        clear()
        about()
        clear()
        logo()
        return ('menu', current_choice, user_input)

    else:
        clear()
        logo()
        return ('menu', current_choice, user_input)

'''
def display_pause_menu(last_map, current_choice, last_input):
    clear()
    user_input = last_input
    current_choice = button(user_input, current_choice)
    user_input = getch()
    if user_input == 'p':
        return
    elif user_input == '\r' and current_choice == 1:
        return
    elif user_input == '\r' and current_choice == 2:
        # Change to about screen

        clear()
        about()
        clear()
        logo()
        return ('menu', current_choice, user_input)
    else:
        clear()
        return('pause', current_choice, user_input)
'''
