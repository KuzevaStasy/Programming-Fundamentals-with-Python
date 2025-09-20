import math

elevate_persons = int(input())
capacity_elevator = int(input())

courses = math.ceil(elevate_persons / capacity_elevator)

print(courses)