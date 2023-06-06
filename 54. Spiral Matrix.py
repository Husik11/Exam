# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
output = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    z = []
    for i in range(m):
        for j in range(n):
            if i == 0 and j != n:
                z.append(matrix[i][j])
            elif i < m and j == n - 1:
                z.append(matrix[i][j])
    for i in range(m - 1, 0, -1):
        for j in range(n - 2, -1, -1):
            if i == m - 1 and j != n - 1:
                z.append(matrix[i][j])
            elif  0 < i < m - 1 and j == 0:
                z.append(matrix[i][j])
    for i in range(m - 1):
        for j in range(n - 1):
            if 0 < i < m - 2 and 0 < j < n:
                z.append(matrix[i][j])
    for i in range(m - 1, 0, -1):
        for j in range(n - 2, -1, -1):
            if i == m - 2 and 0 < j < n - 1:
                z.append(matrix[i][j])
    return z
print(spiralOrder(matrix))
