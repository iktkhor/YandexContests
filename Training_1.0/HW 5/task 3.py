points = int(input())
prefix_up_heights = [0]
prefix_down_heights = [0]
dot = list(map(int, input().split()))
prefix_up_heights.append(dot[1])
prefix_down_heights.append(dot[1])
last_y = dot[1]

for i in range(points - 1):
    x, y = list(map(int, input().split()))
    diff = y - last_y
    if diff <= 0:
        prefix_up_heights.append(prefix_up_heights[len(prefix_up_heights) - 1])
        prefix_down_heights.append(prefix_down_heights[len(prefix_down_heights) - 1] + abs(diff))
    elif diff > 0:
        prefix_up_heights.append(prefix_up_heights[len(prefix_up_heights) - 1] + diff)
        prefix_down_heights.append(prefix_down_heights[len(prefix_down_heights) - 1])
    last_y = y
tracks = int(input())
#print(prefix_up_heights)
#print(prefix_down_heights)

for i in range(tracks):
    start, end = list(map(int, input().split()))
    height = 0
    if end >= start:
        height = prefix_up_heights[end] - prefix_up_heights[start]
    else:
        height = prefix_down_heights[start] - prefix_down_heights[end]
    print(height)

