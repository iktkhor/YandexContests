syns = {}
reverse_syns = {}

for i in range(int(input())):
    ls = input().split()
    syns[ls[0]] = ls[1]
    reverse_syns[ls[1]] = ls[0]

word = input()

if word in syns:
    print(syns[word])
elif word in reverse_syns:
    print(reverse_syns[word])
