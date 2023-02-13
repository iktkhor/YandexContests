N, M = list(map(int, input().split()))
cubes_anya = set([int(input()) for i in range(N)])
cubes_borya = set([int(input()) for i in range(M)])

union_cubes = set()
unique_cubes_anya = set()
unique_cubes_borya = set()

for cube in cubes_anya:
    if cube in cubes_borya:
        union_cubes.add(cube)
    else:
        unique_cubes_anya.add(cube)

for cube in cubes_borya:
    if cube not in union_cubes:
        unique_cubes_borya.add(cube)

print(len(union_cubes))
print(' '.join(map(str, sorted(union_cubes))))
print(len(unique_cubes_anya))
print(' '.join(map(str, sorted(unique_cubes_anya))))
print(len(unique_cubes_borya))
print(' '.join(map(str, sorted(unique_cubes_borya))))
