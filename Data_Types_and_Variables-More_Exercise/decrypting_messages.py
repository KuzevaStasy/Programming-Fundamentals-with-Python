key = int(input())
n = int(input())

message = ""

for _ in range(n):
    ch = input()
    shifted = chr(ord(ch) + key)
    message += shifted

print(message)
