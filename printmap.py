def print_map(file):
	with open(file) as map:
		for line in map:
			print(line[:-1])
			