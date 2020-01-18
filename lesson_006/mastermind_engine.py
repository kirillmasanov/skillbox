from random import randint

number_list = []


def make_number():
    """ The computer guesses the number """
    global number_list
    number_list = [str(randint(1, 9))]
    while len(number_list) != 4:
        next_number = str(randint(0, 9))
        if next_number not in number_list:
            number_list.append(next_number)
    number_list = ''.join(number_list)


def check_number(user_number):
    """ The computer checks the number """
    print(number_list)
    bulls = 0
    cows = 0
    for i in range(len(number_list)):
        if number_list[i] in user_number:
            cows += 1
        if number_list[i] == user_number[i]:
            bulls += 1
    return {'bulls': bulls, 'cows': cows}
