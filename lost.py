from time import sleep
import random
from clear import resize_and_clear as clear
import sys


def loose_game():
    counter = 0
    into = ["UUUUU"]
    while counter < 200:
        print(into[0].rjust(30), end="", flush=True)
        print(into[0].rjust(70), end="", flush=True)
        print(into[0].rjust(100), end="", flush=True)
        sleep(.01)
        counter += 1
    clear()
    with open('loose_msg.uie') as intro_msg:
        for line in intro_msg:
            for char in line:
                print(char, end="", flush=True)
                sleep(.005)
                