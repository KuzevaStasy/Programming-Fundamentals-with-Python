from math import sqrt,floor

def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def dist_to_center(x, y):
    return sqrt(x**2 + y**2)

def closest_point(x1, y1, x2, y2):
    if dist_to_center(x1, y1) <= dist_to_center(x2, y2):
        return (x1, y1), (x2, y2)
    else:
        return (x2, y2), (x1, y1)

def longer_line(x1,y1,x2,y2,x3,y3,x4,y4):

    line1_len = distance(x1, y1, x2, y2)
    line2_len = distance(x3, y3, x4, y4)

    if line1_len >= line2_len:
        p1, p2 = closest_point(x1, y1, x2, y2)
    else:
        p1, p2 = closest_point(x3, y3, x4, y4)

    print(f"({floor(p1[0])}, {floor(p1[1])})({floor(p2[0])}, {floor(p2[1])})")

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
x4, y4 = float(input()), float(input())

longer_line(x1, y1, x2, y2, x3, y3, x4, y4)