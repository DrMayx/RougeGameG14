def logo():  # printing logo
    with open("menu.uie") as picture:
        for line in picture:
            print(line[:-1])


if __name__ == '__main__':
    # Do not run alone
    pass
