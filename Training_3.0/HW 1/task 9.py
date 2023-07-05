N, M, requests = list(map(int, input().split()))

#input_matrix = []
matrix = []
matrix.append([0 for i in range(M + 2)])

for i in range(N):
    input_row = list(map(int, input().split()))
    #input_matrix.append(input_row)
    row = [0]
    row_sum = 0

    for el in range(len(input_row)):
        row_sum += input_row[el]
        row.append(row_sum + matrix[i][el + 1])

    row.append(0)
    matrix.append(row)

matrix.append([0 for i in range(M + 2)])

#print(matrix)

for i in range(requests):
    dots = list(map(int, input().split()))
    x1, y1, x2, y2 = dots
    ans = matrix[x2][y2] - matrix[x2][y1 - 1] - matrix[x1 - 1][y2] + matrix[x1 - 1][y1 - 1]

    print(ans)

