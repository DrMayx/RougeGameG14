class Player:
	'''contains all information about player character'''
	# can contain coordinates ...\
	def __init__(self):
		# character creator
		def character_creator():
			from clear import resize_and_clear as clear
			from time import sleep
			clear()
			allowed_chars='@&QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890_'
			
			while True:
				message = "\n\n\n\n\nWhat's Your name ?\n"
				for char in message:
					print(char, end="", flush=True)
					sleep(.02)
				user_name = input()
				if user_name == '':
					return ('Test','@')
				elif all((c in allowed_chars[2:]) for c in user_name):
					break
				else:
					print("wrong input!")
					sleep(.5)
					clear()

			while True:
				print("\n\nYou can choose which sign you want to be: ")
				message = "Choose Your Hero:\n"
				heroes = "@\t&\t[A-Z]\n"
				for char in message:
					print(char, end="", flush=True)
					sleep(.02)
				for char in heroes:
					print(char, end="", flush=True)
					sleep(.02)
				user_char = input()
				if user_char == '':
					self.level = 100
					self.gold = 25
					return (user_name, '@')
				elif len(user_char) > 1 or user_char not in allowed_chars[:27]:
					print("wrong input!")
					sleep(.5)
					clear()
				else:
					return (user_name,user_char)
			
		
		creator = character_creator()
		
		self.name = creator[0]
		self.player_char = "\033[34m" + creator[1] + "\033[0m"
		self.level = 10
		self.enemies_killed = 0
		self.exp = 0
		self.life=10 * self.level
		self.if_sage = False
		self.gold = 0
		self.potions = 0
		
	def reset(self):
		self.level = 10
		self.enemies_killed = 0
		self.exp = 0
		self.life=10 * self.level
		self.if_sage = False
		self.gold = 0
		self.potions = 0
