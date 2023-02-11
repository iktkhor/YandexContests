A, B, C, D, E = [int(input()) for i in range(5)]

if (A <= D and B <= E) or (B <= D and A <= E):
    print("YES")
elif (A <= D and C <= E) or (C <= D and A <= E):
    print("YES")
elif (C <= D and B <= E) or (B <= D and C <= E):
    print("YES")
else:
    print("NO")
