from clear import resize_and_clear as clear
from movement import getch

def main():
	while True:
		clear()
		user_input = getch()
		if user_input == "":				#if users clicks escape button the program terminates
			break
		elif user_input == 'p':
			break


if __name__ == "__main__":
	main()
	