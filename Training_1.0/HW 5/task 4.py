n, distance = list(map(int, input().split()))
monuments = list(map(int, input().split()))
left = right = 0
right += 1
count = 0

while right < len(monuments):
    diff = monuments[right] - monuments[left]
    if diff > distance:
        count += len(monuments) - right
        left += 1
    else:
        right += 1

print(count)
