n = int(input())
total_free_chairs = 0
game_on = True

for room in range(1, n + 1):
    data = input().split()
    chairs = len(data[0])
    visitors = int(data[1])
    diff = chairs - visitors

    if diff < 0:
        print(f"{abs(diff)} more chairs needed in room {room}")
        game_on = False
    else:
        total_free_chairs += diff

if game_on:
    print(f"Game On, {total_free_chairs} free chairs left")
