def characters_in_range(first, second):
    first_char = ord(first)
    second_char = ord(second)
    result = ""
    for char in range(first_char + 1, second_char):
        result += chr(char) + " "
    return result.strip()


first_character = input()
second_character = input()

printed = characters_in_range(first_character, second_character)
print(printed)