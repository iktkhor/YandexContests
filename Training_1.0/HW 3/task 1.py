numbers = set()
ls = list(map(int, input().split()))

for now in ls:
    numbers.add(now)

print(len(numbers))