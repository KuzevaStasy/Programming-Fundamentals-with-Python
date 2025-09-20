first_char_index = int(input())
second_char_index = int(input())

for i in range(first_char_index, second_char_index + 1):
    print_char = chr(i)
    print(f"{print_char}", end=" ")