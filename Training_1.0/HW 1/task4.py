a = int(input())
b = int(input())
c = int(input())
ans = 0

if a == 0:
    if b == 0:
        if c == 0:
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTION")
    elif b == c ** 2:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
elif c < 0:
    print("NO SOLUTION")
else:
    if (c ** 2 - b) % a == 0:
        ans = (c ** 2 - b) / a
        print(f'{ans:.0f}')
    else:
        print("NO SOLUTION")

