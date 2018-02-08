from random import *

def generate_quiz():
    result = 0
    x = randint(0, 10)
    y = randint(0, 10)
    operators = ['+', '-', '*', '/']
    op = choice(operators)
    random_range = randint(-1, 1)
    if op == '+':
        result = x + y + random_range
    elif op == '-':
        result = x - y + random_range
    elif op == '*':
        result = x * y + random_range
    elif op == '/':
        y = randint(1,3)
        result = x // y + random_range
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    pass
