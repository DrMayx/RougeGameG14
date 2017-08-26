class Colors:
	wall = "\x1b[0;30;40m"
	human = "\x1b[2;33m"
	portal = "\x1b[0;35;45m"
	comment = "\x1b[0;32;40m"
	floor = "\x1b[4;30;47m"
	end = "\x1b[0m"
	

def unfile(filename):
	outcome_list = []
	row_counter=0
	to_print = ""
	with open(filename) as file:
		for line in file:
			outcome_list.append([])
			for char in line:
				if char == "#":			#wall coloring
					to_print = Colors.wall + char + Colors.end
				elif char == "0" :
					to_print = Colors.human + char + Colors.end
				elif char == "$":
					to_print = Colors.portal + char + Colors.end
				elif char == "/":
					to_print = Colors.comment + char
				elif char == "\\":
					to_print =  char + Colors.end
				elif char == "H":
					to_print = Colors.floor + char + Colors.end
				else:
					to_print = char
				outcome_list[row_counter].append(to_print)
			row_counter+=1
	return outcome_list