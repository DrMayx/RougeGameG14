from sys import stdout 
import os

def resize_and_clear():
	stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=150))
	os.system('cls' if os.name == 'nt' else 'clear')


def main():
	resize_and_clear()

main()