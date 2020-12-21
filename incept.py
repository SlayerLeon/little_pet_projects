# -*- coding: utf-8 -*-

import random
from pyfiglet import Figlet


# print f.renderText('text to render')

en = int(input('Enter num:'))

def main(en):
    '''
    функция вывода рандомных чисел и цифр в красивом виде
    '''
    f = Figlet(font='slant')
    r = type(int)
    if en > 100:
        while r != 101:
            r = random.randint(0,200)
            print(f.renderText(f'{r} \n'))
        else:
            print(f.renderText(f'Was founded {r} !'))
    elif en < 100:
        while r != 99:
            r = random.randint(0,100)
            print(f.renderText(f'{r} \n'))
        else:
            print(f.renderText(f'Was founded {r} !'))
     # while r != 99:
        # r = random.randint(0,100)
        # print(f'{r} \n')
    # else:
        # print(f'Was founded {r} !')
    print(main.__doc__)
    return r
    

main(en)
