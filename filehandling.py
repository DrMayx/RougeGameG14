from colors import Colors


def unfile(filename):
    '''function that reads the file and writes
    it's insides to a list also colors every
    character with a specified color
    '''
    outcome_list = []
    row_counter = 0
    to_print = ""
    with open(filename) as file:
        for line in file:
            outcome_list.append([])
            for char in line:
                if char == "#":  # wall coloring
                    to_print = Colors.wall + char + Colors.end
                elif char == "$" or char == '*' or char == '^':  # portal coloring
                    to_print = Colors.portal + char + Colors.end
                elif char == "/":  # comment start coloring
                    to_print = Colors.comment + char
                elif char == "\\":  # comment end coloring
                    to_print = char + Colors.end
                elif char == '|':   #tree foot coloring
                    to_print = Colors.tree + char + Colors.end
                elif char == '8' or char == 'n':
                    to_print = Colors.leafs + char + Colors.end
                else:
                    to_print = char
                outcome_list[row_counter].append(to_print)
            row_counter += 1
    return outcome_list


if __name__ == '__main__':
    # Do not run alone
    pass
