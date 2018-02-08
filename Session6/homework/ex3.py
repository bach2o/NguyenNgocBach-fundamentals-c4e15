from turtle import *

def draw_square(lenght, color):
    speed = 0
    pencolor(color)
    for i in range(4):
        forward(lenght)
        left(90)

# draw_square(50, 'red')
