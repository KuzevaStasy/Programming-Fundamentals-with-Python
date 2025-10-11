schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    parts = command.split(":")
    action = parts[0]
    lesson = parts[1]

    if action == "Add":
        if lesson not in schedule:
            schedule.append(lesson)

    elif action == "Insert":
        index = int(parts[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)

    elif action == "Remove":
        if lesson in schedule:
            schedule.remove(lesson)
        # Remove exercise if it exists
        exercise = f"{lesson}-Exercise"
        if exercise in schedule:
            schedule.remove(exercise)

    elif action == "Swap":
        lesson2 = parts[2]
        if lesson in schedule and lesson2 in schedule:
            index1 = schedule.index(lesson)
            index2 = schedule.index(lesson2)
            schedule[index1], schedule[index2] = schedule[index2], schedule[index1]

            # Swap exercises if they exist
            exercise1 = f"{lesson}-Exercise"
            exercise2 = f"{lesson2}-Exercise"

            if exercise1 in schedule:
                schedule.remove(exercise1)
                schedule.insert(schedule.index(lesson)+1, exercise1)
            if exercise2 in schedule:
                schedule.remove(exercise2)
                schedule.insert(schedule.index(lesson2)+1, exercise2)

    elif action == "Exercise":
        exercise = f"{lesson}-Exercise"
        if lesson in schedule:
            if exercise not in schedule:
                index = schedule.index(lesson)
                schedule.insert(index + 1, exercise)
        else:
            schedule.append(lesson)
            schedule.append(exercise)

# Print the schedule
for i, lesson in enumerate(schedule, 1):
    print(f"{i}.{lesson}")
