def menu():
	with open('menu.uie') as picture:		#printing logo
		for line in picture:
			print(line[:-1])