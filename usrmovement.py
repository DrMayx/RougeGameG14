def move(file, direction, change=0,current_pos = None):
	board = []
	with open(file,'r+') as map_file:
		for line in map_file:
			board.append(el for el in line)
			
