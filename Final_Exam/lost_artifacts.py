import re

text = input()

pattern = re.compile(
    r'([*^]+)'               # opening * or ^
    r'([A-Za-z ]{6,})'       # artifact name
    r'([*^]+)'               # closing * or ^
    r'([^A-Za-z0-9]*)'       # only non-alphanumeric allowed before +++
    r'(\++)'                 # opening +
    r'([-0-9.]+),([-0-9.]+)' # coordinates
    r'(\++)'                 # closing +
)

matches = pattern.findall(text)

valid_artifacts = []

for match in matches:
    artifact_name = match[1]
    separator = match[3]

    # Reject if alphanumeric characters separate the name and +++...+++
    if any(ch.isalnum() for ch in separator):
        continue

    latitude = match[5]
    longitude = match[6]
    coordinates = f"{latitude},{longitude}"

    valid_artifacts.append((artifact_name, coordinates))

if not valid_artifacts:
    print("No valid artifacts found.")
else:
    for name, coord in valid_artifacts:
        print(f"Found {name} at coordinates {coord}.")
