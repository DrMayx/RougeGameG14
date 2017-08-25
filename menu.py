def menu(number):
	with open('menu.uie') as picture:
		for line in picture:
			print(line[:-1])