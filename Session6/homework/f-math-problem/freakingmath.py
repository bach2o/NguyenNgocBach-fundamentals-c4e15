from random import *

def generate_quiz():
    x = randint(0, 10)
    y = randint(0, 10)
    operators = ['+', '-', '*', '/']
    op = choice(operators)
    random_range = randint(-1, 1)
    if op == '+':
        z = x + y
    elif op == '-':
        z = x - y
    elif op == '*':
        z = x * y
    elif op == '/':
        y = randint(1,3)
        z = x // y
    result = z + random_range
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    if op == '+':
        if x + y == result and user_choice == True or x + y != result and user_choice == False:
            return True
        else:
            return False
    elif op == '-':
        if x - y == result and user_choice == True or x - y != result and user_choice == False:
            return True
        else:
            return False
    elif op == '*':
        if x * y == result and user_choice == True or x * y != result and user_choice == False:
            return True
        else:
            return False
    else:
        if x // y == result and user_choice == True or x // y != result and user_choice == False:
            return True
        else:
            return False
