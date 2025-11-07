import re

line = input().strip()
# split on commas, allowing arbitrary spaces around them, and ignore empty tokens
tickets = [t for t in re.split(r'\s*,\s*', line) if t != ""]

winning_symbols = ["@", "#", "$", "^"]

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left = ticket[:10]
    right = ticket[10:]

    best = None  # (streak_length, symbol)

    for sym in winning_symbols:
        # escape symbol in case it's a special regex char (like ^)
        pat = fr"{re.escape(sym)}{{6,10}}"

        # find the longest match in each half (if any)
        left_matches = re.findall(pat, left)
        right_matches = re.findall(pat, right)

        if left_matches and right_matches:
            left_longest = max(len(m) for m in left_matches)
            right_longest = max(len(m) for m in right_matches)
            streak = min(left_longest, right_longest)

            if best is None or streak > best[0]:
                best = (streak, sym)

    if best is None:
        print(f'ticket "{ticket}" - no match')
    else:
        streak, sym = best
        if streak == 10:
            print(f'ticket "{ticket}" - {streak}{sym} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {streak}{sym}')
