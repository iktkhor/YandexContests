import random


def min_diff_rough(shirts, pants):
    ans = [shirts[0], pants[0]]
    min_diff = abs(shirts[0] - pants[0])
    for i in range(len(shirts)):
        for j in range(len(pants)):
            diff = abs(shirts[i] - pants[j])
            if diff < min_diff:
                min_diff = diff
                ans = [shirts[i], pants[j]]
    return ' '.join(map(str, ans))


def min_diff_two_pointers(shirts, pants):
    last_1 = 0
    last_2 = 0
    min_diff = [abs(shirts[last_1] - pants[last_2]), f'{shirts[last_1]} {pants[last_2]}']
    for i in range(len(shirts)):
        last_1 = i
        diff = abs(shirts[last_1] - pants[last_2])
        while last_2 < len(pants) - 1 and (abs(shirts[last_1] - pants[last_2 + 1]) <= diff):
            diff = abs(shirts[last_1] - pants[last_2 + 1])
            last_2 += 1
        if diff < min_diff[0]:
            min_diff = [diff, f'{shirts[last_1]} {pants[last_2]}']
    return min_diff[1]


def stress_test():
    count = 0
    while True:
        shirts = [0] * 5
        for i in range(5):
            shirts[i] = random.randint(1, 10)
        shirts = sorted(shirts)
        pants = [0] * 5
        for i in range(5):
            pants[i] = random.randint(1, 10)
        pants = sorted(pants)
        ans_1 = min_diff_rough(shirts, pants)
        ans_2 = min_diff_two_pointers(shirts, pants)
        print(f'Test #{count}')
        if ans_1 == ans_2:
            print("OK")
        else:
            print(f'Shirts {shirts}')
            print(f'Pants {pants}')
            print(f'min_diff_rough answer = {ans_1}')
            print(f'min_diff_two_pointers answer = {ans_2}')
            break
        count += 1


# N = int(input())
# shirt_values = list(map(int, input().split()))
# M = int(input())
# pant_values = list(map(int, input().split()))
# print(min_diff_two_pointers(shirt_values, pant_values))
stress_test()
