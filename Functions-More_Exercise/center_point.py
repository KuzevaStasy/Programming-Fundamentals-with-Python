from math import sqrt, floor

def closest_point(x1,y1,x2,y2):

    dist1 = sqrt(x1**2 + y1**2)
    dist2 = sqrt(x2**2 + y2**2)

    if dist1 <= dist2:
        print(f"({floor(x1)}, {floor(y1)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})")

x_first_point = float(input())
y_first_point = float(input())
x_second_point = float(input())
y_second_point = float(input())

closest_point(x_first_point, y_first_point, x_second_point, y_second_point)