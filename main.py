import sys
from random import randint, choice, shuffle


def yes_or_not(answer):   # Function that checks if the user entered YES or NO
    while True:

        if answer == 'yes':
            answer = True
            return answer
        elif answer == 'no':
            answer = False
            return answer
        else:
            answer = input('Please give a yes or no answer: ')
            print()


def numbers(numb):     # A function that checks that the user has entered a number
    while not numb.isdigit():
        numb = input('Please give the answer in whole numbers: ')
    numb = int(numb)
    return numb


def generator(num):    # A function that generates a crafty list from which the password will be generated
    generat_list = []
    remainder = num
    for i in range(count):
        if remainder == 0:
            break
        if i == count - 1:
            rand_num = remainder
        else:
            rand_num = randint(1, min(remainder - (count - i - 1), length - len(generat_list)))
        remainder -= rand_num
        generat_list.append(rand_num)

    return generat_list


def pass_generator(r_list):  # Function to generate a password based on a cunning list from generator(num)
    flag = False
    password = []
    r_list_count = r_list
    if exclusion:
        for _ in range(len(r_list)):
            if abs_UP:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(abs_clear_UP_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if abs_down:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(abs_clear_down_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if digits:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(digits_clear_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if symbols:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(symbols_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break
    else:
        for _ in range(len(r_list)):
            if abs_UP:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(abs_UP_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if abs_down:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(abs_down_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if digits:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(digits_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break

            if symbols:
                if len(r_list_count) < 1:
                    break
                else:
                    flag = True
                    for _ in range(r_list_count[0]):
                        password.append(choice(symbols_case))
            if flag:
                flag = False
                r_list_count = r_list_count[1:]
            if len(r_list_count) < 1:
                break
    shuffle(password)
    return password


# INITIALIZING SHEETS AND VARIABLES
digits_case = '0123456789'
digits_clear_case = '23456789'
abs_UP_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abs_clear_UP_case = 'ABCDEFGHJKMNPQRSTUVWXYZ'
abs_down_case = 'abcdefghijklmnopqrstuvwxyz'
abs_clear_down_case = 'abcdefghjkmnpqrstuvwxyz'
symbols_case = '!#$%&*+-=?@^_'
count = 0
case_count = 0

# MAIN PRINTS, INPUTS, EXCEPTIONS
print('Hi. My program will help you generate a password.')
print()
how = input('Write in a number how many passwords you need to generate: ').strip()
how = numbers(how)

abs_UP = input('''Does your password have to include uppercase letters (ABCDEFGHIJKLMNOPQRSTUVWXYZ) ?
Answer in the format: yes or no: ''').lower().strip()
abs_UP = yes_or_not(abs_UP)
if abs_UP:
    case_count += 1

abs_down = input('''Tell me if your password should include lowercase letters (abcdefghijklmnopqrstuvwxyz) ?
Answer in the format: yes or no: ''').lower().strip()
abs_down = yes_or_not(abs_down)
if abs_down:
    case_count += 1

digits = input('''Does your password have to include numbers (0123456789) ?
Answer in the format: yes or no: ''').lower().strip()
digits = yes_or_not(digits)
if digits:
    case_count += 1

symbols = input('''Does your password have to include the characters (!#$%&*+-=?@^_) ?
Answer in the format: yes or no: ''').lower().strip()
symbols = yes_or_not(symbols)
if symbols:
    case_count += 1

count = len([abs_UP_case, abs_down_case, digits_case, symbols_case][:case_count])
if count == 0:
    print('You did not select any modifier. Consequently, the password will be empty. Therefore, further operation of the program makes no sense.')
    print('Try starting over by selecting at least one modifier')
    sys.exit()

exclusion = input('''Do I exclude ambiguous characters (il1Lo0O)?
Answer in the format: yes or no: ''').lower().strip()
exclusion = yes_or_not(exclusion)

length = input("Okay. Now, let's define the maximum length of the password. Set this value with a number: ")
length = numbers(length)
while True:
    if length < case_count:
        length = input('The maximum length of the password cannot be less than the minimum number of modifiers you choose. Please enter it again: ')
        length = numbers(length)
    else:
        break

for i in range(how):    # Basic cycle of the password generator

    random_list = generator(length)

    print(*pass_generator(random_list), sep='')
