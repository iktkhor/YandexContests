interval_1, interval_2, trains_1, trains_2 = [int(input()) for i in range(4)]

min_1 = (1 + interval_1) * trains_1 - interval_1
max_1 = (1 + interval_1) * trains_1 + interval_1
print(min_1, max_1)

min_2 = (1 + interval_2) * trains_2 - interval_2
max_2 = (1 + interval_2) * trains_2 + interval_2
print(min_2, max_2)

if min_1 <= max_2 and min_2 <= max_1:
    print(max(min_1, min_2), min(max_1, max_2))
else:
    print(-1)
