ls = list(map(int, input().split()))
length1 = ls[0]
width1 = ls[1]
length2 = ls[2]
width2 = ls[3]
squares = [[f'{max(length1, length2)} {width1 + width2}', max(length1, length2) * (width1 + width2)],
           [f'{max(length1, width2)} {width1 + length2}', max(length1, width2) * (width1 + length2)],
           [f'{max(width1, width2)} {length1 + length2}', max(width1, width2) * (length1 + length2)],
           [f'{max(width1, length2)} {length1 + width2}', max(width1, length2) * (length1 + width2)]]

min_sq = squares[0][1]
ind_min = 0
print(squares)

for i in range(len(squares)):
    if squares[i][1] < min_sq:
        min_sq = squares[i][1]
        ind_min = i
print(squares[ind_min][0])
