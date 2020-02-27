import argparse


def get_score(game_result='1/--------5/XXXX'):
    list_result = []
    frame = []
    sum = 0
    for ch in game_result:
        if ch not in '123456789X/-':
            raise ValueError('Несоответствующее значение!')
        elif ch == 'X':
            list_result.append(ch)
            if len(frame) == 1:
                raise ValueError('Один бросок перед Х')
        else:
            frame.append(ch)
            if len(frame) == 2:
                list_result.append(frame)
                frame = []
    if len(frame) == 1:
        raise ValueError('Лишнее значение!')
    if len(list_result) != 10:
        raise ValueError('Сыграно не 10 фреймов!')
    for n in list_result:
        if n == 'X':
            sum += 20
        elif n[1] == '/':
            sum += 15
        elif n[0] == '/':
            raise ValueError('Не на своем месте "/"!')
        elif n[0] == n[1] == '-':
            continue
        elif n[0] == '-':
            sum += int(n[1])
        elif n[1] == '-':
            sum += int(n[0])
        else:
            if int(n[0]) + int(n[1]) > 10:
                raise ValueError('Сумма больше 10')
            for k in n:
                if k != '-':
                    sum += int(k)
    return sum


parser = argparse.ArgumentParser(description='Bowling..')
parser.add_argument('-result', action="store", dest="game_result")
args = parser.parse_args()

result = get_score(args.game_result)
print(result)
# print(get_score())
