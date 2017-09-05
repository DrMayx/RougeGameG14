from colors import Colors
from time import sleep
from people import sage


def move(board, original, direction=None, change=0, last=None, player='\033[34m@\x1b[0m'):
    '''function that moves player character through the map
        board is a map (list)
        original is an original map (list)
        direction = [0-up, 1-right] (number)
        change = [1, -1] (number)
        current_pos is a tuple containing a position before move() is called
        player is the default player icon (character)
        '''
    output = None
    
    
    def move_down():
        '''function in charge of movig character up an down'''
        try:
            if board[last[0]+change][last[1]] == " " :
                # movement only on floor that is " "
                board[last[0]+change][last[1]] = player
                board[last[0]][last[1]] = original[last[0]][last[1]]
                return True
            elif board[last[0]+change][last[1]] == "0":
                #here goes the things that sage wants to say
                sage()
                return False
            elif board[last[0]+change][last[1]] == (Colors.portal + "$" + Colors.end):
                board[last[0]+change][last[1]] = player
                board[last[0]][last[1]] = original[last[0]][last[1]]
                output = 2
                return (True,output)
            else:
                idle()
                return False
        except IndexError:
            idle()
            return False
            
            
    def move_right():
        '''function in charge of moving character right and left'''
        try:
            if board[last[0]][last[1]+change] == " ":
                # movement only on floor that is " "
                board[last[0]][last[1]+change] = player
                board[last[0]][last[1]] = original[last[0]][last[1]]
                return True
            elif board[last[0]][last[1]+change] == "0":
                #here goes the intro
                sage()
                return False
            elif board[last[0]][last[1]+change] == (Colors.portal + "$" + Colors.end):
                board[last[0]][last[1]+change] = player
                board[last[0]][last[1]] = original[last[0]][last[1]]
                output = 2
                return (True,output)
            else:
                idle()
                return False
        except IndexError:
            idle()
            return False
        
        
    def idle():
        board[last[0]][last[1]] = player
    
    
    if direction is None and change == 0 and last is None:
        pass
    elif direction == 0:
        check = move_down()
        if check:
            last = [last[0]+change,last[1]]
            try:
                if any(( c in str(check[1]) ) for c in '234'):
                    output = check[1]
            except IndexError:
                pass
            except TypeError:
                print('check: ', check)
    elif direction == 1:
        check = move_right()
        if check:
            last = [last[0],last[1]+change]
            try:
                if any(( c in str(check[1]) ) for c in '234'):
                    output = check[1]
            except IndexError:
                pass
            except TypeError:
                print('check: ', check)
    else:
        idle()

      
    return (last,board,output)


def attack():
    pass


if __name__ == '__main__':
    # Do not run alone
    pass


def getch():
    '''function that takes first input
    character without confirming it with enter
    '''
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch.lower()


if __name__ == '__main__':
        # Do not run alone
    pass
