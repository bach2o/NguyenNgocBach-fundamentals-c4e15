def bopdai(x, y, operator): # function
    answer = 0

    if operator == '+':
        answer = x + y
    elif operator == '-':
        answer = x - y
    elif operator == '*':
        answer = x * y
    elif operator == '/':
        if y == 0:
            print('Fuck off')
        answer = x / y

    return answer


# x = int(input('x = '))
# y = int(input('y = '))
# operator = input('operator = ')
# z = bopdai(x, y, operator)
# print(z)
#
# bopdai(x, y, operator)
# print("{0} {1} {2} = {3}".format(x, operator, y, answer))

# x = float(input('x ='))
# operator = input('Operation(+,-,*,/): ')
# y = float(input('x ='))
#
# answer = 0
#
# if operator == '+':
#     answer = x + y
# elif operator == '-':
#     answer = x - y
# elif operator == '*':
#     answer = x * y
# elif operator == '/':
#     answer = x / y
# else:
#     print('What the hell? ')
#
# print("{0} {1} {2} = {3}".format(x, operator, y, answer))
