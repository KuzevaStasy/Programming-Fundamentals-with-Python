import re

text = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
maches = re.findall(pattern, text)
print(",".join(maches))