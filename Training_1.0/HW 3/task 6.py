def genom_proximity(genom_A, genom_B):
    if len(genom_A) == 1 or len(genom_B) == 1:
        return 0
    pairs_B = set()
    proximity = 0
    for i in range(len(genom_B) - 1):
        pair = genom_B[i] + genom_B[i + 1]
        pairs_B.add(pair)
    for i in range(len(genom_A) - 1):
        pair = genom_A[i] + genom_A[i + 1]
        if pair in pairs_B:
            proximity += 1
    return proximity


genom_A = input()
genom_B = input()
print(genom_proximity(genom_A, genom_B))
