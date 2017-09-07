from time import sleep
from movement import getch as getch
import random
from clear import resize_and_clear as clear
from roguelike import exit

def win():
    counter = 0
    into = ["YOU WIN"]
    while counter < 100:
        print(into[0].rjust(random.randint(0, 101)), end="", flush=True)
        sleep(.03)
        counter += 1
    while counter < 200:
        print(into[0].rjust(30), end="", flush=True)
        sleep(.03)
        counter += 1
    while counter < 300:
        print(into[0].rjust(30), end="", flush=True)
        print(into[0].rjust(70), end="", flush=True)
        print(into[0].rjust(100), end="", flush=True)
        sleep(.01)
        counter += 1
    clear()
    with open('trophy.uie') as intro_msg:
        for line in intro_msg:
            for char in line:
                print(char, end="", flush=True)
                sleep(.005)
    exit()


win()