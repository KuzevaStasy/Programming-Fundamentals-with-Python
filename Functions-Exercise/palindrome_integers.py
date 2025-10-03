def check_palindromes(numbers_for_check):
    for num in numbers_for_check:
        if str(num) == str(num)[::-1]:
            print(True)
        else:
            print(False)



numbers = list(map(int, input().split(", ")))
check_palindromes(numbers)
