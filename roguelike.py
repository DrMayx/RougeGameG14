from sys import exit as forcequit
from clear import resize_and_clear as clear
from movement import getch
from menu import menu
from printmap import print_map
from time import sleep
from filehandling import unfile
import os


def exit():
	exit_msg = "Do you really want to exit[Y/N] ? "
	for char in exit_msg:
		print(char,end="",flush=True)
		sleep(.03) 
	

def main():
	if 	os.name == 'nt':
		print("This application is meant for unix devices.\nClosing the program.")
		sleep(2)
		forcequit()
		
	maps={
		0:"menu",
		1:"respawn.map",
		2:"forrest.map",
		3:"dungeon.map",
		4:"boss.map",
		5:"end.map"
		}
	map_id = 0
	board = []
	clear()
	while True:
		clear()
		#mapcheck
		if map_id == 0:
			menu()
			user_input = getch()
			if user_input == 'p':
				exit()
				safety = getch()
				clear(24,80)
				break
			if user_input == 'o':
				clear()
				map_id = 1
				board = unfile(maps[map_id])
			else:
				clear()
				menu()
		if map_id == 1:
			print_map(board)
			user_input = getch()
			if user_input == 'p':
				exit()
				safety = getch()
				clear(24,80)
				break
		
		


if __name__ == "__main__":
	main()
	