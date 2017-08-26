from clear import resize_and_clear as clear
from movement import getch
from menu import menu
from printmap import print_map
from time import sleep

def exit():
	exit_msg = "Do you really want to exit[Y/N] ? "
	for char in exit_msg:
		print(char,end="",flush=True)
		sleep(.03) 
	

def main(): # todo add those fucking boards!!
	clear()
	menu()
	user_input = getch()
	while True:
		if user_input == 'p':
			exit()
			safety = getch()
			clear(24,80)
			break
		if user_input == 'o':
			clear()
			print_map()
		else:
			clear()
			menu()
		user_input = getch()


if __name__ == "__main__":
	main()
	