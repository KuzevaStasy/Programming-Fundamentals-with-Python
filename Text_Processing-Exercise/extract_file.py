path = input().strip()

# Find last directory separator
sep_index = max(path.rfind("/"), path.rfind("\\"))

# Extract the full file name with extension
full_name = path[sep_index + 1:] if sep_index != -1 else path

# Split name and extension
if "." in full_name:
    name, extension = full_name.rsplit(".", 1)
else:
    name = full_name
    extension = ""

print(f"File name: {name}")
print(f"File extension: {extension}")
