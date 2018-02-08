from random import randint, choice
from calc import eval

x = randint(0, 10)
y = randint(0, 10)
op = choice(["+", "-", "*", "/"])
error = randint(-1, 1)

display_result = bopdai(x, y, op) + error

print("{0} {3} {1} = {2}".format(x, y, display_result, op))

answer = input("Y/N?").upper()

if error == 0:
    if answer == "Y":
        print("Yay")
    else:
        print("Nay")
else:
    if answer == "Y":
        print("Nay")
    else:
