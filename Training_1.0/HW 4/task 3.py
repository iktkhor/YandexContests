words = {}
with open('input.txt') as text:
    for line in text:
        for word in line.split():
            if word not in words:
                words[word] = 0
            words[word] += 1
max_value = max(words.values())
max_words = set()
for key, value in words.items():
    if value == max_value:
        max_words.add(key)
print(sorted(max_words)[0])
