from random import randint
from random import choice
from Cal import bopdai

while True:
    chance = randint(0, 100)
    if chance < 15:
        operator = '/'
    elif 15 <= chance < 35:
        operator = '*'
    elif 35 <= chance < 65:
        operator = '-'
    else:
        operator = '+'

    x = randint(0, 10)
    y = randint(0, 10)
    Tru = 0
    Fal = 0
    random_number = randint(-1, 1)
    # num_range =[-1,0,1]
    # random_number = choice(num_range)
    operator = choice(operators)

    if Tru < Fal:
        if operator == '+':
            answer = x + y
        elif operator == '-':
            answer = x - y
        elif operator == '*':
            answer = x * y
        elif operator == '/':
            y = randint(1,10)
            answer = x / y
    else:
        if operator == '+':
            answer = x + y + random_number
        elif operator == '-':
            answer = x - y + random_number
        elif operator == '*':
            answer = x * y + random_number
        elif operator == '/':
            y = randint(1,10)
            answer = x / y + random_number

    print('{0} {1} {2} = {3}'.format(x, operator, y, answer))

    player_answer = (input('(Y/N)?')).upper()
    if random_number == 0:
        if player_answer == 'Y':
            print('Good')
        elif player_answer == 'N':
            print('Wrong')
        Tru += 1
    else:
        if player_answer == 'N':
            print('Good')
        elif player_answer == 'Y':
            print('Wrong')
        Fal += 1
