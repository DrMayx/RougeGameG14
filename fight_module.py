import random


def forrest_fight():
    quiz_number = []
    quiz_number = random.randint(0, 9)
    print("\nTo kill a monster you have to crack 1 digit code!")
    while True:
        user_guess = digit_guess()
        if str(quiz_number) == user_guess:
            print("HIT")
            break
        if str(quiz_number) < user_guess:
            print('Your digit is too high!')

        if str(quiz_number) > user_guess:
            print("Your digit is too low!")


def digit_guess():
    while True:
        user_guess = input("Guess the digit now!: ")
        if user_guess.isalpha():
            print("Guess a digit or it wont work!")
        elif len(user_guess) != 1:
            print("This has to be exactly one digit!")
        else:
            return user_guess

           
def dungeon_fight():
    print_string_list = ''
    quiz_number = get_two_digit_quiz()
    print(quiz_number)
    print("\nTo kill a monster you have to crack 2 digit code!")
    print("\nHOT - number on correct position" + "\nWARM - number in the code" + "\nCOLD - number not in code")
    while True:
        user_guess = input_two_digit_code()
        hint_list = check_two_digit_code(user_guess, quiz_number)
        for element in hint_list:
            print_string_list += element + ' '
        print(print_string_list)
        if check_result_two(hint_list):
            print("WIN")
            break


def get_two_digit_quiz():
    quiz_number = []
    while len(quiz_number) < 2:
        digit = random.randint(0, 9)
        if digit not in quiz_number:
            quiz_number.append(digit)
    return quiz_number


def input_two_digit_code():
    while True:
        guess = input('Enter two digit code: ')
        if guess.isalpha():
            print('Guess a digit or it won\'t work!')
        elif len(guess) > 2 or len(guess) < 2:
            print('Your code has to have exactly 2 digits!')
        else:
            return list(guess)


def check_two_digit_code(user_guess, quiz_number):
    index = 0
    hint_list = []
    for a in quiz_number:
        if str(a) == user_guess[index]:
            hint_list.insert(0, 'HOT')
        elif str(a) in user_guess:
            hint_list.append('WARM')
        index += 1
    if not hint_list:
        hint_list.append('COLD')

    return hint_list


def check_result_two(hint_list):
    if hint_list == ['HOT']*2:
        return True


def boss_fight():
    print_string_list = ''
    correct_answer = get_random_digits()
    while True:
        user_guess = get_user_input()
        result = compare_user_input_with_answer(user_guess, correct_answer)
        for element in result:
            print_string_list += element + ' '
        print(print_string_list)
        print_string_list = ''
        if check_result_three(result):
            print("WIN")
            break


def get_random_digits():
    correct_answer = []
    while len(correct_answer) < 3:
        digit = random.randint(0, 9)
        if digit not in correct_answer:
            correct_answer.append(digit)
    return correct_answer


def get_user_input():
    while True:
        user_guess = input('Enter three digit code: ')
        if user_guess.isalpha():
            print('Guess a digit or it won\'t work!')
        elif len(user_guess) != 3:
            print('Your code has to have exactly 3 digits!')
        else:
            return list(user_guess)


def compare_user_input_with_answer(user_guess, correct_answer):
    index = 0
    hint_list = []
    for a in correct_answer:
        if str(a) == user_guess[index]:
            hint_list.insert(0, 'HOT')
        elif str(a) in user_guess:
            hint_list.append("WARM")
        index += 1
    if not hint_list:
        hint_list.append("COLD")

    return hint_list


def check_result_three(hint_list):
    if hint_list == ["HOT"] * 3:
        return True

#forrest_fight()
dungeon_fight()
boss_fight()
