first_number = int(input())
second_number = int(input())

print(f"Before:\na = {first_number}\nb = {second_number}")

buffer = first_number
first_number = second_number
second_number = buffer

print(f"After:\na = {first_number}\nb = {second_number}")