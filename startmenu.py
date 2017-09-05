from filehandling import unfile
from menu import logo
from movement import getch
from clear import resize_and_clear as clear
from button import change_button as button

def display_menu(maps, current_choice, last_input):
	user_input = last_input
	logo()
	current_choice = button(user_input, current_choice)
	user_input = getch()
	# here go the buttons!!
	
	if user_input == 'p':
		return
	elif user_input == 'o':
		# Change map to lvl 1
		# Can be modified to show story

		clear()
		board = unfile(maps[1])
		original_board = unfile(maps[1])
		return (1, None, board, original_board)
		
	else:
		clear()
		logo()
		return ('menu', current_choice, user_input)
	
	