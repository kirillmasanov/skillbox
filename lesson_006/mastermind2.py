from mastermind2_engine import make_number, check_number
from mastermind2_ii import guess
from termcolor import cprint, colored

while True:
    make_number()
    k = 0
    while True:
        k += 1
        ii_number = guess()
        rez = check_number(ii_number=ii_number)
        cprint(f'Быков - {rez["bulls"]}, коров - {rez["cows"]}', color='green')
        if list(check_number(ii_number=ii_number).values())[0] == 4:
            cprint(f'Вы отгодали за {k} ходов!', color='cyan')
            break
    more = input(colored('Хотите ли еще парти? - ', color='yellow'))
    if more == 'нет':
        break
