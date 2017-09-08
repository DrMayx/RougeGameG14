# Importing all nescessary modules
from sys import exit as forcequit
from clear import resize_and_clear as clear
from movement import getch
from movement import move
from printmap import print_map
from time import sleep
from filehandling import unfile
from menus import display_menu
from menus import inventory
from enemies import Enemy
from player import Player
from colors import Colors
from random import randint
from lost import loose_game as lost
import os


def exit():
    '''function printing exit message and checks
    the safety input for confirmation to exit.
    Also in future will check for specific key to exit
    '''
    exit_msg = "Do you really want to exit[Y/N] ? "
    for char in exit_msg:
        print(char, end="", flush=True)
        sleep(.03)
    while True:
        safety_check = getch()
        if safety_check == 'y':
            clear(24,80)
            forcequit()
        elif safety_check == 'n':
            break
        else:
            print("\n\nYou have to press [Y] or [N]")



def main():
    '''main function of the game'''
    if os.name == 'nt':
        # System check. App works only on unix system
        # Caused by getch function and console clearing
        # Can be fixed by implementing msvcrt library
        print("This application is meant for unix devices.")
        print("Closing the program.")
        sleep(2)
        forcequit()
    
    player = Player()
    
    args={
    # Define map numbers
        'maps' : {
            0: "menu",
            1: "respawn.map",
            2: "forest.map",
            3: "dungeon.map",
            4: "boss.map",
            5: "end.map",
            },       
            'map_id' : 0,
            'board' : [],
            'current_choice' : 1,
            'last_input' : '',
            'direction' : None,
            'change' : 0,
            'enemies' : [1,True],
            'player' : player,
            'last_pos' : '',
                }
        
    clear()
    while True:
        '''main loop of the game'''
        clear()
        # mapcheck
        ############################################   MAP MENU  ########################################################
        if args['map_id'] == 0:
            status = display_menu(args)
            if status is None:
                exit()
            elif status[0] == args['maps'][0]:
                args['map_id'] = 0
                args['current_choice'] = status[1]
                args['last_input'] = status[2]

            else:
                args['map_id'] = status[0]
                args['last_pos'] = status[1]
                args['board'] = status[2]
        ############################################   MAP SPAWN ########################################################
        elif args['map_id'] == 1:
            if args['last_pos'] is None:
                args['last_pos'] = (33,60)
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
            # If on certain map stay on that map
            # Can be implemented as a standalone function
            print_map(args['board'])
            user_input = getch()
            if user_input == 'p':
                clear(24,80)
                break
            elif user_input == 'w':
                args['direction'] = 0
                args['change'] = -1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                if change[2] is not None:
                    args['map_id'] = change[2]
                    args['board'] = unfile(args['maps'][change[2]])
                    args['last_pos'] = None
                    args['enemies'] = [1, True]
            elif user_input == 's':
                args['direction'] = 0
                args['change'] = 1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
            elif user_input == 'a':
                args['direction'] = 1
                args['change'] = -1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
            elif user_input == 'd':
                args['direction'] = 1
                args['change'] = 1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
            elif user_input == 'i':
                clear()
                inventory(player)
            else:
                exit()
                
                
        ############################################  MAP FOREST ########################################################
        elif args['map_id'] == 2:
            
            enemies_left = 0
            print(enemies_left,' b4')
            if args['last_pos'] is None:
                args['last_pos'] = (3,50)
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                
            if args['enemies'][1]:
                for i in range(10):
                    if randint(0,1):
                        args['enemies'].append(Enemy(1))
                        args['enemies'][0]+=1
                        args['enemies'][args['enemies'][0]].spawn(args['board'])
                        args['board'][args['enemies'][args['enemies'][0]].y_coord][args['enemies'][args['enemies'][0]].x_coord] = args['enemies'][args['enemies'][0]].enemy_char
                if args['enemies'][0] < 2:
                    args['enemies'].append(Enemy(1))
                    args['enemies'][0]+=1
                    args['enemies'][args['enemies'][0]].spawn(args['board'])
                    args['board'][args['enemies'][args['enemies'][0]].y_coord][args['enemies'][args['enemies'][0]].x_coord] = args['enemies'][args['enemies'][0]].enemy_char
            
                args['enemies'][1] = False
            
            print_map(args['board'])
            
            user_input = getch()
            if user_input == 'p':
                clear(24,80)
                break
            elif user_input == 'w':
                args['direction'] = 0
                args['change'] = -1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                if change[2] is not None:
                    args['map_id'] = args['maps'][change[2]]
            elif user_input == 's':
                args['direction'] = 0
                args['change'] = 1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                if change[2] is not None:
                    args['map_id'] = args['maps'][change[2]]
            elif user_input == 'a':
                args['direction'] = 1
                args['change'] = -1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                if change[2] is not None:
                    args['map_id'] = maps[change[2]]
            elif user_input == 'd':
                args['direction'] = 1
                args['change'] = 1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                if change[2] is not None:
                    args['map_id'] = maps[change[2]]
            elif user_input == 'q':
                if player.potions > 0:
                    player.life += player.level*2
                    player.potions -= 1
            elif user_input == 'i':
                clear()
                inventory(player)
            else:
                exit()
                
                
            for line in args['board']:
                if args['enemies'][2].enemy_char in line:
                    print(line)
                    enemies_left +=1
            print(enemies_left,' aftr')
        
            if enemies_left == 0:
                print("Level clear!")
                sleep(1)
                args['map_id'] = 1
                args['current_choice'] = 1
                args['board'] = unfile(args['maps'][1])
                args['last_pos'] = None
                    
        ############################################ MAP DUNGEON ########################################################
        if args['map_id'] == 3:
            
            enemies_left = 0
            clear()
            
            if args['last_pos'] is None:
                args['last_pos'] = (19,109)
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                
            if args['enemies'][1]:
                args['enemies_left'] = 0
                for i in range(15):
                    if randint(0,1):
                        args['enemies'].append(Enemy(2))
                        args['enemies'][0]+=1
                        args['enemies'][args['enemies'][0]].spawn(args['board'])
                        args['board'][args['enemies'][args['enemies'][0]].y_coord][args['enemies'][args['enemies'][0]].x_coord] = args['enemies'][args['enemies'][0]].enemy_char
                if args['enemies'][0] < 2:
                    args['enemies'].append(Enemy(2))
                    args['enemies'][0]+=1
                    args['enemies'][args['enemies'][0]].spawn(args['board'])
                    args['board'][args['enemies'][args['enemies'][0]].y_coord][args['enemies'][args['enemies'][0]].x_coord] = args['enemies'][args['enemies'][0]].enemy_char
            
                args['enemies'][1] = False
            
            print_map(args['board'])
            
            user_input = getch()
            if user_input == 'p':
                clear(24,80)
                break
            elif user_input == 'w':
                args['direction'] = 0
                args['change'] = -1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                if change[2] is not None:
                    args['map_id'] = args['maps'][change[2]]
            elif user_input == 's':
                args['direction'] = 0
                args['change'] = 1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                if change[2] is not None:
                    args['map_id'] = args['maps'][change[2]]
            elif user_input == 'a':
                args['direction'] = 1
                args['change'] = -1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                if change[2] is not None:
                    args['map_id'] = maps[change[2]]
            elif user_input == 'd':
                args['direction'] = 1
                args['change'] = 1
                change = move(args)
                args['last_pos'] = change[0]
                args['board'] = change[1]
                if change[2] is not None:
                    args['map_id'] = maps[change[2]]
            elif user_input == 'q':
                if player.potions > 0:
                    player.life += player.level*2
                    player.potions -= 1
            elif user_input == 'i':
                clear()
                inventory(player)
            else:
                exit()
                
            
            for line in args['board']:
                if args['enemies'][2].enemy_char in line:
                    enemies_left +=1
                    
            if enemies_left == 0:
                print("Level clear!")
                sleep(1)
                args['map_id'] = 1
                args['current_choice'] = 1
                args['board'] = unfile(args['maps'][1])
                args['last_pos'] = None
                        
        
        if args['player'].life == 0:
            clear()
            lost()
            sleep(3)
            args['map_id'] = 0
            args['current_choice'] = 1
            args['last_pos'] = None
if __name__ == "__main__":
    # Check if running as main module
    main()
