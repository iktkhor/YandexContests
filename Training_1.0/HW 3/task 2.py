ls1 = set(list(map(int, input().split())))
ls2 = set(list(map(int, input().split())))
union = []

for num in ls1:
    if num in ls2:
        union.append(num)

print(' '.join(map(str, sorted(union))))
