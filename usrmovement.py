from colors import Colors
from time import sleep


def move(board, original, direction=None, change=0, last=None, player='@'):
    '''function that moves player character through the map
        board is a map (list)
        original is an original map (list)
        direction = [0-up, 1-right] (number)
        change = [1, -1] (number)
        current_pos is a tuple containing a position before move() is called
        '''
    message = None
    
    
    def down():
        '''function in charge of movig character up an down'''
        try:
            if board[last[0]+change][last[1]] == " " :
                board[last[0]+change][last[1]] = player
                board[last[0]][last[1]] = original[last[0]][last[1]]
                return True
            elif board[last[0]+change][last[1]] == "0":
                #here goes the intro
                print('aaaaa!!!!')
                sleep(2)
                return False
            else:
                board[last[0]][last[1]] = player
                return False
        except IndexError:
            board[last[0]][last[1]] = player
            return False
            
    def right():
        '''function in charge of moving character right and left'''
        try:
            if board[last[0]][last[1]+change] == " ":
                board[last[0]][last[1]+change] = player
                board[last[0]][last[1]] = original[last[0]][last[1]]
                return True
            elif board[last[0]+change][last[1]] == "0":
                #here goes the intro
                print('aaaaa!!!!')
                sleep(2)
                return False
            else:
                board[last[0]][last[1]] = player
                return False
        except IndexError:
            board[last[0]][last[1]] = player
            return False
    def idle():
        board[last[0]][last[1]] = player
    
    
        # there goes the code for movement ... still to do
        # the function should check if we want to move onto
        # the wall or not and each map should have a list of
        # characters which are specific to them or use unified
        # set of characters for walls lava portals trees etc
    if direction is None and change == 0 and last is None:
        pass
    elif direction == 0:
        if down():
            last = [last[0]+change,last[1]]
    elif direction == 1:
        if right():
            last = [last[0],last[1]+change]
    else:
        idle()

        
    return (last,board,message)

if __name__ == '__main__':
    # Do not run alone
    pass
