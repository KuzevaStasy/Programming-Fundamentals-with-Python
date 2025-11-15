import re

pattern = r'(w{3}\.[a-z0-9\-]+(\.[a-z]+)+)'

text = input()
while text:
    matches = re.search(pattern, text, re.IGNORECASE)
    if matches:
        print(matches.group())
    text = input()
