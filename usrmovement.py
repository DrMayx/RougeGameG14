def move(file, direction, change=0, current_pos=None):
    '''function that moves player character through the map'''
    board = []
    with open(file, 'r+') as map_file:
        for line in map_file:
            board.append(el for el in line)


if __name__ == '__main__':
    # Do not run alone
    pass
