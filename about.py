from movement import getch
from time import sleep


def print_about():
    into = "10000101010101000101000010100100100101111010001010010010011000001000010001111100101001001\n"
    for char in into:
        print(char.rjust(96), end="", flush=True)
        sleep(.03)
    with open('about_msg.uie') as intro_msg:
        for line in intro_msg:
            for char in line:
                """if getch():
                    return"""
                print(char, end="", flush=True)
                sleep(.005)
        sleep(1)
    print("\n\nClick any button to come back to menu: ")
    user_input = getch()
       