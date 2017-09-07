from movement import getch
import time


def print_about():
    into = "10000101010101000101000010100100100101111010001010010010011000001000010001111100101001001\n"
    for char in into:
        print(char.rjust(96), end="", flush=True)
        time.sleep(.03)
    lines = ["The game is about a gladiator which travel through virtual dimensions - computer forrest, memory dungeon and fight with mad bug boss",
    "\n To complete his journey he has to crack a lot of code!",
    "That\'s a hell lot of trouble for one hero! \n But we believe that you can do it!",
    "\n\nTHIS GAME WAS CREATED BY: \n Maciej Jankowicz & Kuba Mikolajczyk",
    "\n\n ALL RIGHT RESERVED FOR CODECOOL ;)"]
    for char  in lines:
        print(char, end="", flush=True)
        time.sleep(.03)
    print("\n\nClick any button to come back to menu: ")
    user_input = getch()
       