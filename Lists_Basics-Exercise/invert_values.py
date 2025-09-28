
s = input()

numbers = list(map(int, s.split()))
opposites = [-n for n in numbers]

print(opposites)
