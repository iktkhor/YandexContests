def print_gistogram():
    textsymbols = {}
    with open("input.txt") as text:
        for line in text:
            for word in line.split():
                for letter in word:
                    if letter not in textsymbols:
                        textsymbols[letter] = 0
                    textsymbols[letter] += 1
    maxsym = max(textsymbols.values())
    sortedsyms = sorted(textsymbols.keys())
    for row in range(maxsym, 0, -1):
        for sym in sortedsyms:
            if textsymbols[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sortedsyms))


print_gistogram()
