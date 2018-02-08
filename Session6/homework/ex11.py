def is_inside(x1, y1, x2, y2, w, h):
    inside = 0
    if x1 >= x2 and x1 <= x2 + w and y1 >= y2 and y1 <= y2 + h:
        inside = True
    else:
        inside = False
    return(inside)
