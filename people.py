from time import sleep
from clear import resize_and_clear as clear


def sage():
	clear()
	sage_picture = []
	story = []
	with open('sage.g') as picture:
		for line in picture:
			sage_picture.append(line)
	with open('story.txt') as text:
		for line in text:
			story.append(line)
			
	line_counter=0
	for picture in sage_picture:
		line = ""
		if line_counter<len(story):
			line+=story[line_counter][:-1].rjust(64)
			line+= picture[:-1]
		else:
			line+=picture[:-1].rjust(150)
		print(line)
		line_counter+=1
	sleep(5)