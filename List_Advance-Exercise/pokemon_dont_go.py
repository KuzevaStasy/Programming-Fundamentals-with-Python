sequence = list(map(int, input().split()))
total_removed = 0

while sequence:
    index = int(input())

    if index < 0:
        removed = sequence.pop(0)
        total_removed += removed
        # Copy last element to the first position
        sequence.insert(0, sequence[-1])
    elif index >= len(sequence):
        removed = sequence.pop(-1)
        total_removed += removed
        # Copy first element to the last position
        sequence.append(sequence[0])
    else:
        removed = sequence.pop(index)
        total_removed += removed

    # Adjust the remaining elements
    for i in range(len(sequence)):
        if sequence[i] <= removed:
            sequence[i] += removed
        else:
            sequence[i] -= removed

print(total_removed)