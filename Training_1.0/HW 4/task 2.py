words = {}

with open('input.txt') as text:
    for line in text:
        for word in line.split():
            if word not in words:
                print(0, end=" ")
                words[word] = 0
            else:
                print(words[word], end=" ")

            words[word] += 1