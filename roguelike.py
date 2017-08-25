from clear import resize_and_clear as clear
from movement import getch
from menu import menu


def main():
	menu_counter = 1
	while True:
		clear()
		menu(menu_counter%3)
		menu_counter+=1
		if menu_counter > 2 :
			menu_counter = 1
		user_input = getch()
		if user_input == 'p':
			break


if __name__ == "__main__":
	main()
	