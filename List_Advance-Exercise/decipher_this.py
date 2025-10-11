message = input().split()
decoded_words = []

for word in message:
    # Extract the number (ASCII code) from the beginning of the word
    digits = ''.join([ch for ch in word if ch.isdigit()])
    letters = [ch for ch in word if not ch.isdigit()]

    # Convert the number to a character
    first_letter = chr(int(digits))

    # Swap the second and last letters if there are at least 2 letters
    if len(letters) > 1:
        letters[0], letters[-1] = letters[-1], letters[0]

    decoded_word = first_letter + ''.join(letters)
    decoded_words.append(decoded_word)

print(' '.join(decoded_words))
