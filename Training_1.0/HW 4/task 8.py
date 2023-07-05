def get_letters_dict(fragment_text):
    letters = {}
    for letter in fragment_text:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
    return letters


def compare_dict(dict_1, dict_2):
    for key in dict_1.keys():
        if key not in dict_2:
            return False
        elif dict_1[key] != dict_2[key]:
            return False
    return True


def get_decoding(signs_, sequence_signs):
    ans = 0
    unique_signs = get_letters_dict(signs_)
    #print(sorted(unique_signs))

    for i in range(len(sequence_signs) - len(signs_) + 1):
        fragment = sequence_signs[i:i + len(signs_)]
        #print(i, fragment_signs)
        fragment_signs = {}
        for j in range(i, i + len(signs_)):
            sign = sequence_signs[j]
            if sign not in fragment_signs:
                fragment_signs[sign] = 0
            fragment_signs[sign] += 1

        if compare_dict(unique_signs, fragment_signs):
            ans += 1

    return ans


input()
signs = input()
seq = input()
print(get_decoding(signs, seq))
