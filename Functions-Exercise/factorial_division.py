def factorial_division(a, b):
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    factorial_a = factorial(a)
    factorial_b = factorial(b)

    division_result = factorial_a / factorial_b
    print(f"{division_result:.2f}")


num1 = int(input())
num2 = int(input())
factorial_division(num1, num2)
