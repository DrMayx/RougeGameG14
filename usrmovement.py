def move(board, original, direction=None, change=0, current_pos=None, player='@'):
    '''function that moves player character through the map
        board is a map (list)
        original is an original map (list)
        direction = [0-up, 1-right] (number)
        change = [1, -1] (number)
        current_pos is a tuple containing a position before move() is called
        '''
    
    
    last = [current_pos[0],current_pos[1]]
    
    def up():   # z jakiegoś powodu nie podmienia poprzedniego znaku ...
        try:
            if board[last[0]-1][last[1]] == "H":
                board[last[0]-1][last[1]] = player
                board[last[0]][last[1]] = original[last[0]][last[1]]
            else:
                board[last[0]][last[1]] = player
        except IndexError:
            board[last[0]][last[1]] = player
            
    def down():
        pass
    def right():
        pass
    def left():
        pass
    
    
        # there goes the code for movement ... still to do
        # the function should check if we want to move onto
        # the wall or not and each map should have a list of
        # characters which are specific to them or use unified
        # set of characters for walls lava portals trees etc
    if direction is None or change == 0 or current_pos is None:
        pass
    elif direction == 0:
        if change == 1:
            up()
            last = [last[0]-1,last[1]]
        elif change == -1:
            down()
        else:
            pass
    elif direction == 1:
        if change == 1:
            right()
        elif change == 0:
            left()
        else:
            pass
        
        

        
    return (last,board)

if __name__ == '__main__':
    # Do not run alone
    pass
