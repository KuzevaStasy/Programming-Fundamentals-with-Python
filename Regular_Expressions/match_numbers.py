import re

text = input()

pattern = r'(?<!\S)-?(?:0|[1-9]\d*)(?:\.\d+)?(?!\S)'

matches = re.findall(pattern, text)

print(' '.join(matches))
