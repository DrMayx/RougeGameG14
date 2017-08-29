from sys import stdout
import os


def resize_and_clear(row=50, col=150):
    '''Resize the console and clear it'''
    stdout.write("\x1b[8;{rows};{cols}t".format(rows=row, cols=col))
    print("\n" * 5)
    os.system('clear')


if __name__ == '__main__':
    # Do not run alone
    pass
