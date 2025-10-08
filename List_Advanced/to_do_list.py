notes = []

while True:
    command = input()
    if command == "End":
        break

    importance, note = command.split("-", 1)
    importance = int(importance)

    notes.append((importance, note))


sorted_notes = []
for _ in range(len(notes)):
    min_note = min(notes, key=lambda x: x[0])
    notes.remove(min_note)  # remove it
    sorted_notes.append(min_note[1])  # keep only the note text

print(sorted_notes)
