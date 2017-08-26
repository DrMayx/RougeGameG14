def menu():		#printing logo
	with open("menu.uie") as picture:
		for line in picture:
			print(line[:-1])
