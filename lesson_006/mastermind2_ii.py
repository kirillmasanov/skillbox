from random import randint

def guess():
    ii_number = [str(randint(1, 9))]
    while len(ii_number) != 4:
        next_number = str(randint(0, 9))
        if next_number not in ii_number:
            ii_number.append(next_number)
    ii_number = ''.join(ii_number)
    return ii_number
