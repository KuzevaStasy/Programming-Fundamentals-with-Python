def get_even_numbers(num):
    return list(filter(lambda x: x % 2 == 0, num))

numbers = list(map(int, input().split()))
even_numbers = get_even_numbers(numbers)

print(even_numbers)
