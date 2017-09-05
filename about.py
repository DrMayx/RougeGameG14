from movement import getch
import time


def print_about():
    about = "~~Authors of this project are anonymous for now but maybe in future someone will tell a word or two"
    for char in about:
        print(char, end="", flush=True)
        time.sleep(.03)
    print("\n\nClick any button to come back to menu: ")
    user_input = getch()
       