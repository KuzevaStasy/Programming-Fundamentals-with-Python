numbers_input = input()

def round_numbers(nums):
    numbers = nums.split()
    rounded = []
    for n in numbers:
        rounded.append(round(float(n)))

    return rounded


result = round_numbers(numbers_input)
print(result)
