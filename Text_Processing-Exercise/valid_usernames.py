usernames = input().split(", ")

valid_usernames = []

for username in usernames:
    if 3 <= len(username) <= 16:
        valid = True
        for ch in username:
            if not (ch.isalnum() or ch == "-" or ch == "_"):
                valid = False
                break
        if valid:
            valid_usernames.append(username)

for name in valid_usernames:
    print(name)
