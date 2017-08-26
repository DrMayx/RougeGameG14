def print_map():
	with open("respawn.map") as board:
		for line in board:
			print(line[:-1])
