# Importing all nescessary modules
from sys import exit as forcequit
from clear import resize_and_clear as clear
from movement import getch
from printmap import print_map
from time import sleep
from usrmovement import move
from startmenu import display_menu
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
    safety = getch()
    clear(24, 80)


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

    # Define map numbers
    maps = {
        0: "menu",
        1: "respawn.map",
        2: "forrest.map",
        3: "dungeon.map",
        4: "boss.map",
        5: "end.map"
    }
    map_id = 0
    board = []
    clear()
    while True:
        '''main loop of the game'''
        clear()
        # mapcheck
        if map_id == 0:
            status = display_menu(maps)
            if status == None:
                exit()
                break
            if status == maps[0]:
                map_id = 0
            else:
                map_id = status[0]
                last_pos = status[1]
                board = status[2]
                original_board = status[3]
        if map_id == 1:
            print(last_pos)
            if last_pos is None:
                change = move(board,original_board,last=(33,59))
                last_pos=change[0]
                board=change[1]
            # If on certain map stay on that map
            # Can be implemented as a standalone function
            print_map(board)
            user_input = getch()
            if user_input == 'p':
                exit()
                break
            elif user_input == 'w':
                change = move(board,original_board,0,-1,last_pos)
                last_pos=change[0]
                board=change[1]
            elif user_input == 's':
                change = move(board,original_board,0,1,last_pos)
                last_pos=change[0]
                board=change[1]
            elif user_input == 'a':
                change = move(board,original_board,1,-1,last_pos)
                last_pos=change[0]
                board=change[1]
            elif user_input == 'd':
                change = move(board,original_board,1,1,last_pos)
                last_pos=change[0]
                board=change[1]
        sleep(.05)


if __name__ == "__main__":
    # Check if running as main module
    main()
