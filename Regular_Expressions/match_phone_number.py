import re

text = input()

pattern = r'\+359([ -])2\1\d{3}\1\d{4}\b'

matches = re.findall(pattern, text)

matches = [match.group(0) for match in re.finditer(pattern, text)]

print(', '.join(matches))
