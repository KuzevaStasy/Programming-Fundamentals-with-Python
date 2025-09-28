offers = list(map(int, input().split(", ")))
beggars_count = int(input())

result = [0] * beggars_count

for i in range(len(offers)):
    beggar_index = i % beggars_count
    result[beggar_index] += offers[i]

print(result)