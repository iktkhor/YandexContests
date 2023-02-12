ls = []

const_flag = True
asc_flag = True
weak_asc_flag = True
desc_flag = True
weak_desc = True
rand = True

while True:
    x = int(input())

    if x == -2000000000:
        break
    else:
        ls.append(x)

for i in range(len(ls) - 1):
    if const_flag and ls[i] != ls[i + 1]:
        const_flag = False
    if asc_flag and ls[i] >= ls[i + 1]:
        asc_flag = False
    if weak_asc_flag and ls[i] > ls[i + 1]:
        weak_asc_flag = False
    if desc_flag and ls[i] <= ls[i + 1]:
        desc_flag = False
    if weak_desc and ls[i] < ls[i + 1]:
        weak_desc = False

if const_flag:
    print("CONSTANT")
elif asc_flag:
    print("ASCENDING")
elif weak_asc_flag:
    print("WEAKLY ASCENDING")
elif desc_flag:
    print("DESCENDING")
elif weak_desc:
    print("WEAKLY DESCENDING")
else:
    print("RANDOM")
