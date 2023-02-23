def prefix_nums(numbers):
    prefix = [0]
    now_sum = 0
    for i in range(len(numbers)):
        now_sum += numbers[i]
        prefix.append(now_sum)
    return prefix


def count_sets(numbers, k):
    def get_sum(start, end):
        return prefix[end + 1] - prefix[start]

    prefix = prefix_nums(numbers)
    right = 0
    count = 0
    for i in range(len(numbers)):
        left = i
        while right < len(numbers) and get_sum(left, right) <= k:
            if get_sum(left, right) == k:
                count += 1
            right += 1
    return count


cars, happy_number = list(map(int, input().split()))
car_numbers = list(map(int, input().split()))
print(count_sets(car_numbers, happy_number))
