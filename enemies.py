class Enemy:
	'''class containing all information about enemies'''
	# can contain coordinates
	
	enemy_char='\x1b[1;32;41m<\x1b[0m'
	
	def __init__(self,level= 0):
		self.level = level
		if level == 1 :
			self.life = 1
			self.damage = 1
		elif level == 2:
			self.life = level
			self.damage = level
		elif level == 3:
			self.life = 3
			self.damage = 3
			
	def spawn(self,board):
		from random import randint
		while True:
			self.x_coord = randint(0, len(board[0])-1)
			self.y_coord = randint(0, len(board)-1)
			if board[self.y_coord][self.x_coord] == " ":
				break
			
