from colors import Colors
from time import sleep
from people import sage
from people import shop
from fightmodule import fight
from random import randint
from fightmodule import doors

# board, direction=None, change=0, last=None, user=None, enemy=None
def move(args):
    '''function that moves user character through the map
        board is a map (list)
        direction = [0-up, 1-right] (number)
        change = [1, -1] (number)
        user is the default user icon (character)
        '''
    
    
    board = args['board']
    direction = args['direction']
    change = args['change']
    last = args['last_pos']
    user = args['player']
    enemy = args['enemies']
    enemies_left = args['enemies'][0]
        
    try:
        user_cpy = user
        character = user.player_char
    except TypeError:
        print(user)
        sleep(5)
        return
    
    output = None
    
    def move_down(player, enemies):
        '''function in charge of movig character up an down'''
        enemies_left = enemies[0]
        for element in enemies:
            try:
                if element.x_coord == last[1] and element.y_coord == (last[0]+change):
                    enemy = element
            except AttributeError:
                pass
        try:
            if board[last[0]+change][last[1]] == ' ':
                # movement only on floor that is " "
                board[last[0]+change][last[1]] = character
                board[last[0]][last[1]] = " "
                return True
            elif board[last[0]+change][last[1]] == '0':
                #here goes the things that sage wants to say
                if player.if_sage == False:
                    player.if_sage = sage()
                else:
                    shop(player)
                return False
            elif board[last[0]+change][last[1]] == Colors.portal + '$' + Colors.end:
                board[last[0]][last[1]] = " "
                output = 2
                return (True,output)
            elif board[last[0]+change][last[1]] == Colors.portal + '*' + Colors.end:
                if player.level >= 2:
                    board[last[0]][last[1]] = ' '
                    output = 3
                    return (True, output)
                else:
                    return False
            elif board[last[0]+change][last[1]] == Colors.portal + '^' + Colors.end:
                from enemies import Enemy
                

                enemy = Enemy(3)
                fight(player,enemy)
                from win import wingame as win
                #win()
            elif '<' in board[last[0]+change][last[1]]:
                fight(player,enemy)
                if enemy.life == 0:
                    board[enemy.y_coord][enemy.x_coord] = Colors.money + 'o' + Colors.end
                    args['enemies'][0] -= 1
                    player.enemies_killed +=1
                return False
            elif 'o' in board[last[0]+change][last[1]]:
                player.gold += enemy.level*randint(1, 10)
                board[last[0]+change][last[1]] = character
                board[last[0]][last[1]] = ' '
                return True
            elif board[last[0]+change][last[1]] == '=':
                if doors():
                    board[last[0]+change][last[1]] = ' '
                return False
            else:
                idle()
                return False
        except IndexError:
            idle()
            return False
            
            
    def move_right(player, enemies):
        '''function in charge of moving character right and left'''
        enemies_left = enemies[0]
        for element in enemies:
            try:
                if element.x_coord == (last[1]+change) and element.y_coord == last[0]:
                    enemy = element
            except AttributeError:
                pass
        try:
            if board[last[0]][last[1]+change] == " ":
                # movement only on floor that is " "
                board[last[0]][last[1]+change] = character
                board[last[0]][last[1]] = " "
                return True
            elif board[last[0]][last[1]+change] == "0":
                #here goes the intro
                if player.if_sage == False:
                    player.if_sage = sage()
                else:
                    shop(player)
                return False
            elif '<' in board[last[0]][last[1]+change]:
                fight(player,enemy)
                if enemy.life == 0:
                    board[enemy.y_coord][enemy.x_coord] = Colors.money + 'o' + Colors.end
                    args['enemies'][0] -= 1
                    player.enemies_killed +=1
                return False
            elif 'o' in board[last[0]][last[1]+change]:
                player.gold += enemy.level*randint(1, 10)
                board[last[0]][last[1]+change] = character
                board[last[0]][last[1]] = ' '
                return True
            elif board[last[0]][last[1]+change] == '=':
                if doors():
                    board[last[0]][last[1]+change] = ' '
                return False
            else:
                idle()
                return False
        except IndexError:
            idle()
            return False
        
        
    def idle():
        board[last[0]][last[1]] = character
    
    
    if direction is None and change == 0 and last is None:
        pass
    elif direction == 0:
        check = move_down(user, enemy)
        if check:
            last = [last[0]+change,last[1]]
            try:
                if any(( c in str(check[1]) ) for c in '234'):
                    output = check[1]
            except IndexError:
                pass
            except TypeError:
                pass
    elif direction == 1:
        check = move_right(user, enemy)
        if check:
            last = [last[0],last[1]+change]
            try:
                if any(( c in str(check[1]) ) for c in '234'):
                    output = check[1]
            except IndexError:
                pass
            except TypeError:
                pass
    else:
        idle()
    
    args['enemies'][0] = enemies_left
    return (last,board,output)


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
