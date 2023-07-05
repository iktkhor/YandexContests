ls = list(map(int, input().split()))
K_1 = ls[0]
P_1 = 1
N_1 = 0
M = ls[1]
K_2 = ls[2]
P_2 = ls[3]
N_2 = ls[4]

# если этаж 2-ой квартиры > номера квартиры
if (M * (P_2 - 1)) + N_2 > K_2:
    P_1 = -1
    N_1 = -1
elif M < P_2:
    P_1 = -1
    N_1 = -1
elif N_2 == 1 and P_2 == 1:
    # если этаж второй квартиры и подъезд == 1
    P_1 = 0
    N_1 = 1
else:
    lvl = K_2 // N_2

    if (lvl * N_2) + lvl < K_2:
        lvl += 1

    if K_1 % lvl == 0:
        N_1 = K_1 // lvl
    else:
        N_1 = K_1 // lvl + 1

    while N_1 - M > 0:
        N_1 -= M
        P_1 += 1


print(P_1, N_1)
