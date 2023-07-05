def back():
    if len(stack) > 0:
        return stack[len(stack) - 1]


trains = int(input())
seq = list(map(int, input().split()))
stack = []
pos = 0
num = 1
while pos < trains:
    stack.append(seq[pos])
    pos += 1
    while back() == num:
        num += 1
        stack.pop()

if len(stack) > 0:
    print("NO")
else:
    print("YES")
