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
    
    user.reset()
    logo()
    
    current_choice = button(user_input, current_choice)
    
    print('\n\n')
    print("player:".rjust(65), "name:".rjust(24))
    print(user.player_char.rjust(71), user.name.rjust(27))
    user_input = getch()

    if user_input == '\r' and current_choice == 4:
        return
    if user_input == '\r' and current_choice == 1:
        # Change map to lvl 1
        # Can be modified to show story

        clear()
        #intro()
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

def inventory(player):
    # numbers in rjust are calculated to sum up 
    # with characters to 55 becase this is the length of first print
    # all is made to be a visual representation of what is to be printed
    print("=============================================")
    print("#")
    print('#', "Gold:".rjust(19),
          '{}'.rjust(11).format(player.gold))
    print('#', "Helath potions:".rjust(19),
          '{}'.rjust(11).format(player.potions))
    print("#")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print('#', '\x1b[0;33m{}\x1b[0m'.rjust(10).format(player.name),
          '{}'.rjust(5).format(player.player_char),
          'Life:'.rjust(8),
          '{}'.rjust(10).format(player.life))
    print('#')
    print('#', 'Level:'.rjust(19),
          '{}'.rjust(11).format(player.level))
    print('#', 'Experience:'.rjust(19),
          '{}'.rjust(11).format(player.exp))
    print('#', 'Enemies killed:'.rjust(19),
          '{}'.rjust(11).format(player.enemies_killed))
    print('#')
    print('=============================================')
    print('\nTo exit press any key.\n')
    getch()
    
def hall_of_fame(player):
    score = player.enemies_killed*player.level + player.lifes + player.exp
    hscores = []
    with open('hscores') as table:
        for line in table:
            hscores.append(line.split(','))
    if score >= hscores[0][1]:
        to_write = str(score) + ',' + str(player.name)
        print('TOP SCORE : ', player.name, ": ", score)
        with open('hscores','w') as table:
            table.write(to_write)
    else:
        print('TOP SCORE : ', hscores[1], ": ", hscores[0])
