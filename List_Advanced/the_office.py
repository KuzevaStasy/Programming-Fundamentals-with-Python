happiness_values = list(map(int, input().split()))
factor = int(input())

improved_happiness = [h * factor for h in happiness_values]

average_happiness = sum(improved_happiness) / len(improved_happiness)

happy_count = len([h for h in improved_happiness if h >= average_happiness])

total_count = len(improved_happiness)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
