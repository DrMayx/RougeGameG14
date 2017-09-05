from filehandling import unfile
from menu import logo
from movement import getch
from clear import resize_and_clear as clear


def display_menu(maps):
	logo()
	user_input = getch()
	# here go the buttons!!
	
	if user_input == '\x1b':
		return
	elif user_input == '\r':
		# Change map to lvl 1
		# Can be modified to show story

		clear()
		board = unfile(maps[1])
		original_board = unfile(maps[1])
		return (1, None, board, original_board)
		
	else:
		clear()
		logo()
		return 'menu'
	
	