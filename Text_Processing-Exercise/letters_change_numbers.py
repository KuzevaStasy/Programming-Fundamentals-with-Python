strings = input().split()
total = 0

for s in strings:
    first = s[0]
    last = s[-1]
    number = int(s[1:-1])

    # Position in alphabet (A/a = 1, B/b = 2, ...)
    if first.isupper():
        number /= (ord(first) - ord('A') + 1)
    else:
        number *= (ord(first) - ord('a') + 1)

    if last.isupper():
        number -= (ord(last) - ord('A') + 1)
    else:
        number += (ord(last) - ord('a') + 1)

    total += number

print(f"{total:.2f}")
