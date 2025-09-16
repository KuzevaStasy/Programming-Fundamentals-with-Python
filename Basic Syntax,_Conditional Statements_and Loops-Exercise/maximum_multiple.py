divisor = int(input())
boundary = int(input())

int_divide = boundary // divisor

multiplier = int_divide * divisor


if multiplier < boundary:
    print(multiplier)
else:
    print(boundary)