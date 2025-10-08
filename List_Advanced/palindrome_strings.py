words = input().split()
palindrome_to_search = input()

palindromes = [word for word in words if word == word[::-1]]

count = palindromes.count(palindrome_to_search)

print(palindromes)
print(f"Found palindrome {count} times")
