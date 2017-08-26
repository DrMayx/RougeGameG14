from clear import resize_and_clear as clear
from movement import getch
from menu import menu


def main(): # todo add those fucking boards!!
	menu_counter = 1
	while True:
		clear()
		menu()
		user_input = getch()
		if user_input == 'p':
			break


if __name__ == "__main__":
	main()
	