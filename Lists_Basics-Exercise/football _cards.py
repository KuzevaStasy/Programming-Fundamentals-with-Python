cards = input().split()

team_a = 11
team_b = 11

sent_off_a = []
sent_off_b = []

game_terminated = False

for card in cards:
    team, num = card.split('-')
    num = int(num)

    if team == 'A':
        if num not in sent_off_a:
            sent_off_a.append(num)
            team_a -= 1
    else:  # team == 'B'
        if num not in sent_off_b:
            sent_off_b.append(num)
            team_b -= 1

    if team_a < 7 or team_b < 7:
        game_terminated = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")
if game_terminated:
    print("Game was terminated")
