times = list(map(float, input().split()))

middle_index = len(times) // 2

# Left car: start to the middle (excluding middle)
left_times = times[:middle_index]
left_total = 0
for t in left_times:
    left_total += t
    if t == 0:
        left_total *= 0.8  # reduce by 20%

# Right car: end to the middle (excluding middle)
right_times = times[-1:middle_index:-1]  # reverse from end to middle
right_total = 0
for t in right_times:
    right_total += t
    if t == 0:
        right_total *= 0.8  # reduce by 20%

# Determine the winner
if left_total <= right_total:
    print(f"The winner is left with total time: {left_total:.1f}")
else:
    print(f"The winner is right with total time: {right_total:.1f}")
