str1, str2 = input().split()

total_sum = 0
min_len = min(len(str1), len(str2))

# Multiply character codes for overlapping characters
for i in range(min_len):
    total_sum += ord(str1[i]) * ord(str2[i])

# Add remaining characters (from the longer string)
if len(str1) > len(str2):
    for ch in str1[min_len:]:
        total_sum += ord(ch)
else:
    for ch in str2[min_len:]:
        total_sum += ord(ch)

print(total_sum)
