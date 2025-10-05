def tribonacci(n):
    sequence = [1, 1, 2]

    if n <= 3:
        print(" ".join(str(sequence[i]) for i in range(n)))
        return

    for i in range(3, n):
        sequence.append(sequence[i-1] + sequence[i-2] + sequence[i-3])

    print(" ".join(map(str, sequence[:n])))

number = int(input())
tribonacci(number)