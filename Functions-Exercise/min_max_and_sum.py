def process_numbers(num):
    minimum = min(num)
    maximum = max(num)
    total = sum(num)

    print(f"The minimum number is {minimum}")
    print(f"The maximum number is {maximum}")
    print(f"The sum number is: {total}")


numbers = list(map(int, input().split()))
process_numbers(numbers)
