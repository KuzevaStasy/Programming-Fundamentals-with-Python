def odd_even_number(num):
    number_str = str(num)
    odd_sum = 0
    even_sum = 0
    for digit in number_str:
        d = int(digit)
        if d % 2 == 0:
            even_sum += d
        else:
            odd_sum += d
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

number = int(input())
odd_even_number(number)