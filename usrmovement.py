def move(board, direction=None, change=0, current_pos=None):
    '''function that moves player character through the map
        board is a map (list)
        direction = [0-up, 1-right] (number)
        change = [1, -1](number)
        current pos is a tuple containing a position before move() is called
        '''
    char = ""

    if direction is None or change == 0 or current_pos is None:
        pass
    elif change == 1 and direction == 0:
        # there goes the code for movement ... still to do
        # the function should check if we want to move onto
        # the wall or not and each map should have a list of
        # characters which are specific to them or use unified
        # set of characters for walls lava portals trees etc
        char = board[current_pos[0]][current_pos[1]]


if __name__ == '__main__':
    # Do not run alone
    pass
