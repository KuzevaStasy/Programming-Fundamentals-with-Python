def check_perfect_number(number):
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(check_perfect_number(num))
