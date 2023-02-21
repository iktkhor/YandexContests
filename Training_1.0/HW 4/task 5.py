blocks = int(input())
blocks_sizes = {}
for i in range(blocks):
    sizes = list(map(int, input().split()))
    if sizes[0] not in blocks_sizes:
        blocks_sizes[sizes[0]] = sizes[1]
    elif sizes[1] > blocks_sizes[sizes[0]]:
        blocks_sizes[sizes[0]] = sizes[1]

print(sum(blocks_sizes.values()))

