birds = int(input())
dots = {}

for i in range(birds):
    x, y = map(int, input().split())
    if x not in dots:
        dots[x] = set()
    dots[x].add(y)

print(len(dots.keys()))
