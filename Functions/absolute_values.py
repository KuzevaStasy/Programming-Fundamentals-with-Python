numbers = input().split()
lst = []

for number in numbers:
    number = float(number)
    abs_number = abs(number)
    lst.append(abs_number)

print(lst)