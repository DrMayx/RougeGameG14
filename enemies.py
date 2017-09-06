class Enemy:
	'''class containing all information about enemies'''
	# can contain coordinates
	
	enemy_char='<'
	
	def __init__(self,level= 0):
		self.level = level
		
		if level == 1 :
			self.life = 1
			self.damage = 1
		if level == 2:
			self.life == 2
			self.damage = 2
		if level == 3:
			self.life = 3
			self.damage = 3
			
	def spawn(self,board):
		from random import randint
		while True:
			self.x_coord = randint(0, len(board[0])-1)
			self.y_coord = randint(0, len(board)-1)
			if board[self.y_coord][self.x_coord] == " ":
				break

			
