n = int(input())

balanced = True
last_bracket = ""

for _ in range(n):
    line = input().strip()

    if line == "(":
        if last_bracket == "(":
            balanced = False
        last_bracket = "("
    elif line == ")":
        if last_bracket != "(":
            balanced = False
        last_bracket = ")"

if last_bracket == "(":
    balanced = False

print("BALANCED" if balanced else "UNBALANCED")
