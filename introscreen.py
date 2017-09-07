from time import sleep
from movement import getch as getch


def intro():
    with open('intro_msg.uie') as intro_msg:
        for line in intro_msg:
            for char in line:
                """if getch():
                    return"""
                print(char, end="", flush=True)
                sleep(.005)
        sleep(1)
    print("\n\nClick any button to continue: ")
    user_input = getch()