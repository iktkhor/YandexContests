numbers = []
phone_numbers = []


for i in range(10):
    numbers.append(str(i))

for i in range(4):
    phone_numbers.append(input())

for i in range(4):
    count = 0
    new_num = ""

    for s in phone_numbers[i]:
        if s in numbers:
            new_num += s

    if len(new_num) == 7:
        new_num = "8495" + new_num
    elif new_num[0] == "7":
        new_num = "8" + new_num[1:11]

    phone_numbers[i] = new_num


for i in range(1, 4):
    if phone_numbers[0] == phone_numbers[i]:
        print("YES")
    else:
        print("NO")