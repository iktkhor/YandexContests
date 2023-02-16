numbers = list(map(int, input().split()))
max_neg1 = min(numbers[0], numbers[1])
max_neg2 = max(numbers[0], numbers[1])
max_pos1 = max(numbers[0], numbers[1])
max_pos2 = min(numbers[0], numbers[1])


for i in range(2, len(numbers)):
    if numbers[i] < 0:
        if numbers[i] < max_neg1:
            max_neg2 = max_neg1
            max_neg1 = numbers[i]
        elif numbers[i] < max_neg2:
            max_neg2 = numbers[i]
    elif numbers[i] > 0:
        if numbers[i] > max_pos1:
            max_pos2 = max_pos1
            max_pos1 = numbers[i]
        elif numbers[i] > max_pos2:
            max_pos2 = numbers[i]

if max_neg1 * max_neg2 > max_pos1 * max_pos2:
    print(min(max_neg1, max_neg2), max(max_neg1, max_neg2))
else:
    print(min(max_pos1, max_pos2), max(max_pos1, max_pos2))
