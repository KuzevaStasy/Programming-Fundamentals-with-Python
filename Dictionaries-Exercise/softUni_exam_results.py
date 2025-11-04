def exam_statistics():
    users = {}       # username -> max points
    submissions = {} # language -> submission count

    while True:
        line = input()
        if line == "exam finished":
            break

        parts = line.split("-")

        if parts[1] == "banned":
            username = parts[0]
            if username in users:
                del users[username]
            continue

        username, language, points = parts[0], parts[1], int(parts[2])

        # Count submissions per language
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

        # Track highest score per user
        if username not in users:
            users[username] = points
        else:
            if points > users[username]:
                users[username] = points

    # Print results
    print("Results:")
    for username, points in users.items():
        print(f"{username} | {points}")

    # Print submissions per language
    print("Submissions:")
    for language, count in submissions.items():
        print(f"{language} - {count}")

exam_statistics()
