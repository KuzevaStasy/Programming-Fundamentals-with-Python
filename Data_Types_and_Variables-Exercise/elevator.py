from math import ceil

elevate_persons = int(input())
capacity_elevator = int(input())

courses = ceil(elevate_persons / capacity_elevator)

print(courses)
