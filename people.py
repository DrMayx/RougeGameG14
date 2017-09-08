from time import sleep
from clear import resize_and_clear as clear


def sage():
	clear()
	sage_picture = []
	story = []
	with open('story.txt') as text:
		for line in text:
			print(line)
			
	sleep(7)
	return True


def shop(player):
	clear()
	print("\n\n\nOne potion costs 10 coins.")
	print("\nTo buy one press 'b'")
	print("To exit the shop press 'e'")
	while True:
		user_input = getch()
		if user_input == 'b':
			if player.gold >= 10:
				player.potions += 1
				player.gold -= 10
				print("You bought a potion!")
				sleep(.7)
		elif user_input == 'e':
			break
			
# redefined because didnt want to work
def getch():
    '''function that takes first input
    character without confirming it with enter
    '''
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch.lower()
