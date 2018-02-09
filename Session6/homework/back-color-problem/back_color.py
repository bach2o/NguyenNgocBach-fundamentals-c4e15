from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    color_names = ['RED', 'GREEN', 'BLUE', 'YELLOW']
    text = choice(color_names)
    color_codes = ['#3F51B5', '#C62828', '#FFD600', '#4CAF50']
    color = choice(color_codes)
    types = ['meaning', 'color']
    if choice(types) == 'meaning':
        quiz_type = 0
    else:
        quiz_type = 1
    return [
                text,
                color,
                quiz_type
                # randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    corordinate = []
    if quiz_type == 0:
        for items in shapes:
            if (items['text']).upper() == text:
                corordinate = items['rect']
                x0 = corordinate[0]
                y0 = corordinate[1]
                w = corordinate[2]
                h = corordinate[3]
                if x >= x0 and x <= x0 + w and y >= y0 and y <= y0 + h:
                    return True
                else:
                    return False
    else:
        for items in shapes:
            if items['color'] == color:
                corordinate = items['rect']
                x0 = corordinate[0]
                y0 = corordinate[1]
                w = corordinate[2]
                h = corordinate[3]
                if x >= x0 and x <= x0 + w and y >= y0 and y <= y0 + h:
                    return True
                else:
                    return False
