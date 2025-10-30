# Create a dictionary to store student data
students = {}

while True:
    line = input()
    if ":" not in line:  # the last line is the course name
        course_to_search = line
        break

    name, student_id, course = line.split(":")
    students[student_id] = {"name": name, "course": course}

# Print students enrolled in the given course
for student_id, info in students.items():
    if info["course"].replace(" ", "_").lower() == course_to_search:
        print(f"{info['name']} - {student_id}")
