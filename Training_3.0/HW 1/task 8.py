min_x = 2 * 10 ** 9
min_y = 2 * 10 ** 9
max_x = -2 * 10 ** 9
max_y = -2 * 10 ** 9
count = int(input())
for i in range(count):
    dot = list(map(int, input().split()))
    if dot[0] < min_x:
        min_x = dot[0]
    if dot[0] > max_x:
        max_x = dot[0]
    if dot[1] < min_y:
        min_y = dot[1]
    if dot[1] > max_y:
        max_y = dot[1]
print(min_x, min_y, max_x, max_y)
