text = input()

emoticons = []
for i in range(len(text) - 1):        # -1 so i+1 is safe
    if text[i] == ":" and not text[i+1].isspace():
        emoticons.append(text[i:i+2])

for emo in emoticons:
    print(emo)
