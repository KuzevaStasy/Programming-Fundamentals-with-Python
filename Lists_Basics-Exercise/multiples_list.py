factor = int(input())
count = int(input())
number = 1
lst = []

for i in range(count):
    multy = factor * number
    lst.append(multy)
    number += 1
print(lst)