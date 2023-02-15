words = set()

with open('input.txt') as text:
    for line in text:
        #print(line, end="")
        for word in line.split():
            words.add(word)

print(len(words))
