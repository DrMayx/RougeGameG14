
class bg_color:
    ''' colors used for background '''
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'
    end = '\033[0m'


class fg_color:
    ''' colors used for foreground '''
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'
    end = '\033[0m'


def button_on(button_type):
    if button_type == "start":
        with open('start_button.uie') as picture:
            for line in picture:
                print(bg_color.green + line[:-1] + bg_color.end)
    if button_type == "about":
        with open('about_button.uie') as picture:
            for line in picture:
                print(bg_color.green + line[:-1] + bg_color.end)
    if button_type == "high_scores":
        with open('highscore_button.uie') as picture:
            for line in picture:
                print(bg_color.green + line[:-1] + bg_color.end)
    if button_type == "exit":
        with open('exit_button.uie') as picture:
            for line in picture:
                print(bg_color.green + line[:-1] + bg_color.end)


def button_off(button_type):
    if button_type == "start":
        with open('start_button.uie') as picture:
            for line in picture:
                print(line[:-1])
    if button_type == "about":
        with open('about_button.uie') as picture:
            for line in picture:
                print(line[:-1])
    if button_type == "high_scores":
        with open('highscore_button.uie') as picture:
            for line in picture:
                print(line[:-1])
    if button_type == "exit":
        with open('exit_button.uie') as picture:
            for line in picture:
                print(line[:-1])


def select_button(current_choice):
    if current_choice == 0:
        button_on("start")
        button_off("about")
        button_off('high_scores')
        button_off("exit")
        current_choice += 1
        return current_choice
    if current_choice == 1:
        button_on("start")
        button_off("about")
        button_off('high_scores')
        button_off("exit")
        current_choice = 1
        return current_choice
    elif current_choice == 2:
        button_off("start")
        button_on("about")
        button_off('high_scores')
        button_off("exit")
        current_choice = 2
        return current_choice
    elif current_choice == 3:
        button_off("start")
        button_off('about')
        button_on("high_scores")
        button_off("exit")
        current_choice = 3
        return current_choice
    elif current_choice == 4:
        button_off("start")
        button_off("about")
        button_off('high_scores')
        button_on("exit")
        current_choice = 4
        return current_choice


def change_button(user_input, current_choice):
    if user_input == 'w':
        if current_choice == 1:
            current_choice = 1
        else:
            current_choice -= 1
    if user_input == 's':
        if current_choice == 4:
            current_choice = 4
        else:
            current_choice += 1
    if user_input == '':
        current_choice = 0
    current_choice = select_button(current_choice)
    return current_choice
