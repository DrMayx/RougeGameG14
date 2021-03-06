from random import randint
from time import sleep
from clear import resize_and_clear as clear


def fight(player,enemy):
    clear()
    print("You fight enemy lvl",enemy.level)
    quiz =[]
    if enemy.level == 1:
            forrest_fight(player, enemy)
    elif enemy.level == 3:
        boss_fight(player,enemy)
    else:
        quiz = get_quiz(enemy.level)
        while player.life>0:
            guessed = {"hot":0, "warm":0}
            clear()
            print('LIFES: ',player.life,"\tEXP: ", player.exp)
            print('Enemy lifes: ', enemy.life)
            user_guess = digit_guess(enemy.level)
            for i in range(enemy.level):
                if user_guess[i] == quiz[i]:
                    guessed["hot"]+=1
                elif user_guess[i] in quiz:
                    guessed["warm"]+=1
                    player.life-=1
            print("Hot " *guessed["hot"], "Warm " *guessed["warm"])
            print("\n")
            if guessed["hot"]==0 and guessed["warm"]==0:
                print("Cold")
                player.life-=1
            elif guessed["hot"] == enemy.level:
                print("HIT")
                quiz = get_quiz(enemy.level)
                enemy.life-=1
            if enemy.life <1:
                player.exp+=enemy.level
                print("EXPERIENCE INCREASED")
                break

            if player.life<1:
                break
                
            sleep(.7)
            
def digit_guess(level):
    while True:
        user_guess = input("Guess the number now!: ")
        if user_guess.isalpha():
            print("Guess a digit or it wont work!")
        elif len(user_guess) != level:
            print("This has to be exactly {0} digit!".format(level))
        else:
            return list(user_guess)
            
            
def forrest_fight(player, enemy):
        FIRST_LEVEL = 1
        quiz_number = randint(0, 9)
        print("\nTo kill a monster you have to crack 1 digit code!")
        while True:
            print('LIFES: ',player.life,"\tEXP: ", player.exp)
            print('Enemy lifes: ', enemy.life)
            user_guess = int(digit_guess(FIRST_LEVEL)[0])
            if quiz_number == user_guess:
                print("HIT")
                enemy.life-=1
                player.exp+=1
                break
            if quiz_number < user_guess:
                print('Your digit is too high!')
                player.life-=1
            if quiz_number > user_guess:
                print("Your digit is too low!")
                player.life-=1

            if player.life<1:
                break 
                
def get_quiz(level):
        quiz_number = []
        while len(quiz_number) < level:
            digit = randint(0, 9)
            if str(digit) not in quiz_number:
                quiz_number.append(str(digit))
        return quiz_number
    
    
def doors():
    clear()
    user_input = input("To destroy the door in front of you type 'DESTROY': ").upper()
    if user_input == 'DESTROY':
        return True
    else:
        return False    
    
def boss_fight(player,enemy):
    print_string_list = ''
    correct_answer = get_random_digits()
    while True:
        print_string_list = ''
        user_guess = get_user_input()
        result = compare_user_input_with_answer(user_guess, correct_answer)
        for element in result:
            print_string_list += element + ' '
        print(print_string_list)
        print_string_list = ''
        if check_result_three(result):
            print("WIN")
            player.exp+=100
            player.gold += 1000
            break
        else:
            player.life -= enemy.damage

def get_random_digits():
    correct_answer = []
    while len(correct_answer) < 3:
        digit = randint(0, 9)
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

def nie_chce_mi_chowac_tego_komentarza_wiec_zamykam_go_w_funkcji():            
    '''
    def forrest_fight():
    
    
    def forrest_fight(player, enemy):
    
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
                player.life -= enemy.damage
            if str(quiz_number) > user_guess:
                print("Your digit is too low!")
                player.life -= enemy.damage


    def digit_guess(level):
        while True:
            user_guess = input("Guess the number now!: ")
            if user_guess.isalpha():
                print("Guess a digit or it wont work!")
            elif len(user_guess) != level:
                print("This has to be exactly $d digit!" % level)
            else:
                return list(user_guess)

           
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
            else:
                player.life -= enemy.damage


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



    <<<<<<< HEAD

    #forrest_fight()
    #dungeon_fight()
    #boss_fight()
    =======
    >>>>>>> 076dba7309527605253065dc320734c89189e04a

'''
pass
