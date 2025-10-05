def sign_of_product(a,b,c):

    if a == 0 or b == 0 or c == 0:
        print("zero")
        return

    negatives = 0
    for num in (a, b, c):
        if num < 0:
            negatives += 1

    if negatives % 2 == 0:
        print("positive")
    else:
        print("negative")

first = int(input())
second = int(input())
third = int(input())

sign_of_product(first, second, third)