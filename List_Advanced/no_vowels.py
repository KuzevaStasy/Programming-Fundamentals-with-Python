text = input()

vowels = 'aeiouAEIOU'

no_vowels = ''.join([char for char in text if char not in vowels])

print(no_vowels)
